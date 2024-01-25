#Write a function called hello that returns a string of characters. This function will take as argument a variable name. This function will return a string "Hello name".

def hello(name = "Anonymous"):
    return "Hello " + name

print(hello())

#Create a function sum_of_students that calculates and counts the number of students in a list and returns the total. The function will have to return an integer.

list_students = [["Jean", "Alice", "Edwige", "Peter", "James"],
["Redouane", "Justine", "Adrien", "Nicolas", "Pierre"]]


def sum_of_students(list_students):
    total = 0
    for etudiant in list_students:
        total += len(etudiant)
    return total

print(sum_of_students(list_students))

#3. Is divisible ?
#Create a function is_divisible(n, x, y) that checks if a number n is divisible by two numbers x AND y. All inputs are positive, non-zero digits.

"""def is_divisible(n, x, y):
    if n % x == 0 and n % y == 0:
        return f"{(n, x, y)} --> True because {n} is divisible by {x} and {y}"
    elif n % x == 0 and n % y != 0: 
        return False
    elif n % x != 0 and n % y == 0:
        return f"{(n, x, y)} --> False because {n} is not divisible by {x}"
    elif n % y != 0 and n % y != 0:
        return f"{(n, x, y)} --> False because {n} is not divisible by {x} neither {y}"""

def is_divisible(n, x, y):
    if n % x == 0 and n % y == 0:
        return True
    else: return False
 
print(is_divisible(3, 3, 4))
print(is_divisible(12, 3, 4))

#4. Abbreviate a two-word name
#Write a function to convert a name into initials. This functions strictly takes two words with one space in between them.
#Example :
#Sam Harris => S.H
#Patrick Feeney => P.F

def abbreviate_name(first_name, last_name):
    return first_name[0] + "." + last_name[0]

print(abbreviate_name("Sam", "Harris"))

#5. Sum of positive
#You get an array of numbers, return the sum of all of the positives ones.
#Example :
#[1,-4,7,12] => 1 + 7 + 12 = 20

list_num = [1,-4,7,12]

def positive_sum(list_num):
        sum = 0
        for num in list_num:
            if num > 0:
                sum += num
        return sum
    
print(positive_sum(list_num))

#6 Sum mixed array
#Given an array of integers as strings and numbers, return the sum of the array values as if all were numbers.
#Return your answer as a number.
#Example :
#mixed_sum(['5', '0', 9, 3, 2, 1, '9', 6, 7]) => 42

def mixed_sum(array):
    sum = 0
    for num in array:
        num = int(num)
        sum += num
    return sum

print(mixed_sum(['5', '0', 9, 3, 2, 1, '9', 6, 7]))


#7. Return the day
#Complete the function which returns the weekday according to the input number:
#1 returns "Sunday"
#2 returns "Monday"
#3 returns "Tuesday"
#4 returns "Wednesday"
#5 returns "Thursday"
#6 returns "Friday"
#7 returns "Saturday"
#Otherwise returns "Wrong, please enter a number between 1 and 7"

def what_day(number):
    i = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
    if 0 < number <= 7:
        return i[number - 1]
    else: 
        return "Wrong, please enter a number between 1 and 7"

print(what_day(1))
     

#8. Summation
#Write a program that finds the summation of every number from 1 to number. The number will always be a positive integer greater than 0.
#Example :
#summation(2) -> 3
#1 + 2
#summation(8) -> 36
 #1 + 2 + 3 + 4 + 5 + 6 + 7 + 8

def summation(numbers):
    total = 0
    for i in range(1, numbers + 1):
        total += i
    return total

print(summation(6))

#9. If you can't sleep, just count sheep!!
# Given a non-negative integer, 3 for example, return a string saying: "1 sheep...2 sheep...3 sheep...". Input will always be valid, i.e. no negative integers.

def count_sheep(number):
    saut = ""
    for i in range(1, number + 1):
        saut += str(i) + " sheep..."
    return saut
        
print(count_sheep(3))

#10. Student's final grade

#Create a function final_grade, which calculates the final grade of a student depending on two parameters: a grade for the exam_grade and a number of completed projects.

#This function should take two arguments: exam_grade, grade of the exam (from 0 to 100), and completed_projects, number of completed projects (0 and above).

#This function should return a number, i.e. the final grade. There are four types of final grades:

#100, if a grade for the exam is more than 90 or if the number of completed projects more than 10.
#90, if a grade for the exam is more than 75 and if the number of completed projects is minimum 5.
#75, if a grade for the exam is more than 50 and if the number of completed projects is minimum 2.
#0, in other cases

def final_grade(exam_grade, completed_projects):
    if exam_grade >= 90 or completed_projects >= 10:
        taux_reussite = 100
    elif exam_grade >= 75 and completed_projects >= 5:
        taux_reussite = 90
    elif exam_grade >= 50 and completed_projects >= 2:
        taux_reussite = 75
    else: taux_reussite = 0
    return taux_reussite

print(final_grade(25, 12))


import unittest


class TestNotebook(unittest.TestCase):
    def test_hello(self):
        self.assertEqual(hello(), "Hello Anonymous")
        self.assertEqual(hello("Jean"), "Hello Jean")

    def test_sum_of_students(self):
        self.assertEqual(
            sum_of_students(
                [
                    ["Jean", "Alice", "Edwige", "Peter", "James"],
                    ["Redouane", "Justine", "Adrien", "Nicolas", "Pierre"],
                ]
            ),
            10,
        )

    def test_is_divisible(self):
        self.assertEqual(is_divisible(3, 3, 4), False)
        self.assertEqual(is_divisible(12, 3, 4), True)
        self.assertEqual(is_divisible(8, 3, 4), False)
        self.assertEqual(is_divisible(48, 3, 4), True)

    def test_abbreviate_name(self):
        self.assertEqual(abbreviate_name("Sam Harris"), "S.H")
        self.assertEqual(abbreviate_name("Patrick Feenan"), "P.F")
        self.assertEqual(abbreviate_name("Evan Cole"), "E.C")
        self.assertEqual(abbreviate_name("P Favuzzi"), "P.F")
        self.assertEqual(abbreviate_name("David Mendieta"), "D.M")

    def test_positive_sum(self):
        self.assertEqual(positive_sum([1, 2, 3, 4, 5]), 15)
        self.assertEqual(positive_sum([1, -2, 3, 4, 5]), 13)
        self.assertEqual(positive_sum([-1, 2, 3, 4, -5]), 9)
        self.assertEqual(positive_sum([]), 0)
        self.assertEqual(positive_sum([-1, -2, -3, -4, -5]), 0)

    def test_sum_mixed_array(self):
        self.assertEqual(mixed_sum([9, 3, "7", "3"]), 22)
        self.assertEqual(mixed_sum(["5", "0", 9, 3, 2, 1, "9", 6, 7]), 42)
        self.assertEqual(mixed_sum(["3", 6, 6, 0, "5", 8, 5, "6", 2, "0"]), 41)
        self.assertEqual(mixed_sum(["1", "5", "8", 8, 9, 9, 2, "3"]), 45)
        self.assertEqual(mixed_sum([8, 0, 0, 8, 5, 7, 2, 3, 7, 8, 6, 7]), 61)

    def test_return_day(self):
        self.assertEqual(what_day(1), "Sunday")
        self.assertEqual(what_day(2), "Monday")
        self.assertEqual(what_day(3), "Tuesday")
        self.assertEqual(what_day(8), "Wrong, please enter a number between 1 and 7")
        self.assertEqual(what_day(20), "Wrong, please enter a number between 1 and 7")

    def test_summation(self):
        self.assertEqual(summation(1), 1)
        self.assertEqual(summation(8), 36)

    def test_count_sheep(self):
        self.assertEqual(count_sheep(1), "1 sheep...")
        self.assertEqual(count_sheep(2), "1 sheep...2 sheep...")
        self.assertEqual(count_sheep(3), "1 sheep...2 sheep...3 sheep...")

    def test_final_grade(self):
        self.assertEqual(final_grade(100, 12), 100)
        self.assertEqual(final_grade(85, 5), 90)


unittest.main(argv=[""], verbosity=2, exit=False)

