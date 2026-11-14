# PRIORIZA - Mobilidade sem barreiras
# Time 404
# Giovanna Ciola RM 575631
# Nathaly Vieira Barbosa RM 575407
# Marina Lobato Soares RM 575475
# Jamil de Jesus Chaluppe Filho RM 575697
# Gustavo Moreira Souza RM 576147


stop_points = ["Terminal Pq. D. Pedro II", "Lgo. Pateo do Colégio", "R. Boa Vista, 364"]
service_types = ["FISICA", "VISUAL", "AUDITIVA", "IDOSO", "MOBILIDADE REDUZIDA", "GESTANTE", "AUTISTA", "NENHUM"]
bus_status = ["A CAMINHO", "ONIBUS CHEGOU", "ONIBUS ACABOU DE SAIR", "SEM ONIBUS"]

line = "2002-10"
seats = 3 
seat_availabilities = 3
led = "APAGADO"

while True:
    print("\n=== PRIORIZA ===")
    print("1 - Solicitar atendimento prioritário")
    print("2 - Cancelar solicitação")
    print("3 - Ver ônibus")
    print("4 - Simular viagem")
    print("5 - Sair")

    choice = int(input("Escolha uma opção: "))
    match choice:
        case 1:
            name = input("Nome do passageiro: ")
            print("Tipos de atendimento:")
            for i in range(len(service_types)):
                print(f"{i + 1} - {service_types[i]}")
            type_number = int(input("Escolha o tipo: "))
            while type_number < 1 or type_number > len(service_types):
                print("Tipo invalido.")
                type_number = int(input("Escolha o tipo: "))
            passenger_type = service_types[type_number - 1]

            print(f"Paradas da linha {line}:")
            for i in range(len(stop_points)):
                print(f"{i + 1} - {stop_points[i]}")
            stop_number = int(input("Escolha o ponto de embarque: "))
            while stop_number < 1 or stop_number > len(stop_points):
                print("Ponto invalido.")
                stop_number = int(input("Escolha o ponto de embarque: "))
            point = stop_points[stop_number - 1]

            amount = int(input("Quantos assentos? "))
            if passenger_type == "NENHUM":
                print("Passageiro sem direito a tal assento")
            elif amount < 1 or amount > seat_availabilities:
                print("Assentos indisponiveis no momento.")
            else:
                seat_availabilities -= amount
                led = "ACESO"
                print("Passageiro tem direito ao assento preferencial")
                print("Solicitação enviada com sucesso!")
                print("Seu pedido já foi informado ao motorista.")
                print(f"[MOTORISTA] - {name} - {line} - {passenger_type} - {point} - {amount} Assentos foram alugados")
                print(f"LED dos assentos preferenciais: {led}")

        case 2:
            amount = int(input("Quantos assentos deseja cancelar? "))
            occupied = seats - seat_availabilities
            if amount < 1 or amount > occupied:
                print("Não foi possivel cancelar o agendamento")
            else:
                seat_availabilities += amount
                if seat_availabilities == seats:
                    led = "APAGADO"
                print("O cancelamento do agendamento foi realizado com sucesso.")
                print(f"[MOTORISTA] - {line} - {amount} Assentos foram liberados")
                print(f"LED dos assentos preferenciais: {led}")

        case 3:
            print(f"Linha {line} - assentos livres: {seat_availabilities} de {seats} - LED {led}")

        case 4:
            print("INICIOU A VIAGEM")
            for i in range(len(stop_points)):
                for j in range(len(bus_status)):
                    print(f"{line} - {stop_points[i]} : {bus_status[j]}")
            print("PONTO FINAL")

        case 5:
            print("Programa encerrado. Obrigado por usar o Prioriza!")
            break

        case _:
            print("Opção invalida.")