def toateCifrelePrime(n):
    '''
    Functia verifica daca un numar are toate cifrele prime
    :param n: numar intreg
    :return: True, daca numarul are toate cifrele prime sau False, in caz contrar
    '''
    while n:
        if n%10==1 or n%10==4 or n%10==6 or n%10==8 or n%10==9:
            return False
        n=n//10
    return True

def test_toateCifrelePrime():

  assert toateCifrelePrime(55) is True
  assert toateCifrelePrime(375) is True
  assert toateCifrelePrime(48) is False
  assert toateCifrelePrime(485) is False


def toateNumereleCifrePrime(l):
    '''
    determina daca toate numerele dintr-o lista au toate cifrele prime
    :param l: lista de numere intregi
    :return: True, daca toate numerele din lista au toate cifrele prime sau False, in caz contrar
    '''
    for x in l:
        if toateCifrelePrime(x)==False:
            return False
    return True
def test_toateNumereleCifrePrime():

  assert toateNumereleCifrePrime([233,3,57]) is True
  assert toateNumereleCifrePrime([233,8,57]) is False
  assert toateNumereleCifrePrime([33,57]) is True



def get_longest_prime_digits(lst):
    '''
    determina cea mai lunga subsecventa de numere formate din cifre prime
    :param l: lista de numere intregi
    :return: cea mai lunga subsecventa de numere formate din cifre prime din lista
    '''
    subsecventaMaxima=[]
    for i in range(len(lst)):
        for j in range(i,len(lst)):
            if toateNumereleCifrePrime(lst[i:j+1]) and len(lst[i:j+1]) > len(subsecventaMaxima):
                subsecventaMaxima=lst[i:j+1]
    return subsecventaMaxima

def test_get_longest_prime_digits():
    assert get_longest_prime_digits([33,5,73,24])==[33,5,73]
    assert get_longest_prime_digits([146,35,7,689,18])==[35,7]
    assert get_longest_prime_digits([46,233,56])==[233]

def is_palindrome(n):
    '''
    Determina daca un numar este palindrom
    :param: n numar intreg
    :return: True daca n este palindrom sau False, in caz contrar
    '''
    auxiliar = int(n)
    oglindit = 0
    while auxiliar > 0:
        oglindit = oglindit * 10 + auxiliar % 10
        auxiliar = auxiliar // 10
    if n == oglindit:
        return True
    else:
        return False

def test_is_palindrome():
    assert is_palindrome(167) is False
    assert is_palindrome(353) is True
    assert is_palindrome(79) is False

def toateElementelePalindroame(lst):
    """
    Determina daca toate numerele dintr-o lista sunt palindrom
    :param: lista de numere intregi
    :return: True daca toate numerele sunt palindrom sau False, in caz contrar
    """
    for x in lst:
        if is_palindrome(x) is False:
            return False
    return True

def test_toateElementelePalindroame():

    assert toateElementelePalindroame([22,343,77]) is True
    assert toateElementelePalindroame([565,88]) is True
    assert toateElementelePalindroame([21,67,77]) is False

def get_longest_all_palindromes(lst):
    """
    Determina cea mai lunga subsecventa de numere palindroame
    :param: lista de numere intregi
    :return: cea mai lunga subsecventa de numere palindrom din lista
    """
    subsecventaMaxima = []
    for i in range(len(lst)):
        for j in range(i,len(lst)):
            if toateElementelePalindroame(lst[i:j + 1]) and len(lst[i:j + 1]) > len(subsecventaMaxima):
                subsecventaMaxima = lst[i:j + 1]
    return subsecventaMaxima

def test_get_longest_all_palindromes():
    assert get_longest_all_palindromes([43, 33, 676, 5]) == [33, 676, 5]
    assert get_longest_all_palindromes([44, 389, 55, 121, 88]) == [55, 121, 88]

def semneAlternante(lst):
    '''
    determina daca toate nr din lista au semne alternante
    :param lst: lista de numere intregi
    :return: True daca lista este formata din din numere cu semne alternante sau False, in caz contrar
    '''

    ok=True
    if lst[0]<0:
        ok=False
    else:
        ok=True
    for x in lst[1:]:
        if (x<0 and ok==False) or (x>0 and ok==True):
            return False
        ok=not ok
    return True

def testSemneAlternante():

    assert semneAlternante([2,3,4]) is False
    assert semneAlternante([17,-5,91]) is True
    assert semneAlternante([-34,72,-4]) is True
    assert semneAlternante([22,16,-1]) is False


def get_longest_alternating_signs(lst):
    '''
    determina cea mai lunga subsecventa de numere cu semne alternante
    :param lst: lista de nr intregi
    :return: cea mai lunga subsecventa de numere cu semne alternante
    '''

    subsecventaMaxima = []
    for i in range(len(lst)):
        for j in range(i,len(lst)):
            if semneAlternante(lst[i:j + 1]) and len(lst[i:j + 1]) > len(subsecventaMaxima):
                subsecventaMaxima = lst[i:j + 1]
    return subsecventaMaxima

def test_get_longest_alternating_signs():
    assert get_longest_alternating_signs([2,-3,4,5])==[2,-3,4]
    assert get_longest_alternating_signs([12,48,-18,51,-9])==[48,-18,51,-9]
    assert get_longest_alternating_signs([4,-25,-6,36,-27,74])==[-6,36,-27,74]

def printMenu():
    print("1.Citire")
    print("2. Subsecventa in care toate numerele au semne alternante.")
    print("3. Subsecventa in care toate numerele sunt formate din cifre prime.")
    print("4. Subsecventa in care toate numerele sunt palindroame.")
    print("5. Iesire")

def citireListe():
    lst=[]
    n=int(input("Dati numarul de elemente din lista: "))
    for i in range(n):
        lst.append(int(input("lst["+ str(i) + "]=")))
    return lst

def main():
    test_toateCifrelePrime()
    test_toateNumereleCifrePrime()
    test_get_longest_prime_digits()
    test_is_palindrome()
    test_toateElementelePalindroame()
    test_get_longest_all_palindromes()
    testSemneAlternante()
    l=[]
    while True:
        printMenu()
        optiune = input("Dati optiunea: ")
        if optiune == "1":
            l=citireListe()
            printMenu()
            optiune=input("Alegeti optiunea: ")
            if optiune == "2":
              print(get_longest_alternating_signs(l))
            elif optiune == "3":
              print(get_longest_prime_digits(l))
            elif optiune=="4":
                print(get_longest_all_palindromes(l))
            elif optiune == "5":
                break
            else:
                print("Optiune gresita! Reincercati!")

main()