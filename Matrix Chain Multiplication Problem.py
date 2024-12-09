from tabulate import tabulate

class MatrixChainMultiplier:
    def __init__(self, dimensions):
        self.n = len(dimensions) - 1
        self.dimensions = dimensions
        self.m = [[float('inf')] * self.n for _ in range(self.n)]
        self.s = [[0] * self.n for _ in range(self.n)]

    def solve(self):
        for i in range(self.n):
            self.m[i][i] = 0

        for length in range(2, self.n + 1):
            for i in range(self.n - length + 1):
                j = i + length - 1
                for k in range(i, j):
                    cost = self.m[i][k] + self.m[k + 1][j] + (self.dimensions[i] * self.dimensions[k + 1] * self.dimensions[j + 1])
                    if cost < self.m[i][j]:
                        self.m[i][j] = cost
                        self.s[i][j] = k

    def print_optimal_parenthesis(self, i, j):
        if i == j:
            print(f"A{j + 1}", end="")
        else:
            print("(", end="")
            self.print_optimal_parenthesis(i, self.s[i][j])
            self.print_optimal_parenthesis(self.s[i][j] + 1, j)
            print(")", end="")

    def print_solution(self):
        print("Minimum Scalar Multiplications Matrix:")
        print(tabulate(self.m, tablefmt='grid'))

        print("\nOptimal Parenthesization Matrix:")
        print(tabulate(self.s, tablefmt='grid'))

        print("\nOptimal Parenthesization:")
        self.print_optimal_parenthesis(0, self.n - 1)


# Taking input from the user
dimensions = []
num_matrices = int(input("Enter the number of matrices: "))
for _ in range(num_matrices + 1):
    dimension = int(input("Enter the dimension of matrices: "))
    dimensions.append(dimension)

# Creating an instance of the MatrixChainMultiplier class
multiplier = MatrixChainMultiplier(dimensions)
# Solving the problem
multiplier.solve()
# Printing the solution
multiplier.print_solution()
