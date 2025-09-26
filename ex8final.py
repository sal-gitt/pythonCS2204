import time

class BST:
    def __init__(self):
        self.tree = []

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
                left_index = 2 * index + 1
                if left_index >= len(self.tree):
                    self._expand_tree(left_index)
                if self.tree[left_index] is None:
                    self.tree[left_index] = new_node
                    return
                index = left_index
            else:
                right_index = 2 * index + 2
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

    def visualize_preorder(self, index=0):
        if index >= len(self.tree) or self.tree[index] is None:
            return
        print(self.tree[index]["Visitor"], end=", ")
        self.visualize_preorder(2 * index + 1)
        self.visualize_preorder(2 * index + 2)

    def visualize_inorder(self, index=0):
        if index >= len(self.tree) or self.tree[index] is None:
            return
        self.visualize_inorder(2 * index + 1)
        print(self.tree[index]["Visitor"], end=", ")
        self.visualize_inorder(2 * index + 2)

    def visualize_postorder(self, index=0):
        if index >= len(self.tree) or self.tree[index] is None:
            return
        self.visualize_postorder(2 * index + 1)
        self.visualize_postorder(2 * index + 2)
        print(self.tree[index]["Visitor"], end=", ")

bst = BST()
while True:
print("\n--- Visitor BST Menu ---")
        print("1. Add new visitor")
        print("2. Search by name")
        print("3. Search by hour")
        print("4. Delete by name")
        print("5. Delete by hour")
        print("6. Display tree (Pre-order)")
        print("7. Display tree (In-order)")
        print("8. Display tree (Post-order)")
        print("9. Exit")

        choice = input("Enter your choice (1-9): ")

        match choice:
            case "1":
                name = input("Enter visitor name: ")
                bst.insert(name)
                print(f"Visitor '{name}' added.")
            case "2":
                name = input("Enter name to search: ")
                result = bst.search_by_name(name)
                print("Search result:", result if result else "No match found.")
            case "3":
                hour = int(input("Enter hour to search: "))
                result = bst.search_by_timeframe(hour)
                print("Search result:", result if result else "No match found.")
            case "4":
                name = input("Enter name to delete: ")
                bst.delete_by_name(name)
                print(f"Visitor '{name}' deleted.")
            case "5":
                hour = int(input("Enter hour to delete visitors: "))
                bst.delete_by_timeframe(hour)
                print(f"Visitors in hour {hour} deleted.")
            case "6":
                print("Pre-order traversal:")
                bst.visualize_preorder()
                print()
            case "7":
                print("In-order traversal:")
                bst.visualize_inorder()
                print()
            case "8":
                print("Post-order traversal:")
                bst.visualize_postorder()
                print()
            case "9":
                print("Exiting program.")
                break
            case _:
                print("Invalid choice. Please enter a number between 1 and 9.")
