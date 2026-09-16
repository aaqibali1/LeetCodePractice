class Solution:
    def minEatingSpeed(self, piles, h):
        left = 1
        right = max(piles)

        while left < right:
            speed = left + (right - left) // 2

            hours = 0

            for pile in piles:
                hours += (pile + speed - 1) // speed

            if hours <= h:
                # Speed works, so try a smaller speed.
                right = speed
            else:
                # Speed is too slow, so increase it.
                left = speed + 1

        return left
