
class Sistema():
    def __init__(self, nome):
        self.nome = nome
        

    def iniciar(self, usuario, email, senha, logado):

        try:
            from Login import Login
            login = Login(usuario, email, senha, logado)

            if(logado):
                print(f'------- {usuario}, Bem vindo ao módulo {self.nome} --------')
                print(f'------- Escolha a opção desejada --------')
                opcao = int(input("1 - Sair \n"))

                if(opcao == 1):
                    login.deslogar()
            else:
                usuario = input("Informe seu usuário: ")       
                email = input("Informe seu email: ")       
                senha = input("Informe sua senha: ")  
                login.logar(usuario, email, senha)     
        except:
            print("Não foi possível completar a requisição.")
    




