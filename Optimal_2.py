import heapq
from collections import defaultdict

def match_requests(requests, sellers):
    # Step 1: Organize sellers into a dictionary of min-heaps
    seller_dict = defaultdict(list)
    
    for eq_type, price in sellers:
        heapq.heappush(seller_dict[eq_type], price)
    
    # Step 2: Process buyer requests
    result = []
    for eq_type, max_price in requests:
        if eq_type in seller_dict:
            while seller_dict[eq_type] and seller_dict[eq_type][0] > max_price:
                heapq.heappop(seller_dict[eq_type])  # Remove overpriced items
            
            if seller_dict[eq_type]:
                result.append(heapq.heappop(seller_dict[eq_type]))  # Get the lowest valid price
            else:
                result.append(None)
        else:
            result.append(None)
    
    return result

# Example usage:
requests = [("excavator", 50000), ("bulldozer", 70000)]
sellers = [("excavator", 45000), ("bulldozer", 68000), ("excavator", 48000)]

print(match_requests(requests, sellers))