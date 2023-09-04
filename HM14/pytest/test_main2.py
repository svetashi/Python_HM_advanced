import pytest, sys
from hm2 import Student

def test_string1():
    r = Student("Ivan", "Cherbakov", "Nikolaevich")
    assert r.__dict__ == {'_personal_name': 'Ivan', '_first_name': 'Cherbakov', '_second_name': 'Nikolaevich'}, 'Fio generated wrong'

def test_string2():
    r = Student("Kolya", "Victorovich", "Nikola")
    assert r.__dict__ == {'_personal_name': 'Kolya', '_first_name': 'Victorovich', '_second_name': 'Nikola'}, 'Fio generated wrong'

def test_string3():
    r = Student("Anton", "Ilin", "Khoma")
    assert r.__dict__ == {'_personal_name': 'Anton', '_first_name': 'Ilin', '_second_name': 'Khoma'}, 'Fio generated wrong'

if __name__ == '__main__':
    pytest.main([sys.argv[0]])
