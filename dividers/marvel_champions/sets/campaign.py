from model import Campaign, Hero, Aspect, AspectDeck, Villain, Modular

sinister_motives = Campaign(
    heroes=[Hero("Ghost-Spider",
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
                 obligation="Worried Father")],
    aspects=[AspectDeck("Ghost-Spider",
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
                        })],
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
                      })],
    modulars=[Modular("City in Chaos",
                      cards={
                          "Panic in the Streets": 1,
                          "Rhino": 1,
                          "Calling in Favors": 1,
                          "Now or Never": 2
                      })]
)