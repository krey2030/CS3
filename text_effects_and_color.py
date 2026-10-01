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
"""
by:Tau Comlines
—Kurt Ashe Rey. Intal
"""
