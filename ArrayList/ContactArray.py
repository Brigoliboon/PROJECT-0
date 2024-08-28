# Array List implementation of Contacts
from Contact import Contact
#ContactList<object> stores the Contact<object> in an array
class ContactList:
    """Contact List class that creates an array list of the phonebook.
    """
    
    def __init__(self, size: int = 50):
        """
            Create an array list of contacts with default storage size of 50.
        """
        self.phonebook = [None] * size
        self.size = 0
    #get's the size of the ContactList
    def getSize(self):
        """
            Get the size of this contact list.
        """
        return self.size
    #<----- activity -----> status: Completed
    def first(self) -> Contact:
        """
            Get the first contact in this contact list.
            Returns none if the list is empty.
        """
        # Complete this Method
        if self.isEmpty():
            return None
        else:
            return self.getContactAtIndex(0)
    #<----- activity -----> status: Completed
    def getLast(self) -> Contact:
        """
            Get the last contact in this contact list.
            Returns none if the list is empty.
        """
        # Complete this Method
        if self.isEmpty():
            return None
        else:
            return self.getContactAtIndex(self.getSize()-1)
    #<----- activity -----> status: Completed
    def getContactAtIndex(self, index: int) -> Contact:
        """Gets the contact at given index in the contact linked list.
        Returns None if index is not found in the list.

        Args:
            index (int): Index to get in the contact linked list.

        Returns:
            Contact: Contact at index.
        """
        # Complete this Method
        if self.phonebook[index] is not None:
            return self.phonebook[index]
        else:
            return None
    #<----- activity -----> status: Completed
    def getContact(self, student_num: str) -> Contact:
        """Gets the contact based on given student number. Will return None
        if contact is not found.

        Args:
            student_num (str): Student number to base search from.

        Returns:
            Contact: Contact information.
        """
        contact:Contact
        # Complete this Method
        for index in range(self.getSize()):
            contact = self.getContactAtIndex(index)
            if contact.getStudentNumber() == student_num:
                return contact
        return None
    #<----- activity -----> status: Completed
    def getContactBySurname(self, surname: str) -> Contact:
        """Gets the contact based on surname. Will return None if contact is not found.
        """
        # Complete this Method
        for i in range(self.getSize()):
            if self.getContactAtIndex(i).getLName() == surname:
                return self.getContactAtIndex(i)
        return None
        
    def isEmpty(self) -> bool:
        """
            Checks if contact list has no contacts.
        """
        return self.getSize() == 0
    #<----- activity -----> status: Completed
    def incrSize(self) -> None:
        """
            Increase the size of this contact list.
        """
        # Complete this Method
        self.size += 1
    def decrSize(self) -> None:
        """
            Decrease the size of this contact list
        """
        self.size -= 1
    #<----- activity -----> status: Completed
    def __increasePhonebookSize(self) -> None:
        """
            Increases the size of this phonebook by two times.
        """
        # Complete this Method
        self.size *= 2
    #<----- activity -----> status: incomplete
    def insert(self, c: Contact) -> None:
        """Inserts new contact at index point.

        Args:
            c (Contact): Contact to be inserted.
        """
        if self.isEmpty():
            self.phonebook[0] = c
            self.incrSize()
        else:
            index = self.__findIndexInsertion(c)
            if index is not None:
                self.__adjustPhonebook(start=index, end=self.size, dir='f')
                self.phonebook[index] = c
                self.incrSize()
            else:
                self.__increasePhonebookSize()
                self.phonebook[self.getSize()] = c
                self.incrSize()
    #<----- activity -----> status: Completed
    def __findIndexInsertion(self, c: Contact) -> int:
        """Finds the index to insert from based on contact's
        last name, and first name if both have the same first names.

        Args:
            c (Contact): Contact to compare and to be inserted.

        Returns:
            int: Node insertion point for new contact.
        """
        f_status:int
        l_status:int
        # Complete this Method
        if not self.isEmpty():
            #iterates all the contacts in the phonebook:list <variable>
            for i in range(self.size):
                l_status = Contact.compare(c,self.phonebook[i],'lname')
                f_status = Contact.compare(c,self.phonebook[i],'fname')
                if l_status == 0: #checks if phonebook[i].lname == c.lname -> 0
                    if f_status == 0: #checks if phonebook[i].fname == c.fname -> 0
                        print(f"the contact {c.getFullName()} is already on the phonebook")
                    else: #if phonebook[i].fname != c.fname
                        if f_status == -1:
                            return i
                else:
                    # continues to iterate until l_status := -1 (while phonebook[i] < c then that means c must be put on a higher index)
                    if l_status == -1:
                        return i
            return self.size
    #<----- activity -----> status: Completed
    def __adjustPhonebook(self, start: int, end = int, dir: str = "f") -> None:
        """
        Adjusts the arrangement of this phonebook from start to end.

        Args:
            index (int): Index for adjustment.
            dir (str): Direction of adjustment:
                "f" -> Forward indexing adjustment. For example, element at index 0 takes the value of the element at index 1.
                "b" -> Backward indexing adjustment. For example, elemet at index 1 takes the value of the element at index 0.
        """
        # Complete this Method
        index = end
        match dir:
            case 'f': #when you insert a contact in the list
                while index != start: #moves the Nonetype from the end to the starting position to make room for the contact to be inserted
                    #visualize it like this (x,y) -> (y,x)
                    x = index-1 
                    y = index #first last index retrieves Nonetype
                    self.phonebook[x], self.phonebook[y] = self.phonebook[y], self.phonebook[x]
                    index -=1
            case 'b': #when you delete a contact in the list
                for index in range(start, end):
                    x = index
                    y = index + 1
                    self.phonebook[x], self.phonebook[y] = self.phonebook[y], self.phonebook[x]
    #<----- activity -----> status: Completed
    def deleteContact(self, stdn: str) -> Contact:
        """Finds the contact based on their student number.
        Returns the deleted contact. Otherwise, returns -1 if not found.

        Args:
            stdn (str): Student number of contact to be deleted.

        Returns:
            Contact: Deleted contact, if found.
        """
        # Complete this Method
        __contact = self.getContact(stdn)
        if __contact is not None:
            for index in range(self.size):
                contact = self.getContactAtIndex(index)
                if Contact.compare(contact, __contact,'student_num') == 0:
                    self.phonebook[index] = None
                    self.__adjustPhonebook(index,end=self.size,dir='b')
                    self.decrSize()
                    return contact
        return -1
    #<----- activity -----> status: Complete && Bonus: 4pts
    def __sort(self, by: str) -> list:
        """
            Sorts the phonebook based on the contact's attribute value.
        
            Args:
                by (str): Attribute value to sort the phonebook from.
            
            Returns:
                list: A copy of this phonebook list sorted based on the attribute value given.
        """
        # Complete this method optionally
        # Correctly completing this method will reward up to 4 bonus points in your MTE.
        # Using __findIndexInsertion & __adjustphonebook method is the best way to go but it is lacking on flexibility so let's use almost the same algorithm instead
        phonebook:list = [contact for contact in self.phonebook if contact is not None] # store's all Contact from the ContactList.phonebook
        # Heap's Algorithm
        for x in range(len(phonebook)-1):
            min_index = x
            for y in range(x+1, len(phonebook)):
                if Contact.compare(phonebook[min_index], phonebook[y], modifier=by) == 1:
                    min_index = y
            phonebook[min_index],phonebook[x] = phonebook[x], phonebook[min_index]
        return phonebook
    #<----- activity -----> status: Complete && Bonus: 1pts
    def __str__(self, f = None, by: str = 'lname') -> str:
        """
        Prints every contact in this contact list.

        Args:
            f (list, optional): A list that filters which contact should
                be outputted in the list of country codes. Defaults to None.
            by (str): Condition whether to print contact on a particular order based from some attribute.
            Note, completing the bonus functionality from this argument is optional.

        Returns:
            str: Every contact in this contact list in a particular order.
        """
        # Complete this method
        s = "<----Phonebook---->"
        if not self.isEmpty():
            # Complete this method.
            # Optionally include viewing contacts in a particular order for up to 1 bonus point in your MTE.
            # You can use the __sort method to sort the contacts before printing them.
            sorted_phonebook = self.__sort(by)
            if f is not None:   
                filtered = [contact for contact in sorted_phonebook if contact.cc in f]
                sorted_phonebook = filtered
            for contact in sorted_phonebook:
                    s += "\n" + str(contact)
        else:
            s += "\nThis phonebook is currently empty..."
        s += "\n<----End---->"
        return s
