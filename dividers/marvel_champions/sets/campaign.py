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
                        })]
)

mutant_genesis = Release(
    heroes=[Hero("Colossus/Piotr Rasputin",
                 signature= {
                     "Shadowcat (Kitty Pryde)": 1,
                     "Piotr’s Studio": 1,
                     "Iron Will": 1,
                     "Titanium Muscles": 1,
                     "Organic Steel": 2,
                     "Made of Rage": 2,
                     "Steel Fist": 3,
                     "Bulletproof Protector": 2,
                     "Armor Up": 2
                 },
                 nemesis= {
                     "Juggernaut": 1,
                     "Rampaging Juggernaut": 1,
                     "Unstoppable": 2,
                     "Slammed": 1
                 },
                 obligation={"Homesick": 1}
                 ),
            Hero("Shadowcat/Kitty Pride",
                 signature= {
                     "Solid / Phased": 1,
                     "Lockheed": 1,
                     "Kitty’s Room": 1,
                     "Acute Control": 1,
                     "Intangible Interference": 1,
                     "Phased and Confused": 2,
                     "Shadowcat Surprise": 3,
                     "Phased Strike": 2,
                     "Airwalk": 2,
                     "Quick Shift": 2
                 },
                 nemesis= {
                     "White Queen": 1,
                     "The Hellfire Club": 1,
                     "Hellfire Pawn": 2,
                     "Telepathic Restraint": 1
                 },
                 obligation= {"Permanently Phased": 1}
                 )],
    aspects=[AspectDeck("Colossus/Piotr Rasputin",
                        aspect=[Aspect.PROTECTION],
                        cards= {
                            # Protection cards
                            "Nightcrawler (Kurt Wagner)": 1,
                            "Polaris (Lorna Dane)": 1,
                            "Protective Training": 3,
                            "Powerful Punch": 3,
                            "Bait and Switch": 3,
                            "Perseverance": 3,
                            "Mutant Protectors": 3,
                            "Defensive Energy": 2,
                            # Basic cards
                            "Professor X (Charles Xavier)": 1,
                            "The X-Jet": 1,
                            "Shadow and Steel": 1,
                            "Energy": 1,
                            "Genius": 1,
                            "Strength": 1
                        }
                        ),
             AspectDeck("Shadowcat/Kitty Pride",
                        aspect=[Aspect.AGGRESSION],
                        cards= {
                            # Aggression cards
                            "Wolverine (Logan)": 1,
                            "Magik (Illyana Rasputin)": 1,
                            "Attack Training": 3,
                            "Gatekeeper": 3,
                            "Team Strike": 3,
                            "Toe to Toe": 3,
                            "Aggressive Energy": 2,
                            # Basic cards
                            "Colossus (Piotr Rasputin)": 1,
                            "X-Mansion": 1,
                            "Shadow and Steel": 1,
                            "Ready to Rumble": 3,
                            "Energy": 1,
                            "Genius": 1,
                            "Strength": 1
                        })],
    villains= [Villain("Sabretooth",
                       villain_deck= [
                           "Sabretooth (I)",
                           "Sabretooth (II)",
                           "Sabretooth (III)"
                       ],
                       schemes= [
                           "Stalked by Sabretooth",
                           "The Injured Senator"
                       ],
                       encounter= {
                           "Find the Senator": 1,
                           "Robert Kelly": 1,
                           "Adamantium Claws": 1,
                           "Animal Ferocity": 1,
                           "Sabretooth Strikes": 2,
                           "Unreleting Savage": 3,
                           "Medical Emergency": 2,
                           "Feral Rage": 1
                       }),
               Villain("Project Wideawake",
                       villain_deck=[
                           "Sentinel (I)",
                           "Sentinel (II)",
                           "Sentinel (III)"
                       ],
                       schemes=["Night of the Sentinels"],
                       encounter= {
                           "Mutant at the Mall/Jubilee (Jubilation Lee)": 1,
                           "Rictor": 1,
                           "Boom Boom": 1,
                           "Cannonball": 1,
                           "Wolfsbane": 1,
                           "Sentinel Mark IV": 2,
                           "Gauntlet Beam": 2,
                           "Learning A.I.": 1,
                           "Adaptive Armor": 1,
                           "Self-Repair": 1,
                           "Mutant Detected": 2,
                           "Warn the Others": 2,
                           "Abduction Protocols": 4
                       }),
               Villain("Master Mold",
                       villain_deck= [
                           "Master Mold (I)",
                           "Master Mold (II)",
                           "Master Mold (III)"
                       ],
                       schemes= [
                           "The Sentinel Factory",
                           "Master Mold's Agenda"
                       ],
                       encounter= {
                           "Sentinel Mark VIII": 2,
                           "Unit Upgrade": 2,
                           "Stun Beam": 2,
                           "Master Mold's Children": 2,
                           "Shields Up": 2,
                           "Intruder Alert!": 1,
                           "Insert Virus Program": 2
                       }),
               Villain("Mansion Attack",
                       villain_deck= [
                           "Avalanche",
                           "Blob",
                           "Pyro",
                           "Toad"
                       ],
                       schemes= [
                           "The Brotherhood Strikes!",
                           "The Atrium",
                           "The Cafeteria",
                           "The Basketball Court",
                           "The Courtyard"
                       ],
                       encounter= {
                           "Save the School": 1,
                           "Brotherhood Beatdown": 3,
                           "Ground Swell": 2,
                           "Immovable": 2,
                           "Pyromaniac": 2,
                           "Hopping Mad": 2,
                           "Protect the Students": 2,
                           "Under Siege": 2
                       }),
               Villain("Magneto",
                       villain_deck= [
                           "Magneto (I)",
                           "Magneto (II)",
                           "Magneto (III)"
                       ],
                       schemes= [
                           "Asteroid M",
                           "Factory Online",
                           "The Rule of Magnus"
                       ],
                       encounter= {
                           "Boarding Party/Sabotage Master Mold": 1,
                           "Orbital Decay/Physical Strain": 1,
                           "M-Type Sentinel": 4,
                           "Magneto's Helmet": 1,
                           "Magneto's Armor": 1,
                           "Magnetic Bubble": 1,
                           "Wrapped in Metal": 1,
                           "Master of Magnetism": 2,
                           "Electric Shock": 2,
                           "Electromagnetic Blast": 2,
                           "Metal Shards": 2,
                           "Magnetic Missile": 2,
                           "Magnetic Mayhem": 1,
                           "Magnetically Sealed": 1,
                           "Seized!": 1
                       })],
    modulars= [Modular("Brotherhood",
                       cards= {
                           "Avalanche": 1,
                           "Blob": 1,
                           "Pyro": 1,
                           "Toad": 1,
                           "Homo Superior": 2,
                           "Mutant Terrorists": 1,
                           "The Brotherhood": 1
                       }),
               Modular("Mystique",
                       cards= {
                           "Mystique": 1,
                           "Metamorphic Mayhem": 1,
                           "Infiltration": 2,
                           "Shapeshifter Surprise": 1
                       }),
               Modular("Zero Tolerance",
                       cards={
                           "Sentinel Mark II": 2,
                           "Sentinel Mark III": 2,
                           "Energy Barrier": 2,
                           "Operation Zero Tolerance": 1
                       }),
               Modular("Sentinels",
                       cards= {
                           "Sentinel Mark V": 2,
                           "Sentinel Mark VI": 2,
                           "Targeted for Elimination": 2,
                           "Relentless Robots": 1
                       }),
               Modular("Acolytes",
                       cards= {
                           "Fabian Cortez": 1,
                           "Amelia Voght": 1,
                           "Senyaka": 1,
                           "Delgado": 1,
                           "Unuscione": 1,
                           "Zeal for the Cause": 1,
                           "The Acolytes": 1
                       }),
               Modular("Future Past",
                       cards= {
                           "Nimrod": 1,
                           "Bastion": 1,
                           "Nimrod's Portal": 1,
                           "Bastion's Machinations": 1,
                           "Nano-Sentinel Tech": 1
                       })],
    campaigns=[Campaign("Mutant Genesis Campaign",
                        cards= {
                            "Frightened Police/Metro P.D.": 1,
                            "Enemy of My Enemy/Magneto": 1,
                            "Find the Prisoners/Rescue Captives": 1,
                            "Reactive Defense/Surprise Attack": 1,
                            "Magneto's Fortress/Magneto's Power": 1
                        }),
               Campaign("Brawler",
                        cards= {
                            "Coup de Grâce": 1,
                            "Swagger": 1,
                            "Brazen Defense": 1,
                            "Ferocious Attack": 1,
                            "War Cry": 1
                        }),
               Campaign("Commander",
                        cards= {
                            "Coup de Grâce": 1,
                            "Compassion": 1,
                            "Group Assault": 1,
                            "Shock and Awe": 1,
                            "Improvisation": 1
                        }),
               Campaign("Defender",
                        cards= {
                            "Swagger": 1,
                            "Surprise!": 1,
                            "Heroic Intervention": 1,
                            "Determined Defense": 1,
                            "Bodyguard": 1
                        }),
               Campaign("Peacekeeper",
                        cards= {
                            "Surprise!": 1,
                            "Compassion": 1,
                            "Rescue Operation": 1,
                            "Mentorship": 1,
                            "Fortitude": 1
                        })]
)