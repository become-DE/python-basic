numbers = [ 12, 75, 150, 180, 145, 525, 50]
N = len(numbers)
for i in range(N):
    if numbers[i] > 500:
            break
    if numbers[i] % 5 == 0:
        if numbers[i] > 150:
            continue
        print(numbers[i])