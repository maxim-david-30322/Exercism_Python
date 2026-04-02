color_codes = {
    "black": 0,
    "brown": 1,
    "red": 2,
    "orange": 3,
    "yellow": 4,
    "green": 5,
    "blue": 6,
    "violet": 7,
    "grey": 8,
    "white": 9
}
mag={
    3:'kilo',
    6:'mega',
    9:'giga'

}

def label(colors):
    color=[]
   # color=f"{color_codes[colors[1]]}{color_codes[colors[2]]}
    if colors[2]=='black':
        if colors[1]=='black':
            return ("0 ohms")
        rezistor= (f"{color_codes[colors[0]]}{color_codes[colors[1]]}")
    else:
        rezistor=(f"{color_codes[colors[0]]}{color_codes[colors[1]]}{'0'*color_codes[colors[2]]}")

    zero=rezistor.count("0")
    zero_round=(zero//3)*3
    rezistor=rezistor.lstrip("0")
    if zero_round>0:
        magnitude=mag[zero_round]
        zero_str="0"*(zero_round)
        rezistor=rezistor[:-len(zero_str)]
        return(rezistor+(f" {magnitude}ohms"))
    return(rezistor+(f" ohms"))
