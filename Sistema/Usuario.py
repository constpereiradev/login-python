from Sistema import Sistema

class Usuario(Sistema):
    def __init__(self, usuario, email, senha, logado):
        self.usuario = usuario
        self.email = email
        self.senha = senha
        self.logado = logado
        pass


    def abrirSistema(self):
        try:
            Sistema.iniciar(self, self.usuario, self.email, self.senha, self.logado)
        except:
            print("Não foi possível completar a requisição.")
        
    
usuario = Usuario('', '', '', False)
usuario.abrirSistema()