# import from file
def import_file(): 
    with open('PYTHONTASKS/TASKS_S07/input.csv') as source, open('PYTHONTASKS/TASKS_S07/phonebook.csv', 'a') as destination:
        for line in source:
            destination.write(line)
            print(f"Contact {line} added")
    print("Import completed successfully \n")
