class Solution(object):
    def canBeEqual(self, target, arr):
        r=True
        for i in arr:
            if i not in target:
                r=False
                break
            else:
                target.remove(i)
        return r
        