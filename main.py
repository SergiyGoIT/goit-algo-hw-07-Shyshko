# Завдання 1: Знайти найбільше значення у двійковому дереві пошуку
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def find_max(root):
    if not root:
        return None
    current = root
    while current.right:
        current = current.right
    return current.value

# Завдання 2: Знайти найменше значення у двійковому дереві пошуку
def find_min(root):
    if not root:
        return None
    current = root
    while current.left:
        current = current.left
    return current.value

# Завдання 3: Знайти суму всіх значень у двійковому дереві пошуку
def sum_values(root):
    if not root:
        return 0
    return root.value + sum_values(root.left) + sum_values(root.right)

# Завдання 4: Система коментарів
class Comment:
    def __init__(self, text, author):
        self.text = text
        self.author = author
        self.replies = []
        self.is_deleted = False

    def add_reply(self, reply):
        self.replies.append(reply)

    def remove_reply(self):
        self.text = "Цей коментар було видалено."
        self.is_deleted = True

    def display(self, level=0):
        indent = "    " * level
        if self.is_deleted:
            print(f"{indent}{self.text}")
        else:
            print(f"{indent}{self.author}: {self.text}")
        for reply in self.replies:
            reply.display(level + 1)

# Приклад використання
if __name__ == "__main__":
    # Тестування двійкового дерева
    root = Node(10)
    root.left = Node(5)
    root.right = Node(15)
    root.left.left = Node(3)
    root.left.right = Node(7)
    root.right.right = Node(20)

    print("Завдання 1: Найбільше значення:", find_max(root))  # Очікуваний результат: 20
    print("Завдання 2: Найменше значення:", find_min(root))  # Очікуваний результат: 3
    print("Завдання 3: Сума всіх значень:", sum_values(root))  # Очікуваний результат: 60

    print("\nЗавдання 4: Система коментарів")
    root_comment = Comment("Яка цікава стаття!", "Бодя")
    reply1 = Comment("Стаття повне розчарування :(", "Андрій")
    reply2 = Comment("Що в ній цікавого?", "Марина")

    root_comment.add_reply(reply1)
    root_comment.add_reply(reply2)

    reply1_1 = Comment("Не стаття, а перевели купу паперу ні нащо...", "Сергій")
    reply1.add_reply(reply1_1)

    reply1.remove_reply()

    root_comment.display()