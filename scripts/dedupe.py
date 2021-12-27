import csv

# Open file
filename='/Users/nic/git/xios-guide-to-monsters/monsters.csv'
output_filename = '/Users/nic/git/xios-guide-to-monsters/monsters.csv'
# try:
#     fhand = open(filename)
# except:
#     print('File cannot be opened.')
#     exit()

# Iterate over lines in File
# for line in fhand:
#      reader = csv.reader(line, skipinitialspace=True)
#      for row in reader:
#          print(row)

fields = []
rows = []
name = size = type = environment = hp = ac = initiative = alignment = legendary = lair = unique = cr = tags = source = ''

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)

    for row in csvreader:

        if name.lower() == row[0].lower(): # If this monster is a duplicate of the previous one, take non-empty values
            if size == '':
                size = row[1]
            if type == '':
                type = row[2]
            if environment == '':
                environment = row[3]
            if hp == '':
                hp = row[4]
            if ac == '':
                ac = row[5]
            if initiative == '':
                initiative = row[6]
            if alignment == '':
                alignment = row[7]
            if legendary == '':
                legendary = row[8]
            if lair == '':
                lair = row[9]
            if unique == '':
                unique = row[10]
            if cr == '':
                cr = row[11]
            if tags == '':
                tags = row[12]
            if source == '':
                source = row[13]
            print('Duplicate:', name)
            newrow = '' + name, size, type, environment, hp, ac, initiative, alignment, legendary, lair, unique, cr, tags, source
            rows.pop()
            rows.append(newrow)
        else:
            name = row[0]
            size = row[1]
            type = row[2]
            environment = row[3]
            hp = row[4]
            ac = row[5]
            initiative = row[6]
            alignment = row[7]
            legendary = row[8]
            lair = row[9]
            unique = row[10]
            cr = row[11]
            tags = row[12]
            source = row[13]
            rows.append(row)

    with open(output_filename, 'w') as output_file:
        # fields = ['name', 'size', 'type', 'environment', 'hp', 'ac', 'initiative', 'alignment', 'legendary', 'lair', 'unique', 'cr', 'tags', 'source']
        writer = csv.writer(output_file)
        output_file.write(",".join(fields) + '\n')
        writer.writerows(rows)

    # # get total number of rows
    # print("Total no. of rows: %d"%(csvreader.line_num))
    #
    # # printing the field names
    # print('Field names are:' + ', '.join(field for field in fields))
