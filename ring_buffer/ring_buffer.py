class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.list_array = []
        self.list_index = 0

    def append(self, item):
        if len(self.list_array) < self.capacity:
            self.list_array.append(item)
        else:
            self.list_array[self.list_index] = item
            if self.list_index < (self.capacity - 1):
                self.list_index += 1
            else:
                self.list_index = 0

    def get(self):
        return self.list_array