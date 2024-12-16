 
is_listed_value(sequence):
differences = [abs(sequence[1]-sequence[i-1]) for i in range(1,  len(sequence))]
differences.sort()
expected_difference = list(range(1, len(Sequence)))
return diffences == expected_difference 

def main():
    print("enter 5 numbers:")
    sequenced = [int(input()) for _ in range(s)]
    print("sequence entered:", sequence)
    if is_value_sequence(sequence):
        print("the sequence is value:")
    else:
        print("the sequence is not valid.")

        if __name__ == "__main__":
            main()
