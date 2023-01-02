# data import
def input_data(): 
    firstname = input( "Enter your First Name: ") 
    lastname = input( "Enter your Last Name: ")
    phone_num = input( "Enter your Phone number: ")
    other = input( "Enter details: ") 
    contact_info =(firstname + ',' + lastname + ',' + phone_num + ',' + other + '\n')
    return contact_info

