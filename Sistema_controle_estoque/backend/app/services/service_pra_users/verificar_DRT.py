from app.DATABASE import get_db
import re 
def validar_DRT(drt=str)-> tuple[bool,str]:

    
    if not isinstance(drt,str):
        return False, "campo invalido"
    
    if len(drt)!=9 or  not re.fullmatch(r"\d+",drt):
        return False, "Verifique a DRT"
    
    #verificar o registro ja existe no banco de dados
    with get_db() as conn:
        cursor=conn.cursor()
        cursor.execute("""SELECT drt FROM users 
                       WHERE drt = ? """,(drt,))
        resultado=cursor.fetchall()
        if resultado:
            return False , "DRT ja cadastrada "
        
        
    return True, "ok"

