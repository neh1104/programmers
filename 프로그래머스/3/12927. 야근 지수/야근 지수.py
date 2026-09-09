def solution(n, works):
    s = sum(works)
    if s <= n:
        return 0
    import heapq
    
    heap = [-w for w in works]
    heapq.heapify(heap)
    
    for i in range(n):
        max_val = heapq.heappop(heap)
        heapq.heappush(heap, max_val+1)
    
    return sum(i**2 for i in heap)