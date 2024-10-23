class MyStack:

        def __init__(self, size):
            self.__element_number = 0
            self.__size = size
            self.__stack = []

        def get_stack_size(self):
            return self.__size

        def is_empty(self):
            return len(self.__stack) == 0

        def push(self, element):
            if len(self._stack) >= self._size:
                raise IndexError("Stack is full")
            self.__stack.append(element)
            self.__element_number += 1

        def pop(self):
            if self.__element_number == 0:
                raise IndexError("Stack is empty")
            number = self._stack[self._element_number - 1]
            self._stack[self._element_number - 1] = None
            self.__element_number -= 1
            return number

        def get_element_number(self):
            return self.__element_number

        def peek(self):
            return self._stack[self._element_number - 1]

        def search(self, element):
            number = self.__element_number
            for index in range(len(self.__stack)):
                if element == self.__stack[index]:
                    return number
                number -= 1

            return -1