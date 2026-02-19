import heapq
import math
def build_huffman_tree(symbols, probabilities):
    priority_queue = [[probabilities[i], [symbols[i], ""]] for i in range(len(symbols))]
    heapq.heapify(priority_queue)
    while len(priority_queue) > 1:
        left = heapq.heappop(priority_queue)
        right = heapq.heappop(priority_queue)
        for pair in left[1:]:
            pair[1] = "0" + pair[1]
        for pair in right[1:]:
            pair[1] = "1" + pair[1]
        heapq.heappush(priority_queue, [left[0] + right[0]] + left[1:] + right[1:])
    return sorted(heapq.heappop(priority_queue)[1:], key=lambda x: (len(x[1]), x[0]))
def calculate_metrics(probabilities, codes):
    entropy = -sum(p * math.log2(p) for p in probabilities)
    avg_code_length = sum(len(codes[symbols[i]]) * probabilities[i] for i in range(len(symbols)))
    efficiency = entropy / avg_code_length
    variance = sum(p * (len(codes[symbols[i]]) - avg_code_length) ** 2 for i, p in enumerate(probabilities))
    redundancy = 1 - efficiency
    return entropy, efficiency, variance, redundancy
symbols = ['A', 'B', 'C', 'D', 'E']
probabilities = [0.4, 0.2, 0.2, 0.1, 0.1]
huffman_tree = build_huffman_tree(symbols, probabilities)
codes = {symbol: code for symbol, code in huffman_tree}
entropy, efficiency, variance, redundancy = calculate_metrics(probabilities, codes)
print("Symbol\tProbability\tCode")
for symbol, code in huffman_tree:
    print(f"{symbol}\t{probabilities[symbols.index(symbol)]}\t\t{code}")
print(f"\nEntropy: {entropy:.4f}")
print(f"Efficiency: {efficiency:.4f}")
print(f"Variance: {variance:.4f}")
print(f"Redundancy: {redundancy:.4f}")
