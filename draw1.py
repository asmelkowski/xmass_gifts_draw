import random
import os

latest_draw = {}

if os.path.exists('draw_history.txt'):
    with open('draw_history.txt') as file:
        for line in file.readlines():
            line = line.split(':')
            latest_draw[line[0]] = line[1].rstrip('\n')
    print(latest_draw)

persons = {
        'Mirosława': 'Cich',
        'Tadeusz': 'Cich',
        'Anna': 'Smel',
        'Paweł': 'Smel',
        'Adam': 'Smel',
        'Ewa': 'Smel',
        'Eliza': 'Sien',
        'Dawid': 'Sien',
        'Sylwia': 'Bred',
        'Rudi': 'Bred',
        'Ola': 'Przy',
        'Piotr': 'Przy',
    }

def draw(persons):
    gifts_map = {x: '' for x in persons.keys()}
    receivers = [x for x in persons.keys()]
    for giver in gifts_map.keys():
        loop_count = 0
        while len(gifts_map[giver]) == 0:
            if loop_count < 3:
                person = random.choice(receivers)
                breakpoint()
                if giver != person and persons[giver] != persons[person]:
                    if os.path.exists('draw_history.txt'):
                        if person not in latest_draw[giver]:
                            gifts_map[giver] = person
                            receivers.remove(person)
                    else:
                        gifts_map[giver] = person
                        receivers.remove(person)
                else:
                    loop_count += 1
                    breakpoint()
            else:
                draw(persons)
    with open('draw_history.txt', 'w') as history:
        for giver, receiver in gifts_map.items():
            history.write(f"{giver}:{receiver}\n")
    return gifts_map

print(draw(persons))