import random

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


givers = ['Mirosława', 'Tadeusz', 'Anna', 'Paweł', 'Sylwia',
          'Rudi', 'Eliza', 'Dawid', 'Ola', 'Piotr', 'Adam', 'Ewa']
receivers = givers[:]

def pair(giver, receivers, persons):
    receiver = random.choice(receivers)
    if persons[giver] != persons[receiver] and giver != receiver:
        return [giver, receiver]
    else:
        return None
draw = []
for giver in givers:
    loop_count = 0
    prop_pair = pair(giver, receivers, persons)
    if prop_pair is not None:
        draw.append(prop_pair)
    else:
        if loop_count < 5:
            loop_count += 1
            continue
        else:
            break
print(draw)
print(len(draw))
