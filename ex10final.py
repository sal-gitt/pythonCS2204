from datetime import datetime, timedelta

class CustomerRequest:
    model_priority_map = {
        "RoboLux X10": 4,
        "RoboClean S5": 3,
        "RoboSweep B2": 2,
        "RoboDust M1": 1
    }

    issue_severity_map = {
        "Won't start": 3,
        "Suction power loss": 2,
        "Noisy operation": 1,
        "Battery issues": 2,
        "Brush not spinning": 2,
        "Connectivity problem": 1,
        "Other": 1
    }

    possible_issues = list(issue_severity_map.keys())

    def __init__(self, customer_name, product_model, issue, warranty_end_date, service_expiry_date, request_time=None):
        self.customer_name = customer_name
        self.product_model = product_model

        if issue not in self.possible_issues:
            self.issue = "Other"
            self.issue_description = issue
        else:
            self.issue = issue
            self.issue_description = None

        self.warranty_end_date = warranty_end_date
        self.service_expiry_date = service_expiry_date
        self.request_time = request_time if request_time else datetime.now()
        self.days_before_warranty_end = max((warranty_end_date - self.request_time).days, 0)
        self.has_service = service_expiry_date >= self.request_time
        self.priority = self.calculate_priority()

    def calculate_priority(self):
        model_priority = self.model_priority_map.get(self.product_model, 0)
        warranty_priority = 365 - min(self.days_before_warranty_end, 365)
        issue_priority = self.issue_severity_map.get(self.issue, 1)
        time_priority = -int(self.request_time.timestamp())
        service_priority = 1 if self.has_service else 0
        return (model_priority, issue_priority, warranty_priority, service_priority, time_priority)

    def __lt__(self, other):
        return self.priority < other.priority

    def __repr__(self):
        issue_display = self.issue_description if self.issue == "Other" else self.issue
        return (f"Request({self.customer_name}, Model: {self.product_model}, Issue: {issue_display}, "
                f"Warranty Ends: {self.warranty_end_date.date()}, Service Active: {self.has_service}, "
                f"Request Time: {self.request_time.strftime('%Y-%m-%d %H:%M:%S')})")

class Node:
    def __init__(self, data: CustomerRequest):
        self.data = data
        self.next = None
        self.prev = None

class MaxHeapLinkedList:
    def __init__(self):
        self.head = None

    def insert(self, request: CustomerRequest):
        new_node = Node(request)
        if not self.head or new_node.data > self.head.data:
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
            print(f"Inserted: {request}")
            return

        current = self.head
        while current.next and current.next.data > new_node.data:
            current = current.next

        new_node.next = current.next
        new_node.prev = current
        if current.next:
            current.next.prev = new_node
        current.next = new_node
        print(f"Inserted: {request}")

    def delete_max(self):
        if not self.head:
            print("Heap is empty. No requests to process.")
            return None
        max_node = self.head
        self.head = self.head.next
        if self.head:
            self.head.prev = None
        print(f"Processed (deleted max): {max_node.data}")
        return max_node.data

    def peek_max(self):
        if not self.head:
            print("Heap is empty.")
            return None
        print(f"Next request to process: {self.head.data}")
        return self.head.data

    def display(self):
        if not self.head:
            print("Heap is empty.")
            return
        print("Current Requests in Heap (highest priority first):")
        current = self.head
        while current:
            print(current.data)
            current = current.next

def print_possible_issues():
    print("Possible reported issues:")
    for i, issue in enumerate(CustomerRequest.possible_issues, 1):
        print(f"{i}. {issue}")
    print(f"{len(CustomerRequest.possible_issues) + 1}. Other (enter your own description)")

scheduler = MaxHeapLinkedList()

while True:
  print("\n--- Customer Request Scheduler Menu ---")
  print("1. Insert new request")
  print("2. Display all requests")
  print("3. Peek highest priority request")
  print("4. Process (delete) highest priority request")
  print("5. Exit")
  try:
    choice = int(input("Enter your choice: "))
  except ValueError:
    print("Invalid input. Please enter a number from 1 to 5.")
    continue

        match choice:
            case 1:
                name = input("Customer Name: ")
                model = input("Product Model (RoboLux X10, RoboClean S5, RoboSweep B2, RoboDust M1): ")
                print_possible_issues()
                try:
                    issue_index = int(input("Select issue number: "))
                    if issue_index <= len(CustomerRequest.possible_issues):
                        issue = CustomerRequest.possible_issues[issue_index - 1]
                    else:
                        issue = input("Enter issue description: ")
                except ValueError:
                    print("Invalid issue selection.")
                    continue

                try:
                    warranty_days = int(input("Warranty ends in how many days? "))
                    service_days = int(input("Service subscription ends in how many days? "))
                    now = datetime.now()
                    warranty_end = now + timedelta(days=warranty_days)
                    service_expiry = now + timedelta(days=service_days)
                except ValueError:
                    print("Invalid date input.")
                    continue

                request = CustomerRequest(name, model, issue, warranty_end, service_expiry)
                scheduler.insert(request)

            case 2:
                scheduler.display()

            case 3:
                scheduler.peek_max()

            case 4:
                scheduler.delete_max()

            case 5:
                print("Exiting scheduler. Goodbye!")
                break

            case _:
                print("Invalid choice. Please select a valid option.")
