#Ler um valor inteiro (aceitar somente valores entre 1 e 10) e escrever a tabuada de 1 a 10 do valor lido.

entrada = int(input(" valor:"))

if entrada <= 10:
  for i in range(1,11):
    VALOR = entrada * i
    print(f"{entrada} vezes {i} = {VALOR}")
      
else:
  print(" O valor deve ser menor ou igual a 10")
