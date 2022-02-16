def calculate():
    operation = input('''
 Digite:
+ para adição
- para subtração
* para multiplicação
/ para divisão
''')

    number_1 = float(input("Primeiro número: "))
    number_2 = float(input("Segundo número: "))

    #ADIÇÃO
    if operation == '+':
        print("ADIÇÃO")
        print("{} + {} = ".format(number_1, number_2)) 
        print(number_1 + number_2)

    #SUBTRAÇÃO
    elif operation == "-":   
        print("SUBTRAÇÃO")
        print("{} - {} = ".format(number_1, number_2))
        print(number_1 - number_2)

    #Multiplicação
    elif operation == "*":
        print("MULTIPLICAÇÃO")
        print("{} * {} = ".format(number_1, number_2))
        print(number_1 * number_2)

    #Divisão
    elif operation == "/":    
        print("DIVISÃO")
        print("{} / {} = " .format(number_1, number_2))
        print(number_1 / number_2)

    
    else:
        print("Você não digitou um operador válido, execute o programa novamente.")

    again()
def again():
    calc_again = input('''
    Para calcular novamente tecle:
    S para Sim
    N para Não 
        ''')
        #Se o usuário apertar S run o calculate()
    if calc_again.upper() == 'S':
        calculate()

            #Se o usuário apertar N fale tchau para o usuário e encerre o sistema
    elif calc_again.upper() == 'N':
        print("Até mais")

                #Se o usuário teclar outra coisa rode a função novamente
    else:
        again()

calculate()



