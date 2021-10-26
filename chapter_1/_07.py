def template(x, y, z):
    out_x = ""
    out_y = ""
    out_z = ""
    if type(x) != str:
        out_x = str(x)
    else:
        out_x = x
    if type(y) != str:
        out_y = str(y)
    else:
        out_y = y
    if type(z) != str:
        out_z = str(z)
    else:
        out_z = z
    
    print(out_x + "時の" + out_y + "は" + out_z)

def main():
    template(12, "気温", 22.4)

if __name__ == "__main__":
    main()