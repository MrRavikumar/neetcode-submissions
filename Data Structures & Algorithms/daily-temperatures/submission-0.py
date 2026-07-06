class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        answer = [0] * len(temperatures)
        for i in range(len(temperatures)):
            while stack and stack[-1][1] < temperatures[i]:
                stack_i, stack_temp = stack.pop()
                answer[stack_i] = i - stack_i
            stack.append((i, temperatures[i]))
        return answer