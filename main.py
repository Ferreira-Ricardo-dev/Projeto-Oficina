#Código que vai representar a lógica principal do menu
#Imports de algumas bibliotecas importantes
import os
import json


from components import Vehicle
from users import User
from services import CarWorkshop

def exist_user():
    """Função que vai verificar se existem usuários cadastrados"""
    users = [user for user in os.listdir('.') if user.endswith('.json')]
    if users:
        return True
    else:
        raise FileNotFoundError("Nenhum usuário foi encontrado")
    
def create_admin():
    print("Escreva os dados da nova conta de administrador")
    while True:
        first_name = input("Escreva o primeiro nome: ")
        last_name = input("Escreva o sobrenome: ")
        user_name = input("Escreva o usuário: ")
        password = input("Digite a nova senha do usuário: ")
        new_admin = User(first_name, last_name, password, user_name)
        if new_admin.type == 1:
            print("Conta criada com sucesso. Pode prosseguir com as operações.")

def login_system():
    """Função que vai ser o sistema de login"""
    while True:
        user = input("Digite o nome do usuário: ")
        filename = f'{user}.json'
        try:
            with open(filename, 'r') as user_object:
                user_data = json.load(user_object)
        except:
            print("Nome de usuário incorreto.")
            continue
        else:
            while True:
                password = input("Digite a senha: ")
                if user_data['password'] == password:
                    current_user = User.load_user(user)
                    print(f"Login realizado com sucesso!\n")
                    return current_user
                else:
                    print("Senha incorreta. Tente novamente.")

try:
    exist_user()
except FileNotFoundError as e:
    print(e)
    print("Crie uma conta de administrador para prosseguir.")
    create_admin()
else:
    print("Bem vindo ao Simas Turbo Management System 2.0")
    system_current_user = login_system()

    #Lógica para Admin's
    if system_current_user.type == 1:
        carworkshop_functions = CarWorkshop(system_current_user.type)
        #Loop principal da lógica de menu
        while True:
            print("Escolha uma operação")
            print("1 - Criar um novo usuário")
            print("2 - Excluir um usuário")
            print("3 - Visualizar logs de serviço")
            print("4 - Encerrar")
            try:
                admin_options = int(input())
            except ValueError:
                print("Entrada inválida")
                continue
            else:
                if admin_options == 1:
                    carworkshop_functions.create_accounts()
                    print()
                    continue

                elif admin_options == 2:
                    carworkshop_functions.delete_accounts()
                    print()
                    continue

                elif admin_options == 3:
                    carworkshop_functions.view_services_log()
                    print()
                    continue

                elif admin_options == 4:
                    print("\nObrigado por usar nossos serviços.")
                    print("Encerrando...")
                    break

                else:
                    print("\nEntrada inválida. Escolha uma das opções.")
                    continue

    elif system_current_user.type == 2:
        carworkshop_functions = CarWorkshop(system_current_user.type)
        #Loop principal da lógica de menu
        while True:
            print("Escolha uma operação")
            print("1 - Registrar pedido de serviço no sistema")
            print("2 - Encerrar")
            try:
                seller_options = int(input())
            except ValueError:
                print("Entrada inválida")
                continue
            else:
                if seller_options == 1:
                    func_name = f"{system_current_user.first_name.title()} {system_current_user.last_name.title()}"
                    model = input("Digite o modelo do carro: ")
                    make = input("Digite a fabricante do carro: ")

                    while True:
                        try:
                            year = int(input("Digite o ano do carro: "))
                            break
                        except ValueError:
                            print("Entrada inválida. Digite um número.")
                            continue

                    car = Vehicle(model, make, year)
                    description = input("Qual o serviço: ")

                    while True:
                        try:
                            price = int(input("Qual o valor do serviço: "))
                            if price < 0:
                                print("O valor não pode ser negativo!")
                                continue
                        except ValueError:
                            print("Entrada inválida. Digite um valor númerico.")
                            continue
                        else:
                            break

                    print("Deseja adicionar um diagnóstico inicial do problema: ")
                    print("1 - SIM")
                    print("2 - NÃO")
                    while True:
                        try:
                            diagnostic_option = int(input())
                        except ValueError:
                            print("Entrada inválida. Escolha uma das opções.")
                            continue
                        else:
                            if diagnostic_option == 1:
                                diagnostic = input("Qual o diagnóstico: ")
                            elif diagnostic_option == 2:
                                diagnostic = None
                                break
                            else:
                                print("Entrada inválida. Escolha uma das opções.")
                                continue
                    
                    if diagnostic:
                        carworkshop_functions.get_service(func_name, car.owner['full_name'].title(), car.model, price, description, diagnostic)
                    else:
                        carworkshop_functions.get_service(func_name, car.owner['full_name'].title(), car.model, price, description)
                        print()

                    continue

                elif seller_options == 2:
                    print("\nObrigado por usar nossos serviços.")
                    print("Encerrando...")
                    break

                else:
                    print("\nEntrada inválida. Escolha uma das opções.")
                    continue

    elif system_current_user.type == 3:
        carworkshop_functions = CarWorkshop(system_current_user.type)
        #Loop principal da lógica de menu
        while True:
            print("Escolha uma operação")
            print("1 - Terminar serviço pendente")
            print("2 - Encerrar")
            try:
                mechanic_options = int(input())
            except ValueError:
                print("Entrada inválida")
                continue
            else:
                if mechanic_options == 1:
                    mechanic_name = f"{system_current_user.first_name.title()}"
                    carworkshop_functions.finish_service(mechanic_name)
                    print()

                elif mechanic_options == 2:
                    print("\nObrigado por usar nossos serviços.")
                    print("Encerrando...")
                    continue

                else:
                    print("\nEntrada inválida. Escolha uma das opções.")
                    continue

