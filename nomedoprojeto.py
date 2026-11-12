bus_names = []
arrival_time = []
seat_availabilities = []
linha_vermelha = []

print("=== Nome projeto ===")
print("Integracao com a Linha Vermelha do Metrô \n")
print("1 - Cadastrar ônibus")
print("2 - Listar ônibus")
print("3 - Anunciar próximo ônibus")
print("4 - Simular sensor do ponto")
print("5 - Ver ônibus por estação da Linha Vermelha")
print("6 - Sair")



while True:
    option = int(input("Escolha uma opcao: "))
    match option:
        case 1:
            name = input("Nome da linha: ").capitalize()
            arrival = int(input("Minutos para chegar: "))
            while arrival < 1 or arrival > 120:
                print("Valor inválido. Digite de 1 a 120.")
                arrival = int(input("Minutos para chegar: "))
            availability = input("Assento preferencial livre? (S/N): ").upper() 
            while availability != "S" and availability != "N":
                print("Resposta inválida. Digite S ou N.")
                availability = input("Assento preferencial livre? (S/N): ").upper()
            if availability == "S":
                availability = "Livre"
            else:
                availability = "Ocupado"

            print("Estações da Linha Vermelha: \n")
            station_names = ["Palmeiras-Barra Funda", "República", "Sé", "Brás", "Tatuapé", "Corinthians-Itaquera"]
            for i in range(len(station_names)):
                print(f'{i + 1} - {station_names[i]}')

            station_number = int(input("Em qual estação este ônibus termina? "))
            while station_number < 1 or station_number > 6:
                print("Estação inválida. Digite de 1 a 6.")
                station_number = int(input("Em qual estação este ônibus termina? "))
            print(f'Ônibus cadastrado! Integração na estação {station_names[station_number - 1]}')

            bus_names.append(name)
            arrival_time.append(arrival)
            seat_availabilities.append(availability)
            linha_vermelha.append(station_names[station_number - 1])


        case 2:
            if len(bus_names) == 0:
                print("Nenhum ônibus cadastrado.")
            else: 
                print("--- Ônibus cadastrados ---")
                for i in range(len(bus_names)):
                    print(f'Linha {bus_names[i]} - {arrival_time[i]} min - assento {seat_availabilities[i]} - Integracao {linha_vermelha[i]}')
                

        case 3:
            if len(bus_names) == 0:
                print("Nenhum ônibus cadastrado.")
            else:
                next_bus = 0
                for i in range(len(arrival_time)):
                    if arrival_time[i] < arrival_time[next_bus]:
                        next_bus = i
                print(f'Próximo ônibus, Linha {bus_names[next_bus]}, em {arrival_time[next_bus]} minutos.')
                print(f'Assento preferencial {seat_availabilities[next_bus]}')
                print(f'Este onibus termina na estação {linha_vermelha[next_bus]} da linha vermelha do metrô.')
        case 4:
            print("4 - Simular sensor do ponto")
        case 5:
            print("5 - Ver ônibus por estação da Linha Vermelha")
        case 6:
            print("Programa encerrado. Boa viagem!")
            break
        case _:
            print("Opção inválida.")
    


