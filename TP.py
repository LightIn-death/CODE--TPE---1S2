#!/usr/bin/env python3
# -*- coding: utf-8 -*-





from math import pow
import binascii





Base2 = open('Resultat/Base2.txt', 'a')
BaseDix = open("Resultat/BaseDix.txt","a")






def toBase(numberToConvert,originalBase,wantedBase,chars=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]):
   
    convertedNumber=""
    numberToConvertBase10 = numberToConvert

    powSup = 0

   
    while pow(wantedBase,powSup) < numberToConvertBase10:
        powSup += 1

    if pow(wantedBase,powSup) > numberToConvertBase10:
        powUnder = powSup - 1
    else:
        powUnder = powSup
    while numberToConvertBase10 > 0 :
        coef = wantedBase - 1

        while pow(wantedBase,powUnder)*coef > numberToConvertBase10 :
            coef -= 1


        convertedNumber += chars[coef]
        
        numberToConvertBase10 -= pow(wantedBase,powUnder)*coef
        powUnder -= 1

    if powUnder > 0 :
        while powUnder > 0:
            convertedNumber += "0"
            powUnder -= 1

    return convertedNumber






def TranslateToBinary():

	obj = open("obj.obj","r")
	
	lines = obj.readlines()
	

	lines = str(lines)


	text = lines


	data = bin(int.from_bytes(text.encode(), 'big'))

	print (data)
    
    


	data_list = []
	data_list2 = []
    
    
    


	for Bin in data :

		data_list2.append(Bin)



	del data_list2[0]
	del data_list2[0]



	for Bin in data :

		data_list.append(Bin)
		data_list.append("*2^")
		data_list.append("+")
		print("Binary :",Bin)






	del data_list[0]
	del data_list[0]
	del data_list[0]
	del data_list[0]
	del data_list[0]
	del data_list[0]
	del data_list[-1]

	print(data_list)



	z = 0
	i = 0
	Len = ((int(len(data_list))+1)/3)


	while z != Len :
		i = i+ 2
		data_list.insert(  i, int(Len)-z-1)

		i =i+ 2
		z =z+ 1
		print("cycle",z)



	for item in data_list:
		Base2.write(str(item))

		
	print("Try")



	while  data_list2 != [] :

		new_data_list = []
		Avance = 0
		print('while')


		for bidule in data_list2 :
			if Avance != 20 :
				Avance += 1
				new_data_list.append(bidule)
				del data_list2[0]
				print(Avance)


		new_data_list.reverse()
		i = 0
		Base10 = int(0)

		
		for Bin in new_data_list:
			Base10 = Base10 + (int(Bin) * int(pow(2,i)))
			i = i +1
		


		BaseDix.write(str(Base10))


		print(Base10)

		i = 510 # La variable i est egale au nombre entre incremente de 1

		print("debug")

		Quatre = [] # On definit ici une liste qui sera utiliser plus tard

		adn=[]

		print("debug")


		base4 = toBase(Base10,10,4)

		for i in base4 :
			Quatre.append(int(i))
			adn.append(int(i))

		print(Quatre)


		for n,i in enumerate(adn):
			if i==0:
				adn[n]="A"
		for n,i in enumerate(adn):
			if i==1:
				adn[n]="G"
		for n,i in enumerate(adn):
			if i==2:
				adn[n]="C"
		for n,i in enumerate(adn):
			if i==3:
				adn[n]="T"

		print("debug")
		

		print(adn)

		AdnFile = open('Resultat/ADN.txt', 'a')

		
			
		for item in adn:
			AdnFile.write(str(item))

		for n,i in enumerate(adn):
			if i=="C":
				adn[n]="G"
			if i=="G":
				adn[n]="C"
			if i=="T":
				adn[n]="A"
			if i=="A":
				adn[n]="U"
		
		
		print(adn)
		
		AdnFile = open('Resultat/ARN.txt', 'a')

		for item in adn:
			AdnFile.write(str(item))



                
                
                
                










TranslateToBinary()
