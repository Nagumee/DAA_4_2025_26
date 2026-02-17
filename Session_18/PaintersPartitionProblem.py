class Solution:
    def minTime (self, arr, k):
        n = len(arr)
        low, high = max(arr), sum(arr)

        def can_paint(limit):
            painters = 1
            curr = 0
            for x in arr:
                if curr + x <= limit:
                    curr += x
                else:
                    painters += 1
                    curr = x
                    if painters > k:
                        return False
            return True

        ans = high
        while low <= high:
            mid = (low + high) // 2
            if can_paint(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
        return ans