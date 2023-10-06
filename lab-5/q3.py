class SubsetGenerator:
    def __init__(self):
        self.arr = []

    def print_subsets(self):
        n = len(self.arr)
        num_subsets = 1 << n
        print(num_subsets)

        for i in range(num_subsets):
            subset = []
            for j in range(n):
                if (i >> j) & 1:
                    subset.append(self.arr[j])
            print(subset)

    def take_input(self):
        n = int(input("Enter number of elements: "))
        print("Enter elements:")
        for i in range(n):
            temp = int(input())
            self.arr.append(temp)
        print("List of elements:", self.arr)
        self.print_subsets()


def main():
    subset_generator = SubsetGenerator()
    subset_generator.take_input()


main()
