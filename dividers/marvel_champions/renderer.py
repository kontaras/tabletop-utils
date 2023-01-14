import model
from dominate import tags

def render(dividers: list[model.Divider]) -> None:
    with open('template.html', 'r') as template, open('output.html', 'w') as target:
        for line in template:
            if "<!-- CONTENTS -->" in line:
                for divider in dividers:
                    target.write(render_divider(divider))
            else:
                target.write(line)

def render_divider(divide: model.Divider) -> str:
    box = tags.div()
    box += tags.h2(divide.name)

    card_list = tags.ul()
    for name, quantity in divide.cards.items():
        if quantity > 1:
            card_list += tags.li(f'{name} (x{quantity})')
        else:
            card_list += tags.li(f'{name}')
    box.add(card_list)

    for sub in divide.sublists:
        for tag in render_sub(sub):
            box.add(tag)

    return box.render(xhtml=True)

def render_sub(subitem: model.SubList) -> list[tags.html_tag]:
    title = tags.h3(subitem.name)

    card_list = tags.ul()
    for name, quantity in subitem.cards.items():
        if quantity > 1:
            card_list += tags.li(f'{name} (x{quantity})')
        else:
            card_list += tags.li(f'{name}')

    return [title, card_list]