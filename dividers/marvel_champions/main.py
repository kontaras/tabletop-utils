from renderer import render
from sets.campaign import sinister_motives


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    dividers = []
    sets = []
    sets += sinister_motives.get_heroes()
    sets += sinister_motives.get_aspects()
    sets += sinister_motives.get_villains()
    sets += sinister_motives.get_modulars()


    for cardSet in sets:
        dividers += cardSet.get_dividers()

    render(dividers)


