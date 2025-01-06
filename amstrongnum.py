
# Input a number
num = int(input("Enter a number: "))

# Store the original number
original_num = num
sum_of_powers = 0

# Count the number of digits
digits = len(str(num))

# Loop through each digit
while num > 0:
    digit = num % 10  # Get the last digit
    
    # Calculate digit raised to the power of digits
    power = digit ** digits
    
    # Add the calculated power to sum_of_powers
    sum_of_powers = sum_of_powers + power
    
    # Remove the last digit
    num = num // 10

# Check if the sum equals the original number
if sum_of_powers == original_num:
    print("It is an Armstrong number.")
else:
    print("It is not an Armstrong number.")
