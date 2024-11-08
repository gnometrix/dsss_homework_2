import random

num_of_rounds=6

def random_int_generator(min, max):
    """
    Generates a random integer between min and max value (inclusive)
    returns an integer
    """
    return random.randint(min, max)


def random_operator_generator():
    """
    Generates a random operator and outputs +, - or *
    returns a chosen operator
    """
    return random.choice(['+', '-', '*'])


def math_problem(num1, num2, operator):
    """
    The mathmatical expression is formed from the numbers and operant given
    returns the tuple of math problem and its integer value 
    """
    # mathematical expression obtained
    expression = f"{num1} {operator} {num2}" 
    #the correct answer is calculated
    if operator == '+': 
        ans = num1 + num2 
    elif operator == '-': 
        ans = num1 - num2
    else: 
        ans = num1 * num2
    return expression, ans

def math_quiz():
    '''
    Math quiz game - solve the mathmatical problems generated by the computer.
    Enter the answer as an INTEGER when prompted for your answer to earn points!!
    '''
    points=0

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(num_of_rounds):

        num1 = random_int_generator(1, 10); 
        num2 = random_int_generator(1, 6); 
        operator = random_operator_generator()

        problem, answer = math_problem(num1, num2, operator)
        print(f"\nQuestion: {problem}")
        
        try: 
            user_answer = int(input("Your answer: "))
        except:
            print(f"Not an integer")

        if user_answer == answer:
            print("Correct! You earned a point.")
            points += 1
        else:
            print(f"Wrong answer. The correct answer is {answer}.")

    print(f"\nGame over! Your score is: {points}/{num_of_rounds}")

if __name__ == "__main__":
    math_quiz()
