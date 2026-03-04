#Código que representa a oficina e todas as operações que os usuários podem fazer

#Importando módulos para as operações com json e datetima para alguns métodos
import os
import json
from datetime import datetime

#Importando minhas classes que eu vou usar no sistema
from users import User
from components import Vehicle


class CarWorkshop():
    """Classe que contém as mecânicas principais da Oficina."""
    #Minha ideia é que as métodos da mecânica seja acessadas pelo tipo de usuário
    def __init__(self, type_access):
        #Esse atributo que vai definir as funções que cada usuário pode acessar
        self.type_access = type_access
        self.maintence_services = {}

    #Aqui está o método para o vendedor
    def get_service(self, func_name, client_name, client_car, price, description, diagnostic="NULL"):
        """Método que adiciona um registro de serviço pendente."""
        if self.type_access != 2:
            print("Acesso não autorizado.")
        else:
            now = datetime.now()
            log_format = f"([{now.strftime('%Y-%m/%d %H:%M:%S')}] [{description}] [{func_name}] [{client_car}] Diagnostic: {diagnostic}, Cliente: {client_name}, Orçamento: {str(price)})\n"
            try:
                with open('pendent_services.txt', 'a', encoding='utf-8') as log_object:
                    log_object.write(log_format)
            except FileNotFoundError:
                raise FileNotFoundError("Arquivo de logs não encontrado.")
            else:
                print("Pedido de serviço adicionado com sucesso.")

    #Agora os métodos do mecânico
    def finish_service(self, mechanic):
        """Método que termina um serviço aberto por um funcionário."""
        if self.type_access != 3:
            print("Acesso não autorizado.")
        else:
            try:
                with open('pendent_services.txt', 'r', encoding='utf-8') as log_object:
                    pendent_services = log_object.readlines()
            except FileNotFoundError:
                raise FileNotFoundError("Arquivo de logs não encontrado.")
            else:
                if pendent_services:
                    print("Qual ordem de serviço você deseja finalizar. (Digite o número correspondente a entrada.)")

                    for i, pendent_service in enumerate(pendent_services, start=1):
                        print(f"{i} - {pendent_service.strip()}")

                    while True:
                        try:
                            pendent_service_choose = int(input("\n"))
                        except ValueError:
                            print("Entrada inválida. Escolha algumas das opções acima.")
                            continue
                        else:
                            pendent_service_choose = pendent_service_choose - 1
                            new_log = pendent_services.pop(pendent_service_choose)
                            try:
                                with open('pendent_services.txt', 'w', encoding='utf-8') as log_object:
                                    log_object.writelines(pendent_services)
                            except FileNotFoundError:
                                raise FileNotFoundError("Arquivo de logs não encontrado.")
                            break
                    
                    now = datetime.now()
                    new_log = f"{new_log}Finished - {now.strftime('%Y-%m/%d %H:%M:%S')} by {mechanic}\n"
                    try:
                        with open('finish_services.txt', 'a', encoding='utf-8') as log_object:
                            log_object.write(new_log)
                    except FileNotFoundError:
                        raise FileNotFoundError("Arquivo de logs não encontrado.")
                    else:
                        print("Pedido de serviço finalizado com sucesso.")

                else:
                    print("Nenhuma ordem de serviço para finalzar.")
                    return None
                

    #Agora os métodos do administrador
    def create_accounts(self):
        """Método exclusivo dos administradores para criar contas de usuário."""
        if self.type_access != 1:
            print("Acesso não autorizado.")
        else:
            print("Escreva os dados da nova conta ")
            first_name = input("Escreva o primeiro nome: ")
            last_name = input("Escreva o sobrenome: ")
            user_name = input("Escreva o usuário: ")
            password = input("Digite a nova senha do usuário: ")
            new_user = User(first_name, last_name, password, user_name)
            new_user.save_user()

    def delete_accounts(self):
        """Método exclusivo dos administradores para excluir usuários."""
        if self.type_access != 1:
            print("Acesso não autorizado.")
        else:
            while True:
                user_search = input("Digite o usuário que você deseja excluir: ")
                user_deleted_path = f"{user_search}.json"
                if os.path.exists(user_deleted_path):
                    os.remove(user_deleted_path)
                    print("Usuário excluído com sucesso.")
                    break
                else:
                    print("Usuário não encontrado.")
                    break
        
    def view_services_log(self):
        """Método para visualizar todos os logs no sistema."""
        try:
            with open('finish_services.txt', 'r', encoding='utf-8') as log_finished_object:
                logs_finished = log_finished_object.readlines()
        except FileNotFoundError:
            raise FileNotFoundError("Arquivo de logs não encontrado.")
        else:
            try:
                with open('pendent_services.txt', 'r', encoding='utf-8') as log_pendent_object:
                    logs_pendent = log_pendent_object.readlines()
            except FileNotFoundError:
                raise FileNotFoundError("Arquivo de logs não encontrado.")
            else:
                print("Log dos serviços finalizados")
                for pendent_service in logs_finished:
                        print(f"{pendent_service.strip()}")
                print("\nLog dos serviços pendentes")
                for pendent_service in logs_pendent:
                        print(f"{pendent_service.strip()}\n")

if __name__ == "__main__":
    simas_turbo = CarWorkshop(1)
    #funcional
    #simas_turbo.get_service('gustavo', 'jonas', 'fusion', 'falhando a cada 5 metros.', 200, 'reparo')
    simas_turbo.create_accounts()