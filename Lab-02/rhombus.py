# rhombus pattern
n = int(input("Enter how many rows you want: "))
for i in range(n):
    print(" " * (n - i - 1) + "* " * n)