def solution(operations):
    import heapq
    heap = []
    
    for s in operations:
        o, n = s.split()
        n = int(n)
        
        if o == 'I':
            heapq.heappush(heap, n)
            
        elif heap:
            if n == 1:
                heap.remove(max(heap))
                heapq.heapify(heap)
            else:
                heapq.heappop(heap)
    if not(heap):
        return [0, 0]
    return [max(heap), heap[0]]