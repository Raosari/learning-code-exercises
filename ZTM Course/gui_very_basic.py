

picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]


def display(pic):
    empty = " "
    fill = "*"
    for array in pic:
        for el in array:
            if el == 0:
                print(empty,end= " ")
            else:
                print(fill,end=" ")
        print("") #for a new line

def display2(pic):
    for row in pic:
        display_row = ""
        for pix in row:
            if pix == 1:
                display_row += "* "
            else:
                display_row += "  "
        print(display_row)

display2(picture)