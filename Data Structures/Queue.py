######################################
# Implementation of the Queue (FIFO) in python:
# standard queue operations:
# --------------------------------
# enqueue(): add to queue O(1)
# dequeue(): remove from queue O(1)
# peek(): view the top item of the queue O(1)
# is_empty(): checks if queue is empty  O(1)
#
# Added operations:
# -----------------
# show_queue(): returns items in queue
#
#
# By Doug Purcell
# http://www.purcellconsult.com
#
#
########################################


class Queue:
    """Queue implementation."""
    def __init__(self):
        """create constructor for the Queue."""
        self.q = []

    def enqueue(self, item):
        self.q.append(item)

    def dequeue(self):
        """removes first item from queue"""
        del self.q[0]

    def peek(self):
        """shows the first item in the queue but
        doesn't remove it."""
        print(self.q[0])

    def is_empty(self):
        """checks if queue is empty."""
        return self.q == []

    def show_queue(self):
        print(self.q)


if __name__ == '__main__':
    q = Queue()
    q.enqueue(5)
    q.enqueue('A')
    q.enqueue(1)
    q.show_queue()
    q.dequeue()
    q.enqueue(1000)
    print(q.is_empty())
    q.peek()
    q.show_queue()