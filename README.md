# Pong

Tämä on pong peli eli digitaalinen pöytä tennis.

## Python-versiosta

Peli toimii Python-versiolla `3.13`.

## Dokumentaatio

- [Käyttöohje](./dokumentaatio/kayttoohje.md)
- [Vaatimusmäärittely](./dokumentaatio/vaatimusmaarittely.md)
- [Arkkitehtuurikuvaus](./dokumentaatio/arkkitehtuuri.md)
- [Testausdokumentti](./dokumentaatio/testaus.md)
- [Työaikakirjanpito](./dokumentaatio/tuntikirjanpito.md)
- [Changelog](./dokumentaatio/changelog.md)

## Asennus

* Asenna pelin riippuvuudet komennolla:

```bash
poetry install
```

* Käynnistä peli komennolla:

```bash
poetry run invoke start
```

## Komentorivitoiminnot

### Ohjelman suorittaminen

Pelin voi käynnistää komennolla:

```bash
poetry run invoke start
```

### Testaus

Testit ajetaan komennolla:

```bash
poetry run invoke test
```

### Testikattavuus

Testikattavuusraportin voi luoda komennolla:

```bash
poetry run invoke coverage-report
```

Raportti luodaan _htmlcov_-hakemistoon.

### Pylint

Tiedoston [.pylintrc](./.pylintrc) määrittelee tarkistukset ja ne voidaan suorittaa komennolla:

```bash
poetry run invoke lint
```