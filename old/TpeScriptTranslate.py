#!/usr/bin/env python3
# -*- coding: utf-8 -*-





from math import pow
import binascii




#Entree = open('Truc.obj', 'w')
Base2 = open('Base2.txt', 'w')
BaseDix = open("BaseDix.txt","w")

#ADN = open('sortie.adn', 'w')



def toBase(numberToConvert,originalBase,wantedBase,chars=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]):
    """
    Fonction permettant de convertir un nombre dans une base de départ donnée vers un nombre dans une autre base.
    Paramètres:
        - numberToConvert : Nombre à convertir (str)
        - originalBase :  Base du nombre a convertir (int)
        - wantedBase : Base vers laquelle convertir le nombre (int)
        - chars : Liste des caractères à utiliser lors de la conversion, par défaut les nombre décimaux sont utilisés ( 0 - 9 ) puis les lettres de l'alphabet ( A - Z ). (str list)
    returns :
    numberToConvert in wantedBase (str)

    """
    #### Variables Types Checking:
    ## SI tu as le courage : https://www.pythoncentral.io/validate-python-function-parameters-and-return-types-with-decorators/


    convertedNumber=""
    numberToConvertBase10 = toDecimal(numberToConvert,originalBase,chars)

    powSup = 0

    ### Find Pow Sup
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
        #print("powUnder: ",powUnder ," coef: ",coef, " numberToConvertBase10: ",numberToConvertBase10, " convertedNumber: ", convertedNumber)
        #input("PAUSED")
        numberToConvertBase10 -= pow(wantedBase,powUnder)*coef
        powUnder -= 1

    if powUnder > 0 :
        while powUnder > 0:
            convertedNumber += "0"
            powUnder -= 1

    return convertedNumber


def toDecimal(numberToConvert,originalBase,chars=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]):
    """
    Fonction pour convertir n'import quelle base vers la base de 10.
    Paramètres :
        - numberToConvert : Nombre à convertir (str)
        - originalBase :  Base du nombre a convertir (int)
        - chars : Liste des caractères à utiliser lors de la conversion, par défaut les nombre décimaux sont utilisés ( 0 - 9 ) puis les lettres de l'alphabet ( A - Z ). (str list)
    returns :
        - numberToConvert in base 10 (int)
    """
    convertedNumber = 0
    #print(numberToConvert)
    for power in range(len(numberToConvert)-1,-1,-1):
        convertedNumber += chars.index(numberToConvert[power]) * pow(originalBase,len(numberToConvert)-1-power)
    return convertedNumber





def TranslateToBinary():

	#obj = open('E:\object.obj',"r")
	
	#lines = obj.read()

	#lines = str(lines)



	#print(lines)


	text =  input(">")


	data = bin(int.from_bytes(text.encode(), 'big'))

	print (data)
    
    
    
    

	#text = n.to_bytes((n.bit_length() + 7) // 8, 'big').decode()

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



	data_list2.reverse()
	i = 0
	Base10 = int(0)

	
	for Bin in data_list2:
		Base10 = Base10 + (int(Bin) * int(pow(2,i)))
		i = i +1
	


	BaseDix.write(str(Base10))


	Base4(Base10)







def Base4(Base10):
    
    
    
    nombre = Base10
    print(nombre)
    i = 510 # La variable i est egale au nombre entre incremente de 1
    Final = [] # On definit ici une liste qui sera utiliser plus tard
    adn=[]
    print("Lunch")
    
    
    base4 = toBase(nombre,10,4)
    
    
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

	 print(adn)


	 AdnFile = open('Final.txt', 'w')

	 for item in adn:
         File.write(str(item))


	 if i=="T":
         [n]="U"

    print(adn)


  	 AdnFile = open('Figal.txt', 'w')
       
       in adn:
				AdnFile.write(str(item))

                
                
                
                










binaryTranslate()
