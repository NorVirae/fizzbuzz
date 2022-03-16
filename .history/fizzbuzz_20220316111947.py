
def fbWithTimer(n=100, a=3, b=5):
    for i in range(1, n):
        result = ""
        if i % a:
            result += "fizz"
        if i % 5:
            result += "buzz"
        if result == "":
            result = i
        print(result)

fbWithTimer()