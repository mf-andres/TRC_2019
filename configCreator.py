#dime S
S = str(input("give me S:"))

#preparamos el fichero
fileName = "config" + S + "auto"
f = open(fileName,"w")

#S a entero para iterar
S = int(S)

#ponemos la linea de recursos
recursos = ""
for i in range(S):
	recursos += "17 17 9 "
recursos += "6 \n"
f.write(recursos)

#ponemos el numero de traficos
f.write("\n")
nTraficos = S * 2 
nTraficosStr = str(nTraficos) + "\n"
f.write(nTraficosStr)

#vamos poniendo la descripcion de los traficos
finalNode = S * 3
trafficSourceMagicNumber = -1 #variables iniciadas de modo que luego queden a cero
for i in range(nTraficos):
	f.write("\n")
	f.write("M 0.333333333 \n") #t entre llamadas
	f.write("M 6 \n") #t solicitado
	if(i % 2 == 0):
		trafficSourceMagicNumber += 1 
	trafficSource = i + trafficSourceMagicNumber
	if(i % 2 == 0):
		trafficN2 = trafficSource + 2 	
	nodosRecorridos = str(trafficSource) + " " + str(trafficN2) + " " + str(finalNode) + "\n"  
	f.write(nodosRecorridos) #nodos recorridos

f.close()
