if __name__ == '__main__':
	inicial = str()
	a = str()
	b = str()
	c = str()
	h = str()
	m = str()
	p = str()
	n = str()
	placa = str()
	print("Hola")
	print("Bienvenido al sistema busqueda de placas de Panamá")
	print("Introduzca el primer digito de la PLACA que desea buscar")
	print("en caso de ser PLACA del estado coloque la letra N")
	print("no olvide que las placas se escriben en Mayuscula")
	inicial = input()
	if inicial=="A":
		print(" buscando en la base de datos")
		print("introduzca  los 2 primero digitos de la placa ")
		a = input()
		if a=="AD":
			print(" introduzca la placa")
			placa = input()
			print(" La placa pertenece a un auto de administracion"," ",placa)
		else:
			print(" introduzca la placa")
			placa = input()
			print(" La placa pertenece a un auto particular"," ",placa)
	if inicial=="B":
		print("introduzca  los 2 primero digitos de la placa ")
		b = input()
		if b=="BC":
			print(" buscando en la base de datos")
			print(" introduzca la placa")
			placa = input()
			print(" La placa pertenece a un Bus Escolar"," ",placa)
		else:
			print(" introduzca la placa")
			placa = input()
			print(" La placa pertenece a una flota de buses"," ",placa)
	if inicial=="C":
		print("introduzca  los 2 primero digitos de la placa ")
		c = input()
		if c=="CP":
			print(" buscando en la base de datos")
			print(" introduzca la placa")
			placa = input()
			print(" La placa pertenece a la Autoridad del Canal"," ",placa)
		else:
			if c=="CD":
				print(" introduzca la placa")
				placa = input()
				print(" La placa pertenece a un auto del Cuerpo Diplomatico"," ",placa)
			else:
				if c!="CP o CD":
					print(" placa incorrecta")
	if inicial=="D":
		print(" introduzca la placa")
		placa = input()
		print(" La placa pertenece a un auto de Demostracion"," ",placa)
	if inicial=="E":
		print(" introduzca la placa")
		placa = input()
		print(" La placa pertenece a un auto de Fizcalez y  Jueces"," ",placa)
	if inicial=="G":
		print(" introduzca la placa")
		placa = input()
		print(" La placa pertenece a un auto del Gobierno"," ",placa)
	if inicial=="H":
		print(" introduzca la placa")
		placa = input()
		print(" La placa pertenece a un auto de Radioaficionados"," ",placa)
	if inicial=="M":
		print(" buscando en la base de datos")
		print("introduzca  los 2 primero digitos de la placa ")
		m = input()
		if m=="MA":
			print(" introduzca la placa")
			placa = input()
			print(" La placa pertenece a una moto"," ",placa)
		else:
			if m=="MB":
				print(" introduzca la placa")
				placa = input()
				print(" La placa pertenece a un MetroBus"," ",placa)
			else:
				if m=="MC":
					print(" introduzca la placa")
					placa = input()
					print(" La placa pertenece auto del Cuerpo Diplomatico"," ",placa)
				else:
					if m=="MM":
						print(" introduzca la placa")
						placa = input()
						print(" La placa pertenece a un auto del Cuerpo Diplomatico"," ",placa)
					else:
						if m!="MA,MB,MC,MM":
							print(" placa incorrecta")
	if inicial=="P":
		print(" buscando en la base de datos")
		print("introduzca  los 2 primero digitos de la placa ")
		p = input()
		if p=="PE":
			print(" introduzca la placa")
			placa = input()
			print(" La placa pertenece aun auto del Cuerpo Diplomatico"," ",placa)
		else:
			if p=="PH":
				print(" introduzca la placa")
				placa = input()
				print(" La placa pertenece a un auto del Cuerpo Diplomatico"," ",placa)
			else:
				if p=="PR":
					print(" introduzca la placa")
					placa = input()
					print(" La placa pertenece a un auto de Periodista"," ",placa)
				else:
					if c!="PE,PH,PR":
						print(" placa incorrecta")
	if inicial=="R":
		print(" introduzca la placa")
		placa = input()
		print(" La placa pertenece auto del Cuerpo Diplomatico"," ",placa)
	if inicial=="T":
		print(" introduzca la placa")
		placa = input()
		print(" La placa pertenece a un taxi"," ",placa)
	if inicial=="N":
		print(" introduzca los numeros de la placa")
		placa = input()
		print(" La placa pertenece a un vehiculo del estado"," ",placa)
	if inicial!="A,B,C,D,E,G,H,M,N,P,R,T":
		print("SALIENDO DEL SISTEMA")

