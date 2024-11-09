#1) guess the number game 
number_to_guess = 25  # You can set this to any number you like
print("I'm thinking of a number between 1 and 100. Can you guess it?")
guess = None
while guess != number_to_guess:
    guess = int(input("Enter your guess: "))
    
    if guess < number_to_guess:
        print("Too low! Try again.")
    elif guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print("Congratulations! You've guessed the number.")

print("Thanks for playing!")

#2)CALCULATOR
def addition(a, b):
    c = a + b
    return c

def subtraction(a, b):
    d = a - b
    return d

def mult(a, b):
    e = a * b
    return e

def divi(a, b):
    f = a / b
    return f

def calculate():
    y = int(input('Enter the first number: '))
    z = int(input('Enter the second number: '))
    op = input('Select the operation (+, -, *, /): ')
    
    if op == '+':
        result = addition(y, z)
    elif op == '-':
        result = subtraction(y, z)
    elif op == '*':
        result = mult(y, z)
    elif op == '/':
        result = divi(y, z)
    else:
        print("Invalid operation selected")
        return
    
    print(f'The result is: {result}')

calculate()

                                                                                                                                                                                                                                                


