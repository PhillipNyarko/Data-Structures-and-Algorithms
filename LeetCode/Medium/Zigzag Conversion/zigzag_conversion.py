def zig_zag_conversion(string, rows):
    
    array = 0
    array_position = 0
    direction = "down"
    matrix = []

    for i in range(rows):
        matrix.append([])

    if rows == 1:
        return string

    for i in range(len(string)):
        if array == rows - 1:
            direction = "up"
        elif array == 0:
            direction = "down"

        if direction == "up":
            matrix[array].append(string[i])
            array -= 1
            array_position += 1
        elif direction == "down":
            matrix[array].append(string[i])
            array += 1

    output = []
    for i in range(rows):
        output.append("".join(matrix[i]))

    print("".join(output))


number_of_rows = 4
input_string = "PAYPALISHIRING" 

zig_zag_conversion(input_string, number_of_rows)

