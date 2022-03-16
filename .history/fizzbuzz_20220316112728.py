
def fbWithTimer(n=100, a=3, b=5):
    for i in range(1, n):
        result = ""
        if i % a == 0:
            result += "fizz"
        if i % b == 0:
            result += "buzz
        if result == "":
            