from typing import List

class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

    def get_max_path_value(self) -> int:
        if not self.left and not self.right:
            return self.value

        left_max_path_value = self.left.get_max_path_value() if self.left else 0
        right_max_path_value = self.right.get_max_path_value() if self.right else 0

        max_path_value = max(self.value, self.value + left_max_path_value, self.value + right_max_path_value)
        return max_path_value


def get_max_path_value(root: Node) -> int:
    if not root:
        return 0

    return root.get_max_path_value()


if __name__ == "__main__":
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)
    root.right.right = Node(7)

    max_path_value = get_max_path_value(root)
    print(max_path_value)  # Output: 15
