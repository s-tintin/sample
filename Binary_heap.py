

class BinaryHeap:

    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0


    def heapify_up(self, ind):
        while ind // 2 > 0:

            if self.heap_list[ind] < self.heap_list[ind // 2]:
                temp = self.heap_list[ind // 2]
                self.heap_list[ind // 2] = self.heap_list[ind]
                self.heap_list[ind] = temp
            ind = ind // 2


    def insert(self, value):
        self.heap_list.append(value)
        self.current_size += 1
        self.heapify_up(self.current_size)


    def min_child(self, ind):
        if ind * 2 + 1 > self.current_size:
            return ind * 2
        else:
            if self.heap_list[ind * 2] < self.heap_list[ind * 2 + 1]:
                return ind * 2
            else:
                return ind * 2 + 1


    def heapify_down(self, ind):
        while ind * 2 <= self.current_size:
            minChild = self.min_child(ind)

            if self.heap_list[ind] > self.heap_list[minChild]:
                temp = self.heap_list[ind]
                self.heap_list[ind] = self.heap_list[minChild]
                self.heap_list[minChild] = temp
            ind = minChild


    def delete_min(self):

        ret_val = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size -= 1
        self.heap_list.pop()
        self.heapify_down(1)
        return ret_val


    def bulid_heap(self, num_list):
        ind = len(num_list) // 2
        self.current_size = len(num_list)
        self.heap_list = [0] + num_list[:]
        while ind > 0:
            self.heapify_down(ind)
            ind -= 1



if __name__ == '__main__':

    num_list = [9, 6, 5, 2, 3]
    my_heap = BinaryHeap()
    my_heap.bulid_heap(num_list)
    print(my_heap.heap_list)
    my_heap.delete_min()
    print(my_heap.heap_list)
    my_heap.insert(3)
    print(my_heap.heap_list)
    my_heap.delete_min()
    print(my_heap.heap_list)

