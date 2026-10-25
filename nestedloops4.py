#Write a Python program that prints the numbers 1 to 3.

#For each number, print it 3 times.

#Expected output:

#1 1 1

#2 2 2

#3 3 3

for i in range(1, 4):
    line = ""
    
    for j in range(1, 4):
        line = line + str(i)  
        
    print(line) 