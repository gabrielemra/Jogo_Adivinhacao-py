import random
numero_secreto = random.randint(1, 100)
palpite = 0
tentativas = 0
while palpite != numero_secreto:
  palpite = int(input("Digite um número entre 1 e 100 "))
  tentativas = tentativas + 1
  if palpite > numero_secreto:
    print("Muito alto! Tente um número menor.")
  elif palpite < numero_secreto:
    print("Muito baixo! Tente um número maior.")
print(f"Parabéns! Você acertou o número em {tentativas} tentativas!")
