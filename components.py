#Classe que representa os veículos

class Vehicle():
    """Classe usada na oficina para representar os veículos."""
    def __init__(self, make, model, year):
        """Atributos dos carros da oficina."""
        self.make = make
        self.model = model
        self.year = year
        self.notation = self.get_notations()
        self.owner = self.get_owner_infos()

    def get_owner_infos(self):
        """Função para armazenar os dados do dono do carro."""
        owner_infos = {}
        full_name = input("Digite o nome e o sobrenome do dono: ")
        number = input("Digite o número do dono (formato (XX)XXXXX-XXXX): ")
        owner_infos['full_name'] = full_name
        owner_infos['number'] = number
        return owner_infos

    def get_notations(self):
        """Função que permite a entrada de observações para o veículo."""
        print("Deseja adicionar alguma informação para o veículo: ")
        print("\t1 - SIM\n\t2 - NÃO")
        while True:
            try:
                option = int(input("\t"))
            except ValueError:
                print("Entrada inválida. Escolha entre 1 e 2.")
                continue
            else:
                if option == 1:
                    while True:
                        notations = []
                        obsernation = input("Escreva a observação: ")
                        print("Essa nota está correta?")
                        print("\t1 - SIM\n\t2 - NÃO")
                        try:
                            option_1 = int(input("\t"))
                        except ValueError:
                            print("Entrada inválida. Escolha entre 1 e 2.")
                            continue
                        else:
                            if option_1 == 1:
                                notations.append(obsernation)
                                print("Nota adicionada.")
                                break
                            elif option_1 == 2:
                                print("Nota cancelada.")
                                break
                            else:
                                print("Entrada inválida. Escolha entre 1 e 2.")
                                continue

                    if notations:
                        return notations
                    else:
                        return None
                    
                elif option == 2:
                    return None
                
                else:
                    print("Entrada inválida. Escolha entre 1 e 2.")
                    continue

if __name__ == "__main__":
    car = Vehicle('ford', 'fusion', '2018')
    print(car.owner)
    print(car.notation)