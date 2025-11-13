import logging
import os
from pathlib import Path

# Logging konfigurálása - konzolra és file-ba is

LOG_FILE = Path("homeworks") / "mezofigabor" / "hw_04_exceptions_logging" / "to_do.log"

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE, encoding='utf-8'),
        logging.StreamHandler()
    ]
)

TASKS_FILE = Path("homeworks") / "mezofigabor" / "hw_04_exceptions_logging" / "sample.txt"


def read_tasks():
    """Feladatok beolvasása a fájlból."""
    tasks = []
    try:
        if os.path.exists(TASKS_FILE):
            with open(TASKS_FILE, 'r', encoding='utf-8') as f:
                tasks = [line.strip() for line in f.readlines() if line.strip()]
            logging.info(f'{len(tasks)} feladat betöltve a fájlból.')
        else:
            logging.info('A feladatok fájl nem létezik, új lista létrehozása.')
    except Exception as e:
        logging.error(f'Hiba a feladatok olvasása közben: {e}')
    return tasks


def write_tasks(tasks):
    """Feladatok kiírása a fájlba."""
    try:
        with open(TASKS_FILE, 'w', encoding='utf-8') as f:
            for task in tasks:
                f.write(task + '\n')
        logging.info(f'{len(tasks)} feladat sikeresen mentve a fájlba.')
    except Exception as e:
        logging.error(f'Hiba a feladatok írása közben: {e}')


def display_tasks(tasks):
    """Feladatok megjelenítése."""
    if not tasks:
        print('\nNincs egyetlen feladat sem a listában.')
        logging.info('Feladatok megjelenítése: üres lista.')
    else:
        print('\n=== Feladatok ===')
        for i, task in enumerate(tasks, 1):
            print(f'{i}. {task}')
        print('=================')
        logging.info(f'{len(tasks)} feladat megjelenítve.')


def add_task(tasks, task):
    """Egy feladat hozzáadása a listához."""
    if task:
        tasks.append(task)
        print(f'\nFeladat hozzáadva: "{task}"')
        logging.info(f'Új feladat hozzáadva: {task}')
    else:
        print('\nÜres feladatot nem lehet hozzáadni!')
        logging.warning('Üres feladat hozzáadására történt kísérlet.')


def remove_task(tasks, index):
    """Egy feladat törlése a listából."""
    try:
        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            print(f'\nFeladat törölve: "{removed}"')
            logging.info(f'Feladat törölve: {removed}')
        else:
            print(f'\nÉrvénytelen index! Válassz 1 és {len(tasks)} közötti számot.')
            logging.warning(f'Érvénytelen index törlésre: {index}')
    except Exception as e:
        logging.error(f'Hiba a feladat törlése közben: {e}')


def display_menu():
    """Menü megjelenítése."""
    print('\n=== Feladatkezelő ===')
    print('1. Feladat hozzáadása')
    print('2. Feldatatok megjelenítése')
    print('3. Feladat törlése')
    print('4. Kilépés')
    print('=====================')
