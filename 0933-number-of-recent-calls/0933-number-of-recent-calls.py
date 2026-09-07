from collections import deque

class RecentCounter:

    def __init__(self):
        # Create an empty queue
        self.q = deque()

    def ping(self, t: int) -> int:
        # Add the new request
        self.q.append(t)

        # Remove requests older than 3000 milliseconds
        while self.q[0] < t - 3000:
            self.q.popleft()

        # Return the number of requests in the last 3000 ms
        return len(self.q)


# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)

