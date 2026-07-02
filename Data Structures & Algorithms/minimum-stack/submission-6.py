class MinStack:

    # # Brute Force

    # def __init__(self):
    #     self.st = []
        

    # def push(self, value: int) -> None:
    #     if not self.st:
    #         self.st.append((value, value))
    #         return
    #     mini = min(self.getMin(), value)
    #     self.st.append((value, mini))
        

    # def pop(self) -> None:
    #     self.st.pop()
        

    # def top(self) -> int:
    #     return self.st[-1][0]
        

    # def getMin(self) -> int:
    #     return self.st[-1][-1]

     # Optimal Approach

    def __init__(self):
        self.st = []
        self.mini = None
        

    def push(self, value: int) -> None:
        if not self.st:
            self.mini = value
            self.st.append(value)
            return
        if value > self.mini:
            self.st.append(value)
        else:
            self.st.append(2 * value - self.mini)
            self.mini = value

    def pop(self) -> None:
        if not self.st:
            return -1
        x = self.st.pop()
        if x < self.mini:
            self.mini = 2 * self.mini - x
        

    def top(self) -> int:
        if not self.st:
            return -1

        x = self.st[-1]
        if x > self.mini:
            return x
        return self.mini
        

    def getMin(self) -> int:
        return self.mini