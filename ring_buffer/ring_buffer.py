class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        self.buffer_list = []
        self.counter = 0

    def append(self, item):

        if len(self.buffer_list) < self.capacity:
            self.counter += 1
            self.buffer_list.append(item)
        else:
            if self.counter is self.capacity:
                self.counter = 0
            print('self.counter:', self.counter)
            self.buffer_list.pop(self.counter)
            self.counter += 1
            self.buffer_list.insert(self.counter-1, item)

    def get(self):
        print(self.buffer_list)
        return self.buffer_list
