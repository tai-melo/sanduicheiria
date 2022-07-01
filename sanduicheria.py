nomeloja = 'Tairine' # identificador pessoal
print('Bem Vindo a Lanchonete da {}'.format(nomeloja)) 
print('*'*18 + 'CARDÁPIO'+ '*' * 18)
print('| Código |       Descrição         |  Valor | ')
print('|  100   |    Cachorro Quente      |  9,00  |')
print('|  101   | Cachorro Quente Duplo   | 11,00  |')
print('|  102   |          X-Egg          | 12,00  |')
print('|  103   |        X-Salada         | 12,00  |')
print('|  104   |         X-Bacon         | 14,00  |')
print('|  105   |         X-Tudo          | 17,00  |')
print('|  200   |  Refrigerante Lata      |  5,00  |')
print('|  201   |     Chá Gelado          |  4,00  |')

totalproduto = 0  # VAR acumuladora, ou seja, a conta do usuário vai iniciar zerada.

while True: # teste de validação de dados, o laço infinito 
  codproduto = int(input('Entre com o código do produto desejado:'))
  
  if (codproduto == 100) :   # será inseridas condicionais para que sejam verificados os códigos dos produtos e seus valores
    produto ="Cachorro Quente"
    totalproduto = totalproduto + 9.00
    print('Você pediu {} no valor de R$ 9.00.'.format(produto))
     # a cada condição verificada, e se o teste da condicional estiver correto, finaliza o laço de repetição
  
  elif (codproduto == 101):
    produto ="Cachorro Quente Duplo"
    totalproduto = totalproduto + 11.00
    print('Você pediu {} no valor de R$ 11.00.'.format(produto))
    
  elif (codproduto == 102):
    produto ="X-Egg"    
    totalproduto = totalproduto + 12.00
    print('Você pediu {} no valor R$ 12.00.'.format(produto))
      
  elif (codproduto == 103):
    produto ="X-Salada"    
    totalproduto = totalproduto + 12.00
    print('Você pediu {}  no valor R$ 12.00.'.format(produto))
    
  elif (codproduto == 104):
    produto ="X-Bacon"    
    print('Você pediu {} no valor de R$ 14.00.'.format(produto))
      
  elif (codproduto == 105):
    produto ="X-Tudo"    
    totalproduto = totalproduto + 17.00
    print('Você pediu {} no valor de R$ 17.00.'.format(produto)) 
    
  elif (codproduto == 200):
    produto ="Refrigerante em Lata"
    totalproduto = totalproduto + 5.00
    print('Você pediu {} no valor de R$ 5.00.'.format(produto))    
    
  elif (codproduto == 201):
    produto ="Chá Gelado"
    totalproduto = totalproduto + 4.00
    print('Você pediu {} no valor de R$ 4.00.'.format(produto))    
    
  else:
    print('\nCódigo Inválido')
    continue  # se digitar nenhum dos códigos corretos, retorna para o iníco do laço
    
  pedirmais = int(input('\nDeseja pedir mais alguma coisa?\n 1 - Sim\n 0 - Não\n>> '))# questionamos se o cliente deseja algo mais 
  
  if (pedirmais == 1):    # se desejar algo mais, mostramos o produto que ele escolheu e somamos os valores finais
    continue   
  elif (pedirmais == 0):  # senão quiser mais nada, somente apresenta o valor total e finaliza o laço
    print('\nValor total R$: {:.2f}'.format(totalproduto))
    break  
print('\nObrigada pela visita!')      