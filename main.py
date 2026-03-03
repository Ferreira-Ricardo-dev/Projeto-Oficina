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
                    return current_user
                else:
                    print("Senha incorreta. Tente novamente.")

try:
    exist_user()
except FileNotFoundError as e:
    print(e)
    print("Crie uma conta de administrador para prosseguir.")
    create_admin()
finally:
    print("Bem vindo ao Simas Turbo Management System 2.0")
    system_user_login = login_system()
    print(system_user_login.type)
