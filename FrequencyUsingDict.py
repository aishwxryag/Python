#Function to print letters of a string in decreasing order of frequency using Dictionaries
def most_frequent(word):
    word=word.lower()
    d = dict()
    for key in word:
        if key not in d:
            d[key]=1
        else:
            d[key]+=1
    print("The frequency of letters in the decreasing order: ")
    d_sorted = sorted(d, key=d.get, reverse=True)      #sorting using built-in sorted function
    for r in d_sorted:
        print(r, "=", d[r])


word=input("Enter any word: ")
most_frequent(word)         #calling function


"""OUTPUT:
Enter any word: Mississippi
The frequency of letters in the decreasing order:
i = 4
s = 4
p = 2
m = 1"""
