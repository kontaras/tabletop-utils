from enum import Enum, auto
from collections.abc import Iterable


class SubList:
    def __init__(self, name: str, cards: dict[str, int]):
        self.name = name
        self.cards = cards


class Divider:
    def __init__(self, name: str, cards: dict[str, int],
                 sublists: list[SubList] = []):
        self.name = name
        self.cards = cards
        self.sublists = sublists


class Hero:
    def __init__(self, name: str, signature: dict[str, int],
                 nemesis: dict[str, int], obligation: dict[str, int]):
        self.name = name
        self.signature = signature
        self.nemesis = nemesis
        self.obligation = obligation

    def get_dividers(self) -> list[Divider]:
        nemesis_set = SubList("Nemesis set", self.nemesis)
        obligation_set = SubList("Obligation", self.obligation)
        return [Divider(self.name, self.signature, [nemesis_set, obligation_set])]


class Aspect(Enum):
    AGGRESSION = auto()
    LEADERSHIP = auto()
    PROTECTION = auto()
    JUSTICE = auto()
    MULTICOLOR = auto()


class AspectDeck:
    def __init__(self, name: str, aspect: list[Aspect], cards: dict[str, int]):
        self.name = name
        self.aspect = aspect
        self.cards = cards

    def get_dividers(self) -> list[Divider]:
        title = f'{self.name} ({"/".join(self.aspect_names())})'
        return [Divider(title, self.cards)]

    def aspect_names(self) -> Iterable[str]:
        return map(lambda a: a.name.capitalize(), self.aspect)


class Villain:
    def __init__(self, name: str, villain_deck: list[str], schemes: list[str],
                 encounter: dict[str, int],
                 extra_lists: dict[str, list[str]] = {}):
        self.name = name
        self.villain_deck = villain_deck
        self.schemes = schemes
        self.encounter = encounter
        self.extra_lists = extra_lists

    def get_dividers(self) -> list[Divider]:
        sub_lists = [SubList("Main scheme deck",
                            dict.fromkeys(self.schemes, 1))]
        for name, cards in self.extra_lists.items():
            sub_lists.append(SubList(name, dict.fromkeys(cards, 1) ))
        main_divider = Divider(self.name, dict.fromkeys(self.villain_deck, 1),
                               sub_lists)
        encounter_divider = Divider(self.name + ' encounter set', self.encounter)
        return [main_divider, encounter_divider]

class Modular:
    def __init__(self, name: str, cards: dict[str, int]):
        self.name = name
        self.cards = cards

    def get_dividers(self) -> list[Divider]:
        return [Divider("Modular Encounter: " + self.name, self.cards)]

class Campaign:
    def __init__(self, name: str, cards: dict[str, int]):
        self.name = name
        self.cards = cards

    def get_dividers(self) -> list[Divider]:
        return [Divider(f'Campaign Deck: {self.name}', self.cards)]

class Release:
    def __init__(self, heroes: list[Hero] = [], aspects: list[AspectDeck] = [],
                 villains: list[Villain] = [], modulars: list[Modular] = [],
                 campaigns: list[Campaign] = [], extras: dict[str, int] = {}):
        self.heroes = heroes
        self.aspects = aspects
        self.villains = villains
        self.modulars = modulars
        self.campaigns = campaigns
        self.extras = extras

    def get_heroes(self) -> list[Hero]:
        return self.heroes

    def get_aspects(self) -> list[AspectDeck]:
        return self.aspects

    def get_villains(self) -> list[Villain]:
        return self.villains

    def get_modulars(self) -> list[Modular]:
        return self.modulars

    def get_campaigns(self) -> list[Campaign]:
        return self.campaigns

    def get_extras(self) -> dict[str, int]:
        return self.extras
