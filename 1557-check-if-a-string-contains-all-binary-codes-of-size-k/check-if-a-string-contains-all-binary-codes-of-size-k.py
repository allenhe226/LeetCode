class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:
        possible = set()
        for i in range(len(s)-k+1):
            possible.add(s[i:i+k])
        self.res = True
        self.cur = []
        def backtrack():
            if not self.res:
                return
            if len(self.cur) == k:
                if "".join(self.cur) not in possible:
                    self.res = False
                return
            self.cur.append("0")
            backtrack()
            self.cur.pop()
            self.cur.append("1")
            backtrack()
            self.cur.pop()
        backtrack()
        return self.res
            
