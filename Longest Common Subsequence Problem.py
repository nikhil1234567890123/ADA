from tabulate import tabulate

class LCSFinder:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
        self.m = len(X)
        self.n = len(Y)
        self.c = [[0] * (self.n + 1) for _ in range(self.m + 1)]
        self.b = [[''] * (self.n + 1) for _ in range(self.m + 1)]

    def find_lcs(self):
        for i in range(1, self.m + 1):
            for j in range(1, self.n + 1):
                if self.X[i - 1] == self.Y[j - 1]:
                    self.c[i][j] = self.c[i - 1][j - 1] + 1
                    self.b[i][j] = "diagonal"
                else:
                    if self.c[i - 1][j] >= self.c[i][j - 1]:
                        self.c[i][j] = self.c[i - 1][j]
                        self.b[i][j] = "upper"
                    else:
                        self.c[i][j] = self.c[i][j - 1]
                        self.b[i][j] = "left"

    def print_lcs(self, i, j):
        if i == 0 or j == 0:
            return ''
        if self.b[i][j] == "diagonal":
            return self.print_lcs(i - 1, j - 1) + self.X[i - 1]
        elif self.b[i][j] == "upper":
            return self.print_lcs(i - 1, j)
        else:
            return self.print_lcs(i, j - 1)

    def get_lcs_length(self):
        return self.c[self.m][self.n]

    def display_matrices(self):
        print("\nThe c Grid: ")
        print(tabulate(self.c, tablefmt="grid"))

        print("\nThe b Grid: ")
        print(tabulate(self.b, tablefmt="grid"))

    def display_lcs(self):
        lcs_length = self.get_lcs_length()
        print("\nThe length of Longest Common Subsequence:", lcs_length)
        print("\nThe Longest Common Subsequence:", end=" ")
        lcs = self.print_lcs(self.m, self.n)
        print(lcs)


# Taking input from the user
X = input("Enter the first string: ")
Y = input("Enter the second string: ")

# Creating an instance of the LCSFinder class
lcs_finder = LCSFinder(X, Y)
# Finding the longest common subsequence
lcs_finder.find_lcs()
# Displaying matrices c and b
lcs_finder.display_matrices()
# Displaying the longest common subsequence
lcs_finder.display_lcs()
