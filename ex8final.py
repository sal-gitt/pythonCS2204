
import time

class BST:
    def __init__(self):
        self.tree = []

    def get_left_index(self, index):
        return 2 * index + 1

    def get_right_index(self, index):
        return 2 * index + 2

    def get_parent_index(self, index):
        return (index - 1) // 2 if index != 0 else None

    def get_hour(self, timestamp):
        return int(timestamp // 3600)

    def insert(self, visitor_name):
        timestamp = time.time()
        new_node = {"Visitor": visitor_name, "TimeStamp": timestamp}
        if not self.tree:
            self.tree.append(new_node)
            return

        index = 0
        while index < len(self.tree):
            current = self.tree[index]
            current_hour = self.get_hour(current["TimeStamp"])
            new_hour = self.get_hour(timestamp)

            if new_hour < current_hour or (new_hour == current_hour and visitor_name < current["Visitor"]):
                left_index = self.get_left_index(index)
                if left_index >= len(self.tree):
                    self._expand_tree(left_index)
                if self.tree[left_index] is None:
                    self.tree[left_index] = new_node
                    return
                index = left_index
            else:
                right_index = self.get_right_index(index)
                if right_index >= len(self.tree):
                    self._expand_tree(right_index)
                if self.tree[right_index] is None:
                    self.tree[right_index] = new_node
                    return
                index = right_index

    def _expand_tree(self, index):
        while len(self.tree) <= index:
            self.tree.append(None)

    def search_by_name(self, name):
        return [node for node in self.tree if node and node["Visitor"] == name]

    def search_by_timeframe(self, hour):
        return [node for node in self.tree if node and self.get_hour(node["TimeStamp"]) == hour]

    def delete_by_name(self, name):
        for i in range(len(self.tree)):
            if self.tree[i] and self.tree[i]["Visitor"] == name:
                self.tree[i] = None

    def delete_by_timeframe(self, hour):
        for i in range(len(self.tree)):
            if self.tree[i] and self.get_hour(self.tree[i]["TimeStamp"]) == hour:
                self.tree[i] = None

    def visualize(self):
        for i, node in enumerate(self.tree):
            if node is None:
                continue
            parent = self.tree[self.get_parent_index(i)]["Visitor"] if self.get_parent_index(i) is not None and self.tree[self.get_parent_index(i)] else None
            left_index = self.get_left_index(i)
            right_index = self.get_right_index(i)
            left = self.tree[left_index]["Visitor"] if left_index < len(self.tree) and self.tree[left_index] else None
            right = self.tree[right_index]["Visitor"] if right_index < len(self.tree) and self.tree[right_index] else None
            print(f"Node '{node['Visitor']}' at index {i}: parent - {parent}, left child - {left}, right child - {right}")

# Example usage
if __name__ == "__main__":
    bst = BST()
    visitors = ["Alice", "Bob", "Charlie", "David", "Eve", "Frank", "Grace"]
    for name in visitors:
        bst.insert(name)

    print("\nTree Visualization:")
    bst.visualize()

    print("\nSearch by name 'Alice':")
    print(bst.search_by_name("Alice"))

    current_hour = int(time.time() // 3600)
    print(f"\nSearch by current hour ({current_hour}):")
    print(bst.search_by_timeframe(current_hour))

    print("\nDeleting visitor 'Bob'")
    bst.delete_by_name("Bob")
    bst.visualize()

    print(f"\nDeleting all visitors in hour {current_hour}")
    bst.delete_by_timeframe(current_hour)
    bst.visualize()
