import collections

from renderer import render
from sets.campaign import *
from sets.hero import *
from sets.pnp import *
from sets.scenarios import *


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    releases = [sinister_motives, scarlet_witch, gamora, ronan,
                the_once_and_future_kang]
    sets = collections.defaultdict(list)
    for release in releases:
        sets["heroes"] += release.get_heroes()
        sets["aspects"] += release.get_aspects()
        sets["villains"] += release.get_villains()
        sets["modulars"] += release.get_modulars()
        sets["campaigns"] += release.get_campaigns()

    dividers = []
    for cardType in sets.values():
        for cardSet in cardType:
            dividers += cardSet.get_dividers()

    render(dividers)


