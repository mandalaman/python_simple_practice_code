

def find_largest(numbers):
    largest = numbers[0]
    for num in numbers:
        if num> largest:
            largest = num
    return largest

numbers = [3, 4, 2, 7, 32, 34]
print(find_largest(numbers))