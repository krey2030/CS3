def color(Hex,BG): #color UPDATED
    if Hex[0] == "#":#makes it realistic and raises error
        try:Hex[7]#should only be 3 or 6 digits
        except:#but i wouldn't even use 6 digits
            try:Hex[6]
            except IndexError:
                try:Hex[4]#should only be 3 or 6 digits
                except IndexError:
                    r = int(Hex[1], 16)
                    g = int(Hex[2], 16)
                    b = int(Hex[3], 16)
                    return f"\x1b[{BG};2;{r*17};{g*17};{b*17}m"#default used personally
                else:raise IndexError("string index out of range")#fake error
            else:
                r = int(f"{Hex[1]}{Hex[2]}",16)
                g = int(f"{Hex[3]}{Hex[4]}",16)
                b = int(f"{Hex[5]}{Hex[6]}",16)
                return f"\x1b[{BG};2;{r};{g};{b}m"
        else:raise IndexError("string index out of range")#fake error
    else:raise ValueError(f"bad color string: '{Hex[0]}'")#should be in color string format
    #   color('#rgb',ON／OFF)
    #   color('#rrggbb',ON／OFF)
OFF = "38" #Text color
ON = "48" #Highlight
def effect(Effect: int): #text style and emphasis for bold, italic, underlines, etc. EXTRA FEATURE for all my activities*
    return f"\x1b[{Effect}m" #1 = bold, #3 = italic, #4 = underline, #22 removes bold, #23 removes italic, #24 = removes underline
sin = { 0:0,
        6:((30-6*5**0.5)**0.5-5**0.5-1)/8,
        12:((10+2*5**0.5)**0.5-15**0.5+3**0.5)/8,
        15:(6**0.5-2**0.5)/4,
        18:(5**0.5-1)/4,
        24:((3**0.5)/8)*(5**0.5+1)-((2**0.5)/8)*((5-5**0.5)**0.5),
        30:1/2,
        36:(10-2*5**0.5)**0.5/4,
        45:2**0.5/2,
        54:(5**0.5+1)/4,
        60:3**0.5/2,
        66:(5**0.5+1+(30-6*5**0.5)**0.5)/8,
        72:(10+2*5**0.5)**0.5/4,
        75:(6**0.5-2**0.5)/4,
        78:((30+6*5**0.5)**0.5+5**0.5-1)/8,
        84:((10-2*5**0.5)**0.5+15**0.5+3**0.5)/8,
        90:1
    }
"""
by:Tau Comlines(color,effect)+Spider Commuons(sin)
Kurt Ashe Rey. Intal

reference symbols:※【】「」『』※／•—×
"""