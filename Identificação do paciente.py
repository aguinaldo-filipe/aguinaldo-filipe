nome=input("Qual é o nome do Paciente?")
patente=input("Qual é a patente do paciente?") 
idade=input("Qual é a idade do Paciente?")   
sexo=input("Qual é o sexo do Paciente?")    
raça=input("Qual é a raça do Paciente?")   
naturalidade=input("Onde nasceu o paciente?")
estado_civil=input("Qual é o estado civil do Paciente?")
profissão=input("Qual é a profissão do Paciente?")
religião=input("Qual é a igreja do Paciente?")
residência_anterior=input("Onde o doente vivia?")
residência_actual=input("Onde paciente vive agora")
fonte_do_interrogatório=input("Quem respondeu as perguntas?")
fonte_de_encminhamento=input("De onde vem o Paciente?")

print(f"O nome do paciente é {nome} a sua patente é {patente} tem {idade} anos, é {sexo} da raça {raça} {estado_civil} e de {naturalidade} ")
print(f"O paciente é {profissão} e {religião} viveu em {residência_anterior} e agora vive em {residência_actual} foi ele {fonte_do_interrogatório} quem forneceu as informações e veio do seu {fonte_de_encminhamento}")