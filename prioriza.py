# PRIORIZA
# Time 404
# Giovanna Ciola RM 575631
# Nathaly Vieira Barbosa RM 575407
# Marina Lobato Soares RM 575475
# Jamil de Jesus Chaluppe Filho RM 575697
# Gustavo Moreira Souza RM 576147


stop_points = ["Terminal Pq. D. Pedro II", "Lgo. Pateo do Colegio", "R. Boa Vista, 364"]
service_types = ["FISICA", "VISUAL", "AUDITIVA", "IDOSO", "MOBILIDADE REDUZIDA", "GESTANTE", "AUTISTA", "NENHUM"]
bus_status = ["A CAMINHO", "ONIBUS CHEGOU", "ONIBUS ACABOU DE SAIR", "SEM ONIBUS"]

line = "2002-10"
seats = 3 
seat_availabilities = 3
led = "APAGADO"

request_names = []
request_types = []
request_points = []
request_amounts = []

# MENU PRINCIPAL

while True:
    print("\n=== PRIORIZA ===")
    print("1 - Solicitar atendimento prioritario")
    print("2 - Cancelar solicitacao")
    print("3 - Ver onibus")
    print("4 - Simular viagem")
    print("5 - Sair")

    choice = int(input("Escolha uma opcao: "))
    match choice:

        # 1 - Solicitar atendimento prioritario

        case 1:
            # Nome do passageiro
            name = input("Nome do passageiro: ")
            while name == '':
                print("O nome nao pode ficar vazio.")
                name = input("Nome do passageiro: ")

            # Tipos de atendimento
            print("Tipos de atendimento:")
            for i in range(len(service_types)):
                print(f"{i + 1} - {service_types[i]}")
            type_number = int(input("Escolha o tipo: "))
            while type_number < 1 or type_number > len(service_types):
                print("Tipo invalido.")
                type_number = int(input("Escolha o tipo: "))
            passenger_type = service_types[type_number - 1]

            # Verifica os dados antes de pedir o rstante dos dados
            if passenger_type == "NENHUM":
                print("Este passageiro não tem direito ao assento preferencial.")
            elif seat_availabilities == 0:
                print("Não tem assentos preferenciais livres no momento.")
            else:
                # Ponto de embarque
                print()
                print(f"Pontos da linha {line}:")
                for i in range(len(stop_points)):
                    print(f"{i + 1} - {stop_points[i]}")
                stop_number = int(input("Escolha o ponto de embarque: "))
                while stop_number < 1 or stop_number > len(stop_points):
                    print(f"Ponto invalido. Digite de 1 a {len(stop_points)}.")
                    stop_number = int(input("Escolha o ponto de embarque: "))
                point = stop_points[stop_number - 1]

                # Quantidade de assentos disponiveis
                amount = int(input(f"Quantos assentos? (1 a {seat_availabilities}): "))
                while amount < 1 or amount > seat_availabilities:
                    print(f"Quantidade invalida. Digite de 1 a {seat_availabilities}.")
                    amount = int(input(f"Quantos assentos? (1 a {seat_availabilities}): "))

                # Guarda a solicitacao nas listas
                request_names.append(name)
                request_types.append(passenger_type)
                request_points.append(point)
                request_amounts.append(amount)

                # Reserva os assentos e acende o LED
                seat_availabilities -= amount
                led = "ACESO"

                print("Solicitacao enviada com sucesso!")
                print("Seu pedido já foi informado ao motorista.")
                print(f"[MOTORISTA] {name} - {passenger_type} - embarque em {point} - {amount} assento(s) reservado(s)")
                print(f"LED dos assentos preferenciais: {led}")

        # 2 - Cancelar solicitacao

        case 2:
            if len(request_names) == 0:
                print("Nenhuma solicitacao ativa para cancelar.")
            else:

                # Mostra as solicitacoes ativas
                print("Solicitacoes ativas:")
                for i in range(len(request_names)):
                    print(f"{i + 1} - {request_names[i]} - {request_types[i]} - {request_points[i]} - {request_amounts[i]} assento(s)")

                cancel_number = int(input("Qual solicitacao deseja cancelar? "))
                while cancel_number < 1 or cancel_number > len(request_names):
                    print(f"Solicitacao invalida. Digite de 1 a {len(request_names)}.")
                    cancel_number = int(input("Qual solicitacao deseja cancelar? "))
                index = cancel_number - 1

                # Guarda o nome e a quantidade antes de remover
                canceled_name = request_names[index]
                canceled_amount = request_amounts[index]

                # Remove a solicitacao das 4 listas
                request_names.pop(index)
                request_types.pop(index)
                request_points.pop(index)
                request_amounts.pop(index)

                # Libera os assentos; apaga o LED se todos ficarem livres
                seat_availabilities += canceled_amount
                if seat_availabilities == seats:
                    led = "APAGADO"


                print("Cancelamento realizado com sucesso.")
                print(f"[MOTORISTA] {canceled_name} cancelou - {canceled_amount} assento(s) liberado(s)")
                print(f"LED dos assentos preferenciais: {led}")

        # 3 - Ver onibus e solicitacoes

        case 3:
            print(f"Linha {line} - assentos preferenciais livres: {seat_availabilities} de {seats} - LED {led}")
            if len(request_names) == 0:
                print("Nenhuma solicitacao ativa.")
            else:
                print("Solicitacoes ativas:")
                for i in range(len(request_names)):
                    print(f"- {request_names[i]} ({request_types[i]}) embarca em {request_points[i]} - {request_amounts[i]} assento(s)")

        # 4 - Simular viagem

        case 4:
            print("INICIOU A VIAGEM")
            for i in range(len(stop_points)):
                print(f"Ponto: {stop_points[i]}")
                for j in range(len(bus_status)):
                    print(f"  Antena: {bus_status[j]}")
            print("PONTO FINAL")

        # 5 - Sair

        case 5:
            print("Programa encerrado. Obrigado por usar o Prioriza!")
            break

        # Qualquer outro numero

        case _:
            print("Opcao invalida. Digite um numero de 1 a 5.")