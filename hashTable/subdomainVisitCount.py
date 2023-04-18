# https://leetcode.com/problems/subdomain-visit-count/

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:

        result = []
        lookup = defaultdict(int)
        for cpdomain in cpdomains:

            visit, domain = cpdomain.split(" ")
            lookup[domain] += int(visit)

            for ind, ch in enumerate(domain):
                if ch == ".":
                    lookup[domain[ind+1:]] += int(visit)

        for k , v in lookup.items():
            result.append(str(v) + " " + k)
        
        return result
