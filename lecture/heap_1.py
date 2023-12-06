class MaxHeap:
    def __init__(self, data: int):
        self.heap_array = list()
        self.heap_array.append(None)  # To make root node's  index 1
        self.heap_array.append(data)

    def move_up(self, inserted_idx: int):
        if inserted_idx <= 1:  # validate root index
            return False

        parent_idx = inserted_idx // 2
        if self.heap_array[inserted_idx] > self.heap_array[parent_idx]:
            return True
        else:
            return False

    def move_down(self, popped_idx: int):
        left_child_idx = popped_idx * 2
        right_child_idx = popped_idx * 2 + 1
        if left_child_idx >= len(self.heap_array):
            return False
        elif right_child_idx >= len(self.heap_array):
            if self.heap_array[popped_idx] < self.heap_array[left_child_idx]:
                return True
            else:
                return False
        else:
            bigger_child_idx = max(right_child_idx, left_child_idx)
            if self.heap_array[popped_idx] < self.heap_array[bigger_child_idx]:
                return True
            else:
                return False

    def insert(self, data: int):
        if len(self.heap_array) == 0:
            self.heap_array.append(None)
            self.heap_array.append(data)
            return True

        self.heap_array.append(data)
        inserted_idx = len(self.heap_array) - 1

        while self.move_up(inserted_idx):
            parent_idx = inserted_idx // 2
            self.heap_array[inserted_idx], self.heap_array[parent_idx] = (
                self.heap_array[parent_idx],
                self.heap_array[inserted_idx],
            )
            inserted_idx = parent_idx

        return True

    def pop(self):
        if len(self.heap_array) <= 1:
            return None  # insert가 아니므로 heap_array의 맨 앞 값인 None 반환

        returned_data = self.heap_array[1]
        self.heap_array[1] = self.heap_array[-1]
        del self.heap_array[-1]
        popped_idx = 1

        while self.move_down(popped_idx):
            left_child_idx = popped_idx * 2
            right_child_idx = popped_idx * 2 + 1

            if (
                right_child_idx >= len(self.heap_array)
                and self.heap_array[popped_idx] < self.heap_array[left_child_idx]
            ):
                self.heap_array[right_child_idx], self.heap_array[popped_idx] = (
                    self.heap_array[popped_idx],
                    self.heap_array[right_child_idx],
                )
            else:
                if (
                    self.heap_array[popped_idx]
                    < self.heap_array[
                        bigger_child_idx := max(right_child_idx, left_child_idx)
                    ]
                ):
                    self.heap_array[popped_idx], self.heap_array[bigger_child_idx] = (
                        self.heap_array[bigger_child_idx],
                        self.heap_array[popped_idx],
                    )
        return returned_data


class MinHeap:
    def __init__(self, data: int):
        self.heap_array = list()
        self.heap_array.append(None)
        self.heap_array.append(data)

    def move_up(self, inserted_idx):
        if inserted_idx <= 1:
            return False
        parent_idx = inserted_idx // 2
        if self.heap_array[inserted_idx] < self.heap_array[parent_idx]:
            return True
        else:
            return False

    def insert(self, data):
        if len(self.heap_array) <= 1:
            self.heap_array.append(None)
            self.heap_array.append(data)
            return True

        self.heap_array.append(data)
        inserted_idx = len(self.heap_array) - 1

        while self.move_up(inserted_idx):
            parent_idx = inserted_idx // 2
            self.heap_array[inserted_idx], self.heap_array[parent_idx] = (
                self.heap_array[parent_idx],
                self.heap_array[inserted_idx],
            )
            inserted_idx = parent_idx


if __name__ == "__main__":
    max_heap = MaxHeap(15)
    max_heap.insert(10)
    max_heap.insert(8)
    max_heap.insert(5)
    max_heap.insert(4)
    max_heap.insert(20)
    print(max_heap.heap_array)
    max_heap.pop()
    print(max_heap.heap_array)

    # min_heap = MinHeap(1)
    # min_heap.insert(3)
    # min_heap.insert(5)
    # min_heap.insert(7)
    # min_heap.insert(2)
    # min_heap.insert(10)
    # print(min_heap.heap_array)
