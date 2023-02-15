var =  """18 JAN Lojas Americanas 52,76
18 JAN Padaria Nova Jordao 5,28
19 JAN Recarga*Bilh Unico 20,00
19 JAN Padaria Nova Jordao 5,44
20 JAN Daiso Brasil 35,97
20 JAN Uber *Uber *Trip 14,95
20 JAN Lojas Americanas 5,98
22 JAN Drogaria Sao Paulo 16,06
22 JAN Recarga*Bilh Unico 30,00""".split('\n')


for x in var:
  data = ' '.join(x.split(' ')[0:2])
  valor = x.split(' ')[-1]
  tag = x.replace(data, '').replace(valor, '')                    
  print(data + '|' + tag + '|' + valor)
