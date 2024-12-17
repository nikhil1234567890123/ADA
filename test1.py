def is_valid_sequence(sequence):
    differences = [abs(sequence[i] - sequence[i-1]) 
                   for i in range(1, len(sequence))]
    differences.sort()
    expected_differences = list(range(1, len(sequence)))
    return differences == expected_differences

def main():
    print("Enter 5 numbers:")
    sequence = [int(input()) for _ in range(5)]
    print("Sequence entered:", sequence)
    if is_valid_sequence(sequence):
        print("The sequence is valid.")
    else:
        print("The sequence is not valid.")

if __name__ == "__main__":
    main()
