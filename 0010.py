class SieveOfEritosthenes:
    def __init__(self, limit: int) -> None:
        self.__limit = limit
        self.__marked_list = [True] * (self.__limit + 1)
        self.__marked_list_index = -1

    @property
    def limit(self) -> int:
        return self.__limit

    def __iter__(self):
        return self

    def __next__(self) -> int:
        if self.__limit < 2:
            raise StopIteration
        if self.__marked_list_index == -1:
            self.__marked_list_index = 2
            return 2
        if self.__marked_list_index > self.__limit:
            raise StopIteration
        for prime_multiple in range(self.__marked_list_index * 2, self.__limit + 1, self.__marked_list_index):
            self.__marked_list[prime_multiple] = False
        self.__marked_list_index += 1
        while self.__marked_list_index <= self.__limit:
            if self.__marked_list[self.__marked_list_index]:
                return self.__marked_list_index
            self.__marked_list_index += 1
        raise StopIteration

answer = sum(SieveOfEritosthenes(1999999))
print(answer)