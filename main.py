#interface de usuario
print('\n*************************\n')
print('SIMULADOR DE INVESTIMENTOS MATFIN')
print('\n\n*************************\n\n')
print('''
Escolha um dos seguintes investimentos:
[A] POUPANÇA
[B] CDB(100% do CDI)
[C] LCI/LCA
[D] Outro (escolher taxa)''')

continuar='sim'
while continuar=='sim':
    escolha = input('Sua escolha: ').strip().lower()
    print('')
    #variaveis
    aporte_inicial = int(input('Aporte inicial: R$ '))
    aporte_mensal = int(input('Aporte mensal: R$ '))
    tempo = int(input('Tempo (meses): '))
    tempo_ano = tempo/12
    inflação = 0.045 * tempo_ano
    total_bruto1=0
    total_bruto11=0
    total_bruto111=0
    total_bruto2=0
    total_bruto22=0
    total_bruto222=0


    #ifs de escolha
    if escolha == 'a' or escolha == 'poupança':
        taxa = 0.5
      
    elif escolha == 'b' or escolha == 'cdb':
        taxa = 0.802
        if 6 <= tempo < 12:
            taxa = 0.828
        if 12 <=  tempo < 24:
            taxa = 0.854
        if tempo >= 24:
            taxa = 0.88
                
    elif escolha == 'c' or escolha == 'lci/lca':
        taxa = 1.0143
      
    elif escolha == 'd' or escolha == 'outro' or escolha == 'escolher taxa':
        taxa = float(input('Taxa mensal (porcentagem): '))
      
    #calculo dos totais
    total_investido = aporte_inicial + (aporte_mensal * tempo)
    total_bruto = (aporte_inicial * (1 + (taxa / 100)) ** tempo) + (aporte_mensal * ((1 + (taxa / 100)) ** tempo - 1) / (taxa / 100))
    total_gerado = total_bruto - total_investido
    total_liquido = total_bruto - (total_bruto * inflação) 

          
    #prints para o usuario
    print('')
    print(f'Total investido: R$ {total_investido}')
    print(f'Dinheiro gerado pelo investimento: R$ {total_gerado:.2f}')
    print(f'Total bruto: R${total_bruto:.2f}')
    print(f'Total Corrigido pela  Inflação: R${total_liquido:.2f}')

    #comparação1
    if  escolha == 'b' or escolha == 'cdb':
        taxa = 1.0143
        total_bruto1 = (aporte_inicial * (1 + (taxa / 100)) ** tempo) + (aporte_mensal * ((1 + (taxa / 100)) ** tempo - 1) / (taxa / 100))
        taxa = 0.5
        total_bruto2 = (aporte_inicial * (1 + (taxa / 100)) ** tempo) + (aporte_mensal * ((1 + (taxa / 100)) ** tempo - 1) / (taxa / 100))

    #comparação2
    if  escolha == 'a' or escolha == 'poupança':
        taxa = 1.0143
        total_bruto11 = (aporte_inicial * (1 + (taxa / 100)) ** tempo) + (aporte_mensal * ((1 + (taxa / 100)) ** tempo - 1) / (taxa / 100))     
        taxa = 0.802
        if 6 <= tempo < 12:
            taxa = 0.828
        if 12 <= tempo < 24:
            taxa = 0.854
        if tempo >= 24:
            taxa = 0.88
        total_bruto22 = (aporte_inicial * (1 + (taxa / 100)) ** tempo) + (aporte_mensal * ((1 + (taxa / 100)) ** tempo - 1) / (taxa / 100))
      
    #comparação3
    if  escolha == 'c' or escolha == 'lci/lca':
        taxa = 0.5
        total_bruto111 = (aporte_inicial * (1 + (taxa / 100)) ** tempo) + (aporte_mensal * ((1 + (taxa / 100)) ** tempo - 1) / (taxa / 100))  
        taxa = 0.802
        if 6 <= tempo < 12:
            taxa = 0.828
        if 12 <= tempo < 24: 
            taxa = 0.854
        if tempo >= 24:
            taxa = 0.88
        total_bruto222 = (aporte_inicial * (1 + (taxa / 100)) ** tempo) + (aporte_mensal * ((1 + (taxa / 100)) ** tempo - 1) / (taxa / 100))


    if total_bruto2 > total_bruto1 and total_bruto2 > total_bruto:
        print(f'Poupança é melhor pois o bruto é: R${total_bruto2:.2f}')
    elif total_bruto1 > total_bruto2 and total_bruto1> total_bruto:
        print(f'LCI/LCA é melhor pois o bruto é: R${total_bruto1:.2f}')
    elif total_bruto11 > total_bruto22 and total_bruto11> total_bruto:
        print(f'LCI/LCA é melhor pois o bruto é: R${total_bruto11:.2f}')
    elif total_bruto22 > total_bruto11 and total_bruto22> total_bruto:
        print(f'CDB é melhor pois o bruto é: R${total_bruto22:.2f}')
    elif total_bruto111 > total_bruto222 and total_bruto111> total_bruto:
        print(f'Poupança é melhor pois o bruto é: R${total_bruto111:.2f}')
    elif total_bruto222 > total_bruto111 and total_bruto222> total_bruto:
        print(f'CDB é melhor pois o bruto é: R${total_bruto222:.2f}')

    
    continuar=input('\n\nDeseja continuar a utilizar o simulador?: (Digite "sim" ou "não")\n').strip().lower()
    print('\n')
print('\n** Simulação Encerrada ** \n')
