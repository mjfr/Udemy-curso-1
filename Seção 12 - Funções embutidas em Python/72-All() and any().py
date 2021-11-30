# All e any permitem verificar a correspondência booleana em um iterável. All retorna True caso todas as correspondências forem True e any retorna True se qualquer uma for True

lst_TTFT = [True, True, False, True]
lst_TTTT = [True, True, True, True]
lst_FFTF = [False, False, True, False]
lst_FFFF = [False, False, False, False]

# Como seria o all sem o método
def all_wannabe(iterable):
    for element in iterable:
        if not element:
            return False
    return True

all_wannabe(lst_TTFT)
all_wannabe(lst_TTTT)
all_wannabe(lst_FFTF)
all_wannabe(lst_FFFF)

# Como seria o any sem o método
def any_wannabe(iterable):
    for element in iterable:
        if element:
            return True
    return False

any_wannabe(lst_TTFT)
any_wannabe(lst_TTTT)
any_wannabe(lst_FFTF)
any_wannabe(lst_FFFF)



all(lst_TTFT)
all(lst_TTTT)
all(lst_FFTF)
all(lst_FFFF)
any(lst_TTFT)
any(lst_TTTT)
any(lst_FFTF)
any(lst_FFFF)