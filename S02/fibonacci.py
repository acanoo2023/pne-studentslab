def fibonacci(n):
    series = [0, 1]
    for i in range(2, n):
        next_number = series[-1] + series[-2]
        series.append(next_number)
        return series
n = fibonacci(20)
print("The 5th Fibonacci number is:", n[5])
print("The 10th Fibonacci number is:", n[10])
print("The 15th Fibonacci number is:", n[15])

