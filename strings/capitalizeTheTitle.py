# https://leetcode.com/problems/capitalize-the-title/
class Solution(object):
    def capitalizeTitle(self, title):
        """
        :type title: str
        :rtype: str
        """
        return " ".join([i.lower().title() if len(i)>2 else i.lower() for i in title.split(" ")])
print(Solution().capitalizeTitle("caPITalize tHe giVEn tITLE tO YOu"))
        