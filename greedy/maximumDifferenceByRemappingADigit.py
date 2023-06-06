# https://leetcode.com/problems/maximum-difference-by-remapping-a-digit/

class Solution:
    def minMaxDifference(self, num: int) -> int:

        # Step 1 : Create maximum number
        n = str(num)
        digit = "0"
        for i in n:
            if i == "9":
                continue
            else:
                digit = i
                break

        maximum_value = n.replace(digit, "9")

        # Step 2 : Create minimum number
        digit = n[0]
        minimum_value = n.replace(digit, "0")

        return int(maximum_value) - int(minimum_value)

