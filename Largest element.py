arr = list(map(int, input("Enter numbers: ").split()))
largest = arr[0]

for num in arr:
    if num > largest:
        largest = num

print("Largest element:", largest)
