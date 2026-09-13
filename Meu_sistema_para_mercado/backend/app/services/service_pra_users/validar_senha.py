import re

def validar_senha(senha=str)->tuple[bool,str]:
    #verificar tamnho da senha
    if len(senha) <8 or len(senha)>20:
        e = "curta"
        if len(senha) >20:
            status = "comprida"
        return False , f"senha {status}"

    if not re.search(r"[A-Z]",senha):
        return False, "falta letras maiuscula"
    
    if not re.search(r"[a-z]",senha):
        return False,"falta letras minusculas"
    
    if not re.search(r"[0-9]",senha):
        return False, "falta numeros"
    
    if not re.search(r"[!@#$%^&*(),.?\":{}|<>]", senha):
        return False, "falta caractere especial"
    
    return True, "senha valida"


senha="Testsenha12345!"

print(validar_senha(senha))