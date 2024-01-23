Test_name = "Alan Turing"

Test_age = "42"
print("your age is" ,Test_age)

Name = "Bérénice"
Age = "34"
job = "mathematician"
person = "My name is " + Name + ", I am " + Age + " years old" + ", my job is " + job

print (person)

Name = "Alan Turing"
Age = "42"
job = "mathematician"
person = "Hello, my name is {} and I am {} years old, and I am a {}".format(Name, Age, job)
print (person)

print(Age,type(Age))







import unittest


class TestNotebook(unittest.TestCase):
    def test_name(self):
        self.assertEqual(name, "Alan Turing")

    def test_age(self):
        self.assertEqual(age, 42)

    def test_person(self):
        self.assertEqual(person, ["Alan Turing", 42, "mathematician"])

    def test_text(self):
        self.assertEqual(
            text,
            "Hello, my name is Alan Turing, I am 42 years old and I am a mathematician.",
        )

    def test_type(self):
        self.assertEqual(age_type, int)


unittest.main(argv=[""], verbosity=2, exit=False)