def vcpf(cpf):    
    if len(cpf) == 11 and cpf.isdigit():
        return True
def vmail(mail):
    mail = mail.strip()
    if mail.count('@') != 1:
        return False
    usuario, dominio = mail.split('@')
    if not usuario or not dominio:
        return False
    if '.' not in dominio or dominio.startswith('.') or dominio.endswith('.'):
        return False
    if ' ' in mail:
        return False
    else:
        return True
def vtel(tel):
    digitos=tel.strip('',"")
    if len(digitos) < 10 or len(digitos) > 11 and not digitos.isdigit():
        return False
    else:
        return True
