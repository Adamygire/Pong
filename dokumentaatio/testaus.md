# Testausdokumentti

Peliä on testattu manuaalisin testein sekä automatisoiduin yksikkötestein `unittest`-kirjastolla.

## Yksikkö- ja integraatiotestaus

### Sovelluslogiikka

Sovelluksen keskeisiä logiikkakomponentteja ovat `Paddle`, `Ball` ja kirjautumislogiikasta vastaava `GameScreen`. Näitä testataan seuraavilla testiluokilla:

* `TestPaddle`: Testaa, että maila sijoittuu oikein ja reagoi oikeanpuoleiseen asetukseen.
* `TestBall`: Testaa, että pallo luodaan oikeaan paikkaan, ei ole pelin ulkopuolella ja liikkuu oikein.
* `TestLogin`: Testaa kirjautumistoiminnallisuutta eri tunnus- ja salasanakombinaatioilla.

Testit suoritetaan käyttäen `unittest`-moduulia, ja ne kattavat pelilogiikan tärkeimmät osat.

### Testauskattavuus

Pelin testauksen haarautumakattavuus on tällä hetkellä noin **35 %**, kattaen pääasiassa pelilogiikkaa. 

## Järjestelmätestaus

Järjestelmätestaus on suoritettu manuaalisesti.

### Toiminnallisuudet

Testauksen aikana on käyty läpi seuraavat toiminnot:

* Sovelluksen käynnistyminen ilman virheitä
* Pelaajan kirjautuminen sekä oikeilla että väärillä tunnuksilla
* Pelin käynnistyminen ja pelaaminen
* Mailojen liikuttaminen ja pallon liike
* Pelin loppuminen pallon mennessä ulos kentältä

### Syötteiden käsittely

Kirjautumistoiminnallisuudessa on testattu myös virheellisiä syötteitä, kuten tyhjiä tai vääriä arvoja.

## Laatuongelmat

Sovelluksessa havaittuja puutteita:

* Virheilmoituksia ei näytetä graafisesti, jos esim. kirjautuminen epäonnistuu.
* Virheenkäsittelyä ei ole kaikissa tilanteissa, kuten graafisen käyttöliittymän tai pelin aikana tapahtuvissa poikkeuksissa.
