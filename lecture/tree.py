class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None


class NodeMgmt:
    def __init__(self, head: Node):
        self.head = head

    def insert(self, value: int):
        self.current_node = self.head
        while True:
            if value < self.current_node.value:
                if self.current_node.left:
                    self.current_node = self.current_node.left
                else:
                    self.current_node.left = Node(value)
                    break
            else:
                if self.current_node.right:
                    self.current_node = self.current_node.right
                else:
                    self.current_node.right = Node(value)
                    break

    def search(self, value: int):
        self.current_node = self.head

        while self.current_node:
            if self.current_node.value == value:
                return True
            elif value < self.current_node.value:
                self.current_node = self.current_node.left
            else:
                self.current_node = self.current_node.right
        return False

    def delete(self, value):
        is_searched = False
        self.current_node = self.head
        self.parent = self.head
        while self.current_node:
            if self.current_node.value == value:
                is_searched = True
                break
            else:
                if value < self.current_node.value:
                    self.parent = self.current_node
                    self.current_node = self.current_node.left
                else:
                    self.parent = self.current_node
                    self.current_node = self.current_node.right

        if not is_searched:
            return False

        # case1. child node is None
        if all([not self.current_node.left, not self.current_node.right]):
            if value < self.parent.value:
                self.parent.left = None
            else:
                self.parent.right = None
            del self.current_node

        # case2. only one chile node
        # case2-1. exist left child node
        if self.current_node.left and self.current_node.right is None:
            if value < self.parent.value:
                self.parent.left = self.current_node.left
            else:
                self.parent.right = self.current_node.left

        # case2-2. exist right child node
        if self.current_node.left is None and self.current_node.right:
            if value < self.parent.value:
                self.parent.left = self.current_node.right
            else:
                self.parent.right = self.current_node.right

        # case3. exist both child node
        if self.current_node.left and self.current_node.right:
            # case3-1. find minimum node from right child node in parent node left
            if value < self.parent.value:
                self.change_node = self.current_node.right
                self.change_node_parent = self.change_node.right
                # find leaf left node
                while self.change_node.left:
                    self.change_node_parent = self.change_node
                    self.change_node = self.change_node.left
                if self.change_node.right:
                    self.change_node_parent.left = (
                        self.change_node.right
                    )  # connect change_node_parent and change_node.right
                else:
                    # if change_node.right is None, just delete change_node_parent.left
                    self.change_node_parent.left = None
                self.parent.left = self.change_node  # connect parent and change_node
                self.change_node.right = self.current_node.right
                self.current_node.left = self.current_node.left

            # case3-2 find minimum node from right child node in parent node right
            else:
                self.change_node = self.change_node.right
                self.change_node_parent = self.change_node.right
                while self.change_node.left:
                    self.change_node_parent = self.change_node
                    self.change_node = self.change_node.left
                if self.change_node.right:
                    self.change_node_parent.left = self.change_node.right
                else:
                    self.change_node_parent.left = None
                self.parent.right = self.change_node
                self.change_node.left = self.current_node.left
                self.change_node.right = self.current_node.right


def check_binary_tree():
    # insert random value in binary tree
    import random

    bst_nums = set()
    while len(bst_nums) != 100:
        bst_nums.add(random.randint(0, 999))
    head = Node(500)
    binary_tree = NodeMgmt(head)
    for num in bst_nums:
        binary_tree.insert(num)

    # check search function
    for num in bst_nums:
        if binary_tree.search(num) is False:
            print("search failed", num)
        else:
            print("search success", num)

    # check delete function
    delete_nums = set()
    bst_nums = list(bst_nums)
    while len(delete_nums) != 10:
        delete_nums.add(bst_nums[random.randint(0, 99)])
    for del_num in delete_nums:
        if binary_tree.delete(del_num) is False:
            print("delete failed", del_num)
        else:
            print("delete success", del_num)


if __name__ == "__main__":
    # head = Node(21)
    # bst = NodeMgmt(head)
    # bst.insert(15)
    # print(bst.current_node.left.value)
    check_binary_tree()
