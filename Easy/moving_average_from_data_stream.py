class MovingAverage:
    def __init__(self, size: int):
        """
        Initialize your data structure here.
        """
        self.data = []
        self.size = size
        

    def next(self, val: int) -> float:
        self.data.append(val)
        moving_average = 0.0
        for d in self.data[-self.size:]:
            moving_average += d
        moving_average /= min(self.size, len(self.data))
        return moving_average

# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)