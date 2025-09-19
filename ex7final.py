class BinaryTree:
    def __init__(self):
        self.tree = []

    def insert(self, value):
        self.tree.append(value)

    def get_left_index(self, index):
        return 2 * index + 1

    def get_right_index(self, index):
        return 2 * index + 2

    def get_parent_index(self, index):
        return (index - 1) // 2 if index != 0 else None

    def visualize(self):
        for i, val in enumerate(self.tree):
            parent = self.tree[self.get_parent_index(i)] if self.get_parent_index(i) is not None else None
            left = self.tree[self.get_left_index(i)] if self.get_left_index(i) < len(self.tree) else None
            right = self.tree[self.get_right_index(i)] if self.get_right_index(i) < len(self.tree) else None

            print(f"Node '{val}' at index {i}: parent - {parent}, left child - {left}, right child - {right}")

# Example usage
bt = BinaryTree()
nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
for node in nodes:
    bt.insert(node)

bt.visualize()
