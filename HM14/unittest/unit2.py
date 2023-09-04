from hm2 import Student
import unittest

class TestFString(unittest.TestCase):
    def test_string1(self):
        r = Student("Ivan", "Cherbakov", "Nikolaevich")
        self.assertEqual(r.__dict__, {'_personal_name': 'Ivan', '_first_name': 'Cherbakov', '_second_name': 'Nikolaevich'}, msg="Fio generated wrong")

    def test_string2(self):
        r = Student("Kolya", "Victorovich", "Nikola")
        self.assertEqual(r.__dict__, {'_personal_name': 'Kolya', '_first_name': 'Victorovich', '_second_name': 'Nikola'}, msg="Fio generated wrong")

    def test_string3(self):
        r = Student("Anton", "Ilin", "Khoma")
        self.assertEqual(r.__dict__, {'_personal_name': 'Anton', '_first_name': 'Ilin', '_second_name': 'Khoma'}, msg="Fio generated wrong")
               
if __name__ == '__main__':
    unittest.main()