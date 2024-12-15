def sum_of_subsets(s, k, r):
    x[k] = 1
    if s + w[k] == m:
        sol = [0] * len(w)
        sol[:k + 1] = x[:k + 1]
        print(sol)
    elif s + w[k] + w[k + 1] <= m:
        sum_of_subsets(s + w[k], k + 1, r - w[k])
    if s + r - w[k] >= m and s + w[k + 1] <= m:
        x[k] = 0
        sum_of_subsets(s, k + 1, r - w[k])

n = int(input("Enter the total number of elements: "))
w = []
for i in range(n):
    j = int(input("Enter element number " + str(i + 1) + ": "))
    w.append(j)
m = int(input("Enter the desired sum of elements of the subset: "))
r = sum(w)
x = [0] * len(w)
w.sort()
print(w)
sum_of_subsets(0, 0, r)
