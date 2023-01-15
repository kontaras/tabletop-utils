from model import Release, Hero, Aspect, AspectDeck, Villain, Modular, Campaign

sinister_motives = Release(
    heroes=[Hero("Ghost-Spider/Gwen Stacy",
                 signature= {
                     "Ghost Kick": 3,
                     "Parental Guidance": 1,
                     "Phantom Flip":3,
                     "Pirouette and Punch": 2,
                     "Web Binding": 2,
                     "George Stacy": 1,
                     "Ticket to the Multiverse" : 1,
                     "Web-Bracelet": 2
                 },
                 nemesis= {
                     "Regenerative Research": 1,
                     "The Lizard" : 1,
                     "Experimental Injection": 1,
                     "In Cold Blood": 2
                 },
                 obligation={"Worried Father": 1}),
            Hero("Spider-Man/Miles Morales",
                 signature={
                     "Arachnobatics": 2,
                     "Double Life": 2,
                     "Swing In": 2,
                     "Web-Shot": 3,
                     "Ganke Lee": 1,
                     "Jefferson Davis": 1,
                     "Power Within": 1,
                     "Defense Mechanism": 1,
                     "Web-Shooter": 2
                 },
                 nemesis={
                     "Tracking Prey": 1,
                     "Prowler": 1,
                     "Razor Claws": 1,
                     "Slice and Dice": 2
                 },
                 obligation={"Keeping Secrets": 1}
                 )],
    aspects=[AspectDeck("Ghost-Spider/Gwen Stacy",
                        aspect=[Aspect.PROTECTION],
                        cards={
                            # Protection cards
                            "Silk": 1,
                            "Spider-Man (Miles Morales)": 1,
                            "Spider-UK": 1,
                            "Bait and Switch": 3,
                            "Jump Flip": 3,
                            "Return the Favor": 3,
                            "What Doesn't Kill Me": 3,
                            # Basic cards
                            "Spider-Man (Hobie Brown)": 1,
                            "Across the Spider-Verse": 1,
                            "Young Love": 1,
                            "Energy": 1,
                            "Genius": 1,
                            "Strength": 1,
                            "Web of Life and Destiny": 1,
                            "Plan B": 3
                        }),
             AspectDeck("Spider-Man/Miles Morales",
                        aspect=[Aspect.JUSTICE],
                        cards={
                            # Justice
                            "Monica Chang": 1,
                            "Spider-Woman": 1,
                            "Homeland Intervention": 3,
                            "Global Logistics": 3,
                            "Field Agent": 3,
                            "Surveillance Team": 2,
                            # Basic Cards
                            "Agent 13": 1,
                            "Dum Dum Dugan": 1,
                            "Ghost-Spider": 1,
                            "Spider-Man (Peter Parker)": 1,
                            "Young Love": 1,
                            "Energy": 1,
                            "Genius": 1,
                            "Strength": 1,
                            "Government Liaison": 3,
                            "Sky-Destroyer": 1
                        }
                        )],
    villains=[Villain("Sandman",
                      villain_deck=[
                          "Sandman (I)",
                          "Sandman (II)",
                          "Sandman (III)"
                      ],
                      schemes=["Hapless Pedestrians"],
                      encounter={
                          "City Streets": 1,
                          "Sand Form": 2,
                          "Sand Clone":  4,
                          "Dirt Trap": 2,
                          "Tidal Sands": 1,
                          "Sandslide": 1,
                          "Sand Storm": 1,
                          "Sand Smash": 2
                      }),
              Villain("Venom",
                      villain_deck=[
                          "Venom (I)",
                          "Venom (II)",
                          "Venom (III)"
                      ],
                      schemes=['"Leave Us Alone!"'],
                      encounter={
                          "Bell Tower": 1,
                          "\"Now We're Angry!\"": 1,
                          "Guard to the Bell Tower": 1,
                          "Lashing Out": 1,
                          "Tooth and Nail": 1,
                          "Biting Retort": 2,
                          "For Whom the Bell Tolls": 2
                      }),
              Villain("Mysterio",
                      villain_deck=[
                          "Mysterio (I)",
                          "Mysterio (II)",
                          "Mysterio (III)"
                      ],
                      schemes=[
                          "Maze of Mirrors",
                          "Edge of Reality"
                      ],
                      encounter={
                          "Humongous Hallucination": 1,
                          "Masterful Mirage": 2,
                          "Shifting Apparition": 4,
                          "Déjà Vu": 2,
                          "Fearmonger": 2
                      }),
              Villain("The Sinister Six",
                      villain_deck=[
                          "Doctor Octopus",
                          "Electro",
                          "Hobgoblin",
                          "Kraven the Hunter",
                          "Scorpion",
                          "Vulture"
                      ],
                      schemes=[
                          "Sinister Synchronization",
                          "Sinister Beatdown"
                      ],
                      encounter={
                          "Light at the End": 1,
                          "Heightened Morale": 2,
                          "Taunting Presence": 2,
                          "Team Leader": 1,
                          "Take One for the Team": 1,
                          "Brute Force Barricade": 1,
                          "Frequent Flyers": 1,
                          "High Fashion": 1,
                          "Robotic Enhancements": 1,
                          "Partnership of Pain": 3,
                          "Surprise!": 3
                      }),
              Villain("Venom Goblin",
                      villain_deck=[
                          "Venom Goblin (I)",
                          "Venom Goblin (II)",
                          "Venom Goblin (III)"
                      ],
                      schemes=[
                          "Skies Over New York",
                          "Lower Manhattan",
                          "Midtown Manhattan",
                          "Upper Manhattan"
                      ],
                      encounter={
                          "We Are One": 1,
                          "Symbiotic Berserker": 2,
                          "Symbiotic Monstrosity": 1,
                          "Symbiotic Thrall": 4,
                          "Festering Mass": 1,
                          "Joy Ride": 1,
                          "Spreading Panic": 2
                      })],
    modulars=[Modular("City in Chaos",
                      cards={
                          "Panic in the Streets": 1,
                          "Rhino": 1,
                          "Calling in Favors": 1,
                          "Now or Never": 2
                      }),
              Modular("Down to Earth",
                      cards={
                          "Common Criminal": 3,
                          "Friends and Family": 1,
                          "Volunteer Work": 1,
                          "\"Threat or Menace?\"": 1,
                          "Loose Ends": 1
                      }),
              Modular("Goblin Gear",
                      cards={
                          "Advanced Glider": 1,
                          "Concussive Bombs": 1,
                          "Incendiary Bombs": 1,
                          "Smoke Bombs": 1,
                          "Limitless Supply": 1,
                          "Remote Navigation": 1
                      }),
              Modular("Guerrilla Tactics",
                      cards={
                          "Life-Size Decoy": 2,
                          "Coordinated Effort": 1,
                          "Hidden in Shadow": 1,
                          "Teamwork Makes the Dream Work": 1,
                          "From Every Direction": 2
                      }),
              Modular("Osborn Tech",
                      cards={
                          "Arm Cannon": 1,
                          "Ionic Boots": 1,
                          "Kinetic Armor": 1,
                          "Neocarbon Scales": 1,
                          "Spiked Gauntlet": 1,
                          "Tracking Display": 1
                      }),
              Modular("Personal Nightmare",
                      cards={
                          "Induced Panic": 1,
                          "Evil Doppelgänger": 2,
                          "Fool's Paradise": 1,
                          "Weakness from Within": 1,
                          "Deepest Fears": 2
                      }),
              Modular("Sinister Assault",
                      cards= {
                          "Doctor Octopus": 1,
                          "Electro": 1,
                          "Hobgoblin": 1,
                          "Kraven the Hunter": 1,
                          "Scorpion": 1,
                          "Vulture": 1
                      }),
              Modular("Symbiotic Strength",
                      cards={
                          "Improvised Weapons": 1,
                          "Violent Tendencies": 1,
                          "Webbed Up": 1,
                          "Enraged Symbiote": 3,
                          "Swinging Assault": 2,
                          "Unstable Sentience": 1
                      }),
              Modular("Whispers of Paranoia",
                      cards={
                          "Delusion of Collusion": 2,
                          "Manipulated Mind": 1,
                          "Old Grudge": 1,
                          "Analysis Paralysis": 1
                      })],
    campaigns=[Campaign("S.H.I.E.L.D. Tech",
                        cards={"Compact Darts": 1,
                               "Impact-Dampening Suit": 1,
                               "Laser Goggles": 1,
                               "Propulsion Gauntlet": 1,
                               "Retinal Display": 1,
                               "Shock Knuckles": 1,
                               "Wave Bracers": 1,
                               "Wrist Navigator": 1
                           }),
               Campaign("Venom",
                        cards={
                            "Snitches Get Stitches": 1,
                            "Venom Eddie Brock": 1,
                            "Symbiote Suit": 4
                        }),
               Campaign("Bad Publicity",
                        cards={
                            "Public Outcry": 1,
                            "Smear Campaign": 1
                        }),
               Campaign("Community Service",
                        cards={
                            "Back Alley Burglary": 1,
                            "Cat In a Tree": 1,
                            "Henchmen Heist": 1,
                            "Off the Rails": 1,
                            "Rubble Rescue": 1
                        }),
               Campaign("S.H.I.E.L.D. Tech",
                        cards={
                            "Compact Darts": 1,
                            "Impact-Dampening Suit": 1,
                            "Laser Goggles": 1,
                            "Propulsion Gauntlet": 1,
                            "Retinal Display": 1,
                            "Shock Knuckles": 1,
                            "Wave Bracers": 1,
                            "Wrist Navigator": 1
                        })]
)