# Create a Node class to represent each customer in the waitlist
class Node:
    '''
    A class representing a node in a linked list.
    Attributes:
        name (str): The name of the customer.
        next (Node): A reference to the next node in the list.
    '''
    def __init__(self, name):
        self.name = name
        self.next = None



# Create a LinkedList class to manage the waitlist
class LinkedList:
    '''
    A class representing a linked list to manage a waitlist.
    Attributes:
        head (Node): The first node in the linked list.
    '''

    def __init__(self):
        self.head = None

    def add_front(self, name):
        new_node = Node(name)
        new_node.next = self.head
        self.head = new_node
        print(f"{name} added to the front of the waitlist.")

    def add_end(self, name):
        new_node = Node(name)

        



        
        if self.head is None:
            self.head = new_node
            print(f"{name} added to the end of the waitlist.")
            return

     
        current = self.head
        while current.next is not None:
            current = current.next

        current.next = new_node
        print(f"{name} added to the end of the waitlist.")

    def remove(self, name):
      
        if self.head is None:
            print(f"{name} not found")
            return
        if self.head.name == name:
            self.head = self.head.next
            print(f"Removed {name} from the waitlist")
            return
        current = self.head
        while current.next is not None:
            if current.next.name == name:
                current.next = current.next.next
                print(f"Removed {name} from the waitlist")
                return
            current = current.next

        print(f"{name} not found")

    def print_list(self):
        if self.head is None:
            print("The waitlist is empty")
            return

        current = self.head
        print("Current waitlist:")
        while current is not None:
            print(f"- {current.name}")
            current = current.next
    


def waitlist_generator():
    waitlist = LinkedList()

    while True:
        print("\n--- Waitlist Manager ---")
        print("1. Add customer to front")
        print("2. Add customer to end")
        print("3. Remove customer by name")
        print("4. Print waitlist")
        print("5. Exit")

        choice = input("Choose an option (1–5): ")

        if choice == "1":
            name = input("Enter customer name to add to front: ")
            waitlist.add_front(name)

        elif choice == "2":
            name = input("Enter customer name to add to end: ")
            waitlist.add_end(name)

        elif choice == "3":
            name = input("Enter customer name to remove: ")
            waitlist.remove(name)

        elif choice == "4":
            waitlist.print_list()

        elif choice == "5":
            print("Exiting waitlist manager.")
            break

        else:
            print("Invalid option. Please choose 1–5.")


# Start the program
waitlist_generator()


'''
Design Memo: Write Your Design Memo Include a 200–300 word response in your code or in a .txt file:

This uses a linked list to handle a waitlist. The linked list is a structure that looks a lot like a chain of boxes that are connected one after another.
Each box is a Node and every Node has a customers name as well as the place of the next Node. Instead of storing the names in a typical list
i link each person manually like links in a chain.

Adding someone to the front means making a new Node and letting this new one point to the old first person then i change the head to the new person. 
Adding to the end you have to go through the list until the last person is found and then puttingput the new person there. 
Deleting someone requires me to find the person in the list and then redo the links for the other people so the removed person is left out.

The head is important because it is the very first thing that points to the whole list. It is the one that makes the program the start of the waitlist. 
If the head is None then the list is empty. it all starts with the head because it is from there that you can only move forward in the list.

'''
