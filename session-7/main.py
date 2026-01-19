import random

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_random_elements(self, count):
        for _ in range(count):
            val = random.randint(1, 100)
            new_node = Node(val)
            if not self.head:
                self.head = new_node
            else:
                current = self.head
                while current.next:
                    current = current.next
                current.next = new_node
                new_node.prev = current

    def remove_by_value(self, val):
        current = self.head
        while current:
            if current.data == val:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                
                if current.next:
                    current.next.prev = current.prev
                return True
            current = current.next
        return False

    def display(self):
        current = self.head
        elements = []
        while current:
            elements.append(str(current.data))
            current = current.next
        print(" <-> ".join(elements) if elements else "List is empty")

def main():
    ll = LinkedList()
    try:
        x = int(input("PLease ennter number of random elements to generate: "))
        ll.add_random_elements(x)
    except ValueError:
        return

    ll.display()

    try:
        val_to_delete = int(input("Pleas enter the value you want to remove from the list: "))
        ll.remove_by_value(val_to_delete)
    except ValueError:
        pass

    ll.display()

if __name__ == "__main__":
    main()
