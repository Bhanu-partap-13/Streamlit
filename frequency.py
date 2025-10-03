
class MinHeap:
    def __init__(self):
        self.heap = []  # using a list to represent the heap

    def insert(self, val):
        self.heap.append(val)         # add the new value at the end
        self._heapify_up(len(self.heap) - 1)  # fix heap from bottom to top

    # 2️⃣ Delete the minimum element (root)
    def delete_min(self):
        if not self.heap:
            print("Heap is empty!")
            return None

        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]
        # Move the last element to the root and remove the last
        self.heap[0] = self.heap.pop()
        # Heapify down to maintain the min-heap property
        self._heapify_down(0)
        return root

    # 3️⃣ Display heap elements
    def display(self):
        print("Heap array:", self.heap)

    # Helper function to maintain heap upwards (for insert)
    def _heapify_up(self, index):
        parent = (index - 1) // 2
        while index > 0 and self.heap[index] < self.heap[parent]:
            # swap child with parent
            self.heap[index], self.heap[parent] = self.heap[parent], self.heap[index]
            index = parent
            parent = (index - 1) // 2

    # Helper function to maintain heap downwards (for delete)
    def _heapify_down(self, index):
        size = len(self.heap)
        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            smallest = index

            if left < size and self.heap[left] < self.heap[smallest]:
                smallest = left
            if right < size and self.heap[right] < self.heap[smallest]:
                smallest = right

            if smallest != index:
                self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
                index = smallest
            else:
                break


# 🧪 Example Usage
h = MinHeap()
h.insert(40)
h.insert(20)
h.insert(30)
h.insert(10)
h.insert(50)

print("Heap after insertions:")
h.display()

print("Deleted min:", h.delete_min())
print("Heap after deleting min:")
h.display()
