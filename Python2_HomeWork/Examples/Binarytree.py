from binarytree import tree, bst, Node


class MyNode:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


a = tree(height=2, is_perfect=True)
print(a)
b = bst(height=3, is_perfect=True)
print(b)

root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.right = Node(7)
root.right.left = Node(12)
print(root)


print('*' * 50)
bt = bst(height=5, is_perfect=False)
print(bt)
num = int(input('Что найти: '))

def search(bin_tree, number, path=''):
    print(path)
    if bin_tree.value == number:
        return f'Число {number} находится по следующему пути:\nКорень{path}'
    if number < bin_tree.value and bin_tree.left is not None:
        return search(bin_tree.left, number, path=f'{path}\nШаг влево')
    if number > bin_tree.value and bin_tree.right is not None:
        return search(bin_tree.right, number, path=f'{path}\nШаг вправо')
    return f'Число {number} отсутствует'


print(search(bt, number=num))
