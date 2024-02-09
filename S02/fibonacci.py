def fibonacci(n):
    series = [0, 1]
    for i in range(2, n):
        next_number = series[-1] + series[-2]
        series.append(next_number)
    return series


n = fibonacci(11)
print(n)



