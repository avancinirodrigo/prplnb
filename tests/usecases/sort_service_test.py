from application.usecases import SortService

def test_sort_service():
    sortKeys = ['fruits', 'numbers']
    dicts = {
        'fruits': ['watermelon', 'apple', 'pineapple'],
        'numbers': [1333, 4, 2431, 7],
        'colors': ['green', 'blue', 'yellow']
    }
    ss = SortService(sortKeys, dicts)
    dicts_sorted = ss.exec()
    assert dicts_sorted['fruits'] == ['apple', 'pineapple', 'watermelon']
    assert dicts_sorted['numbers'] == [4, 7, 1333, 2431]
    assert dicts_sorted['colors'] == ['green', 'blue', 'yellow']
