# Function sum of odd numbers 
def sum_of_odd_numbers(n):
    total = 0  # Define total sum


    for i in range(1, n + 1): 
        if i % 2 != 0:  # Check  number if odd
            total += i  # Add odd number total

    return total

# Main function
def main():
    n = int(input("Enter a number: "))
    
    odd_sum = sum_of_odd_numbers(n)
    print("The sum of all odd numbers up to", n, "is:", odd_sum)

# Run and checkmain program
if __name__ == "__main__":
    main()
