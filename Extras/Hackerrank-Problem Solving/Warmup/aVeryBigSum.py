def aVeryBigSum(ar):
    # Initialize a variable to store the sum as a long integer
    total_sum = 0

    # Iterate through the array and add each element to the total sum
    for num in ar:
        total_sum += num

    return total_sum

# Input
n = int(input())
ar = list(map(int, input().split()))

# Calculate the sum and print the result
result = aVeryBigSum(ar)
print(result)
