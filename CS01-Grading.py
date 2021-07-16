A=int(input("คะเเนนเก็บ :"))
B=int(input("คะเเนนสอบกลางภาค :"))
C=int(input("คะเเนนสอบกลางภาค :"))
Z=A+B+C
if(80<=Z<=100):
    print("A")
elif(75<=Z<=79):
    print("B+")
elif(70<=Z<=74):
    print("B")
elif(65<=Z<=69):
    print("C+")
elif(60<=Z<=64):
    print("C")
elif(55<=Z<=59):
    print("D+")
elif(50<=Z<=54):
    print("D")
else:
    print("F")



