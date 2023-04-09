class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class NodeIntManagement:
    def __init__(self, data: int):
        self.head = Node(data)

    def add(self, data: int):
        if self.head == "":
            self.head = Node(data)
        else:
            node = self.head
            while node.next:
                node = node.next
            node.next = Node(data)

    def desc(self):
        node = self.head
        while node:
            print(node.data)
            node = node.next

    def delete(self, data):
        if self.head == "":
            print("There is no node to delete")
            return
        if self.head.data == data:
            self.head = self.head.next
        else:
            node = self.head
            while node.next:
                if node.next.data == data:
                    node.next = node.next.next
                    return
                else:
                    node = node.next



if __name__ == '__main__':
    linkedlist1 = NodeIntManagement(0)
    for i in range(1, 10):
        linkedlist1.add(i)
    linkedlist1.desc()
    linkedlist1.delete(0)
    print("After deleting 0")
    linkedlist1.desc()
    linkedlist1.delete(5)
    print("After deleting 5")
    linkedlist1.desc()
    linkedlist1.delete(9)
    print("After deleting 9")
    linkedlist1.desc()
