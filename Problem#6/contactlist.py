# Mohamad ali fakhoury @ Thurs 2pm
def process_user_contacts(user_input):
    user_contacts = user_input.split()
    contact_dict= {}
    x=0
    tes =[]
    while x< len(user_contacts):
     pretes = str(user_contacts[x])
     tes = str(pretes).split(",")
     contact_dict[tes[0]]= tes[1]
     tes = []
     x=x+1
    
    # Get contact name from input, output contact's phone number
    else:
     contact_name = input("Enter the contact name: ")
     print(contact_dict[contact_name])
    
   
if __name__ == '__main__':
    user_input = input("Enter word pairs (name, phone number): ")

    process_user_contacts(user_input)
