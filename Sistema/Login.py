from Sistema import Sistema


class Login(Sistema):
    def __init__(self, usuario, email, senha, logado):
        self.usuario = usuario
        self.email = email
        self.senha = senha
        self.logado = logado
        pass

    
    def logar(self, usuario, email, senha):

        try:
            if (usuario != 'amanda.pereira' 
            or email != 'amandapereiradevcontact@gmail.com' 
            or senha != '12345'):
                print("Credenciais não encontradas no sistema.")
                self.logado = False

            else:
                self.logado = True
                print("Credenciais encontradas!")
                print("Digite o módulo do sistema que deseja entrar:")
                nomeSistema = input("1 - Financeiro \n2 - Compras \n")

                if(nomeSistema == '1'):
                    nomeSistema = 'Financeiro'
                elif(nomeSistema == '2'):
                    nomeSistema = 'Compras'
                else:
                    quit()
                sistema = Sistema(nomeSistema)    
                sistema.iniciar(usuario, email, senha, self.logado)
        except:
            print("Não foi possível completar a requisição.")

    def deslogar(self):
        if (self.logado):
            try:
                self.logado = False
                print("Adeus :(")
            except:
                print("Não foi possível completar a requisição.")
            


