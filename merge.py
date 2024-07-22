# merge.py
<<<<<<< HEAD
def greet():
    print("Hello from the suhyun_C branch")
def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
=======

def greet():
    print("Hello from the suhyun branch")

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

>>>>>>> 96de74bcca13edd0a58808a62382a22862947b8b
def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b
<<<<<<< HEAD
=======

>>>>>>> 96de74bcca13edd0a58808a62382a22862947b8b
def main():
    print("This is the main function")
    greet()
    result_add = add(10, 5)
    result_sub = subtract(10, 5)
    result_mul = multiply(10, 5)
<<<<<<< HEAD

    result_div = divide(10, 5)
    print(f"Add: {result_add}, Subtract: {result_sub}, Multiply: {result_mul}, Divide: {result_div}
    if __name__ == "__main__":
=======
    result_div = divide(10, 5)
    print(f"Add: {result_add}, Subtract: {result_sub}, Multiply: {result_mul}, Divide: {result_div}")

if __name__ == "__main__":
>>>>>>> 96de74bcca13edd0a58808a62382a22862947b8b
    main()