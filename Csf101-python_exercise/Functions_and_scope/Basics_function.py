def greet():
    print("Hello, World!")
greet()
def greet(name):
    print(f"Hello, {name}!")
greet("jigme")
def square(number):
    return number ** 5
result = square(3)
print(result)
def is_even(number):
    return number % 2 == 0
print(is_even(4))
print(is_even(5))
def print_numbers(n):
    for i in range(1, n + 1):
        print(i)

print_numbers(5)
