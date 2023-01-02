# data save to phonebook

def new_contact(contact_info): 
    db = 'PYTHONTASKS/TASKS_S07/phonebook.csv'
    with open (db, 'a', encoding = 'utf-8') as data:
        data.write(contact_info)
    print( "The contact : \n" + contact_info + " has been save \n")
