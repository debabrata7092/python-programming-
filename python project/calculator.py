number= int(input("ENTER THA 1ST NUMBER :"))
symbol= input("ENTER THA OPERATOT (+    -  %    //      /   *  ) :")
B=int(input("ENTER THA 2ST NUMBER :"))


if symbol== "+":
	print(number+B, "\nsolve")



elif  symbol== "-":
	print(number-B, "\nsolve")



elif symbol== "%":
	print(number%B, "\nsolve")

elif symbol== "//":
	print(number//B, "\nsolve")


elif symbol== "/":
	print(number/B, "\nsolve")


elif  symbol== "*":
	print(number*B, "\nsolve")



else:
	print (" you enter tha inviled operator")
