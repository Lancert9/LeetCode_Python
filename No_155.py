class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.main_stack = list()
        self.support_stack = list()

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.main_stack.append(x)
        if len(self.main_stack) > 1:
            top_item = self.support_stack[-1]
            if x < top_item:
                self.support_stack.append(x)
            else:
                self.support_stack.append(top_item)
        else:
            self.support_stack.append(x)

    def pop(self):
        """
        :rtype: void
        """
        assert len(self.main_stack) >= 0, 'Can not pop from an empty stack.'
        self.main_stack.pop()
        self.support_stack.pop()

    def top(self):
        """
        :rtype: int
        """
        assert len(self.main_stack) >= 0, 'Can not get top from an empty stack.'
        return self.main_stack[-1]

    def getMin(self):
        """
        :rtype: int
        """
        assert len(self.main_stack) >= 0, 'Can not get min from an empty stack'
        return self.support_stack[-1]


if __name__ == '__main__':
    my_stack = MinStack()
    my_stack.push(-2)
    my_stack.push(0)
    my_stack.push(-3)
    print my_stack.getMin()
    my_stack.pop()
    print my_stack.top()
    print my_stack.getMin()
