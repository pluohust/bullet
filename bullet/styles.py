from . import colors

Example = {
    "choices" : ["Item {}".format(i) for i in range(1, 6)], 
    "margin" : 2,
    "pad_right" : 5,
    "align" : 5,
    "shift" : 1
}

Ocean = {
    "bullet" : "",
    "bullet_color" : colors.foreground["cyan"],
    "word_color" : colors.foreground["cyan"],
    "word_on_switch" : colors.foreground["blue"],
    "background_color" : colors.background["blue"],
    "background_on_switch" : colors.background["cyan"]
}

Greece = {
    "bullet" : "αβγ",
    "bullet_color" : colors.foreground["white"],
    "word_color" : colors.foreground["blue"],
    "word_on_switch" : colors.foreground["white"],
    "background_color" : colors.background["white"],
    "background_on_switch" : colors.background["blue"]
}

Christmas = {
    "bullet" : "★",
    "bullet_color" : colors.foreground["white"],
    "word_color" : colors.foreground["white"],
    "word_on_switch" : colors.foreground["red"],
    "background_color" : colors.background["red"],
    "background_on_switch" : colors.background["green"]
}

Lime = {
    "bullet" : "⊙",
    "bullet_color" : colors.foreground["green"],
    "word_color" : colors.foreground["yellow"],
    "word_on_switch" : colors.foreground["green"],
    "background_color" : colors.background["green"],
    "background_on_switch" : colors.background["yellow"]
}
