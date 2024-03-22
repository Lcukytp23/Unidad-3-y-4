class Order:
    def _init_(self, qtty, customer):
        self.customer = customer
        self.qtty = qtty
    
    def print_info(self):
        print("     Customer: " + self.get_customer())
        print("     Quantity: " + str(self.get_qty()))
        print("     ------------")

    def get_qty(self):
        return self.qtty

    def get_customer(self):
        return self.customer


class QueueInterface:
    def size(self):
        pass

    def is_empty(self):
        pass

    def front(self):
        pass

    def enqueue(self, info):
        pass

    def dequeue(self):
        pass


class QueueDump:
    def _init_(self):
        self.queue = []

    def size(self):
        return len(self.queue)

    def is_empty(self):
        return len(self.queue) == 0

    def front(self):
        if self.is_empty():
            return None
        return self.queue[0]

    def enqueue(self, info):
        self.queue.append(info)

    def dequeue(self):
        if self.is_empty():
            return None
        return self.queue.pop(0)


# Implementación de QueueDump
queue_dump = QueueDump()
queue_dump.enqueue(Order(20, "cust1"))
queue_dump.enqueue(Order(30, "cust2"))
queue_dump.enqueue(Order(40, "cust3"))
queue_dump.enqueue(Order(50, "cust3"))

# Mostrar el estado de la cola
print("********* QUEUE DUMP *********")
print("Size:", queue_dump.size())
print("** Elementos:")
for i in range(queue_dump.size()):
    element = queue_dump.dequeue()
    print("  ** Element", i+1)
    element.print_info()
print("")
