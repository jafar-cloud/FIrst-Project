class Solution:
    def solution(self, numbs: tuple[int], val: int):
        target = 0
        indices = []
        for idx, i in enumerate(numbs):
            if target == val:
                return indices.append(idx)

            if target < val:
                target += val
                indices.append(idx)
            
            elif target > val:
                continue


a = Solution()

a.solution((1, 2, 3, 4, 5, 6), 11)
            