# Queue Implementation in Python

queue = []

while True:
    try:
        max_size = int(input("Enter size of the queue: "))
        if max_size <= 0:
            print("Invalid size. Must be greater than 0.")
        else:
            break
    except ValueError:
        print("Invalid value! Please enter an integer.")

def enqueue():
    if len(queue) >= max_size:
        print("Queue Overflow!")
    else:
        element = input("Enter element to enqueue: ")
        queue.append(element)
        print(f"{element} added to queue.")

def dequeue():
    if not queue:
        print("Queue Underflow! Nothing to remove.")
    else:
        removed = queue.pop(0)
        print(f"{removed} dequeued from queue.")

def display():
    if not queue:
        print("Queue is empty!")
    else:
        print("Queue from front to rear:")
        for item in queue:
            print(item)
        print()

while True:
    print("\n------ QUEUE MENU ------")
    print("1. Enqueue")
    print("2. Dequeue")
    print("3. Display")
    print("4. Exit")

    choice = input("Enter your choice (1-4): ")

    if choice == '1':
        enqueue()
    elif choice == '2':
        dequeue()
    elif choice == '3':
        display()
    elif choice == '4':
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice! Please enter 1, 2, 3, or 4.")
