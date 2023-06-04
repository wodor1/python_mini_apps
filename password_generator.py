import random
import string

def jelszo_generator(hossz, szamok, specialis_karakterek):
    karakterek = string.ascii_letters 
    if szamok:
        karakterek += string.digits
    if specialis_karakterek:
        karakterek += string.punctuation
    return ''.join(random.choice(karakterek) for i in range(hossz))

def main():
    hossz = int(input('Milyen hosszú legyen a jelszó összesen (hány karakter)? '))
    szamok = input('Legyenek e benne számok (igen/nem)? ').lower() == 'igen'
    specialis_karakterek = input('Legyenek e benne speciális karakterek (igen/nem)? ').lower() == 'igen'

    jelszo = jelszo_generator(hossz, szamok, specialis_karakterek)
    print('A generált jelszó: ', jelszo)

if __name__ == "__main__":
    main()
