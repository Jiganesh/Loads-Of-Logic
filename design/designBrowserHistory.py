# https://leetcode.com/problems/design-browser-history/


class BrowserHistory:
    
    # Runtime: 283 ms, faster than 84.47% of Python3 online submissions for Design Browser History.
    # Memory Usage: 16.6 MB, less than 65.48% of Python3 online submissions for Design Browser History.
    
    def __init__(self, homepage: str):
        self.bs = [homepage]
        self.fs = []

    def visit(self, url: str) -> None:
        self.bs.append(url)
        self.fs = []

    def back(self, steps: int) -> str:
        
        x = len(self.bs)-1
        steps = min(steps, x)
        
        while self.bs and steps:
            self.fs.append(self.bs.pop())
            steps-=1
        
        return self.bs[-1]
        

    def forward(self, steps: int) -> str:

        x = len(self.fs)
        steps = min(steps, x)
        
        while self.fs and steps:
            self.bs.append(self.fs.pop())
            steps-=1
        
        return self.bs[-1]
        

# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)