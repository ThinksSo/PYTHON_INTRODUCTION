# defining search function         
def search(): 
    db = 'PYTHONTASKS/TASKS_S07/phonebook.csv'
    search_name = input( "Enter a name to search: ") 
    find_name = search_name[1:] 
    first_char = search_name[0] 
    search_name = first_char.upper() + find_name 
    file = open(db, "r+") 
    filecontents = file.readlines() 
      
    found = False 
    for line in filecontents: 
        if search_name in line: 
            print( "Contact is:", end = " ") 
            print(line) 
            found = True 
            break 
    if found == False: 
        print(f"The contact {search_name} isn't in the Phonebook") 
        