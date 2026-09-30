import re 

def validar_name(name: str)->bool:
    
    if not isinstance(name,str):
        return False
    return bool(re.match(r'^[A-Za-z ]+$', name))

