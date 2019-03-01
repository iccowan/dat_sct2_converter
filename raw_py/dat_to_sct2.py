# .dat to .sct2 File Converter for VATSIM
# By Ian Cowan
# Python 3.7

# Prompt the user for the file
file = input('Filename: ')

# Open the file and create output file
opened_file = open(file, 'r')
output_file = open('dat_to_sct2_output.txt', 'w')

# Initialize variables
coordinates = list()
i = 0
output = ''

# Formats each line and adds them to the coordinates list
for line in opened_file:
    if not (line[0:1] == '!'):
        if line[0:1] == 'L':
            coordinates.append('LINE')
        else:
            coordinates.append('N0' + line[3:5] + '.' + line[6:8] + '.' + line[9:16] + ' W' + line[18:21] + '.' + line[22:24] + '.' + line[25:32])

# Removes first 2 unnecessary lines
coordinates.pop(0)
coordinates.pop(1)

# Go through each line of the source file and structure the output properly:
# This prints 2 coordinates on each line (start lat/long & end lat/long) to create a complete line segment on each line
# It will automatically string together all of the points to create a continuous line until it reaches a line break indicated by "LINE"
# This loop is courtesy of https://drakedesignlabs.com - converted from PHP to Python by Ian Cowan
while i + 2 < len(coordinates):
    i += 1
    output += "\t\t\t  " + coordinates[i] + ' ' + coordinates[i + 1] + '\n'
    i += 2
    while coordinates[i] != 'LINE':
        output += '\t\t\t  ' + coordinates[i - 1] + ' ' + coordinates[i] + '\n'
        i += 1

# Puts the line in the file
output_file.write(output)

# Close the files
opened_file.close()
output_file.close()
