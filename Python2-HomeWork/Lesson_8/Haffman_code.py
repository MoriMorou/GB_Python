import heapq
from collections import Counter

# узел
class Node:
    def __init__(self, left=None, right=None):
        self.left = left
        self.right = right

#  лист
class Leaf:
    def __init__(self, ch):
        self.ch = ch


# heapq используем для очереди с приоритетами
# freq частота символа
# queue очередь


def huffman_code(string):
    # строим очередь в виде списка с парами частота и символ
    queue = [(freq, Leaf(ch)) for ch, freq in Counter(string).items()]
    # строим очередь
    heapq.heapify(queue)
    while len(queue) > 1:
        freq1, left = heapq.heappop(queue)
        freq2, right = heapq.heappop(queue)
        heapq.heappush(freq1 + freq2, Node(left, right))


    result = {}
    return result


if __name__ == '__main__':
    string = input("Input the string for encoding: ")
    code = huffman_code(string)
    encoded = "".join(code[ch] for ch in string)
    # выводим результат
    print("Keys =", len(code), "Encoded string length =", len(encoded))
    # для удобства, символы обходим в алфавитном порядке
    for ch in sorted(code):
        print(f'{ch}: {code[ch]}')
    print(encoded)