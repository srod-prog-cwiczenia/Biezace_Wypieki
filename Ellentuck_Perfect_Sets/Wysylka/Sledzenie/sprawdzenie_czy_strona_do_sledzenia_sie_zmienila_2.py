
#!/usr/bin/env python3

import hashlib
import urllib.request
import sys


PLIK = "strona.txt"


def hash_strony(url):
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0"}
    )

    with urllib.request.urlopen(req, timeout=30) as response:
        zawartosc = response.read()
        adres = response.geturl()

    return adres, len(zawartosc), hashlib.sha256(zawartosc).hexdigest()


def main():
    try:
        with open(PLIK, "r", encoding="utf-8") as plik:
            linie = [linia.strip() for linia in plik if linia.strip()]

        if len(linie) != 2:
            raise ValueError(
                "Plik strona.txt musi zawierać URL i hash, po jednej wartości w linii."
            )

        url, hash_wzorcowy = linie

        adres, rozmiar, wynik = hash_strony(url)

        print("Adres:", adres)
        print("Rozmiar:", rozmiar, "bajtów")
        print("SHA-256:", wynik)

        if wynik.lower() != hash_wzorcowy.lower():
            print("ALERT! Coś się na stronie ZMIENIŁO!")
        else:
            print("Na stronie bez zmian.")

    except Exception as e:
        print("Błąd:", e)
        sys.exit(1)


if __name__ == "__main__":
    main()

