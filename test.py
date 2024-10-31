from poker_isomorphisms.main import get_isomorphisms, normalise_flop

flops = ['3c4h5h', 'JcJhAc', 'Ac 8d3d', 'Ac 8d 3d', 'Ac8d3d']

for flop in flops:
    print(f'{flop}: {normalise_flop(flop)}, {get_isomorphisms(flop)}')
    print()