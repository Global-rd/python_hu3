import logging
import logging.config
import yaml   #pip install pyyaml
import pathlib
import sys

BASE_DIR = pathlib.Path(__file__).parent
RED = "\033[31m"
GREEN = "\033[32m"
RESET = "\033[0m"

def load_config(config_path: pathlib.Path) -> dict:
    if "yaml" not in sys.modules:
        print("A PyYAML nincs telepítve. Telepítsd a következő paranccsal: pip install pyyaml")
        sys.exit(1)

    if not config_path.exists():
        print("Nincs meg a configurációs fájl. A program leáll.")
        sys.exit(1)

    try:
        with open(config_path, "r", encoding="utf-8") as f:
            config = yaml.safe_load(f) or {}
    except Exception as e:
        print(f"Hiba a configurációs fájl beolvasásakor: {e}")
        sys.exit(1)

    required = {"tasks_file", "log_dir", "logging_config", "log_file"}
    missing = required - set(config)
    if missing:
        print(f"Hiányzó konfigurációs kulcs(ok): {', '.join(sorted(missing))}")
        sys.exit(1)

    return config        

def setup_logging(logging_config_path: pathlib.Path, log_dir: pathlib.Path, log_file: str) -> logging.Logger:
    """
    Betölti és beállítja a logging konfigurációt YAML-ből.
    Ha hiányzik a log mappa vagy a YAML hibás, a program leáll.
    A YAML-ban szereplő '#LOG_FILE#' helyőrzőt lecseréli a tényleges log fájl elérési útra.
    """
    # Ellenőrizzük, hogy a PyYAML elérhető-e
    if "yaml" not in sys.modules:
        print("A PyYAML nincs telepítve. Telepítsd a következő paranccsal: pip install pyyaml")
        sys.exit(1)

    # Ha nincs log mappa, létrehozzuk
    if not log_dir.exists():
        try:
            log_dir.mkdir(parents=True, exist_ok=True)
            print(f"Nem találtam 'logs' könyvtárat, emiatt létrehoztam: {log_dir}")
        except Exception as e:
            print(f"Nincs 'logs' könyvtár, és nem is sikerült létrehozni a könyvtárat: {e}")
            sys.exit(1)

    # Log config beolvasása és feldolgozása
    try:
        if logging_config_path.exists():
            with open(logging_config_path, "r", encoding="utf-8") as f:
                config = yaml.safe_load(f)

            if not isinstance(config, dict) or not config:
                raise ValueError(f"Üres vagy érvénytelen logging config: {logging_config_path}")

            # A log config file-ban a #LOG_FILE# helyőrző szerepel, amit le kell cserélni
            for handler in (config.get("handlers") or {}).values():
                if not isinstance(handler, dict):
                    continue

                filename = handler.get("filename")
                if not isinstance(filename, str):
                    # pl. console handlernél nincs filename, kihagyjuk
                    continue

                target = (log_dir / log_file).resolve()
                if "#LOG_FILE#" in filename:
                    handler["filename"] = filename.replace("#LOG_FILE#", str(target))

            # Logging konfiguráció alkalmazása
            logging.config.dictConfig(config)
            logger = logging.getLogger()
            logger.info("Logging config betöltve: %s", logging_config_path)
            return logger
        else:
            raise FileNotFoundError(f"Nem található a logger config: {logging_config_path}")

    except Exception as e:
        print(f"Nem sikerült betölteni a logging konfigurációt, emiatt nem tudunk elindulni! ({e})")
        sys.exit(1)


def load_tasks(file_path: pathlib.Path, logger: logging.Logger) -> list[str]:
    tasks: list[str] = []
    try:
        with file_path.open("r", encoding="utf-8") as f:
            tasks = [line.strip() for line in f if line.strip()]
        logger.info("Sikeresen beolvasva %d feladat a(z) '%s' fájlból.", len(tasks), file_path)
    except FileNotFoundError:
        logger.warning("A fájl nem található: '%s'. Üres lista tér vissza.", file_path)
    except PermissionError:
        logger.error("Nincs jogosultság olvasni: '%s'. Üres lista tér vissza.", file_path)
    except Exception as e:
        logger.exception("Váratlan hiba olvasás közben ('%s'): %s", file_path, e)
    return tasks

def save_tasks(file_path: pathlib.Path, tasks: list[str], logger: logging.Logger) -> bool:
    try:
        with file_path.open("w", encoding="utf-8") as f:
            f.write("\n".join(tasks))
        logger.info("Sikeres mentés (%d feladat) -> '%s'", len(tasks), file_path)
        return True
    except PermissionError:
        logger.error("Nincs jogosultság írni ide: '%s'.", file_path)
    except Exception as e:
        logger.exception("Váratlan hiba mentés közben ('%s'): %s", file_path, e)
    return False

def add_task(tasks: list[str], task_text: str, logger: logging.Logger) -> list[str]:
    task_text = task_text.strip()
    if not task_text:
        logger.warning("Üres feladatot próbáltak hozzáadni - kihagyva.")
        return tasks
    new_tasks = tasks + [task_text]
    logger.debug("Feladat hozzáadva: %s", task_text)
    return new_tasks

def remove_task(tasks: list[str], index_1_based: int, logger: logging.Logger) -> tuple[list[str], str | None]:
    idx = index_1_based - 1
    if idx < 0 or idx >= len(tasks):
        logger.warning("Érvénytelen törlési index: %s (lista hossza: %s).", index_1_based, len(tasks))
        return tasks, None
    removed = tasks[idx]
    new_tasks = tasks[:idx] + tasks[idx+1:]
    logger.debug("Feladat törölve: %s", removed)
    return new_tasks, removed

def display_menu() -> None:
    print("\n--- TEENDŐK ---")
    print("1) Új feladat hozzáadása")
    print("2) Feladatok megtekintése")
    print("3) Feladat törlése")
    print("4) Mentés és kilépés")
    print("5) Kilépés mentés nélkül")    

def print_tasks(tasks: list[str]) -> None:
    if not tasks:
        print("Nincs egyetlen feladat sem.")
        return
    for i, t in enumerate(tasks, start=1):
        print(f"{i}. {t}")

# ----- főprogram -----
def main() -> None:
    config = load_config(BASE_DIR / "config.yaml")    
    print(BASE_DIR / config["logging_config"])
    print(BASE_DIR / config["log_dir"])
    print(config["log_file"])
    logger = setup_logging(BASE_DIR / config["logging_config"],BASE_DIR / config["log_dir"], config["log_file"])

    TASKS_FILE = BASE_DIR / config["tasks_file"]

    logger.info("Program indul.")

    tasks = load_tasks(TASKS_FILE, logger)

    while True:
        display_menu()
        choice = input(f"{GREEN}Válassz egy funkciót (1-5): {RESET}").strip()

        #Új feladat felvétele
        if choice == "1":
            text = input("Írd be az új feladatot: ")
            tasks = add_task(tasks, text, logger)
            print("Hozzáadva.")

        #Feladatok listázása
        elif choice == "2":
            print_tasks(tasks)

        #feladatok törlése
        elif choice == "3":
            if not tasks:
                print("Nincs mit törölni.")
                continue
            print_tasks(tasks)
            raw = input("Melyik sorszámot töröljem? ").strip()
            try:
                idx = int(raw)
            except ValueError:
                print(f"{RED}Érvénytelen sorszám.{RESET}")
                continue
            tasks, removed = remove_task(tasks, idx, logger)
            if removed is None:
                print(f"{RED}Érvénytelen sorszám.{RESET}")
            else:
                print(f"Törölve: {removed}")

        #Feladatok mentése
        elif choice == "4":
            ok = save_tasks(TASKS_FILE, tasks, logger)
            print("Feladatok elmentve." if ok else "Mentés sikertelen. Részletek a logban.")
            break

        #Kilépés mentés nélkül
        elif choice == "5":
            break        

        else:
            print(f"{RED}Érvénytelen választás. A lehetséges válaszok: 1, 2, 3, 4, 5.{RESET}")

    logger.info("Program leáll.")

main()
