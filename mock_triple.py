import random

NTS = ('A', 'C', 'G', 'T')

def rand_nuc(k):
    return ''.join(random.choices(NTS, k=k))

def gen_spacer(sequence, number, character):
    # Placeholder: real logic should use inputs
    return rand_nuc(20)

def gen_pbs(spacer, number, character):
    # Placeholder: real logic should use inputs
    length = random.randint(8, 24)
    remnant = len(spacer) - 3 - length
    spmatch = spacer[max(remnant, 0):-3]
    rest = rand_nuc(-remnant) if remnant < 0 else ''
    return spmatch + rest

def gen_rtt(number, character):
    # Placeholder: real logic should use inputs
    length = random.randint(8, 40)
    return rand_nuc(length)

def generate_triples(sequence, number, character):
    n = 20  # For demonstration; real logic may use 'number'
    triples = []
    for _ in range(n):
        spacer = gen_spacer(sequence, number, character)
        pbs = gen_pbs(spacer, number, character)
        rtt = gen_rtt(number, character)
        triples.append((spacer, pbs, rtt))
    return triples

def gc_aberration(s):
    pgc = sum(1 for c in s if c in ('G', 'C')) / len(s)
    return (pgc - 0.5) * 2

def length_aberration(s):
    ls = len(s)
    if ls == 25:
        return 0
    if ls < 25:
        return (ls - 8) / 17
    return ((ls - 25) ** 0.5) / (30 ** 0.5)

def score_triples(triples):
    results = []
    for triple in triples:
        ext3 = triple[1] + triple[2]
        dev = (gc_aberration(ext3) + length_aberration(ext3)) ** 2
        score = 1 / (1 + 3 * dev)
        score = score * 100
        results.append((*triple, round(score, 2)))
    return results