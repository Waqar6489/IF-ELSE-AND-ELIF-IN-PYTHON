'''Write a program to find out whether a student has passed or failed if it requires a 
total of 40% and at least 33% in each subject to pass. Assume 3 subjects and 
take marks as an input from the user?'''

m1=int(input("Enter the marks 1 :"))
m2=int(input("Enter the marks 2 :"))
m3=int(input("Enter the marks 3 :"))
pt=(100)*(m1+m2+m3)/300
if(pt>=40 and m1>=33 and m2>=33 and m3>=33):
    print("you are pass",pt)
else:    
    print("you are fail",pt)