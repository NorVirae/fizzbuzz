
def fbWithTimer(n=100, a=3, b=):
    for i in range(1, n):
        result = ""
        if i % 3:
            result += "fizz"
        if i % 5:
            result += "buzz"
        if result == "":
            result = i
        print(result)

fbWithTimer()