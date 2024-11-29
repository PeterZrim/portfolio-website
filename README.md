# Pete-Tech Portfolio Website

## Naslednji koraki za večjezično podporo

1. Namestitev gettext orodja:
   - Prenesite gettext z: https://mlocati.github.io/articles/gettext-iconv-windows.html
   - Namestite preneseno datoteko
   - Ponovno zaženite računalnik

2. Po ponovnem zagonu:
   - Odprite Command Prompt ali PowerShell
   - Preverite, če je gettext nameščen z ukazom: `msgfmt --version`
   - Če ukaz deluje, nadaljujte s 3. korakom
   - Če ukaz ne deluje, preverite če je gettext v sistemski poti (Path)

3. Ustvarjanje prevodnih datotek:
   ```bash
   cd C:/Users/Peter/CascadeProjects/portfolio_website
   python manage.py makemessages -l de
   python manage.py makemessages -l sl
   ```

4. Po ustvarjanju prevodnih datotek me kontaktirajte za pomoč pri prevajanju.

## Projekt vsebuje:
- Večjezična podpora (EN, DE, SL)
- Vremenska napoved
- Prikaz kriptovalut
- Galerija
- Blog
- Kontaktni obrazec

## Tehnologije:
- Python 3.11
- Django 4.2.7
- Bootstrap 5
- OpenWeather API
- CoinGecko API
