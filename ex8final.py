from datetime import datetime
from collections import defaultdict

class Entry:
    def __init__(self, name: str, entry_time: str, purpose: str):
        self.name = name
        self.entry_time = datetime.strptime(entry_time, '%Y-%m-%d %H:%M:%S')
        self.purpose = purpose

    def __str__(self):
        return f"Name: {self.name}, Time: {self.entry_time}, Purpose: {self.purpose}"

class Node:
    def __init__(self, entry: LogEntry):
        self.entry = entry
        self.left = None
        self.right = None

class BST:
    def __init__(self, sort_by='name'):
        if sort_by not in ('name', 'time', 'purpose'):
            raise ValueError("Sort_by must be 'name', 'time', or 'purpose'")
        self.root = None
        self.sort_by = sort_by

    def _compare(self, e1: LogEntry, e2: LogEntry):
        if self.sort_by == 'name':
            return (e1.name.lower() > e2.name.lower()) - (e1.name.lower() < e2.name.lower())
        elif self.sort_by == 'time':
            return (e1.entry_time > e2.entry_time) - (e1.entry_time < e2.entry_time)
        elif self.sort_by == 'purpose':
            return (e1.purpose.lower() > e2.purpose.lower()) - (e1.purpose.lower() < e2.purpose.lower())

    def insert(self, entry: LogEntry):
        def _insert(node, entry):
            if node is None:
                return BSTNode(entry)
            cmp = self._compare(entry, node.entry)
            if cmp < 0:
                node.left = _insert(node.left, entry)
            else:
                node.right = _insert(node.right, entry)
            return node
        self.root = _insert(self.root, entry)

    def display_entries(self):
        print(f"\nLog Entries (Sorted by {self.sort_by}):")
        def _in_order(node):
            if node:
                _in_order(node.left)
                print(node.entry)
                _in_order(node.right)
        _in_order(self.root)

    def post_order(self):
        print(f"\nLog Entries (Post-order traversal by {self.sort_by}):")
        def _post_order(node):
            if node:
                _post_order(node.left)
                _post_order(node.right)
                print(node.entry)
        _post_order(self.root)

    def search(self, key):
        results = []
        if self.sort_by == 'time':
            try:
                search_time = datetime.strptime(key, '%Y-%m-%d %H:%M:%S')
            except ValueError:
                print("Invalid time format. Use YYYY-MM-DD HH:MM:SS")
                return results
            def _search_by_time(node):
                if node:
                    if node.entry.entry_time == search_time:
                        results.append(node.entry)
                    if search_time < node.entry.entry_time:
                        _search_by_time(node.left)
                    else:
                        _search_by_time(node.right)
            _search_by_time(self.root)
        elif self.sort_by == 'name':
            search_name = key.lower()
            def _search_by_name(node):
                if node:
                    if node.entry.name.lower() == search_name:
                        results.append(node.entry)
                    _search_by_name(node.left)
                    _search_by_name(node.right)
            _search_by_name(self.root)
        return results

    def search_by_timeframe(self, date_str, start_time_str, end_time_str):
        results = []
        try:
            date = datetime.strptime(date_str, '%Y-%m-%d').date()
            start_time = datetime.strptime(start_time_str, '%H:%M').time()
            end_time = datetime.strptime(end_time_str, '%H:%M').time()
        except ValueError:
            print("Invalid date or time format.")
            return results
        def _traverse(node):
            if node:
                _traverse(node.left)
                entry_date = node.entry.entry_time.date()
                entry_time = node.entry.entry_time.time()
                if (entry_date == date and start_time <= entry_time <= end_time):
                    results.append(node.entry)
                _traverse(node.right)
        _traverse(self.root)
        return results

    def generate_duplicate_entries_tree(self):
        name_counts = defaultdict(int)
        def _count_names(node):
            if node:
                _count_names(node.left)
                name_counts[node.entry.name.lower()] += 1
                _count_names(node.right)
        _count_names(self.root)
        duplicates_tree = LogBookBST(sort_by='name')
        def _collect_duplicates(node):
            if node:
                _collect_duplicates(node.left)
                if name_counts[node.entry.name.lower()] > 1:
                    duplicates_tree.insert(node.entry)
                _collect_duplicates(node.right)
        _collect_duplicates(self.root)
        return duplicates_tree

    def generate_shared_purpose_tree(self):
        purpose_count = defaultdict(int)
        def _count_purposes(node):
            if node:
                _count_purposes(node.left)
                purpose_count[node.entry.purpose.lower()] += 1
                _count_purposes(node.right)
        _count_purposes(self.root)
        shared_purpose_tree = LogBookBST(sort_by='purpose')
        def _insert_shared_purposes(node):
            if node:
                _insert_shared_purposes(node.left)
                if purpose_count[node.entry.purpose.lower()] > 1:
                    shared_purpose_tree.insert(node.entry)
                _insert_shared_purposes(node.right)
        _insert_shared_purposes(self.root)
        return shared_purpose_tree

logbook = LogBookBST(sort_by='time')

while True:
    print("\n--- Visitor LogBook Menu ---")
    print("1. Add new log entry")
    print("2. Display all entries (in-order)")
    print("3. Display entries (post-order)")
    print("4. Search by visitor name")
    print("5. Search by exact entry time")
    print("6. Search by date and timeframe")
    print("7. Show duplicate visitors tree")
    print("8. Show shared purpose tree")
    print("9. Exit")

    try:
        choice = int(input("Enter your choice: "))
    except ValueError:
        print("Invalid input. Please enter a number.")            
        continue

    match choice:
        case 1:
            name = input("Visitor Name: ")
            time_str = input("Entry Time (YYYY-MM-DD HH:MM:SS): ")
            purpose = input("Purpose of Visit: ")
            try:
                entry = LogEntry(name, time_str, purpose)
                logbook.insert(entry)
                print("Entry added successfully.")
            except ValueError:
                print("Invalid date format. Please try again.")
        case 2:
            logbook.display_entries()
            
        case 3:
            logbook.post_order()

        case 4:
            name_query = input("Enter visitor name to search: ")
            results = logbook.search(name_query)
            print(f"\nSearch results for name '{name_query}':")
            for r in results:
                print(r)
        case 5:
            time_query = input("Enter entry time (YYYY-MM-DD HH:MM:SS): ")
            results = logbook.search(time_query) 
            print(f"\nSearch results for time '{time_query}':")
            for r in results:
                print(r)
                
        case 6:
            date = input("Enter date (YYYY-MM-DD): ")
            start = input("Start time (HH:MM): ")   
            end = input("End time (HH:MM): ")
            results = logbook.search_by_timeframe(date, start, end)
            print(f"\nEntries on {date} between {start} and {end}:")
            for r in results:
                print(r)

        case 7:
            duplicates_tree = logbook.generate_duplicate_entries_tree()
            duplicates_tree.display_entries()                
            duplicates_tree.post_order()

        case 8:
            purpose_tree = logbook.generate_shared_purpose_tree()
            purpose_tree.display_entries()      
            purpose_tree.post_order()

        case 9:
            print("Exiting LogBook. Goodbye!")
            break
            
        case _:
            print("Invalid choice. Please select a valid option.")
