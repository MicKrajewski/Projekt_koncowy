from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from multiselectfield import MultiSelectField

REPU = (
    (1, "*"),
    (2, "**"),
    (3, "***"),
    (4, "****"),
    (5, "*****"),
)

MON = (
    (1, "bida aż piszczy"),
    (2, "jest na wodę"),
    (3, "woda + buty"),
    (4, "bogaty wujek"),
    (5, "jak u Abramowicza"),
)

NOGA = (
    (1, "lewa"),
    (2, "prawa"),
    (3, "obie"),
    (4, "obie ch***we"),
)

POSI = (
    (1, "Bramkarz"),
    (2, "Prawy obrońca"),
    (3, "Środkowy obrońca"),
    (4, "Lewy obrońca"),
    (5, "Prawy wahadłowy"),
    (6, "Lewy wahadłowy"),
    (7, "Defensywny pomocnik"),
    (8, "Prawy pomocnik"),
    (9, "Środkowy pomocnik"),
    (10, "Lewy pomocnik"),
    (11, "Wysunięty rozgrywający"),
    (12, "Napastnik"),
)

HAJ = (
    (1, "gra z wątroby"),
    (2, "nie gubi chleba"),
    (3, "truskawka na torcie"),
    (4, "ma automatyzmy"),
    (5, "jest turbo"),
    (6, "gra z kija"),
    (7, "ma detale"),
    (8, "gra piłkę życzliwą"),
    (9, "widać, że mu się chce"),
)

BK = (
    (1, "setka w 3 sekundy"),
    (2, "Karyna na trybunach"),
    (3, "brzuch piwny"),
    (4, "mądrzejszy od trenera"),
    (5, "modne włosy"),
    (6, "boiskowy brutal"),
    (7, "szybko się gotuje"),
    (8, "nieodporny na szyderę z trybun"),
)


class Club(models.Model):
    name = models.CharField(max_length=64, verbose_name="Nazwa")
    city = models.CharField(max_length=64, verbose_name="Miasto")
    league = models.CharField(max_length=64, verbose_name="Liga")
    year = models.IntegerField(validators=[MinValueValidator(1800), MaxValueValidator(2018)], verbose_name="Rok założenia")
    reputation = models.IntegerField(choices=REPU, verbose_name="Reputacja")
    money = models.IntegerField(choices=MON, verbose_name="Stan finansów")
    arena_name = models.CharField(max_length=64, verbose_name="Nazwa stadionu")
    arena_capacity = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100000)],
                                         verbose_name="Pojemność stadionu")
    # player = models.ManyToManyField(Player, verbose_name="Lista piłkarzy", default=0)


class Player(models.Model):
    clubs = models.ForeignKey(Club, on_delete=models.CASCADE, verbose_name="Klub")
    first_name = models.CharField(max_length=64, verbose_name="Imię")
    last_name = models.CharField(max_length=64, verbose_name="Naziwsko")
    pseudo = models.CharField(max_length=64, verbose_name="Pseudonim")
    age = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(100)],
                                         verbose_name="Wiek")
    weight = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(200)],
                                         verbose_name="Waga")
    height = models.IntegerField(validators=[MinValueValidator(100), MaxValueValidator(250)],
                                 verbose_name="Wzrost")
    nationality = models.CharField(max_length=64, verbose_name="Narodowość")
    paid =  models.CharField(max_length=34, verbose_name="Wartość")
    ca = models.IntegerField(choices=REPU, verbose_name="Obecne umiejętności")
    pa = models.IntegerField(choices=REPU, verbose_name="Potencjalne umiejętnośći")
    leg = models.IntegerField(choices=NOGA, verbose_name="Preferowana noga")
    position = MultiSelectField(choices=POSI, verbose_name="Pozycje")
    dos = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)],
                                         verbose_name="Dośrodkowania")
    dryb = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)],
                              verbose_name="Drybling")
    glow = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)],
                              verbose_name="Gra głową")
    kry = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)],
                              verbose_name="Krycie")
    odb = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)],
                              verbose_name="Odbiór piłki")
    pod = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)],
                              verbose_name="Podania")
    przy = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)],
                              verbose_name="Przyjęcie")
    rzk = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)],
                              verbose_name="rzuty karne")
    rzr = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)],
                              verbose_name="Rzuty rożne")
    rzw = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)],
                              verbose_name="Rzuty wolne")
    tech = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)],
                              verbose_name="Technika")
    wyk = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)],
                              verbose_name="Wykańczanie akcji")
    agre = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)],
                              verbose_name="Agresja")
    dec = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)],
                              verbose_name="Decyzje")
    det = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)],
                              verbose_name="Determinacja")
    konc = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)],
                              verbose_name="Koncentracja")
    opa = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)],
                              verbose_name="Opanowanie")
    prac = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)],
                              verbose_name="Pracowitość")
    prze = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)],
                              verbose_name="Przewidywanie")
    przyw = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)],
                              verbose_name="Przywodztwo")
    wale = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)],
                              verbose_name="Waleczność")
    wsp = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)],
                              verbose_name="Współpraca")
    przys = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)],
                              verbose_name="Przyspieszenie")
    row = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)],
                              verbose_name="Równowaga")
    sil = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)],
                              verbose_name="Siła")
    sko = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)],
                              verbose_name="Skoczność")
    spr = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)],
                              verbose_name="Sprawność")
    szybk = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)],
                              verbose_name="Szybkość")
    wytrz = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)],
                              verbose_name="Wytrzymałość")
    zwinn = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)],
                              verbose_name="zwinność")
    chwy = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)],
                              verbose_name="Chwytanie")
    eksc = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)],
                              verbose_name="Ekscentryczność")
    gnp = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)],
                              verbose_name="Gra na przedpolu")
    jnj = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)],
                              verbose_name="Jeden na jednego")
    komu = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)],
                              verbose_name="Komunikacja")
    refl = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)],
                              verbose_name="Refleks")
    sdp = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)],
                              verbose_name="Skłonność do piąstkowania")
    wdp = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)],
                              verbose_name="Wyjścia do piłki")
    wyko = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)],
                              verbose_name="Wykopy")
    wyrz = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)],
                              verbose_name="Wyrzuty")
    zawys = models.IntegerField(validators=[MinValueValidator(0), MaxValueValidator(20)],
                              verbose_name="Zasięg wyskoku")
    hajto = MultiSelectField(choices=HAJ, verbose_name="cechy by Hajto")
    bclas = MultiSelectField(choices=BK, verbose_name="cechy B-klasowe")
    description = models.TextField(verbose_name="Dodatkowy opis")


    @property
    def name(self):
        return "{} {}".format(self.first_name, self.last_name)

    def __str__(self):
        return self.name

    @property
    def hajto_list(self):
        list = []
        for element in self.hajto:
            list.append(self.hajto_value(int(element)))
        return list

    def hajto_value(self, id):
        for element in HAJ:
            if element[0] == id:
                return element[1]
        return None

    @property
    def bclas_list(self):
        list = []
        for element in self.bclas:
            list.append(self.bclas_value(int(element)))
        return list

    def bclas_value(self, id):
        for element in BK:
            if element[0] == id:
                return element[1]
        return None


class Shortlist(models.Model):
    shortlist_name = models.CharField(max_length=64, verbose_name="Nazwa shortlisty")
    players = models.ManyToManyField(Player, verbose_name="Lista piłkarzy", default=0)
