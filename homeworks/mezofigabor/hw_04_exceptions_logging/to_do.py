from  to_do_resource import *

def main():
    
    logging.info('Feladatkezelő alkalmazás indítása.')
    
    # Feladatok betöltése a program indításakor
    tasks = read_tasks()
    
    while True:
        display_menu()
        choice = input('Válassz egy opciót (1-4): ').strip()
        
        # Input ellenőrzése
        if choice not in ['1', '2', '3', '4']:
            print('\nÉrvénytelen választás! Kérlek válassz 1, 2, 3 vagy 4 közül.')
            logging.warning(f'Érvénytelen menüválasztás: {choice}')
            continue
        
        if choice == '1':
            task = input('\nÍrd be az új feladatot: ').strip()
            add_task(tasks, task)
        
        elif choice == '2':
            display_tasks(tasks)
        
        elif choice == '3':
            display_tasks(tasks)
            if tasks:
                try:
                    index = int(input('\nMelyik feladatot szeretnéd törölni? (szám): '))
                    remove_task(tasks, index)
                except ValueError:
                    print('\nÉrvénytelen bemenet! Adj meg egy számot.')
                    logging.warning('Érvénytelen szám bemenet a törléshez.')
        
        elif choice == '4':
            # Kilépés előtt mentés
            write_tasks(tasks)
            print('\nViszlát! A feladatok mentve.')
            logging.info('Feladatkezelő alkalmazás bezárása.')
            break

# Ezt beletettem mert tök jó cucc:). Csak akkor fut le a main ha ezt a fájlt futtatjuk.Import esetén nem fut le.
if __name__ == '__main__':
    main()