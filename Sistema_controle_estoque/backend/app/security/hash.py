import bcrypt

def criar_hash(senha_original=str)->bytes:
    salt =bcrypt.gensalt(rounds=12)
    return bcrypt.hashpw(senha_original.encode("utf-8"),salt)