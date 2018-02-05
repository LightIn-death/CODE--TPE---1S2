#!/usr/bin/env python3 
# -*- coding: utf-8 -*-



from math import pow

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
