from model import Hero, Release, Aspect, AspectDeck

scarlet_witch = Release(
    heroes= [Hero("Scarlet Witch/Wanda Maximoff",
                  signature={
                      "Quicksilver (Pietro Maximoff)": 1,
                      "Chaos Magic": 1,
                      "Hex Bolt": 4,
                      "Molecular Decay": 3,
                      "Warp Reality": 1,
                      "Agatha Harkness": 1,
                      "Magic Shield": 3,
                      "Scarlet Witch's Crest": 1
                  },
                  nemesis={
                      "The Next Evolution": 1,
                      "Luminous": 1,
                      "Magical Suspension": 1,
                      "Chaos Manipulation": 1
                  },
                  obligation={"Slipping Sanity": 2})],
    aspects=[AspectDeck("Scarlet Witch/Wanda Maximoff",
                        aspect=[Aspect.JUSTICE],
                        cards={
                            # Justice
                            "Speed (Thomas Shepherd)": 1,
                            "Wiccan (William Kaplan)": 1,
                            "Crisis Averted": 3,
                            "Multitasking": 3,
                            "Swift Retribution": 3,
                            "Turn the Tide": 3,
                            "The Power of Justice": 2,
                            "Heroic Intuition": 2,
                            # Basic
                            "Order and Chaos": 1,
                            "Spiritual Meditation": 3,
                            "Energy": 1,
                            "Genius": 1,
                            "Strength": 1
                        })],
    extras={
        "Browbeat": 3,
        "Last Stand": 3,
        "Bait and Switch": 3,
        "Recuperation": 3
    }
)

gamora = Release(
    heroes=[Hero("Gamora",
                 signature={
                     "Nebula": 1,
                     "Acrobatic Move": 2,
                     "Crosscounter": 2,
                     "Set the Pace": 2,
                     "Decisive Blow": 2,
                     "Forward Momentum": 2,
                     "Conditioning Room": 1,
                     "Keen Instincts": 2,
                     "Gamora's Sword": 1
                 },
                 nemesis={
                     "Sibling Rivalry": 1,
                     "Nebula": 1,
                     "In a Bind": 1,
                     "Waylay": 2
                 },
                 obligation={"Unfulfilled Destiny": 1})],
    aspects=[AspectDeck("Gamora",
                        aspect=[
                            Aspect.AGGRESSION,
                            Aspect.MULTICOLOR
                        ],
                        cards={
                            # Aggression+ cards
                            "Angela (Aldrif Odinsdottir)": 1,
                            "Clobber": 3,
                            "Plan of Attack": 3,
                            "Uppercut": 2,
                            "First Hit": 3,
                            "Impede": 3,
                            "Combat Training": 2,
                            "Godslayer": 1,
                            # Basic Cards
                            "Drax": 1,
                            "Hit and Run": 3,
                            "Energy": 1,
                            "Genius": 1,
                            "Strength": 1
                        })],
    extras={
        "Pivotal Moment": 3,
        "Comms Implant": 3,
        "True Grit": 3,
        "Enhanced Reflexes": 3
    }
)