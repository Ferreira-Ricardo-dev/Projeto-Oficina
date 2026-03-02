#Aqui estão as classes que representam as pessoas envolvidas no négocio

#Módulo necessário para salvar os usuários
import json


class User():
    """Classe com as características bases das pessoas na oficina."""
    def __init__(self, first_name, last_name, password, user_name):
        self.first_name = first_name
        self.last_name = last_name
        self._user_name = user_name
        self.password = password
        self.type = self.get_type()
        self.success_registre()

    @classmethod
    def load_user(cls, username):
        filename = f'{username}.json'
        try:
            with open(filename, 'r') as user_file:
                user_data = json.load(user_file)
            obj = cls.__new__(cls)
            obj.__dict__.update(user_data)
            return obj
        except FileNotFoundError:
            print("Usuário não encontrado.")
            return None


    @property
    def password(self):
        """Getter: Retorna a senha de forma controlada."""
        return self.__password
    
    @password.setter
    def password(self, new_password):
        """Aplica uma lógica de validação para a senha."""
        while True:
            try:
                if any(char.isdigit() for char in new_password):
                    print("Senha cadastrada com sucesso.")
                    self.__password = new_password
                    break
                else:
                    raise ValueError("Senha inválida. A senha deve possuir entre 1 a 8 caracteres e ao menos 1 número.")
            except ValueError as e:
                print(e)
                new_password = input("Senha: ")
                continue

    def get_type(self):
        """
        Função que controla qual o tipo de usuário será criado.
        1 - Admin
        2 - Vendedor
        3 - Mecânico
        """
        print("Qual o tipo de conta será criada (Escolha de 1 a 3)")
        print("\t1 - Administrador")
        print("\t2 - Vendedor")
        print("\t3 - Mecânico")
        while True:
            try:
                type = int(input("\t"))
            except ValueError:
                print("Entrada inválida. Escolha de 1 a 3.")
                continue
            else:
                print("Tipo definido com sucesso.")
                return type
                
    def success_registre(self):
        """Mensagem indicando a criação do usuário."""
        print("\nUsuário criado com sucesso!")

    def save_user(self):
        """Função para salvar usuários."""
        filename = f"{self._user_name}.json"
        user_data = {}
        user_data['first_name'] = self.first_name
        user_data['last_name'] = self.last_name
        user_data['_user_name'] = self._user_name
        user_data['password'] = self.password
        user_data['type'] = self.type
        try:
            with open(filename, 'w') as user_file:
                json.dump(user_data, user_file)
        except FileNotFoundError:
            print("Não foi possível salvar o usuário.")
        else:
            print(f"Usuário {self.first_name.title()} salvo com sucesso.")

    def show_user(self):
        """Função para mostrar dados do usuário."""
        print("Dados do usuário: ")
        print(f"Usuário: {self._user_name}")
        print(f"Nome: {self.first_name}")
        print(f"Sobrenome: {self.last_name}")

if __name__ == '__main__':
    #Teste para a lógica de senha
    print("Hello world")
    user_1 = User.load_user('rick@123')
    user_1.show_user()