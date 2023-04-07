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
        if self.head == data:
            ...


if __name__ == '__main__':
    # linkedlist1 = NodeIntManagement(0)
    # linkedlist1.desc()
    # for i in range(1, 10):
    #     linkedlist1.add(i)
    # linkedlist1.desc()
    node1 = Node(1)
    node2 = Node(2)
    node22 = Node(22)
    node1.next = node2
    node2.next = node22
    print(node1.next)
    temp = node1
    node1 = node1.next
    del temp
    print(node1.data, node1.next.data)

    node3 = Node(3)
    node4 = Node(4)
    node5 = Node(5)
    node3.next = node4
    node4.next = node5
    node3 = node3.next
    print(node3.data, node3.next.data)
