#!/usr/bin/env python3

import sys
import hashlib
import urllib.request


def hash_strony(url):
    req = urllib.request.Request(
        url,
        headers={"User-Agent": "Mozilla/5.0"}
    )

    with urllib.request.urlopen(req, timeout=30) as response:
        zawartosc = response.read()
        adres = response.geturl()

    wynik = hashlib.sha256(zawartosc).hexdigest()

    print("Adres:", adres)
    print("Rozmiar:", len(zawartosc), "bajtów")
    print("SHA-256:", wynik)
    if wynik != "08643e1bbb7d7ce696ebd4e73e31bfeae2af4b733f4422a26f1a21e6acf0640b":
        print ("ALERT! Cos sie na stronie ZMIENILO!!!")
    else:
        print ("Na stronie bez zmian.")
if __name__ == "__main__":
#    if len(sys.argv) != 2:
#        print(f"Użycie: python3 {sys.argv[0]} URL")
#        sys.exit(1)

    try:
#        hash_strony(sys.argv[1])
        hash_strony("https://track.authorhub.elsevier.com?uuid=bc6a8076-8994-48f7-9a13-91c6503eb810")
    except Exception as e:
        print("Błąd:", e)
        sys.exit(1)
