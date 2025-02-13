def calculate_average(numbers):
    if not numbers:
        return 0  # Handle empty list
    total = sum(numbers)
    average = total / len(numbers)
    return average

# Example usage that can cause ZeroDivisionError
data = []
average = calculate_average(data)
print(f"The average is: {average}")
data = [10,20,30,40,50]
average = calculate_average(data)
print(f"The average is: {average}")