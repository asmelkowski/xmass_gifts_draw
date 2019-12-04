import random
import os

draw_history = []

if os.path.exists('draw_history.txt'):
    with open('draw_history.txt', 'r') as history:
        for line in history.readlines():
            pair = line.split(', ')
            pair[1] = pair[1].rstrip('\n')
            pair.sort()
            draw_history.append(pair)

names1 = ['Mirosława', 'Tadeusz', 'Anna', 'Paweł', 'Sylwia',
          'Rudi', 'Eliza', 'Dawid', 'Ola', 'Piotr', 'Adam', 'Ewa']
names2 = names1[:]

dissallowed_pairs = {
    'Mirosława': 'Tadeusz',
    'Tadeusz': 'Mirosława',
    'Anna': 'Paweł',
    'Paweł': 'Anna',
    'Sylwia': 'Rudi',
    'Rudi': 'Sylwia',
    'Eliza': 'Dawid',
    'Dawid': 'Eliza',
    'Ola': 'Piotr',
    'Piotr': 'Ola',
    'Adam': "",
    'Ewa': ""
}

draw = []

while names1 and names2:
    first = random.choice(names1)
    names1.remove(first)
    second = random.choice(names2)
    names2.remove(second)
    temp_pair = [first, second].sort()
    if first != second and first != dissallowed_pairs[second] and second != dissallowed_pairs[first] and temp_pair not in draw_history:
        draw.append([first, second])
    else:
        names1.append(first)
        names2.append(second)

with open('draw_history.txt', 'a') as outfile:
    for pair in draw:
        outfile.write(f"{pair[0]}, {pair[1]}\n")
print(draw)
