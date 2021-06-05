import random
import string

import cherrypy


class StringGenerator(object):
    @cherrypy.expose
    def index(self):
        return """
            <!DOCTYPE html>
            <html>
              <head>
                <meta charset="utf-8">
                <meta name="viewport" content="width=device-width, initial-scale=1">
                <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bulma@0.9.2/css/bulma.min.css">
                <title>Trabalho LTPC2</title>
          </head>
          <body>
          <h1>Trabalho LTPC</h1>
          <p>Nosso projeto foi desenvolvido para facilitar a vida de algumas pessoas(idosos)que convivem com o Alzheimer diariamente.Decidimos desenvolver um projeto simples, mas que pode ajudar em diversos aspectos.Se trata doacionamento de LEDs e LCD, possibilitando o entendimento de quando a pessoa deve tomar os seus remédios no horário correto.Esse site esta sendo Utilizado como uma platafora de testes para o nosso projeto. </p><br>
          <img src="https://hermanoprojetos.files.wordpress.com/2016/07/b0026-engrenagem2bcom2bmovimentos.gif"><br>
            <form method="get" action="generate">
              <input class="input" type="text" placeholder="Seu usuario" name="idd"><br><br>
             <input class="input" type="text" placeholder="Sua senha" name="password"><br><br>
              <button type="submit">Prosseguir</button>
              <a href="https://github.com/vitormicael/FATEC-MECATRONICA-1600792021046-vitormicael/blob/master/projeto-ltpc-2" class="button">codigo fonte</a>
            </form>
          </body>
        </html>"""

    @cherrypy.expose
    def generate(self, idd, password):
     usuario_1 = 'Vmicael'
     usuario_2 = 'Rchicarelli'
     usuario_3 = 'Mzanini'
     senha_1 = '12345'
     senha_2 = '1234'
     senha_3 = '123'
     if idd == usuario_1 and senha_1 == password or idd == usuario_2 and password == senha_2 or idd == usuario_3 and senha_3 == password:
         print('Acesso permitido')
     if idd == usuario_1:
       out = 'Tome o seu remédio vermelho as 09:00 e o seu remédio verde às 11:20. Você tem consulta no dia 12/02/2021 às 14:00 na R. São João, nº 213'
     elif idd == usuario_2:
       out = 'Tome o seu remédio vermelho as 09:55 e o seu remédio verde às 14:30. Você tem consulta no dia 11/12/2021 às 14:50 na R. São João, nº 514'
     elif idd == usuario_3:
        out = 'Tome o seu remédio vermelho as 15:30 e o seu remédio verde às 17:00. Você tem consulta no dia 03/06/2021 às 09:15 na R. São João, nº 115'
     else:
        out = 'Usuário ou Senha incorreto'
     return '%s (<a href="./">back</a>)' % out

if __name__ == '__main__':
    cherrypy.quickstart(StringGenerator())
