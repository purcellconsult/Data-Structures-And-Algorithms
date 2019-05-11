#################################################
# Stacks data structure implementation in python:
# Implements stack using list
# Common stack operations:
# push(): adds item to stack O(1)
# pop(): removes top item from stack  O(1)
# peek(): views top item in stack(doesn't remove)  O(1)
# is_empty(): checks to see if stack is empty  O(1)
#
#
#
# By Doug Purcell
# http://www.purcellconsult.com
#
#
#
##################################################


class Stack():
    """Stack implementation in python."""
    def __init__(self):
        self.items = []

    def push(self, item):
        """adds item to the end of a stack."""
        self.items.append(item)

    def pop(self):
        """removes the last item from a stack"""
        return self.items.pop()

    def get_items(self):
        """returns the items from a stack."""
        return self.items

    def is_empty(self):
        """checks if a stack is empty or not."""
        if len(self.items) == 0:
            return True
        return False

    def peek(self):
        """views the top item of the stack."""
        if self.is_empty():
            return
        print(self.items[-1])

    def beautify(self):
        """Formats the stack so that it looks
        more like a real world stack.
        Displays stack vertically."""
        a = -1
        while a >= -(len(self.items)):
            print(self.items[a])
            print('-')
            a -= 1


if __name__ == '__main__':
    s = Stack()
    s.push('A')
    s.push('B')
    s.push('C')
    print(s.pop())
    print(s.pop())
    print()
    s.push('D')
    s.push('E')
    s.push('F')
    print(s.get_items())
    print(s.is_empty())
    s.peek()
    print()
    s.beautify()
