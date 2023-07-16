"""
Кастомное множество с новой операцией - взятие случайного элемента из множества. Все операции должны работать за O(1)
"""
import random


class CustomSet:
    def __init__(self):
        self.index_map = {}
        self.values_list = []  # choice from random works by O(1), but not for set

    def __str__(self) -> str:
        return str(self.values_list)

    def contains(self, value) -> bool:
        return value in self.index_map

    def add(self, value) -> None:
        if self.contains(value):
            return
        self.index_map[value] = len(self.values_list)
        self.values_list.append(value)

    def remove(self, value):
        if not self.contains(value):
            return
        i = self.index_map[value]
        last_el = self.values_list[-1]
        self.values_list[i], self.values_list[-1] = self.values_list[-1], self.values_list[i]
        self.index_map[last_el] = i
        self.values_list.pop()
        del self.index_map[value]

    def random_value(self):
        return random.choice(self.values_list)


def main():
    my_set = CustomSet()
    my_set.add(1)  # [1]
    my_set.add(2)  # [1, 2]
    my_set.add(3)  # [1, 2, 3]
    print(my_set)  # [1, 2, 3]
    my_set.remove(2)  # [1, 3]
    my_set.add(4)  # [1, 3, 4]
    my_set.add(2)  # [1, 3, 4, 2]
    my_set.remove(4)  # [1, 3, 2]
    my_set.remove(1)  # [2, 3] (порядок нам не важен)
    print(my_set)  # [2, 3]
    print(my_set.random_value())
    print(my_set.random_value())


if __name__ == '__main__':
    main()
