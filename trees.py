class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, current_node, key):
        if key < current_node.val:
            if current_node.left is None:
                current_node.left = Node(key)
            else:
                self._insert_recursive(current_node.left, key)
        elif key > current_node.val:
            if current_node.right is None:
                current_node.right = Node(key)
            else:
                self._insert_recursive(current_node.right, key)

    def find_max(self):
        if self.root is None:
            return None

        current = self.root

        while current.right is not None:
            current = current.right
        return current.val

    def find_min(self):
        #Знаходить найменше значення у двійковому дереві пошуку.#
        if self.root is None:
            return None

        current = self.root
        # Найменший елемент завжди знаходиться в крайньому лівому вузлі
        while current.left is not None:
            current = current.left
        return current.val

    def find_sum(self):
        return self._sum_recursive(self.root)

    def _sum_recursive(self, node):
        if node is None:
            return 0
        return node.val + self._sum_recursive(node.left) + self._sum_recursive(node.right)

print("--- Демонстрація роботи з Двійковим деревом пошуку ---")
bst = BinarySearchTree()
elements = [65, 90, 30, 20, 80, 60, 15, 25, 75, 40, 55]
for el in elements:
    bst.insert(el)

print(f"Елементи в дереві: {elements}")
print(f"Найбільше значення в дереві: {bst.find_max()}")  # Очікуваний результат: 80
print(f"Найменше значення в дереві: {bst.find_min()}")    # Очікуваний результат: 20
print(f"Сума всіх значень в дереві: {bst.find_sum()}")      # Очікуваний результат: 450
print("-" * 50)


class Comment:
    def __init__(self, text: str, author: str):
        self.text = text
        self.author = author
        self.replies = []
        self.is_deleted = False

    def add_reply(self, reply):
        self.replies.append(reply)

    def remove_reply(self, reply):
        for r in self.replies:
            if r == reply:
                r.text = "Цей коментар було видалено."
                r.author = ""
                r.is_deleted = True
                break

    def display(self, level=0):
        indent = "    " * level
        if self.is_deleted:
            print(f"{indent}{self.text}")
        else:
            print(f"{indent}{self.author}: {self.text}")
        
        for reply in self.replies:
            reply.display(level + 1)

print("\n---------------- Завдання 4 ------------------")
print("\n--- Демонстрація роботи системи коментарів ---")

root_comment = Comment("Яка чудова книга!", "Бодя")
reply1 = Comment("Книга повне розчарування :(", "Андрій")
reply2 = Comment("Що в ній чудового?", "Марина")

root_comment.add_reply(reply1)
root_comment.add_reply(reply2)

reply1_1 = Comment("Не книжка, а перевели купу паперу ні нащо...", "Сергій")
reply1.add_reply(reply1_1)

root_comment.remove_reply(reply1)

root_comment.display()
print("-" * 50)
