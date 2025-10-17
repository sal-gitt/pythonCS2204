import uuid

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def __init__(self):
        self.root = None

    def get_height(self, node):
        return node.height if node else 0

    def get_balance(self, node):
        return self.get_height(node.left) - self.get_height(node.right) if node else 0

    def rotate_right(self, y):
        x = y.left
        T2 = x.right
        x.right = y
        y.left = T2
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        return x

    def rotate_left(self, x):
        y = x.right
        T2 = y.left
        y.left = x
        x.right = T2
        x.height = 1 + max(self.get_height(x.left), self.get_height(x.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))
        return y

    def insert(self, root, key, value):
        if not root:
            return AVLNode(key, value)
        if key < root.key:
            root.left = self.insert(root.left, key, value)
        elif key > root.key:
            root.right = self.insert(root.right, key, value)
        else:
            return root

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        if balance > 1:
            if key < root.left.key:
                return self.rotate_right(root)
            else:
                root.left = self.rotate_left(root.left)
                return self.rotate_right(root)

        if balance < -1:
            if key > root.right.key:
                return self.rotate_left(root)
            else:
                root.right = self.rotate_right(root.right)
                return self.rotate_left(root)

        return root

    def delete(self, root, key):
        if not root:
            return root
        if key < root.key:
            root.left = self.delete(root.left, key)
        elif key > root.key:
            root.right = self.delete(root.right, key)
        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left
            temp = self.get_min_value_node(root.right)
            root.key = temp.key
            root.value = temp.value
            root.right = self.delete(root.right, temp.key)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        balance = self.get_balance(root)

        if balance > 1:
            if self.get_balance(root.left) >= 0:
                return self.rotate_right(root)
            else:
                root.left = self.rotate_left(root.left)
                return self.rotate_right(root)

        if balance < -1:
            if self.get_balance(root.right) <= 0:
                return self.rotate_left(root)
            else:
                root.right = self.rotate_right(root.right)
                return self.rotate_left(root)

        return root

    def get_min_value_node(self, root):
        current = root
        while current.left:
            current = current.left
        return current

    def inorder(self, root):
        return self.inorder(root.left) + [(root.key, root.value)] + self.inorder(root.right) if root else []

    def postorder(self, root):
        return self.postorder(root.left) + self.postorder(root.right) + [(root.key, root.value)] if root else []

class EnrollmentSystem:
    def __init__(self):
        self.enrollments = AVLTree()
        self.enrollment_root = None
        self.course_trees = {}

    def generate_enrollment_id(self):
        return str(uuid.uuid4())[:8]

    def enroll_student(self, student_name, course_ids):
        enrollment_id = self.generate_enrollment_id()
        record = {'name': student_name, 'id': enrollment_id, 'courses': course_ids}
        self.enrollment_root = self.enrollments.insert(self.enrollment_root, enrollment_id, record)

        for course in course_ids:
            if course not in self.course_trees:
                self.course_trees[course] = AVLTree()
            course_tree = self.course_trees[course]
            course_root = getattr(course_tree, 'root', None)
            course_root = course_tree.insert(course_root, enrollment_id, student_name)
            course_tree.root = course_root

        print(f"Student {student_name} enrolled with ID {enrollment_id}")

    def delete_student_by_id(self, enrollment_id):
        node = self.find_node(self.enrollment_root, enrollment_id)
        if node:
            for course in node.value['courses']:
                if course in self.course_trees:
                    self.course_trees[course].root = self.course_trees[course].delete(self.course_trees[course].root, enrollment_id)
            self.enrollment_root = self.enrollments.delete(self.enrollment_root, enrollment_id)
            print(f"Enrollment ID {enrollment_id} deleted.")
        else:
            print("Enrollment ID not found.")

    def remove_course_from_student(self, enrollment_id, course_id):
        node = self.find_node(self.enrollment_root, enrollment_id)
        if node and course_id in node.value['courses']:
            node.value['courses'].remove(course_id)
            if course_id in self.course_trees:
                self.course_trees[course_id].root = self.course_trees[course_id].delete(self.course_trees[course_id].root, enrollment_id)
            print(f"Course {course_id} removed from student {enrollment_id}")
        else:
            print("Student or course not found.")

    def find_node(self, root, key):
        if not root:
            return None
        if key < root.key:
            return self.find_node(root.left, key)
        elif key > root.key:
            return self.find_node(root.right, key)
        else:
            return root

    def display_all_enrollments(self):
        print("\nAll Enrollments (In-order):")
        for key, value in self.enrollments.inorder(self.enrollment_root):
            print(f"ID: {key}, Name: {value['name']}, Courses: {value['courses']}")

    def inorder_traversal(self):
        return self.enrollments.inorder(self.enrollment_root)

    def postorder_traversal(self):
        return self.enrollments.postorder(self.enrollment_root)

system = EnrollmentSystem()
while True:
  print("\n--- Enrollment System Menu ---")
  print("1. Enroll a student")
  print("2. Display all enrollments")
  print("3. Remove a course from a student")
  print("4. Delete a student by ID")
  print("5. Show in-order traversal")
  print("6. Show post-order traversal")
  print("7. Exit")

try:
  choice = int(input("Enter your choice: "))
  except ValueError:
    print("Invalid input. Please enter a number.")
    continue

match choice:
case 1:
  name = input("Enter student name: ")
  courses = input("Enter course IDs (comma-separated): ").split(",")
  courses = [c.strip() for c in courses if c.strip()]
  system.enroll_student(name, courses)
  
case 2:            
  system.display_all_enrollments()
case 3:
  eid = input("Enter enrollment ID: ")
  cid = input("Enter course ID to remove: ")
  system.remove_course_from_student(eid, cid)

case 4:
  eid = input("Enter enrollment ID to delete: ")
  system.delete_student_by_id(eid)

case 5:
  print("\nIn-order Traversal:")
  for key, val in system.inorder_traversal():
    print(f"{key}: {val}")

case 6:
  print("\nPost-order Traversal:")
  for key, val in system.postorder_traversal():
    print(f"{key}: {val}")

case 7:
  print("Exiting Enrollment System. Goodbye!")
  break

case _:
  print("Invalid choice. Please select a valid option.")
