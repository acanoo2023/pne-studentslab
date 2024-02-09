def fibonacci(n):
    series = [0, 1]
    for i in range(2, n):
        next_number = series[-1] + series[-2]
        series.append(next_number)
    return series

def fibosum(n):
    series = fibonacci(15)

    count = 0
    for i in range(0, n + 1):
        count += int(series[i])

    return count

print("Sum of the First 5 terms of the Fibonacci series:", fibosum(5))
print("Sum of the First 10 terms of the Fibonacci series:", fibosum(10))
