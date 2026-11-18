
class Employee:
    # --- 1. Initializer --------------------------------------------
    # Runs automatically when a new Employee object is created.
    # Double underscores make the attributes private.
    def __init__(self, name, employee_id, department, title):
        self.__name = name
        self.__employee_id = employee_id
        self.__department = department
        self.__title = title

    # --- 2. Accessor (getter) methods -------------------------------
    def get_name(self):
        return self.__name

    def get_employee_id(self):
        return self.__employee_id

    def get_department(self):
        return self.__department

    def get_title(self):
        return self.__title

    # --- 3. Mutator (setter) methods --------------------------------
    def set_name(self, name):
        self.__name = name

    def set_department(self, department):
        self.__department = department

    def set_title(self, title):
        self.__title = title

    # --- 4. __str__ --------------------------------------------------
    # Returns a string describing the employee.
    def __str__(self):
        return (f"Name: {self.__name}\n"
                f"ID number: {self.__employee_id}\n"
                f"Department: {self.__department}\n"
                f"Title: {self.__title}")
