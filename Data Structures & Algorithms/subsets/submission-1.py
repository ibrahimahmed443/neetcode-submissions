class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        out = []
        def sub(p, up):
            if not up:
                out.append(p[:])
                return
            
            p.append(up[0])
            sub(p, up[1:])
            p.pop()
            sub(p, up[1:])

        sub([], nums)
        return out