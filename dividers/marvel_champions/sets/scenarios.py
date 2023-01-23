from model import Release, Modular, Villain

the_once_and_future_kang = Release(villains=[
    Villain("Kang",
            villain_deck=[
                "Kang (The Conqueror) (I)",
                "Kang (Immortus) (II)",
                "Kang (Iron Lad) (II)",
                "Kang (Rama-Tut) (II)",
                "Kang (Scarlet Centurion) (II)",
                "Kang (The Conqueror) (III)"
            ],
            schemes=[
                "Kang's Arrival",
                "The Master of Time",
                "The Chronopolis",
                "Inexorable Fate",
                "The Realm of Rama-Tut",
                "The Present Future War",
                "Kang's Wrath"
            ],
            encounter={
                "Temporal Shield": 2,
                "Future Weapon": 2,
                "Frozen in Time": 1,
                "Macrobots": 3,
                "Weakened": 2,
                "Stolen Memories": 2,
                "Depowered": 2,
                "Time-Travel Hijinks": 2,
                "Corrupted Timestream": 1,
                "Kang's Dominion": 4,
                "Pinned Down": 1,
                "Rampage": 2,
                "Energy Blast": 2,
                "Manipulated Timestream": 1,
                "Time-Travel Tactics": 2,
                "Past Machinations": 1
            },
            extra_lists={
                "Expert Kang": [
                    "Kang (The Conqueror) (I)",
                    "Kang (Immortus) (II)",
                    "Kang (Iron Lad) (II)",
                    "Kang (Rama-Tut) (II)",
                    "Kang (Scarlet Centurion) (II)",
                    "Kang (The Conqueror) (III)"
                ]
            })],
    modulars=[
        Modular("Temporal",
                cards={
                    "Ancient Warrior": 3,
                    "Chitauri Soldier": 2,
                    "Tyrannosaurus Rex": 1,
                    "Time Portal": 1
                }),
        Modular("Anachronauts",
                cards={
                    "Apocryphus": 1,
                    "Deathunt 9000": 1,
                    "Sir Raston": 1,
                    "Terminatrix": 1,
                    "Wildrun": 1,
                    "The Anachronauts": 2,
                    "Kang's Chosen": 2
                }),
        Modular("Master of Time",
                cards={
                    "Kang (Master of Time)": 1,
                    "Time-Displaced Soldier": 2,
                    "Fear of Kang": 2,
                    "Light of Centuries Sphere": 1,
                    "Ancient Grudge": 2
                })
    ]
)