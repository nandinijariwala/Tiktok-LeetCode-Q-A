class Solution:
    def minSwaps(self, data: List[int]) -> int:
        ones = sum(data)
        
        max_ones = curr_ones = 0
        
        left = right = 0
        
        while right < len(data):
            curr_ones += data[right]
            
            right += 1
            
            if right - left > ones:
                curr_ones -= data[left]
                left += 1
                
            max_ones = max(max_ones, curr_ones)
        
        return ones - max_ones
            
        