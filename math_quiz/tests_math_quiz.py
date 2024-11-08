import unittest
from math_quiz import random_int_generator,random_operator_generator,math_problem

class TestMathGame(unittest.TestCase):

    def test_random_int_generator(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_int_generator(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_random_operator_generator(self):
        for _ in range(1000):
             rand_operator = random_operator_generator()
             self.assertIn(rand_operator, ['+', '-', '*'])

    def test_math_problem(self):
            test_cases = [
                (5,2,'+','5 + 2', 7),
                (2,4,'*','2 * 4', 8),
                (2,2,'+','2 + 2', 4),
                (3,1,'-','3 - 1', 2),
                (5,3,'*','5 * 3', 15),
                (7,3,'-','7 - 3', 4),
                (9,5,'+','9 + 5', 14),
                (3,3,'*','3 * 3', 9),
                (8,5,'+','8 + 5', 13),
                (6,1,'-','6 - 1', 5),
                (8,1,'+','8 + 1', 9),
                (7,4,'*','7 * 4', 28),
                (9,3,'-','9 - 3', 6),
            ]

            for num1, num2, operator, expected_problem, expected_answer in test_cases:
                problem, answer = math_problem(num1,num2,operator)
                self.assertEqual(expected_problem, problem)
                self.assertEqual(expected_answer,answer)

if __name__ == "__main__":
    unittest.main()
