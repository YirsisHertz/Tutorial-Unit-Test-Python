from Cifrar import cifrar

def test_CifrarPass():
    tipo = type(cifrar("hola"))
    assert tipo == str

def test_GeneraDiferentesPass():
    
    unhash_pass = "hola"
    
    prueba1 = cifrar(unhash_pass)
    prueba2 = cifrar(unhash_pass)

    assert prueba1 != prueba2

def test_ConvierteTiposDiferentes():
    value = 9182
    tipo = type(cifrar(value))

    assert tipo == str
