# `Hádek` - _Python Hra_

Vítejte ve **hře [Hádek](https://github.com/Benrod133/had)** od **[Benrod133](https://github.com/Benrod133/)**! _`Tato tato hra slouží pouze pro účel zábavy.`_

## Funkce

- Zábavná herní mechanika.
- Napsáno kompletně v Pythonu. **[*](#django)**  
- Snadno přizpůsobitelné a rozšiřitelné.

## Požadavky

- Python 3.8 nebo novější
- Potřebné knihovny (nainstalujte pomocí _[requirements.txt](https://github.com/Benrod133/had/blob/main/requirements.txt)_)

## Instalace

1. Naklonujte repozitář:
    ```bash
    git clone https://github.com/Benrod133/had.git
    ```
2. Přejděte do složky projektu:
    ```bash
    cd had
    ```
3. Nainstalujte knihovny:
    ```bash
    pip install -r requirements.txt
    ```

## Použití
1.  Soubory _[celkovy_cas.txt](celkovy_cas.txt)_ a _[nej_skore.txt](nej_skore.txt)_ změňte na hodnotu **0**(aktuální hodnota je již odehraná hra)  
    - _(Pomocí terminálu)_ Spusťte příkaz:
          ```bash
          echo 0 > nej_skore.txt
          echo 0 > celkovy_cas.txt
          ```
    - _(Pomocí průzkumníka souborů)_ Otevřete postupně soubory _[celkovy_cas.txt](celkovy_cas.txt)_ a _[nej_skore.txt](nej_skore.txt)_ a jejich hodnotu nastavte na
        ```txt
        0
        ```
2.  - _(Pomocí terminálu)_ Spusťte hru pomocí následujícího příkazu:
        ```bash
        python main.py
        ```
    - _(Stránka s hramy)_ spusťte django ↓
        ```bash
        cd www
        python manage.py runserver
        ```
        a poté ve vašem prohlížeči otevřete url **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**.

## Chyby
- Pokud soubor `celkovy_cas.txt` chybí nebo obsahuje neplatná data, vytvořte jej ručně ve složce projektu a zadejte výchozí hodnotu `0`. Alternativně, upravte kód tak, aby soubor automaticky vytvořil:
    ```python
    try:
        with open("celkovy_cas.txt", "r") as file:
            cas = int(file.read().strip())
    except (FileNotFoundError, ValueError):
        cas = 0
        with open("celkovy_cas.txt", "w") as file:
            file.write("0")
    ```
- Pokud chybí nějaké další soubory, upravte to stejně ;)

# Django
Tento kód je napsán kompletně v jazyce [Python](https://www.python.org) s _jedinou vijjímkou_ a to v [Djangu](https://www.djangoproject.com)
---
# _přeji příjemný požitek ze hry [Hádek](https://github.com/Benrod133/had);)_

_pokud máte nějaké další dotazy, neváhejte nám napsat na email: [alextrefny.cz@gmail.com](mailto:alextrefny.cz@mgail.com)_
