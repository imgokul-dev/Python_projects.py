numbers = [10,20,30,40,50]

target = 50

for i in range(len(numbers)):
    if numbers[i] == target:
        print("Found at index: ",i)
        break