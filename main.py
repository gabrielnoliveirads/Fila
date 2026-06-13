#declarando variaveis
fila = []
senha = 0
desistencia = 0
atendidos = 0
tempo = 0

#criando a repeticao infinita
while True:
    print()
    print("G - Gerar senha comum")
    print("P - Gerar senha preferencial")
    print("C - Chamar próximo cliente")
    print("A - Avançar tempo")
    print("F - Exibir fila")
    print("E - Exibir estatísticas")
    print("S - Sair")
    print()
    
    opcao = input("Qual opção que deseja acionar: ").upper()
    print()
    
    # criando execucao de cada opcao com a respectiva letra
    if opcao == 'G':
        senha +=1
        cliente = [senha, "C", 0]
        fila.append(cliente)
        print(f'Senha {senha} gerada para cliente comum.')
    
    elif opcao == 'P':
        senha+=1
        cliente =[senha, 'P', 0]
        fila.append(cliente)
        print(f'Senha {senha} gerada para cliente preferencial.')
    
    elif opcao == 'C':
        for cliente in fila:
            if cliente[2] >= 8 and cliente[1] == 'C':
                print('Cliente chamado:')
                print(f"Senha {cliente[0]} | Tipo {cliente[1]} | Espera {cliente[2]}")
                tempo += cliente[2]
                fila.remove(cliente)
                atendidos+=1
                break
        else:
            for cliente in fila:
                if cliente[1] == 'P': 
                    print('Cliente chamado:')
                    print(f"Senha {cliente[0]} | Tipo {cliente[1]} | Espera {cliente[2]}")
                    tempo += cliente[2]
                    fila.remove(cliente)
                    atendidos+=1
                    break
            else:
                for cliente in fila:
                    if cliente[1] == 'C': 
                        print('Cliente chamado:')
                        print(f"Senha {cliente[0]} | Tipo {cliente[1]} | Espera {cliente[2]}")
                        tempo += cliente[2]
                        fila.remove(cliente)
                        atendidos+=1
                        break
                else: 
                    print('Não há clientes aguardando')
                
                
    elif opcao == 'A':
        for cliente in fila[:]:
            cliente[2] += 1
            if cliente[2] >= 10:
                print('Cliente desistiu:')
                print(f"Senha {cliente[0]} | Tipo {cliente[1]} | Espera {cliente[2]}")
                fila.remove(cliente)
                desistencia += 1
    
    elif opcao == 'F':
        if len(fila) == 0:
            print('Não há clientes aguardando')
        else:
            print('Fila atual:')
            for cliente in fila:
                print(f"Senha {cliente[0]} | Tipo {cliente[1]} | Espera {cliente[2]}")
    
    elif opcao == 'E':
            print(f'Total de senhas geradas: {senha}.')
            print(f'Total de clientes atendidos: {atendidos}.')
            print(f'Total de clientes que desistiram: {desistencia}.')
            print(f'Quantidade de clientes ainda aguardando na fila:{len(fila)}.')
            if atendidos == 0:
                print(f'Nenhum cliente foi atendido, portanto, ainda não é possível calcular o tempo médio de espera dos atendidos.')
            else:
                print(f'Tempo médio de espera dos clientes atendidos: {tempo/atendidos}.')
    elif opcao == 'S':
        print('Fim do atendimento | Banco Boa Sorte S.A.')
        break
    
    #trantando qualquer outra entrada que nao seja a adequada
    else:
        print('Opção inválida.')
