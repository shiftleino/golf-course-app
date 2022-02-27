# Tietokantasovellus - Helsingin yliopisto
Tämä repositorio sisältää <I>Tietokantasovellus</I>-kurssin harjoitustyön. This repository contains the course project for the course Tietokantasovellus at University of Helsinki. The description is in Finnish (below). You can test the app here: https://golf-course-app.herokuapp.com.

## Golf Course App
Sovelluksen avulla voi tarkastella Uudenmaan golf-kenttiä. Käyttäjä voi sovelluksessa katsoa kenttiä Uudenmaan kartalta, tarkastella kenttien tietoja ja lähettää arvioita kentistä. Kaikki sovelluksen toiminnallisuudet on listattu Toiminnallisuudet-osioon. Sovellus on web-sovellus ja se on toteutettu Pythonin Flask-kirjastolla. Voit kokeilla sovellusta osoitteessa: https://golf-course-app.herokuapp.com.

### Toiminnallisuudet
Sovelluksessa on kaksi eri käyttäjäroolia: käyttäjä ja ylläpitäjä.<br>
Käyttäjä voi:
- Tarkastella yksittäisen golf-kentän tietoja
    - Etäisyys Helsingin keskustasta ja matkan pituus autolla
    - Kentän hinnasto
    - Kuinka monta reikää kentällä on
    - Linkki kentän nettisivuille.
- Tarkastella kenttiä yhdestä listasta etäisyyden tai hinnaston mukaisessa järjestyksessä.
- Antaa arvion yksittäisestä kentästä
- Tarkastella muiden käyttäjien antamia arvioita

Ylläpitäjä voi käyttäjän toiminnallisuuksien lisäksi:
- Lisätä ja poistaa golf-kenttiä
- Muuttaa golf-kenttien tietoja
- Poistaa käyttäjien antamia arvioita.

### Toiminnallisuuksien testaus
Nykyisiä toiminnallisuuksia voi testata herokussa luomalla käyttäjän ja kirjautumalla sisään. Käyttäjä voi tämän jälkeen selata Uudenmaan golf-kenttiä taulukosta etäisyyden ja hinnan mukaisessa järjestyksessä, sekä klikkaamalla kenttien nimien sisältämiä linkkejä tarkastella yksittäisen kentän tietoja ja hinnastoa. Yksittäisen kentän sivulta käyttäjä pääsee myös katsomaan muiden käyttäjien antamia arvioita ja lisäämään oman arvionsa muiden nähtäville. Ylläpitäjän toiminnallisuuksia voi kurssin arvioinnissa testata käyttämällä seuraavia tunnuksia: admin, nimda1234. Älä kuitenkaan poista jo lisättyjä oikeita kenttiä.

### Tietojen muoto
Sovelluksessa etäisyys Helsingin keskustasta on ilmoitettu kokonaislukuna. Matka-aika Helsingistä on nopein matka-aika autolla ilmoitettuna minuuteissa ja niin ikään kokonaislukuna. Taulukossa näytetään "Green fee" nimellä tallennettu hinta.

### Työkalut
- Python
- Flask
- PostgreSQL
- Heroku
