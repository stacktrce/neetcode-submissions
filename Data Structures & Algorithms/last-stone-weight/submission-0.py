class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        max_heap = [-x for x in stones]
        heapq.heapify(max_heap)

        while len(max_heap) > 1:
            max = heapq.heappop(max_heap)
            second = heapq.heappop(max_heap)
            if second > max:
                heapq.heappush(max_heap, max - second)
        
        max_heap.append(0)
        return abs(max_heap[0])