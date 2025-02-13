def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list to avoid ZeroDivisionError
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Example usage
data = []
average = calculate_average(data)
print(f"The average is: {average}") # Output: The average is: 0
data = [10,20,30,40,50]
average = calculate_average(data)
print(f"The average is: {average}") # Output: The average is: 30.0