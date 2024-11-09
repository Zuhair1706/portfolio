#1. Fibonacci Series of value 10:
def fibonacci(n):
    fib_series = [0, 1]
    while len(fib_series) < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series
print(fibonacci(10))


#2. Factorial of 7:
def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

print(factorial(7))


#3. Check if a number is an Armstrong number:
def is_armstrong_number(num):
    num_str = str(num)
    power = len(num_str)
    sum_of_powers = sum(int(digit) ** power for digit in num_str)
    return num == sum_of_powers

number = 153  
print(is_armstrong_number(number))


#4. Swapping of two numbers:

def swap(a, b,):
    a,b = b,a
    return a,b
x, y = 5, 10
x, y = swap(x, y)
print(x, y)

#5 password checking:
def check_password_match(password1, password2):
    return password1 == password2

password1 = input()
password2 = input()

if check_password_match(password1, password2):
    print("Passwords match.")
else:
    print("Passwords do not match.")


