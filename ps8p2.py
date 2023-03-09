firstNum = 1
secondNum = 1
print(firstNum)
print(secondNum)

for i in range(2, 20):
    nextNum = firstNum + secondNum
    print(nextNum)
    firstNum = secondNum
    secondNum = nextNum
