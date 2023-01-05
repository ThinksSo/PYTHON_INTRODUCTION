import user_menu
import data_save
import data_export
import data_import
import fimport


def user_choice():
    choice = user_menu.user_menu()
    if choice == "1":
        file = 'PYTHONTASKS/TASKS_S07/phonebook.csv'
        db = open(file, "r+")
        contents = db.read()
        if len(contents) == 0:
            print("No contact in the phonebook.")
        else:
            print(contents)
        db.close
        enter = input("Press Enter to continue ...\n")
        user_choice()
    elif choice == "2":
        data = data_import.input_data()
        data_save.new_contact(data)
        enter = input("Press Enter to continue ...")
        user_choice()
    elif choice == "3":
        data_export.search()
        enter = input("Press Enter to continue ...")
        user_choice()
    elif choice == "4":
        fimport.import_file()
        enter = input("Press Enter to continue ...")
        user_choice()
    elif choice == "0":
        print("Thank you! \n")
    else:
        print("Invalid input, please try again\n")
        enter = input("Press Enter to continue ...")
        user_choice()
