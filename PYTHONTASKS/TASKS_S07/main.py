from os.path import exists
import processing

# PHONEBOOK
print('\n \t PHONEBOOK')

path = 'PYTHONTASKS/TASKS_S07/phonebook.csv'
valid = exists(path)
if not valid:
    file = 'PYTHONTASKS/TASKS_S07/phonebook.csv'
    with open (file, 'w', encoding = 'utf-8') as data:
        data.write(f'LastName,FirstName,PhoneNumber,Details\n')


processing.user_choice()

