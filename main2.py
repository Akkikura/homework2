import types


def flat_generator(list_of_lists):
    lists = list_of_lists
    current_list_index = 0
    current_element = 0
    while current_list_index < len(lists):
        current_list = lists[current_list_index]
        while current_element < len(current_list):
            item = current_list[current_element]
            yield item
            current_element += 1
        current_element = 0
        current_list_index += 1


def test_2():
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for flat_iterator_item, check_item in zip(
            flat_generator(list_of_lists_1),
            ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]
    ):
        assert flat_iterator_item == check_item

    assert list(flat_generator(list_of_lists_1)) == ['a', 'b', 'c', 'd', 'e', 'f', 'h', False, 1, 2, None]

    assert isinstance(flat_generator(list_of_lists_1), types.GeneratorType)


if __name__ == '__main__':
    test_2()
