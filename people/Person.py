from datetime import date
from random import randrange
from dateutil import parser


class Person:
    """
    This class represents a person within the University.
    """

    __email = ""
    __phone = ""
    __address = ""
    __zip = ""
    __state = ""
    __city = ""

    def __init__(self, fname: str, lname: str, dob:str, preferred_name: str=""):
        """
        Base constructor for Person class.
        :param fname: Person first name.
        :param lname: Person last name.
        :param preferred_name: Person preferred name - defaults to "".
        :param dob: Person dob as String
        """
        self._id = randrange(10000, 999999999)
        self.__fname = fname
        self.__lname = lname
        self._preferred_name = preferred_name
        # this is not a great way to do this but not writing the regex
        self.__dob = parser.parse(dob).date()

    @property
    def name(self) -> str:
        """
        Returns the person's name
        If a preferred name is given, it returns the preferred name.
        If not, it returns the person's first and last name.
        :return: person's name
        """
        if self._preferred_name != "":
            return self._preferred_name
        return self.__fname + " " + self.__lname

    @name.setter
    def name(self, new_name: str):
        """
        Sets the person's preferred name
        :param new_name: new preferred name
        """
        self._preferred_name = new_name

    def set_full_name(self, fname: str, lname: str):
        """
        Sets the person's full name given a new first & last name
        :param fname: person's first name
        :param lname: person's last name
        """
        self.__fname = fname
        self.__lname = lname

    # We will add a few default getters and setters
    @property
    def dob(self) -> date:
        return self.__dob

    def age(self) -> int:
        """
        Returns the person's age
        :return: Today - DOB // 365 (age in years)
        """
        return (date.today() - self.__dob).days // 365

    @dob.setter
    def dob(self, new_dob: str):
        self.__dob = parser.parse(new_dob).date()

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, new_email: str):
        if new_email != "" and "@" in new_email:
            self.__email = new_email

    @property
    def phone(self) -> str:
        return self.__phone

    @phone.setter
    def phone(self, new_phone: str):
        self.__phone = new_phone

    @property
    def address(self) -> str:
        return self.__address

    @address.setter
    def address(self, new_address: str):
        self.__address = new_address

    @property
    def zip(self) -> str:
        return self.__zip

    @zip.setter
    def zip(self, new_zip: str):
        self.__zip = new_zip

    @property
    def state(self) -> str:
        return self.__state

    @state.setter
    def state(self, new_state: str):

    @property
    def city(self) -> str:
        return self.__city

    @city.setter
    def city(self, new_city: str):
        self.__city = new_city
