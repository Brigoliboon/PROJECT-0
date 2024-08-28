# Source file for Contact class that is holding the user's information

class Contact:
    """
        A contact object used by Phonebook. Each contact has their own
        name, student number, contact number, and occupation. 
        
        The full contact number of a contact is a combination of its country code, area code,
        and contact number, IN ORDER.
    """
    #database for country codes
    COUNTRY_CODES = {
        60: "Federation of Malaysia", # Malaysia
        62: "Republic of Indonesia", # Indonesia
        63: "Republic of the Philippines", # Philippines
        65: "Republic of Singapore", # Singapore
        66: "Kingdom of Thailand", # Thailand
        84: "Socialist Republic of Vietnam", # Vietnam
        673: "Brunei Darussalam", # Brunei
        855: "Kingdom of Cambodia", # Cambodia
        856: "Lao People's Democratic Republic", # Burma
        95: "Republic of the Union of Myanmar", # Myanmar
        670: "Democratic Republic of Timor Leste" # Timor Leste
    }
    # Contact __init__
    def __init__(self, stdn: str, fname: str, sname: str, occupation: str,
                    gender: str, cc: int, area: int, number: int):
        """
        Args:
            stdn (str): Student number
            fname (str): First name of the contact
            sname (str): Last name of the contact
            occupation (str): Contact's work title
            gender (str): Contact's gender
            cc (int): Contact's country code
            area (int): Contact's area code
            number (int): Contact's contact number
        """
        self.student_num = stdn
        self.fname = fname
        self.lname = sname 
        self.occupation = occupation
        self.gender = gender 
        self.cc = cc 
        self.area = area
        self.number = number 
    #mainly for debugging purposes
    def __repr__(self) -> str:
        #inconsistent variable names: std -> student_num, sname -> lname
        return f"Contact(std={self.student_num}, fname={self.fname}, sname={self.lname}, occupation={self.occupation},gender={self.gender},cc={self.cc},area={self.area}, number={self.number})"
    #<-------- READ -------->
    # get contact's student number
    def getStudentNumber(self) -> str:
        """Get the contact's student number.

        Returns:
            str: String student number.
        """
        return self.student_num
    #get the contact's first name
    def getFName(self) -> str:
        """Get the contact's first name.

        Returns:
            str: First name.
        """
        return self.fname
    #get the contact's last name
    def getLName(self) -> str:
        """Get the contact's last name

        Returns:
            str: Last name.
        """
        return self.lname
    #get the contact's full name (self.fname, self.lname)
    def getFullName(self) -> str:
        """Gets the full name of the contact, which is a concatenation 
        of its first name and last name.

        Returns:
            str: Full name of the contact.
        """
        return self.fname + " " + self.lname
    #get contact's occupation
    def getOccupation(self) -> str:
        """Get the contact's occupation or work.

        Returns:
            str: Occupation.
        """
        return self.occupation
    #get contact's gender
    def getGender(self) -> str:
        """Get the contact's gender.

        Returns:
            str: Male or Female.
        """
        return self.gender
    #get contact's pronoun
    def getPronoun(self) -> str:
        return "His" if self.getGender() == "M" else "Her"
    #get contact's country code
    def getCountryCode(self) -> str:
        """Gets the string value of the contact's country code.
        This refers to the different countries and their respective 
        country codes

        Returns:
            str: The name of the country associated to that country code value.
        """
        return Contact.COUNTRY_CODES[self.getNumericCountryCode()]
    #get contact's country code(self.cc) -> int
    def getNumericCountryCode(self) -> int:
        """Get the numeric country code of this contact.

        Returns:
            int: Numeric country code.
        """
        return self.cc
    #get contact's area code(self.area) -> int
    def getAreaCode(self) -> int:
        """Get numeric area code of this contact

        Returns:
            int: Numeric area code.
        """
        return self.area
    #get contact's number(self.number) -> int
    def getContactNumber(self) -> int:
        """Get the contact number of this contact.

        Returns:
            int: Contact number only.
        """
        return self.number
    #get contact's full number(concat using formatter"{}-{}-{}": getNumericCountryCode()->int, getAreaCode()->int, getContactNumber()->int)
    def getFullContactNumber(self) -> str:
        """Get the full contact number of this contact.

        Returns:
            str: Full contact number, including numeric country code, 
            area code, and contact number.
        """
        return "{}-{}-{}".format(self.getNumericCountryCode(),
                                self.getAreaCode(),
                                self.getContactNumber())
    #get contact's Contact<Object> attributes
    #<----- activity -----> status: Completed && Bonus: 2pts
    def get(self, attr: str) -> any:
        """
            Get the value of selected attribute for this object.

            Args:
                self (Contact): This object.
                attr (str): Attribute of this object to retrieve from.
        """
        # Optionally complete this method for up to 2 additional points in your MTE.
        attributes = {
            'student_num':self.getStudentNumber,
            'fname':self.getFName,
            'lname':self.getLName,
            'occupation':self.getOccupation,
            'gender':self.getGender,
            'cc':self.getCountryCode,
            'area':self.getAreaCode,
            'number':self.getContactNumber,
                      }
        if attr in attributes:
            attribute = attributes[attr]
            return attribute()
        return None
    #<-------- UPDATE -------->
    #update contact's student number    
    def setStudentNumber(self, new_stdn: str) -> None:
        """Sets a new student number of this contact.
        Args:
            new_stdn (str): New student number.
        """
        self.student_num = new_stdn
    #update contact's first name
    def setFName(self, new_fname : str) -> None:
        """Sets a new new first name of this contact.

        Args:
            new_fname (str): New first name.
        """
        self.fname = new_fname
    #update contact's last name
    def setLName(self, new_sname: str) -> None:
        """Sets a new last name of this contact.

        Args:
            new_sname (str): New last name.
        """
        self.lname = new_sname
    #update contact's gender   
    def setGender(self, new_gender: str) -> None:
        """Sets a new gender of this contact. Must be either M or F.
        Will return -1 if new gender value is invalid.
        Args:
            new_gender (str): _description_
        """
        if new_gender.capitalize() != "M" or new_gender.capitalize != "F":
            print("Sorry, that is an invalid value for gender.")
            return -1
        else: 
            self.gender = new_gender
    #update contact's occupation
    def setOccupation(self, new_occupation: str) -> None:
        """Sets a new occupation of this contact.

        Args:
            new_occupation (str): New occupation.
        """
        self.occupation = new_occupation
    #update contact's country code
    def setCountryCode(self, new_country_code: int) -> None:
        """Sets a new country code for this contact. 
        New country code must exist in the current.
        Returns -1 if new country code is not successfully set.

        Args:
            new_country_code (int): New country code.
        """
        if not new_country_code in Contact.COUNTRY_CODES:
            print("Sorry, this country code does not exist. Try again.")
            return -1
        else: 
            self.cc = new_country_code
    #update contact's area code      
    def setAreaCode(self, new_area: int) -> None:
        """Sets a new area code for this contact.

        Args:
            new_area (int): New area code.
        """
        self.area = new_area
    #update contact's contact number
    def setContactNumber(self, new_number: int) -> None:
        """Sets new contact number for this contact.

        Args:
            new_number (int): New contact number.
        """
        self.number = new_number
    #<----- activity -----> status: Completed
    @staticmethod
    def compareNames(c1: 'Contact', c2: 'Contact', comparison_type: int = 0) -> int:
        """Compares the names of two different contacts. 
        
        Args:
            c1 (Contact): Contact 1
            c2 (Contact): Contact 2
            comparison_type (int): 0 to compare last names. 1 to compare first names. Defaults to 0.
 
        Returns:
            int: 1 if name value of c1 > c2.
            0 if both contacts have same name value.
            -1 if name value of c1 < c2.
        """
        # Complete this method
        #switch-case
        match comparison_type:
            case 0: #compare last names
                if c1.getLName() > c2.getLName():
                    return 1
                elif c1.getFName() < c2.getFName():
                    return -1
                else:
                    return 0
            case 1: #compare first names
                if c1.getLName() > c2.getLName():
                    return 1
                elif c1.getLName() < c2.getLName():
                    return -1
                else:
                    return 0       
    #<----- activity -----> status: Completed && Bonus: 3pts
    @staticmethod
    def compare(c1: 'Contact', c2: 'Contact', modifier: str) -> int:
        """
            Compares two contacts based on a comparison method.

        Args:
            c1 (Contact): Contact 1
            c2 (Contact): Contact 2
            modifier: Attribute to compare with one another with.

        Returns:
            int: 1 if c1 wins comparison over c2. 0 if both contact are equal in comparison. -1 if c1 loses comparison to c2.
        """
        # Optionally complete (and only utilize this method instead of the compareNames() method)
        # in comparing attribute values (used in completing another bonus part of the project)
        # Bonus points may receive up to 3 points in your MTE.
        match modifier:
            case 'lname':
                return Contact.compareNames(c1,c2,0)
            case 'fname':
                return Contact.compareNames(c1,c2,1)
        c1= c1.get(modifier)
        c2= c2.get(modifier)
        if c1 and c2 is not None:
            if c1 > c2:
                return 1
            elif c1 < c2:
                return -1
            else:
                return 0
    def __str__(self) -> str:
        """Returns a string representation of this contact."""
        return "{}, {}, with student number {}, is a/an {}. {} phone number is {}.".format(
            self.getLName(), self.getFName(), self.getStudentNumber(), self.getOccupation(),
            self.getPronoun(), self.getFullContactNumber())
