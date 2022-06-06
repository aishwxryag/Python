n=int(input("Enter the number of terms for Fibonacci series: "))
first_term = 0                   #first term of Fibonacci series is always 0
second_term = 1                  #second term of Fibonacci series is always 1

if n==1:
    print("The Fibonacci series is: ",first_term)
elif n>1:
    print("The Fibonacci series is: " ,first_term, second_term, end=" ")
    for x in range(2,n):
        next_term = first_term + second_term
        print(next_term, end=" ")
        first_term = second_term
        second_term = next_term
else:
    print("Please enter a valid number.")


"""OUTPUT:
Enter the number of terms for Fibonacci series: 20
The Fibonacci series is:  0 1 1 2 3 5 8 13 21 34 55 89 144 233 377 610 987 1597 2584 4181"""
