def feladatok_olvasasa():
    pass

def feladatok_irasa():
    pass

def feladatok_megjelenitese():
    pass

def egy_feladat_hozzaadasa():
    pass

def egy_fealadat_torlese():
    pass

def display_menu():
    print("What do you want to do? Please select the number: ")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

def get_user_response():
    if response == "1":
        return egy_feladat_hozzaadasa()
    elif response == "2":
        return feladatok_megjelenitese()
    elif response == "3":
        return egy_fealadat_torlese()
    elif response == "4":
        print ("Exit")
        #break

while True:
    display_menu()
    response = input("Select one option (1-4):")
    if response not in ["1", "2", "3", "4"]:
        print("Give a valid number")
    elif get_user_response()
    
