color_codes = {
    "black": 0, "brown": 1, "red": 2, "orange": 3, "yellow": 4,
    "green": 5, "blue": 6, "violet": 7, "grey": 8, "white": 9
}
mag = {3: 'kilo', 6: 'mega', 9: 'giga'}
tolerance_codes = {
    "grey": 0.05, "violet": 0.1, "blue": 0.25, "green": 0.5,
    "brown": 1, "red": 2, "gold": 5, "silver": 10
}


def resistor_label(colors):

    if all(c=="black" for c in colors):
        return "0 ohms"
    
    if len(colors) == 4:
            # 4-band: digit, digit, multiplier, tolerance
            value = (color_codes[colors[0]] * 10 + color_codes[colors[1]]) * (10 ** color_codes[colors[2]])
            tolerance = tolerance_codes[colors[3]]
    elif len(colors) == 5:
            # 5-band: digit, digit, digit, multiplier, tolerance
            value = (color_codes[colors[0]] * 100 + color_codes[colors[1]] * 10 + color_codes[colors[2]]) * (10 ** color_codes[colors[3]])
            tolerance = tolerance_codes[colors[4]]
    else:
        return "Invalid band count"

    res_str=str(value)
    magnitude=""

    if value >= 1_000_000_000:
            value /= 1_000_000_000
            magnitude = "giga"
    elif value >= 1_000_000:
            value /= 1_000_000
            magnitude = "mega"
    elif value >= 1_000:
            value /= 1_000
            magnitude = "kilo"
    
    reformated_value=f"{value:g}"
    return f"{reformated_value} {magnitude}ohms ±{tolerance}%"