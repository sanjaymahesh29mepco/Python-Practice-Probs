import math
def sort_by_prob(sym, prob):
    com = list(zip(sym, prob))
    com.sort(key=lambda x: x[1], reverse=True)
    return [x[0] for x in com], [x[1] for x in com]
def shannon(sym, prob, prefix=''):
    if len(sym) == 1:
        return {sym[0]: prefix}
    total = sum(prob)
    cumu = 0
    split = 0
    for i, p in enumerate(prob):
        cumu += p
        if cumu >= total / 2:
            split = i + 1
            break
    leftsym = sym[:split]
    leftprob = prob[:split]
    rigsym = sym[split:]
    rigprob = prob[split:]
    codes = {}
    codes.update(shannon(leftsym, leftprob, prefix + '0'))
    codes.update(shannon(rigsym, rigprob, prefix + '1'))
    return codes
def calculate(prob, codes):
    entro = -sum(p * math.log2(p) for p in prob)
    avg = sum(len(codes[sym[i]]) * prob[i] for i in range(len(sym)))
    effi = entro / avg
    vari = sum(p * (len(codes[sym[i]]) - avg) ** 2 for i, p in enumerate(prob))
    redud = 1 - effi
    return entro, effi, vari, redud
sym = ['A', 'B', 'C', 'D', 'E']
prob = [0.4, 0.2, 0.2, 0.1, 0.1]
sym, prob = sort_by_prob(sym, prob)
codes = shannon(sym, prob)
entro, effi, vari, redud = calculate(prob, codes)
print("Symbol\tProbability\tCode")
for symbol in sym:
    print(f"{symbol}\t{prob[sym.index(symbol)]}\t\t{codes[symbol]}")
print(f"\nEntropy: {entro:.4f}")
print(f"Efficiency: {effi:.4f}")
print(f"Variance: {vari:.4f}")
print(f"Redundancy: {redud:.4f}")
