from bisect import bisect_left, bisect_right

class FenwickTree:
    def __init__(self, size):
        self.size = size
        self.tree = [0] * (size + 1)  
    
    def update(self, index, value):
        while index <= self.size:
            self.tree[index] += value
            index += index & -index  # Move to next  index which is responsive
    
    def query(self, index):
        total = 0
        while index > 0:
            total += self.tree[index]
            index -= index & -index  # for miving to parent node
        return total
    
    def range_query(self, left, right):
        return self.query(right) - self.query(left - 1)

def maintenance_log_analysis(maintenance_logs, queries):
    # Step 1: Extract and sort unique dates for indexing
    unique_dates = sorted(set(date for _, date, _ in maintenance_logs))
    date_to_index = {date: i + 1 for i, date in enumerate(unique_dates)}  
    
    # Step 2: Building Fenwick Tree
    fenwick_tree = FenwickTree(len(unique_dates))
    for _, date, cost in maintenance_logs:
        fenwick_tree.update(date_to_index[date], cost)
    
    # Step 3: Processing  Queries
    results = []
    for start_date, end_date in queries:
        left_idx = bisect_left(unique_dates, start_date) + 1
        right_idx = bisect_right(unique_dates, end_date)  # No need to add 1 here

        # for ensuring indices in valid range
        if left_idx > len(unique_dates) or right_idx == 0 or left_idx > right_idx:
            results.append(0)
        else:
            results.append(fenwick_tree.range_query(left_idx, right_idx))

    return results

# Example usage:
maintenance_logs = [
    (101, "2024-01-01", 500),
    (102, "2024-01-10", 300),
    (101, "2024-01-15", 700)
]
queries = [("2024-01-01", "2024-01-10"), ("2024-01-01", "2024-01-15")]

print(maintenance_log_analysis(maintenance_logs, queries))
