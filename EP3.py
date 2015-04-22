# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 11:26:03 2015

@author: Bruna
"""

def calculo_usuario(id, pe, se, al, fa):
    # calculo do tmb e calorias 
    # id (anos); pe (kg); se (M or F); al (m); fa (atividade)
    if se == "M" or se == "m":
        TMB = 88.36 + (13.4*pe) + (4.8*al*100) - (5.7*id)
    elif se == "F" or se == "f":
        TMB = 447.6 + (9.2*pe) + (3.1*al*100) - (4.3*id)
    if TMB == 0:
        print ("sexo invalido")
    elif fa == "muito baixo":
        Calorias = TMB * 1.2
    elif fa == "baixo":
        Calorias = TMB * 1.375
    elif fa == "medio":
        Calorias = TMB * 1.55
    elif fa == "alto":
        Calorias = TMB * 1.725
    elif fa == "muito alto":
        Calorias = TMB * 1.9
    IMC = 1.3*pe/al
    if IMC < 18.5:
        IMC_Desc = "magra"
    elif IMC >= 18.5 and IMC < 25:
        IMC_Desc = "saudavel"
    elif IMC >= 25 and IMC < 30:
        IMC_Desc = "sobrepeso"
    elif IMC >= 30:
        IMC_Desc = "obeso"
    return(TMB, Calorias, IMC, IMC_Desc)

def calculo_alim(alim, qtd):
    # calculo de calorias para qtd de alimento
    cal_alim = 0  
    prot_alim = 0
    carb_alim = 0
    gord_alim = 0   
    for i in alimentos:
        if i[0] == alim:
            cal_alim  = float(i[2])*qtd/int(i[1])
            prot_alim = float(i[3])*qtd/int(i[1])
            carb_alim = float(i[4])*qtd/int(i[1])
            gord_alim = float(i[5])*qtd/int(i[1])
            break
    return(cal_alim, prot_alim, carb_alim, gord_alim)   

