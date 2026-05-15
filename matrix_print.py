row = int(input("Enter no of rows:"))
column = int(input("Enter no of columns:"))

matrix =[]

for i in range(row):
    row =[]
    for j in range (column):
        element = int(input(f"Enter the element of position {i+1}{j+1}:"))
        row.append(element)
    matrix.append(row)

print("2D Array",matrix)