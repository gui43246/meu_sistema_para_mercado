import bcrypt

def verifique_hash(senha_digitada=str,hash_armazenado=bytes)->bool:
    
    return bcrypt.checkpw(senha_digitada.encode("utf-8"),hash_armazenado)
