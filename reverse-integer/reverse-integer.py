def reverse(self, x):
    symbol = False
    if x < 0:
        symbol = True
    num = str(abs(x))
    reverseNum = int(num[::-1])
    if symbol:
        reverseNum = -reverseNum
    maxNum = pow(2, 31) - 1
    minNum = -pow(2, 31)
    if reverseNum >= maxNum or reverseNum <= minNum:
        return 0
    return reverseNum