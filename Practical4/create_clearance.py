#  Pseudocode: Define age/weight/gender/cr → validate inputs → calculate CrCl with Cockcroft-Gault Equation → adjust for female → print result/error

age=int(input("Your age:"))
weight=int(input("Your weight(kg):"))
gender=input("Your gender")
cr=int(input("Your creatine concentration(μmol/l):"))
if age>100:
    print("age is out of range!")
elif weight>80 or weight<20:
    print("weight is out of range!")
elif cr>100 or cr<0:
    print("creatine concentration is out of range!")
else:
    if gender=="woman" or "Woman":
        crcl=(140-age)*weight/72/cr*0.85
        print("CrCl=",crcl)
    elif gender=="man" or "Man":
        crcl=(140-age)*weight/72/cr
        print("CrCl=",crcl)
    else:
        print("gender is wrong!")
