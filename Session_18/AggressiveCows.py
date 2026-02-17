class Solution:
    def aggressiveCows(self, stalls, k):
        stalls.sort()
        n = len(stalls)

        def can_place(d):
            count = 1
            last = stalls[0]
            for i in range(1, n):
                if stalls[i] - last >= d:
                    count += 1
                    last = stalls[i]
                    if count >= k:
                        return True
            return False

        low, high = 1, stalls[-1] - stalls[0]
        ans = 0
        while low <= high:
            mid = (low + high) // 2
            if can_place(mid):
                ans = mid
                low = mid + 1
            else:
                high = mid - 1
        return ans
        