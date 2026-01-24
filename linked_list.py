class Node:
    """
    An object for storing a single node for Linked List.
    Models two attributes - data and the link to the next node in the list.
    """
    data = None
    next_node = None

    def __init__(self, data):
        self.data = data

    def __repr__(self):
        return f"<Node data: {self.data}>"


class LinkedList:
    """
    Singly Linked List.
    """
    def __init__(self):
        self.head = None
    
    def is_empty(self):
        return self.head == None

    def size(self):
        """
        Returns the number of nodes in the list
        Taken O(n) time.
        """
        current = self.head
        count = 0

        while (current != None):
            count += 1
            current = current.next_node
        
        return count
    
    
    def add(self, data):
        """
        Adds data to the head of the linked list.
        Takes O(1) constant time.
        """
        new_node = Node(data)
        new_node.next_node = self.head
        self.head = new_node


    def search(self, key):
        """
        Search for the first node containing data that matches the key.
        Returns node or `None` if not found.

        Takes O(n) linear time.
        """
        current = self.head
        
        while current != None:
            if current.data == key:
                return current
            else:
                current = current.next_node
        return None


    def insert(self, data, index):
        """
        Inserts a new Node containing data at index position.
        Insertion takes O(1) time but findind the node at the 
        insertion point takes O(n) time.

        Takes overall O(n) time.
        """
        if index == 0:
            self.add(data)

        if index > 0:
            new = Node(data)   

            position = index
            current = self.head

            while position > 1:
                current = new.next_node
                position -= 1
            
            previous_node = current
            next_node = current.next_node

            previous_node.next_node = new
            new.next_node = next_node


    def remove(self, key):
        """
        Removes Node contains data that matches the key.
        Returns the Node or None if the key doesn't exist.

        Takes O(n) time.
        """
        current = self.head
        previous = None
        found = False

        while current and not found:
            if current.data == key and current is self.head:
                found = True
                self.head = current.next_node
            elif current.data == key:
                found = True
                previous.next_node = current.next_node
            else:
                previous = current
                current = current.next_node
            
        return current
    

    def remove_at_index(self, key, index):
        ...


    def node_at_index(self, index):
        if index == 0:
            return self.head
        else:
            current = self.head
            position = 0

            while position < index:
                current = current.next_node
                position += 1

            return current


    def __repr__(self):
        """
        Returns string representation of the list.
        Takes O(n) time.
        """
        nodes = []
        current = self.head

        while current:
            if current is self.head:
                nodes.append(f"[Head: {current.data}]")
            elif current.next_node is None:
                nodes.append(f"[Tail: {current.data}]")
            else:
                nodes.append(f"{current.data}")
        
            current = current.next_node
        return "->".join(nodes)

# l = LinkedList()    # create linked list type
# l.add(1)
# l.add(2)
# l.add(3)
# l.add(4)
# print(l.size())
# print(l)
# print(l.search(4)) # True as it does exist.
# print(l.search(5)) # False as it does not exist.

# To do as challenge: remove at index and node at index.