import os
import csv

dir='/Users/nic/git/xios-guide-to-monsters/'
filename = dir + 'monsters.csv'

if not os.path.exists(dir + '/monsterfiles'):
    os.makedirs(dir + '/monsterfiles')

monsterFilePath = dir + 'monsterfiles/'

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile)
    fields = next(csvreader)
    for row in csvreader:
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
        name = name.replace(',', ' -')
        name = name.replace('/', ' or ')
        print(name)
        with open(monsterFilePath + name + '.md', 'w') as output_file:
            string = f'''---
name: {name}
size: {size}
type: {type}
environment: {environment}
hp: {hp}
ac: {ac}
initiative: {initiative}
alignment: {alignment}
legendary: {legendary}
lair: {lair}
unique: {unique}
cr: {cr}
tags: {tags}
source: "{source}"
---'''
            output_file.write(string)
