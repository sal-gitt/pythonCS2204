class BinaryTree:
    def __init__(self):
        self.tree = []

    def visualize_preorder(self, i = 0):
        print(self.tree[i], end = " ")
        if (2*i+1) < len(self.tree):
            self.visualize_preorder(2*i+1)
        if (2*i+2) < len(self.tree):
            self.visualize_preorder(2*i+2)
        
    def visualize_inorder(self, i = 0):
        if (2*i+1) < len(self.tree):
            self.visualize_inorder(2*i+1)
        print(self.tree[i], end = " ")
        if (2*i+2) < len(self.tree):
            self.visualize_inorder(2*i+2)
            
    def visualize_postorder(self, i = 0):
        if (2*i+1) < len(self.tree):
            self.visualize_postorder(2*i+1)
        if (2*i+2) < len(self.tree):
            self.visualize_postorder(2*i+2)
        print(self.tree[i], end = " ")
            
bt = BinaryTree()
nodes = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
bt.tree.extend(nodes)

bt.visualize_preorder()
print()
bt.visualize_inorder()
print()
bt.visualize_postorder()
