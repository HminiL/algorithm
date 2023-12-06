from icecream import ic


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def print_all_nodes(head):
    print("===print_all_nodes===")
    node = head
    while node:
        print(node.data)
        node = node.next


def create_several_nodes(start: int, end: int):
    """create several nodes and link them automatically
    :return: head node
    """
    head = Node(start)
    node = head
    for i in range(start + 1, end + 1):
        node.next = Node(i)
        node = node.next
    return head


def first_practice():
    """create a head node and link it to the next node manually
    :return: nothing
    """
    node1 = Node(1)
    node2 = Node(2)
    node1.next = node2
    head = node1
    ic(head.data)
    ic(head.next.data)
    ic(node2.data)


def add(head, data):
    node = head
    while node.next:
        node = node.next
    node.next = Node(data)


def second_practice():
    """create a head node and link it to the next node automatically with a function
    :return: nothing
    """
    head = Node(1)
    add(head, 2)
    add(head, 3)
    ic(head.data)
    ic(head.next.data)
    ic(head.next.next.data)


def third_practice():
    """create a middle node and link previous and next nodes automatically
    :return: nothing
    """
    head = create_several_nodes(1, 10)
    print_all_nodes(head)

    # search for a specific node to add a new node in between
    node = head
    search = True
    while search:
        if node.data == 5:
            search = False
        else:
            node = node.next

    # add a new node in between
    new_node = Node(5.5)
    new_node_next = node.next
    node.next = new_node
    new_node.next = new_node_next
    print("---after adding a new node---")
    print_all_nodes(head)


if __name__ == "__main__":
    first_practice()
    second_practice()
    third_practice()
