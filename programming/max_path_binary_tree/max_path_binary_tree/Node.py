class Node:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

    def get_max_path_value(self) -> int:
        if self is None:
            return 0

        left_max_path_value = self.left.get_max_path_value() if self.left else 0
        right_max_path_value = self.right.get_max_path_value() if self.right else 0

        max_path_value = max(self.value, self.value + left_max_path_value, self.value + right_max_path_value)
        max_path_value = max(max_path_value, left_max_path_value + right_max_path_value + self.value)

        return max_path_value
