
    def fbWithTimer(n=100):
        for i in range(1, n):
            result = ""
            if i % 3:
                result += "fizz"
            if i % 5:
                result += "buzz"
            if result == "":
                result = i
            print()