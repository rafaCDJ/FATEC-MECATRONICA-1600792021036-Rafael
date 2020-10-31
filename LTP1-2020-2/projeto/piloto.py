import random
repeticao = 0
email1 = 'gmail'
senha_id1 = '2468'
senha_id2 = '123456'
senha_id3 = '1234'
saldo_ID1 = 1000
saldo_ID2 = 250
saldo_ID3 = 3000
resposta = 'Sim'
Sim = True
usuario = input('Informe o seu ID: ')
email = input('Informe o seu e-mail: ')
senha = input('Informe a sua senha: ')

while resposta == 'Sim':
 if usuario == 'id1':
  if email == 'email1':
   if senha == senha_id1:
    recebedor = input('Informe o ID recebedor do pagamento: ')
    print('Seu saldo atual é de R$',saldo_ID1)
    valor_pagamento = float(input('Informe o valor a ser pago: '))
    if saldo_ID1 > valor_pagamento:
      pagamento = (saldo_ID1-valor_pagamento)
      print('Transação realizada com sucesso')
      print('Transação realizada por:', usuario)
      print('Transação realizada para:', recebedor)
      print('Valor da transação R$',valor_pagamento)
      print("sua chave de segurança é:"),print(random.randrange(1000, 9999))
      print(email)
      resposta = input('Deseja realizar outra transação? (Sim ou Não) ')
