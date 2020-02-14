class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.head
        self.head = new_node

    def insert_after(self, previous_node, new_data):
        if previous_node is None:
            print("Previous Node cannot be None")
            return
        new_node = Node(new_data)
        new_node.next = previous_node.next
        previous_node.next = new_node

    def insert_by_position(self, position, new_data):
        if self.head is None:
            print("There is no position in empty linklist")
            return
        desired_node = self.head
        for i in range(1, position):
            if desired_node.next is None:
                print("Position cannot be less than size of linked list")
                return
            desired_node = desired_node.next
        new_node = Node(new_data)
        new_node.next = desired_node.next
        desired_node.next = new_node

    def traverse(self):
        if self.head is None:
            print("LinkedList is empty")
            return
        current_node = self.head
        print(current_node.value)
        while current_node.next:
            current_node = current_node.next
            print(current_node.value)

    def reverse(self):
        stack = []
        if self.head is None:
            print("LinkedList is empty")
            return
        current_node = self.head
        stack.append(current_node)
        while current_node.next:
            current_node = current_node.next
            stack.append(current_node)

        self.head = stack.pop()
        current_node = self.head
        while stack:
            new_node = stack.pop()
            current_node.next = new_node
            current_node = current_node.next
        current_node.next = None

    def append(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node

        end = self.head
        while end.next:
            end = end.next
        end.next = new_node

    def pop(self):
        if self.head is None:
            print("LinkedList is empty")
            return
        current_node = self.head
        while current_node.next:
            previous_node = current_node
            current_node = current_node.next
            if current_node.next is None:
                previous_node.next = None

    def remove(self, position):
        if self.head is None:
            print("LinkedList is empty")
            return
        current_node = self.head

        for _ in range(position - 1):
            current_node = current_node.next
        current_node.next = current_node.next.next


if __name__ == "__main__":
    ll = LinkedList()
    ll.push(33)
    print("Traverse linked list after pushing")
    ll.traverse()
    ll.append(12)
    ll.append(13)
    ll.append(14)
    print("Traverse linked list after appending")
    ll.traverse()
    ll.reverse()
    print("Traverse linked list after reversing the linked list")
    ll.traverse()
    print("Remove element from the reversed linked list: ")
    ll.remove(2)
    print("Traverse linked list after removing item: ")
    ll.traverse()
    ll.insert_by_position(2, 50)
    print("Traverse linked list after adding item by position:")
    ll.traverse()
    ll.pop()
    print("Traverse linked list after popping item:")
    ll.traverse()

