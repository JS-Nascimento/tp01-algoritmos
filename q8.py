class ArraySorter:
    def __init__(self, items=None):
        if items is None:
            self.__a = []
        else:
            self.__a = items
        self.__nItems = len(self.__a)

    def swap(self, i, j):

        self.__a[i], self.__a[j] = self.__a[j], self.__a[i]

    def cocktailShakerSort(self):

        left = 0
        right = self.__nItems - 1
        swapped = True

        while swapped:
            swapped = False
            for i in range(left, right):
                if self.__a[i] > self.__a[i + 1]:
                    self.swap(i, i + 1)
                    swapped = True

            right -= 1

            if not swapped:
                break

            swapped = False

            for i in range(right, left, -1):
                if self.__a[i] < self.__a[i - 1]:
                    self.swap(i, i - 1)
                    swapped = True

            left += 1

    def print_array(self):

        print(self.__a)

if __name__ == '__main__':

    sorter = ArraySorter([64, 34, 25, 12, 22, 11, 90])
    print("Array original:")
    sorter.print_array()

    sorter.cocktailShakerSort()

    print("Array ordenado:")
    sorter.print_array()
