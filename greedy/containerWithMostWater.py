# Problem_Link: https://leetcode.com/problems/container-with-most-water/

# Runtime: 580 ms, faster than 99.97% of Python3 online submissions for Container With Most Water.
# Memory Usage: 27.6 MB, less than 17.98% of Python3 online submissions for Container With Most Water.

def maxArea(height):
    bar1, bar2 = 0, len(height)-1
    max_area=0
    tallest = max(height)

    while bar1 < bar2:

        area = (bar2-bar1)*min(height[bar1], height[bar2])
        max_area = max(area, max_area)
        if height[bar1] < height[bar2]:
            bar1 += 1
        else:
            bar2 -= 1

        if (bar2-bar1)*tallest < max_area:
            break
    return max_area


height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(maxArea(height))
