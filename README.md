# LuizVieira_BrunadiBisceglie_Ep3
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
