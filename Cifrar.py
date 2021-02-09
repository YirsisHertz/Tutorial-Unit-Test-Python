import bcrypt

def cifrar(unhash_pass):

    if type(unhash_pass) != str:
        unhash_pass = str(unhash_pass)

    return bcrypt.hashpw(unhash_pass.encode(), bcrypt.gensalt()).decode()

