class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area, left, right = 0, 0, len(height) - 1

        while left < right:
            lenght = right - left
            max_area = max(max_area, lenght * min(height[left], height[right]))
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1

        return max_area
