# Just as we would pass in a value to a Python list's append method, our add_to_front method should accept a value to be added to the list:
class SLNode:
    def __init__(self, val):
        self.value = val
        self.next = None



class SList:
    def __init__(self):
        self.head = None
        

    def add_to_front(self, val): # Added this line, takes a value
        new_node = SLNode(val) # Create a new instance of our Node class the given value
        current_head = self.head # Save the current head in a variable
        new_node.next = current_head # Set the new node's next to the list's current head
        self.head = new_node # Set the list's head to the node we created in the last step
        return self
    
    def print_values(self):
        runner = self.head # A pointer to the list's first node
        while ( runner != None ): # iterating while runner is a node and not None
            print( runner.value )
            runner = runner.next   # Set the runner to its neighbor
        return self        # Once the loop is done, return self to allow for chaining
    
    def add_to_back(self, val):     # Accepts a value
        new_node = SLNode(val)
        runner = self.head      # Set an iterator to start at the front of the list
        while ( runner.next != None ):
            runner = runner.next # Increment the runner to the next node in the list
        runner.next = new_node #  Increment the runner to the next node in the list
        return self # Return self to allow for chaining
        

# Testing our class
my_list = SList()   # Create a new instance of a list
my_list.add_to_front(2).add_to_front(1).add_to_back(3).print_values() # List is chained

# Expected output:
# 2
# 1
# 3