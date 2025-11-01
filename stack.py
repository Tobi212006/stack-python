# Stack Implementation in Python

stack = []

# Step 1: Ask user for stack size
while True:
    try:
        max_size = int(input("Enter size of the stack: "))
        if max_size <= 0:
            print("Invalid size. Must be greater than 0.")
        else:
            break
    except ValueError:
        print("Invalid value! Please enter an integer.")

# Step 2: Define stack operations
def push():
    if len(stack) >= max_size:
        print("Stack Overflow! Cannot add more elements.")
    else:
        element = input("Enter the element: ")
        stack.append(element)
        print(f"{element} appended to the stack.")

def pop():
    if not stack:
        print("Stack is empty! Nothing to pop.")
    else:
        popped = stack.pop()
        print(f"{popped} popped from the stack.")

def display():
    if not stack:
        print("Stack is empty!")
    else:
        print("\nStack from bottom to top:")
        for item in reversed(stack):
            print(item)
        print()

# Step 3: Menu-driven interface
while True:
    print("\n------ MENU ------")
    print("1. Push")
    print("2. Pop")
    print("3. Display")
    print("4. Exit")
    
    choice = input("Enter your choice (1-4): ")
    
    if choice == '1':
        push()
    elif choice == '2':
        pop()
    elif choice == '3':
        display()
    elif choice == '4':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter 1, 2, 3, or 4.")
