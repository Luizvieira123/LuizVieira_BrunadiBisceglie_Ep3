# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 11:25:19 2015

@author: LuizJR
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



# leitura do arquivo Alimentos
arq_alimentos=open("alimentos.csv",encoding="latin1", mode="r")
al=arq_alimentos.readlines()
arq_alimentos.close()
alim=[]
alimentos=[]
for i in al[1:]:
    alim = i.strip()
    if alim != "":
        alimentos.append(alim.split(','))

# Leitura do arquivo Usuario
arq_usuario=open("usuario.csv",encoding="latin1",mode="r")
us = arq_usuario.readlines()
arq_usuario.close()
usu=[]
usuario=[]
for i in us[1:2]:
    usu = i.strip()
    if usu != "":
        usuario.append(usu.split(','))
di=[]
dieta=[]
for i in us[3:]:
    di = i.strip()
    if di != "":
        dieta.append(di.split(','))

# Calculo das Calorias por Alimiento Consumido
for i in dieta:
    temp = calculo_alim(i[1], int(i[2]))
    j = 0
    while j < 4:
        i.append(temp[j])
        j = j+1

# Calculo da Dieta Diaria
dieta_dia=[]
dia=[]
for i in dieta:
    dia.append(i[0])
dia.sort()

temp1=0
while temp1 < len(dia)-1:
    if dia[temp1] == dia[temp1+1]:
        dia.pop(temp1)
    else:
        temp1=temp1+1
for i in dia:
    cal_dia = 0
    prot_dia = 0
    carb_dia = 0
    gord_dia = 0
    temp1 = []
    for j in dieta:
        if i == j[0]:
            cal_dia = cal_dia + j[3]
            prot_dia = prot_dia + j[4]
            carb_dia = carb_dia + j[5]
            gord_dia = gord_dia + j[6]
    temp1.append(i)
    temp1.append(cal_dia)
    temp1.append(prot_dia)
    temp1.append(carb_dia)
    temp1.append(gord_dia)
    dieta_dia.append(temp1)
dieta_dia.sort()

# Calculo do Delta de Calorias
calc_usu=[]
calc_usu=calculo_usuario(int(usuario[0][1]),int(usuario[0][2]),usuario[0][3],float(usuario[0][4]),usuario[0][5])
for i in dieta_dia:
    deltacal = calc_usu[1]-i[1]
    i.append(deltacal)

# Escrever em arquivo texto IMC e Delta Caloria
arq_resultados=open("resultados.txt",encoding="latin1", mode="w")
arq_resultados.write(str(usuario[0][0]))
arq_resultados.write("  IMC= %.2f" % calc_usu[2])
arq_resultados.write("  ( %s" % str(calc_usu[3]))
arq_resultados.write(" ) ")
for i in dieta_dia:
    arq_resultados.write("  Dia= %s" % str(i[0]))
    arq_resultados.write("  Delta_Calorias= %.2f" % i[5])
arq_resultados.close()



 
#lista de calorias recomendadas por dia
cal_rec=[]
for i in dia:
    cal_rec.append(calc_usu[1])

#lista de dias
dias = []
for i in range (1, len(dia) + 1):
    dias.append(i)

#lista das calorias diarias consumidas
cal_cons = []
for i in range (0, len (dia)):
    cal_cons.append(dieta_dia[i][1])

#lista de proteinas diárias consumidas

prot_cons = []
for i in range (0, len (dia)):
    prot_cons.append(dieta_dia[i][2])

#lista de carbo diário consumido

carbo_cons = []
for i in range (0, len (dia)):
    carbo_cons.append(dieta_dia[i][3])

#lista de gorduras diárias consumidas

gord_cons = []
for i in range (0, len (dia)):
    gord_cons.append(dieta_dia[i][4])

#plotar gráfico da qt diaria recomendada de cal e a qt consumida de cal, prot, carb e gord, por dia

import matplotlib.pyplot as plt
import datetime as dt

dias1 =[]
dias1 = [dt.datetime.strptime(d,'%d/%m/%y').date() for d in dia]
temp = range(len(dias1))

import matplotlib.dates as mdates

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())
plt.plot(dias1, cal_rec)
plt.plot(dias1, cal_cons)
plt.gcf().autofmt_xdate()
plt.title('Calorias Recomendadas e Cosnumidas por Dia \n')
plt.ylabel('calorias recomendadas (azul), \n calorias consumidas (verde)')
plt.xlabel('dia')
plt.show()

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%Y'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator())
plt.plot(dias1, prot_cons)
plt.plot(dias1, carbo_cons)
plt.plot(dias1, gord_cons)
plt.title('Proteinas, Caboidratos e Gorduras Consumidas por Dia \n')
plt.ylabel('proteinas consumidas (azul), \n  carboidratos consumidos (verde), \n gorduras consumidas (vermelho)')
plt.xlabel('dia')
plt.show()

 