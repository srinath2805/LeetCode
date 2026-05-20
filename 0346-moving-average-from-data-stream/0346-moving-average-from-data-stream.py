from collections import deque

class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.queue = deque()
        self.window_sum = 0.0

    def next(self, val: int) -> float:
        # Add the new value
        self.queue.append(val)
        self.window_sum += val

        # Remove oldest if we exceed window size
        if len(self.queue) > self.size:
            removed = self.queue.popleft()
            self.window_sum -= removed

        # Return moving average
        return self.window_sum / len(self.queue)