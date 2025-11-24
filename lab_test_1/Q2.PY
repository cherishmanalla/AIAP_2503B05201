"""
Queue implementation for Q2.

Generated with help from an AI assistant, then tightened manually so that
dequeue/peek raise the proper IndexError on underflow and the demo scenarios
exercise those edge cases instead of silently failing.
"""


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if self.is_empty():
            raise IndexError("dequeue from empty queue")
        return self.items.pop(0)

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty queue")
        return self.items[0]

    def is_empty(self):
        return len(self.items) == 0

    def __len__(self):
        return len(self.items)


print("Scenario 1: Basic enqueue/dequeue")
q = Queue()
q.enqueue(10)
q.enqueue(20)
print("Dequeued:", q.dequeue())       
print("Peek:", q.peek())              

print("\nScenario 2: Peek without removal")
q.enqueue(30)
print("Peek:", q.peek())              
print("Length:", len(q))              

print("\nScenario 3: Multiple dequeues")
print("Dequeued:", q.dequeue())       
print("Dequeued:", q.dequeue())       

print("\nScenario 4: Dequeue from empty queue")
try:
    q.dequeue()
except IndexError as e:
    print("Caught expected error:", e)

print("\nScenario 5: Peek from empty queue")
try:
    q.peek()
except IndexError as e:
    print("Caught expected error:", e)

print("\nScenario 6: Enqueue different data types")
q.enqueue("hello")
q.enqueue([1, 2, 3])
print("Peek:", q.peek())             
print("Length:", len(q))              

print("\nAll tests completed.")

