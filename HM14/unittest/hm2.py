class String:
    @classmethod
    def verify_fio(cls, coord):
        if type(coord) != str:
            raise TypeError ("Ошибка введеного ФИО!")

        if not coord.istitle() or not coord.isalpha():
            raise TypeError("Ошибка введеного ФИО!")

    def __set_name__(self, owner, name):
        self.name = "_" + name
    
    def __get__(self, instance, owner):
        return instance.__dict__[self.name]
    
    def __set__(self, instance, value):
        self.verify_fio(value)
        instance.__dict__[self.name] = value



class Student:
    personal_name = String()
    first_name = String()
    second_name = String()

    def __init__(self,personal_name,first_name,second_name):
        self.personal_name = personal_name
        self.first_name = first_name
        self.second_name = second_name

# r = Student("Ivan", "Cherbakov", "Nikolaevich")
# print(r.__dict__)
