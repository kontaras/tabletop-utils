from renderer import render
from sets.campaign import *
from sets.hero import *
from sets.pnp import *


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    releases = [sinister_motives, scarlet_witch, gamora, ronan]
    sets = []
    for release in releases:
        sets += release.get_heroes()
        sets += release.get_aspects()
        sets += release.get_villains()
        sets += release.get_modulars()
        sets += release.get_campaigns()

    dividers = []
    for cardSet in sets:
        dividers += cardSet.get_dividers()

    render(dividers)


