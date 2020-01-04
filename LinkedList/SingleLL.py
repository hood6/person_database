class SingleLinkedList:
    def __init__(self):
        self.head = self.tail = self.curr = self.prev = None
        self.length = 0

    def check_head(self):
        if self.head is None:
            print("List is empty")
            return False
        else:
            return True

    def iterate_for(self):
        if not self.check_head():
            return
        self.prev = self.curr
        self.curr = self.curr.next_node

    def reset_curr(self):
        if not self.check_head():
            return
        self.curr = self.head
        self.prev = None

    def add_to_tail(self, data):
        if self.head is None:
            self.head = self.tail = self.curr = Node(data, None)
            return
        self.tail.next_node = Node(data, None)
        self.tail = self.tail.next_node
        self.length += 1

    def remove_from_tail(self):
        if not self.check_head():
            return
        self.reset_curr()
        while self.curr.next_node is not self.tail:
            self.iterate_for()
        self.tail = self.curr
        self.tail.next_node = None
        self.length -= 1

    def peek_curr(self):
        if not self.check_head():
            return
        return self.curr.data

    def print_list(self):
        if not self.check_head():
            return
        self.reset_curr()
        while self.curr:
            print(f"{self.curr.data.to_string()}\n")
            if self.curr is self.tail:
                return
            self.iterate_for()


class Node:
    def __init__(self, data, next_node):
        self.data = data
        self.next = next_node
