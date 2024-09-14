#develop  a program for tracking student grades and calculating  averages
#allow users to input grades for different subjects 
print(("enter no of subjects"));
a=int(input("enter subject marks"))
b=int(input("enter subject marks"))
c=int(input("enter subject marks"))
d=int(input("enter subject marks"))
k=(a+b+c+d)/4
if(k>90 or k<100):
    print("A grade")
    if(k>70 and k<90):
         print("B grade")
else:
    print(" c grade ")