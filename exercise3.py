class FlatIterator:

    def __init__(self, list_of_list):
        self.list_of_list = list_of_list
        self.current_list = []
        self.current_index = 0

    def __iter__(self):
        self.current_list = self.flatten(self.list_of_list)
        self.current_index = 0
        return self

    def __next__(self):
        if self.current_index >= len(self.current_list):
            raise StopIteration

        item = self.current_list[self.current_index]
        self.current_index += 1
        return item

    def flatten(self, nested_list):
        flattened_list = []
        for item in nested_list:
            if isinstance(item, list):
                flattened_list.extend(self.flatten(item))
            else:
                flattened_list.append(item)
        return flattened_list

def test_3():

    list_of_lists_2 = [
        [['a'], ['b', 'c']],
        ['d', 'e', [['f'], 'h'], False],
        [1, 2, None, [[[[['!']]]]], []]
    ]

    for flat_iterator_item, check_item in zip(
            FlatIterator(list_of_lists_2),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']
    ):

        assert flat_iterator_item == check_item
    print(list(FlatIterator(list_of_lists_2)))
    assert list(FlatIterator(list_of_lists_2)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None, '!']


if __name__ == '__main__':
    test_3()