#Program to print positive numbers in a list

input_list=[] #to store input numbers
pst_list=[] #to store positive numbers
pst_number=0

length = int(input("How many numbers are going to be entered? "))

for i in range(length):
    numbers = int(input("Enter the numbers "))
    input_list.append(numbers)
print("Input List: " , input_list)
print("Output: ", end='')

i=0
for number in input_list:
    if input_list[i]>=0:
        pst_number=input_list[i]
        print(str(pst_number) +"\t",end='')
        pst_list.append(pst_number)
    i+=1
print("\nEven numbers: ", pst_list)
print("End of program")


"""OUTPUT:
How many numbers are going to be entered? 5
Enter the numbers -4
Enter the numbers -3
Enter the numbers 2
Enter the numbers 1
Enter the numbers 0
Input List:  [-4, -3, 2, 1, 0]
Output: 2       1       0
Even numbers:  [2, 1, 0]
End of program"""
