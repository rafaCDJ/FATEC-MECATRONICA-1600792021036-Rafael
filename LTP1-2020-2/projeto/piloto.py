import random
repeticao = 0
senha_ID1 = '2468'
senha_ID2 = '123456'
senha_ID3 = '1234'
saldo_atualID1 = 1000.00
saldo_atualID2 = 250.00
saldo_atualID3 = 3000.00
resposta = 'Sim'
ID1 = senha_ID1
ID2 = senha_ID2
ID3 = senha_ID3
Sim = True
while resposta1 == 'Sim':
  print('ID1 gera uma operação de recebimento de R$ 250.00 para o ID2')
  print('ID1 é a usuária Ana')
  print('ID2 é o usuário Rodrigo')
  print('ID3 é o usuário Paulo')
  usuario = input('Informe o seu  ou nome de Usuário: ')
  senha = input('Informe a sua senha: ')
  email = input('Informe o seu e-mail: ')
  if usuario == 'ID2' or 'Rodrigo':
    if senha == senha_ID2:
      print('Seu saldo atual é de R$',saldo_atualID2)
      recebedor = input('Informe o ID recebedor do pagamento: ')
      if recebedor == 'ID1' or 'Ana':
        valor_pagamento = float(input('Informe o valor da transação: '))
        if saldo_atualID2 >= valor_pagamento:
           pagamento = (saldo_atualID2 - valor_pagamento)
           saldo_atualID2 = (saldo_atualID2 - valor_pagamento)
           saldo_atualID1 = (saldo_atualID1 + valor_pagamento)
           print('Transação realizada com sucesso')
           print('Transação realizada por:', usuario)
           print('Transação realizada para:', recebedor)
           print('Valor da transação R$',valor_pagamento)
           print("sua chave de segurança é:"),print(random.randrange(1000, 9999))
           print(email)
           print(saldo_atualID1)
           print(saldo_atualID2)
           print(saldo_atualID3)
        elif saldo_atualID3 < valor_pagamento:
          print('Você não tem saldo o suficiente para realizar a transação')
          saldo_atualID1 = saldo_atualID1
          saldo_atualID2 = saldo_atualID2
  elif senha != senha_ID2:
    print('Usuário ou senha incorreta')
    resposta1 = input('Deseja tentar novamente? (Sim ou Não) ')
  elif usuario != 'ID2':
    print('Usuário ou senha incorreta')
    resposta = input('Deseja tentar novamente? (Sim ou Não) ')
  print('ID1 gera uma operação de recebimento de R$ 250.00 para o ID3')
  usuario = input('Informe o seu ID: ')
  senha = input('Informe a sua senha: ')
  email = input('Informe o seu e-mail: ')
  if usuario == 'ID3' or 'Paulo':
    if senha == senha_ID3:
      print('Seu saldo atual é de R$', saldo_atualID3)
      recebedor = input('Informe o ID recebedor do pagamento: ')
      if recebedor == 'ID1' or 'Ana':
        valor_pagamento = float(input('Informe o valor da transação: '))
        if saldo_atualID3 >= valor_pagamento:
          pagamento = (saldo_atualID3 - valor_pagamento)
          saldo_atualID3 = (saldo_atualID3 - valor_pagamento)
          saldo_atualID1 = (saldo_atualID1 + valor_pagamento)
          print('Transação realizada com sucesso')
          print('Transação realizada por:', usuario)
          print('Transação realizada para:', recebedor)
          print('Valor da transação R$',valor_pagamento)
          print("sua chave de segurança é:"),print(random.randrange(1000, 9999))
          print(email)
          print(saldo_atualID1)
          print(saldo_atualID2)
          print(saldo_atualID3)    
        elif saldo_atualID3 < valor_pagamento:
          print('Você não tem saldo o suficiente para realizar a transação')
          saldo_atualID3 = saldo_atualID3
          saldo_atualID1 = saldo_atualID1
  elif senha != senha_ID3 or usuario != 'ID3':
    print('Usuário ou Senha incorreta')
    resposta = input('Deseja tentar novamente? (Sim ou Não) ')
  elif usuario != 'ID3':
    print('Usuário ou senha incorreta')
    resposta = input('Deseja tentar novamente? (Sim ou Não) ')
  print('ID1 gera uma operação de recebimento de R$ 250.00 para o ID2')
  usuario = input('Informe o seu ID: ')
  senha = input('Informe a sua senha: ')
  email = input('Informe o seu e-mail: ')
  if usuario == 'ID2' or 'Rodrigo':
    if senha == senha_ID2:
      print('Seu saldo atual é de R$', saldo_atualID2)
      recebedor = input('Informe o ID recebedor do pagamento: ')
      if recebedor == 'ID1' or 'Ana':
        valor_pagamento = float(input('Informe o valor da transação: '))
        if saldo_atualID2 >= valor_pagamento:
          pagamento = (saldo_atualID2 - valor_pagamento)
          saldo_atualID1 = (saldo_atualID1 + valor_pagamento)
          saldo_atualID2 = (saldo_atualID2 - valor_pagamento)
          print('Transação realizada com sucesso')
          print('Transação realizada por:', usuario)
          print('Transação realizada para:', recebedor)
          print('Valor da transação R$',valor_pagamento)
          print("sua chave de segurança é:"),print(random.randrange(1000, 9999))
          print(email)
          print(saldo_atualID1 + pagamento)
          print(saldo_atualID2 + pagamento)
          print(saldo_atualID3 + pagamento)          
        elif saldo_atualID2 < valor_pagamento:
          print('Você não tem saldo o suficiente para realizar a transação')
          saldo_atualID1 = saldo_atualID1
          saldo_atualID2 = saldo_atualID2
          print(saldo_atualID1)
          print(saldo_atualID2)
          print(saldo_atualID3)
  while resposta2 == 'Sim':
     elif senha != senha_ID2 or usuario != 'ID2':
      print('Usuário ou senha incorreta')
      resposta2 = input('Deseja tentar novamente? (Sim ou Não) ')
  print('ID2 gera uma operação de recebimento de R$ 1000.00 para o ID3')
  usuario = input('Informe o seu ID: ')
  senha = input('Informe a sua senha: ')
  email = input('Informe o seu e-mail: ')
  while resposta3 == 'Sim':
  if usuario == 'ID3' or 'Paulo':
    if senha == senha_ID3:
      print('Seu saldo atual é de R$', saldo_atualID3)
      recebedor = input('Informe o ID recebedor do pagamento: ')
      if recebedor == 'ID2' or 'Rodrigo':
        valor_pagamento = float(input('Informe o valor da transação: '))
        if saldo_atualID3 >= valor_pagamento:
          pagamento = (saldo_atualID3 - valor_pagamento)
          saldo_atualID3 = (saldo_atualID3 - valor_pagamento)
          saldo_atualID2 = (saldo_atualID2 + valor_pagamento)
          print('Transação realizada com sucesso')
          print('Transação realizada por:', usuario)
          print('Transação realizada para:', recebedor)
          print('Valor da transação R$',valor_pagamento)
          print("sua chave de segurança é:"),print(random.randrange(1000, 9999))
          print(email)
          print(saldo_atualID1)
          print(saldo_atualID2)
          print(saldo_atualID3)          
        elif saldo_atualID3 < valor_pagamento:
          print('Você não tem saldo o suficiente para realizar a transação')
          saldo_atualID3 = saldo_atualID3
          saldo_atualID2 = saldo_atualID2
  elif senha != senha_ID3 or usuario != 'ID3':
    print('Usuário ou Senha incorreta')
    resposta3 = input('Deseja tentar novamente? (Sim ou Não')
  resposta = input('Deseja realizar outra transação? (Sim ou Não) ')
print('Fim do programa')
