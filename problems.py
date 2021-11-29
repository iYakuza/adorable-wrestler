#1. Afișați în consolă rezultatul expresiei: 9 * (12-5) - 2**3
print(9 * (12-5) - 2**3)

#2. Realizați un nou program care calculează și afișează șapte la puterea a treia.
print (7**3)

#3. Se știe că Andrei are 7 mere. Ana are de 3 ori mai multe mere decât Andrei, iar Ștefan are de 49 de ori mai multe mere decât Andrei.
# Să se afle câte mere au cei trei copii în total folosindu-se o expresie care conține adunarea, înmulțirea și ridicarea la putere (+,*,**).
Andrei=7
Ana=3*Andrei
Stefan=49*Andrei
print(Andrei+Ana+Stefan)

#4. O mașină folosește o cantitate de x litri pentru a parcurge distanța Constanța-București.
# O altă mașină folosește y litri pentru aceeași distanță, știind că y=2*x.
# Să se scrie un program în care să se citească variabila x și să se determine suma necesarului de combustibil.
def cat_combustibil (x, y):
    x = input("Cat consuma masina ta?\n")
    x = int (x)
    y = x * 2
    print(f'Daca masina ta consuma {x} litri, atunci masina mea consuma {y}\n')

cat_combustibil ("x","y")

#5. Creați un convertor de timp, transformând astfel orele și minutele introduse de la tastatură în secunde.
def time_conv(h,m,s):
    h = input ("Cate ore? ")
    h = int (h)
    
    m = input ("Si cate minute? ")
    m = int (m)

    s = h*3600 + m*60
    print(f'Sigur nu ai vrut sa spui {s} secunde?\n')

time_conv("h","m","s")

#6. Să se scrie un program în care să se convertească șirul "110" într-un număr întreg și afisați tipul de dată astfel obținut.
def data_conv(str,num):
    str = "110"
    num = int (str)

    print(f'You might think that {str} is {type(str)}, when in fact it is a {type(num)}.\n "Cum am facut?"\n- Vlad Grigorescu\n')

data_conv("str","num")

#7. Într-un stup sunt 5 albine și de 2 ori mai mulți bondari.
# Fiecare albină produce 200ml de miere zilnic.
# Câți bondari sunt în stup? Dar câtă miere este produsă zilnic de cele 5 albine?
def stup(albine,bondari,miere):
    albine = 5
    albine = int (albine)
    bondari = albine * 2
    miere = albine * 200
    print(f'{albine} albine si {bondari} bondari fac orgie intr-un stup\nfetele cu tate mari, {miere} de mililitri de miere pe zi produc\n')

stup("albine","bondari","miere")

#8. La gradina zoologică sunt 5 urși panda, 2 hipopotami, 4 iepuri și 6 vulpi.
# Câte picioare au în total animalele de la gradina zoologică?
def zoo(animal, picior):
    animal = ["panda","hipo","vulpix","iepur"]
    animal[0]=5
    animal[1]=2
    animal[2]=4
    animal[3]=6
    sum = 0
    for i in animal:
        sum += i
    picior = 4 * sum
    print(f'number of legs is: {picior}')

zoo("animal","picior")

#9. La întâlnirea de 10 ani a veteranilor de război, Andy Anderson își revede cu drag colegii, alături de care a luptat pe front pentru libertatea țării.
# Andy își dă seama că cifrele numerelor de identificare, însumate, reprezintă vârsta camarazilor săi.
# Ajută-l pe Andy să afle dacă ceilalți veterani sunt mai bătrâni decât el.
def vet(vet_cod):
    vet_cod = input("What is your vet code, bruh?\n")
    vet_cod = int (vet_cod)
    str_vet_cod = str (vet_cod)
    length = len(str_vet_cod)
    if length == 7:
        vet_cod = int (vet_cod)
        str_vet_cod = str (vet_cod)
        list_1 = list(str_vet_cod.strip(" "))
        ints = [int(item) for item in list_1]
        sum = 0
        for n in ints:
            sum += n
        print(f'age is {sum}')
    while length != 7:
        vet_cod = input ("Bruh, put on your glasses and try again\n")
        vet_cod = int (vet_cod)
        str_vet_cod = str (vet_cod)
        length = len(str_vet_cod)
        if length == 7:
            vet_cod = int (vet_cod)
            str_vet_cod = str (vet_cod)
            list_1 = list(str_vet_cod.strip(" "))
            ints = [int(item) for item in list_1]
            sum = 0
            for n in ints:
                sum += n
            print(f'age is {sum}')

vet("vet_cod")

#10. O populație de bacterii se dublează la fiecare oră a zilei și se înjumătățește la fiecare oră din noapte.
# Se consideră ziua de h1 ore și noaptea de h2 ore.
# De cate ori va crește populația de bacterii după z zile? (h1,h2,z - variabile introduse de la tastatură)
def Freeman(h1,h2,z,neo):
    h1 = int(input("Cate ore are ziua?\n"))
    h2 = int(input("Cate ore are noaptea?\n"))
    z = int(input("Cate zile dupa Hristos au bacteriile?\n"))
    h3 = int(h1 + h2)
    if h3 == 24:
        neo = 1
        for j in range (z):
            for i in range (h1):
                neo *= 2
                # print(f'ora {i+1}: {neo}')
            for i in range (h2):
                neo /= 2
            #     print(f'ora {i+1}: {neo}')
            # print(f'ziua {j+1}: {neo}')
        print(f'u have {neo} bacterii')

    while h3 != 24:
        h1 = int(input("Man, pe Terra avem 24h. Cate ore are ziua?\n"))
        h2 = int(input("Man, pe Terra avem 24h. Cate ore are noaptea?\n"))
        z = int(input("Again. Cate zile dupa Hristos au bacteriile?\n"))
        h3 = int(h1 + h2)
        if h3 == 24:
            neo = 1
            for j in range (z):
                for i in range (h1):
                    neo *= 2
                    # print(f'ora {i+1}: {neo}')
                for i in range (h2):
                    neo /= 2
                #     print(f'ora {i+1}: {neo}')
                # print(f'ziua {j+1}: {neo}')
            print(f'u have {neo} bacterii')

Freeman("h1","h2","z", "neo")