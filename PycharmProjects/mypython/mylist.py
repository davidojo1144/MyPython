class ArrayList:
    def __init__(self):
        self.__array = []

    def is_empty(self):
        return len(self.__array) == 0

    def add(self, element):
        if element == None:
            return False
        self.__array.append(element)
        return True

    def size(self):
        return len(self.__array)

    def remove(self, index, element):
        if index < 0 or index >= len(self.__array):
            raise IndexError

        self.__array.pop(element)