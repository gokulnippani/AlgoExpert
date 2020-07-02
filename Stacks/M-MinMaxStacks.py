class MinMaxStack:
    def __init__(self):
        self.minMaxStack = []
        self.stack = []
    def peek(self):
        return self.stack[len(self.stack)-1]

    def pop(self):
        self.minMaxStack.pop()
        return self.stack.pop()

    def push(self, number):
        newMinMax = {"min": number, "max": number}
        if len(self.minMaxStack):
            prevMinMax = self.minMaxStack[len(self.minMaxStack) - 1 ]
            newMinMax["min"] = min(newMinMax["min"], prevMinMax["min"])
            newMinMax["max"] = max(newMinMax["max"], prevMinMax["max"])
        
        self.minMaxStack.append(newMinMax)
        self.stack.append(number)

    # O(1) time | O(1) space
    def getMin(self):
        return self.minMaxStack[len(self.minMaxStack) - 1]["min"]

    def getMax(self):
        return self.minMaxStack[len(self.minMaxStack) - 1]["max"]

minMax = MinMaxStack()
minMax.push(1)
minMax.push(7)
print(minMax.getMax())

