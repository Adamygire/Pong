# Vaatimusmäärittely

## Sovelluksen tarkoitus

Sovelluksen avulla käyttäjät voivat pelata shakkia. Sovellusta on mahdollista käyttää useamman rekisteröityneen käyttäjän, joilla kaikilla on oma yksilöllinen tulostaulu ja pelihistoria.

## Käyttäjät
Alkuvaiheessa sovelluksessa on ainoastaan yksi käyttäjärooli eli normaali käyttäjä. Myöhemmin sovellukseen saatetaan lisätä suuremmilla oikeuksilla varustettu pääkäyttäjä, joka voi hallita pelivaihtoehtoja ja käyttäjien tietoja.

Perusversion tarjoama toiminnallisuus

### Ennen kirjautumista

Käyttäjä voi luoda järjestelmään käyttäjätunnuksen.
Käyttäjätunnuksen täytyy olla uniikki ja pituudeltaan vähintään 3 merkkiä.
Käyttäjä voi kirjautua järjestelmään.
Kirjautuminen onnistuu syöttämällä olemassaoleva käyttäjätunnus ja salasana kirjautumislomakkeelle.
Jos käyttäjää ei ole olemassa, tai salasana ei täsmää, järjestelmä ilmoittaa tästä.

### Kirjautumisen jälkeen

Käyttäjä näkee oman tulostaulunsa, jossa näkyvät aiemmat pelitulokset ja voitot.
Käyttäjä voi aloittaa uuden pelin, jossa hän voi valita pelivastustajakseen joko tietokoneen tai toisen rekisteröityneen käyttäjän.
Pelissä käyttäjä voi valita pelitilan (esim. normaali peli tai aikarajoitteinen peli).
Pelissä on mahdollista käyttää shakin sääntöjen mukaisia toimintoja, kuten siirtää nappuloita, peruuttaa siirtoja ja tarkastella pelilautaa.
Käyttäjä voi päättää pelin ennenaikaisesti (esim. luovutus tai tasapeli).
Pelin tulos näkyy haluttaessa vain sen pelaajalle, mutta myös mahdollisuus tallentaa tulos ja jakaa se muiden kanssa.
Käyttäjä voi poistaa pelitulosmerkintänsä, jolloin tulos häviää taulusta.
Käyttäjä voi kirjautua ulos järjestelmästä.
