first_num: float = input("Enter First Number : \n")
second_num: float = input("Enter Second Number : \n")
print("Enter + To Add | Enter - To Subtract | Enter * To Multiply | Enter / To Divide | Enter '%' For Modulus Division")
sum = float(first_num) + float(second_num)
sub = float(first_num) - float(second_num)
mul = float(first_num) * float(second_num)
div = float(first_num) / float(second_num)
moddiv = float(first_num) % float(second_num)

choose_opp = input("Enter Sign To Calculate : ")
if choose_opp == "+":
    print(""+str(first_num) + "+" + str(second_num) +" = "+str(sum))
elif choose_opp == "-":
    print(""+str(first_num) + "-" + str(second_num) +" = "+str(sub))
elif choose_opp == "*":
    print(""+str(first_num) + "x" + str(second_num) +" = "+str(mul))
elif choose_opp == "/":
    print(""+str(first_num) + "/" + str(second_num) +" = "+str(div))
elif choose_opp == "%":
    print(""+str(first_num) + " mod " + str(second_num) +" = "+str(moddiv))
else:
    print("Wrong Input! Check Your Sign")

