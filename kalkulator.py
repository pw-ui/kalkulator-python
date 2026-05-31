#!/usr/bin/env python3
#Prosty kalkulator konsolowy.
#Cztery podstawowe działania: + - * /
#Działa w pętli aż użytkownik wpisze 'q'.

def dodaj(a, b):
    return a + b

def odejmij(a, b):
    return a - b

def pomnoz(a, b):
    return a * b

def podziel(a, b):
    if b == 0:
        raise ZeroDivisionError("Nie można dzielić przez zero.")
    return a / b

def pobierz_liczbe(komunikat):
    while True:
        tekst = input(komunikat).replace(",", ".")
        try:
            return float(tekst)
        except ValueError:
            print("To nie jest poprawna liczba. Spróbuj jeszcze raz.")

def main():
    operacje = {
        "+": dodaj,
        "-": odejmij,
        "*": pomnoz,
        "/": podziel,
    }

    print("KALKULATOR")
    print("Dostępne operacje: + - * /")
    print("Wpisz 'q', aby zakończyć.\n")

    while True:
        op = input("Wybierz rodzaj operacji (+ - * / lub q): ").strip()
        if op == "q":
            print("Adios!")
            break
        if op not in operacje:
            print("Nieznana operacja. Spróbuj jeszcze raz.\n")
            continue

        a = pobierz_liczbe("Podaj pierwszą liczbę: ")
        b = pobierz_liczbe("Podaj drugą liczbę: ")

        try:
            wynik = operacje[op](a, b)
            print(f"Wynik: {a} {op} {b} = {wynik}\n")
        except ZeroDivisionError as e:
            print(f"Błąd: {e}\n")


if __name__ == "__main__":
    main()
