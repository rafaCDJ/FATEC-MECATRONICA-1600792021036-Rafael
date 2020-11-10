def lados():
  continuar = True
  while continuar==True:
    lado = float(input("informe um lado do triangulo"))
    continuar = lado < 0
  return lado

def semiperimetro(primeiro_valor,segundo_valor,terceiro_valor):
  return (primeiro_valor+segundo_valor+terceiro_valor)/2

def areatriangulo(semip,primeiro_valor,segundo_valor,terceiro_valor):
  return (semip*(semip-primeiro_valor)*(semip-segundo_valor)*(semip-terceiro_valor))**0.5

def saida(areatriangulo):
  print ("a area do triangulo é de:" ,resultado )

primeiro_valor = lados()
segundo_valor = lados()
terceiro_valor = lados()
semip = semiperimetro(primeiro_valor,segundo_valor,terceiro_valor)
resultado = areatriangulo(semip,primeiro_valor,segundo_valor,terceiro_valor)
saida(areatriangulo)
