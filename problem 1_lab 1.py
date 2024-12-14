n = int(input("Enter the number of elements: "))
numbers = []

for i in range(n):
    num = int(input("Enter number {}: ".format(i+1)))
    numbers.append(num)

numbers.sort()

print("Sorted numbers:", numbers)

mean = sum(numbers) / n
median = numbers[n // 2] if n % 2 == 1 else (numbers[n // 2 - 1] + numbers[n // 2]) / 2

freq = {}
for num in numbers:
    freq[num] = freq.get(num, 0) + 1
mode = max(freq, key=freq.get)

print("Mean:", mean)
print("Median:", median)
print("Mode:", mode)