from poker_isomorphisms.main import flop_isomorphisms, flop_normalise

flops = ['3c4h5h', 'JcJhAc', 'Ac 8d3d', 'Ac 8d 3d', 'Ac8d3d']

for flop in flops:
    print(f'{flop}: {flop_normalise(flop)}, {flop_isomorphisms(flop)}')
    print()