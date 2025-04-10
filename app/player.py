import random


class Player:
    random.seed(20)
    pearson_table = list(range(256))
    random.shuffle(pearson_table)

    def __init__(self, uid: str, name: str, score: int = 0):
        self._uid = uid
        self._name = name
        self._score = score

    @property
    def score(self):
        return self._score

    @score.setter
    def score(self, score):
        if score < 0:
            raise ValueError("Score must be a positive integer value.")
        self._score = score

    @property
    def uid(self):
        return self._uid

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @classmethod
    def hash(cls, key: str) -> int:
        byte_values = bytes(key, encoding='utf8')
        _hash = 0
        for each_byte in byte_values:
            _hash = cls.pearson_table[_hash ^ each_byte]
        return _hash

    def _pearson_hash(self, key) -> int:
        byte_values = bytes(key, encoding='utf8')
        _hash = 0
        for each_byte in byte_values:
            _hash = self.pearson_table[_hash ^ each_byte]
        return _hash

    @classmethod
    def sort(cls, arr: list["Player"], descend=True):
        list_sorted = Player.is_sorted(arr, descend=descend)

        if list_sorted or len(arr) <= 1:
            return arr

        pivot = arr[0]
        left = []
        right = []

        for x in arr[1:]:
            if descend is False and x < pivot or descend and x > pivot:
                left.append(x)
            else:
                right.append(x)

        return cls.sort(left, descend) + [pivot] + cls.sort(right, descend)

    @staticmethod
    def is_sorted(arr: list["Player"], descend=True):
        list_sorted = False
        index = 0

        while index < len(arr) - 1:
            if descend and arr[index] > arr[index + 1] or descend is False and arr[index] < arr[index + 1]:
                list_sorted = True
                index += 1
            else:
                list_sorted = False
                break
        return list_sorted

    def __hash__(self) -> int:
        return self._pearson_hash(self._uid)

    def __str__(self):
        return f'Unique Id: {self.uid}, Player Name: {self.name}'

    def __lt__(self, other: 'Player') -> bool:
        return self.score < other.score

    def __gt__(self, other: 'Player') -> bool:
        return self.score > other.score

    def __ge__(self, other: 'Player') -> bool:
        return self.score >= other.score

    def __repr__(self):
        class_name = type(self).__name__
        return f"{class_name}({self.score})"


if __name__ == "__main__":
    dan = Player('04', "Dan", 25)
    alice = Player('01', "Alice", 5)
    bob = Player('02', "Bob", 10)
    charlie = Player('03', "Charlie", 15)
    print(Player.sort([dan, alice, bob, charlie], descend=False))

    print(Player.sort([dan, alice, bob, charlie]))

