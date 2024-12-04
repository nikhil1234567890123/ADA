from tabulate import tabulate

class AssemblyLineScheduler:
    def __init__(self, station1, station2, t1, t2, e1, e2, x1, x2):
        self.station = [station1, station2]
        self.t = [t1, t2]
        self.e = [e1, e2]
        self.x = [x1, x2]
        self.n = len(station1)
        self.f = [[0 for i in range(self.n)] for j in range(2)]
        self.decision = [[0 for i in range(self.n)] for j in range(2)]
    
    def compute_schedule(self):
        self.f[0][0] = self.e[0] + self.station[0][0]
        self.f[1][0] = self.e[1] + self.station[1][0]

        for j in range(1, self.n):
            if self.f[0][j-1] + self.station[0][j] <= self.f[1][j-1] + self.t[1][j-1] + self.station[0][j]:
                self.f[0][j] = self.f[0][j-1] + self.station[0][j]
                self.decision[0][j] = 1
            else:
                self.f[0][j] = self.f[1][j-1] + self.t[1][j-1] + self.station[0][j]
                self.decision[0][j] = 2

            if self.f[1][j-1] + self.station[1][j] <= self.f[0][j-1] + self.t[0][j-1] + self.station[1][j]:
                self.f[1][j] = self.f[1][j-1] + self.station[1][j]
                self.decision[1][j] = 2
            else:
                self.f[1][j] = self.f[0][j-1] + self.t[0][j-1] + self.station[1][j]
                self.decision[1][j] = 1

    def print_schedule(self):
        print("Effort Matrix:")
        print(tabulate(self.f, tablefmt="grid"))
        print("\nDecision Matrix:")
        print(tabulate(self.decision, tablefmt="grid"))

        if (self.f[0][-1] + self.x[0]) <= (self.f[1][-1] + self.x[1]):
            final = self.f[0][-1] + self.x[0]
            line = 1
        else:
            final = self.f[1][-1] + self.x[1]
            line = 2

        print("\n\nSelected Lines at each station: ")
        self.print_stations(line)

        return final, line

    def print_stations(self, l):
        i = l - 1
        print("Line " + str(i+1) + " station " + str(self.n))
        for j in range(self.n - 1, 0, -1):
            i = self.decision[i][j]
            print("Line " + str(i) + " station " + str(j))
            i = i - 1

# Taking the input from the user
e1 = int(input("Enter the entry time of assembly line 1: "))
e2 = int(input("Enter the entry time of assembly line 2: "))
x1 = int(input("Enter the exit time of assembly line 1: "))
x2 = int(input("Enter the exit time of assembly line 2: "))
station1 = []
station2 = []
m = int(input("Enter the number of stations on one assembly line: "))
for i in range(m):
    j = int(input("Enter the amount of work at station " + str(i+1) + " of assembly line 1: "))
    k = int(input("Enter the amount of work at station " + str(i+1) + " of assembly line 2: "))
    station1.append(j)
    station2.append(k)
t1 = []
t2 = []
for i in range(m-1):
    j = int(input("Enter the amount of work to change station from 1 to 2 at station " + str(i+1) + " : "))
    k = int(input("Enter the amount of work to change station from 2 to 1 at station " + str(i+1) + " : "))
    t1.append(j)
    t2.append(k)

# Creating an instance of the AssemblyLineScheduler class
scheduler = AssemblyLineScheduler(station1, station2, t1, t2, e1, e2, x1, x2)
# Computing the schedule
scheduler.compute_schedule()
# Printing the schedule
mincost, line = scheduler.print_schedule()
print("\nMinimum cost is " + str(mincost) + " from assembly line " + str(line))
