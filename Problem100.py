import math

def test():
    inputs = ["1 10", "100 200", "201 210", "900 1000", "22 22"]
    for input in inputs:
        splitInput = input.split()
        maxCycleLength = Problem100(int(splitInput[0]), int(splitInput[1]))
        print(f"{splitInput[0]} {splitInput[1]} {maxCycleLength}")

def Problem100(lowerBound, upperBound):
    #the 3N + 1 problem
    #https://onlinejudge.org/index.php?option=com_onlinejudge&Itemid=8&category=3&page=show_problem&problem=36
    
    def getCycleLength(n):
        if n == 1:
            return 1
        if n % 2 != 0:
            return 1 + getCycleLength(3 * n + 1)
        else:
            return 1 + getCycleLength(n / 2)
        
    maxCycleLength = 0
    greatestPowerOf2InInputRange = 0
    #find highest power of 2 in input range, for us to use as the MINIMUM cycle length - possible greater cycle lenghts would lie only in the inputs after such power of 2
    for i in range(upperBound,lowerBound, -1):
        log2n = math.log(i, 2)
        if str(log2n).endswith('.0'):
            maxCycleLength = log2n + 1
            break

    for i in range(max(greatestPowerOf2InInputRange + 1, lowerBound), upperBound):
        cycleLength = getCycleLength(i)
        if cycleLength > maxCycleLength:
            maxCycleLength = cycleLength

    return maxCycleLength

test()