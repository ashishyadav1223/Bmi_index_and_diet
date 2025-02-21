class Stack:
    def __init__(self):
        self.stack = []  # Initialize an empty stack (a list)

    def push(self, item):
        self.stack.append(item)  # Add item to the top of the stack
        print(f"Item {item} added to the stack")

    def pop(self):
        if not self.is_empty():  # Check if stack is not empty
            item = self.stack.pop()  # Remove the top item
            print(f"Item {item} popped from the stack")
            return item
        else:
            print("Stack is empty, nothing to pop!")
            return None  # Return None if stack is empty

    def is_empty(self):
        return len(self.stack) == 0  # Check if the stack is empty

    def display(self):
        print("Current Stack:", self.stack)  # Display the stack content
s = Stack()  # Create a new stack
s.push(10)   # Add 10 to the stack
s.push(20)   # Add 20 to the stack
s.display()  # Display current stack -> Output: [10, 20]

s.pop()      # Remove and return 20 (last added)
s.display()  # Display current stack -> Output: [10]

s.pop()      # Remove and return 10
s.display()  # Display current stack -> Output: []

s.pop()      # Try to remove from empty stack -> Output: "Stack is empty, nothing to pop!"
