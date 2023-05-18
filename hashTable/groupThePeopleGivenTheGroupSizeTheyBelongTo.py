# https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:

        groups = defaultdict(list)
        for ind, group_members in enumerate(groupSizes):
            groups[group_members].append(ind)

        result = []

        def making_group (k, v):
            for i in range(0, len(v), k):
                result.append(v[i: i+k])

        for k, v  in groups.items():
            making_group(k, v)

        return result
