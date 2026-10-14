class PriorityQueue:
    def __init__(self):
        self.queue = []

    def insert(self, item, priority):
        self.queue.append((priority, item))

    def delete(self):
        if len(self.queue) == 0:
            print("Priority Queue is empty")
            return

        min_index = 0

        for i in range(1, len(self.queue)):
            if self.queue[i][0] < self.queue[min_index][0]:
                min_index = i

        priority, item = self.queue[min_index]
        self.queue.pop(min_index)

        print(priority, item)

    def display(self):
        if len(self.queue) == 0:
            print("Priority Queue is empty")
            return

        for priority, item in self.queue:
            print(priority, item)


pq = PriorityQueue()

pq.insert("Write assignment", 3)
pq.insert("Attend class", 1)
pq.insert("Complete lab", 2)

print("Priority Queue:")
pq.display()

print("\nRemoving items according to priority:")
pq.delete()
pq.delete()
pq.delete()