class Login:
    def __init__(self, usuario, contraseña):
        self._usuario = usuario
        self._contraseña = contraseña
    
    def validar_usuario(self, usuario_intento):
        return usuario_intento == self._usuario
    
    def validar_contraseña(self, contraseña_intento):
        return contraseña_intento == self._contraseña
    
    def autenticar(self, usuario_intento, contraseña_intento):
        if self.validar_usuario(usuario_intento) and self.validar_contraseña(contraseña_intento):
            print("Autenticación exitosa")
            return True
        else:
            print("Usuario o contraseña incorrectos")
            return False

login_sistema = Login("admin", "segura123")
login_sistema.autenticar("admin", "segura123")
login_sistema.autenticar("user", "123456")