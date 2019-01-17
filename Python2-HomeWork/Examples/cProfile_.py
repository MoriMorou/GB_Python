import cProfile


def get_len(array):
    return len(array)


def get_sum(array):
    sum_ = 0
    for item in array:
        sum_ += item
    return sum_


def main():
    lst = [i for i in range(10000000)]
    len_ = get_len(lst)
    sum_ = get_sum(lst)


cProfile.run('main()')
