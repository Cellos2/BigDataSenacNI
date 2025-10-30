###diadasemana=int(input(Quá é o dia da Semanavocê quer saber?))

#if diadasemana==1:  
    #print('Domingo')
#elif diadasemana==2:
    #print('Segunda')
#elif diadasemana==3:
    #print('Terça')
#elif diadasemana==4:
    #print('Quarta')
#elif diadasemana==5:
    #print('Quinta')
#elif diadasemana==6:
    #print('Sexta')
#elif diadasemana==7:
    #print('Sábado') 
#else
    #print(Esse número é inválido!)

semana=int(input('Qual é o dia que vocÊ quer saber?'))

match semana:
    case 1:
        print('Domingo')
    case 2:
        print('Segunda')
    case 3:
        print('Terça')
    case 4:
        print('Quarta')
    case 5:
        print('Quinta')
    case 6:
        print('Sexta')
    case 7:
        print('Sábado')
    case _:
        print('Número do dia Inválido!')
        
           
    
 
