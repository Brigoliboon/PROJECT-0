# Main Python File to run from
from ContactArray import ContactList
from Contact import Contact

MENUS = {
    "main": {
        1: "Store to ASEAN Phonebook",
        2: "Edit entry in ASEAN Phonebook",
        3: "Delete entry from ASEAN Phonebook",
        4: "View/Search ASEAN Phonebook",
        5: "Exit"
    },
    "views": {
        1: "Search by country",
        2: "Search by surname",
        3: "View all",
        4: "Go back to main menu"
    },
    "edit": {
        1: "Student Number",
        2: "Surname",
        3: "Gender",
        4: "Occupation",
        5: "Country Code",
        6: "Area Code",
        7: "Phone Number",
        8: "None - Go back to main menu"
    },
    "cc": {
        1: "Burma", # 856
        2: "Cambodia", # 855
        3: "Thailand", # 66
        4: "Vietnam", # 84
        5: "Malaysia", # 60
        6: "Philippines", # 63
        7: "Indonesia", # 62
        8: "Timor Leste", # 670
        9: "Laos", # 95
        10: "Brunei", # 673
        11: "Singapore", #65
        12: "All",
        0: "No More"
    }
}
#displays menu on terminal
def showMenu(   target: str, inline :int = None):
    """Shows the target menu in the ASEAN Phonebook program.
    
    Args:
        target (str): Target menu to show. Refer to MENUS dictionary.
        inline (int): If not none, then will create an inline menu with n items each.
    """
    print("\n<-----Menu----->")
    i = 1 if inline != None else None
    for menu in MENUS[target]:
        out = "[{}]".format(menu)
        if inline != None and i == inline:
            out = "\n[{}]".format(menu)
        print("{} {}".format(out, MENUS[target][menu]), end= "\t" if inline != None else "\n")
        if i != None:
            i = 1 if i == inline else i + 1
#returns Contact<object>     
def receiveContactInfo() -> Contact:
    """Cast several prompts for user to input about the
    contact's data.

    Returns:
       Contact: Contact object created based from data.
    """
    stdn = prompt("Enter student number: ")    
    lname = prompt("Enter surname: ")
    fname = prompt("Enter first name: ")
    occupation = prompt("Enter occupation: ")
    gender = prompt("Enter gender (M for male, F for female): ")
    cc = int(prompt("Enter country code: "))
    area = int(prompt("Enter area code: "))
    number = int(prompt("Enter number: "))
    return Contact(stdn,fname,lname,occupation,gender,cc,area,number)
#returns a string type of prompt received from user
def prompt(phrase: str) -> str:
    """Prompts an input to the user

    Args:
        phrase (str): Input phrase.

    Returns:
        str : Returns a string type of inputted value.
    """
    return input(phrase)
# match case logic for ASEAN country codes
def convertChoices(choices: list) -> list:
    """Converts choices from the phonebook menu
    into proper country code value for accuracy purposes.

    Args:
        choices (list): Choices selected by user during prompt.

    Returns:
        list: Converted values of choices.
    """
    for i in range(0, len(choices)):
        match choices[i]:
            case 1:
                choices[i] = 856
            case 2:
                choices[i] = 855
            case 3:
                choices[i] = 66
            case 4: 
                choices[i] = 84
            case 5:
                choices[i] = 60
            case 6:
                choices[i] = 63
            case 7:
                choices[i] = 62
            case 8:
                choices[i] = 670
            case 9:
                choices[i] = 95
            case 10:
                choices[i] = 673
            case 11:
                choices[i] = 65
    return choices
#variables
error_message:str = "Error Message: {}"
contact_notFound = "Contact with the {} '{}' was not found."
enter_studentNum: str = "Enter student nummber: "
# <----- CREATE ---->
createContact_success: str  = "Contact successfully added..."
createContact_failed: str = "Contact failed to add."
# <----- Update ----->
updateContact_dir: dict = MENUS['edit']
updateContact_func: dict = {1:Contact.setStudentNumber, 2:Contact.setLName, 3:Contact.setGender, 4:Contact.setOccupation, 5:Contact.setCountryCode, 6:Contact.setAreaCode, 7:Contact.setContactNumber}
updateContact_header: str = "Here is the existing information about {}"
updateContact_headerConfirm: str = "Which of the following do you wish to change?"
updateContact_change: str = "Enter new {}: "
#<----- DELETE ----->
deleteContact_confirmation: str = "Are you sure you want to delete this contact [Y/N]?"
deleteContact_success: str = "Contact {} has been successfully deleted."
deleteContact_cancelled:str = "Contact {} deletion cancelled."
# <----- READ ----->
readContact_countryHeader:str = "Here are the students from {}."
if __name__ == "__main__":
    pb = ContactList()
    while True:
        showMenu("main")
        opt = int(input("Select Operation: "))
        # Complete your code here
        if opt in MENUS['main']:
            match opt:
                case 1: # [1] Store to ASEAN Phonebook
                    while True:
                        try:
                            contact = receiveContactInfo()
                            pb.insert(contact)
                            print(createContact_success)
                        except ValueError as error:
                            print(createContact_failed)
                            print(error_message.format(error))
                        user_prompt = prompt("Do you want to add a new one (Y / N)? ")
                        if user_prompt.capitalize() == "Y":
                            continue
                        break
                case 2: # [2] Edit entry in ASEAN Phonebook
                    student_number = prompt(enter_studentNum)
                    contact = pb.getContact(student_number)
                    if contact is not None:
                        print(updateContact_header.format(contact.getStudentNumber()))
                        print(contact)
                        print(updateContact_headerConfirm)
                        showMenu("edit")
                        opt = int(input("Enter choice: "))
                        if opt in updateContact_dir:
                            new_value = prompt(updateContact_change.format(updateContact_dir[opt]))
                            updateContact_func[1](contact, new_value)
                        elif opt == 8:
                            continue
                    else:
                        print(contact_notFound.format("student number",student_number))
                case 3: # [3] Delete entry from ASEAN Phonebook
                    student_number = prompt(enter_studentNum)
                    contact = pb.getContact(student_number)
                    if contact is not None:
                        confirmation = prompt(deleteContact_confirmation)
                        if confirmation.capitalize() == "Y":
                            pb.deleteContact(student_number)
                            print(deleteContact_success.format(student_number))
                        elif confirmation.capitalize() == "N":
                            print(deleteContact_cancelled)
                case 4: # [4] View/Search ASEAN Phonebook
                    showMenu("views")
                    opt = int(input("Select Operation: "))
                    match opt:
                        case 1: # [1] Search by country
                            choices = []
                            print("From which country:")
                            showMenu("cc",inline=5)
                            while True:
                                opt = int(input("Enter choice {}: ".format(len(choices)+1)))
                                if opt in MENUS['cc'] and opt != 0:
                                    choices += str(opt)
                                    continue
                                elif opt == 0:
                                    print(pb.__str__(f=convertChoices([int(choice) for choice in choices]), by='cc'))
                                    break
                        case 2: # [2] Search by surname
                            surname = input("Enter surname: ")
                            contact = pb.getContactBySurname(surname)
                            if contact is not None:
                                print(contact.__str__())
                            else:
                                print(contact_notFound.format("surname", surname))
                        case 3: # [3] View all
                            print(pb.__str__())
                        case 4: # [4] Go back to main menu
                            pass
                case 5: # [5] Exit
                    exit()
