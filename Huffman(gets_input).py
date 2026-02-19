import heapq
import math

class Node:
    def __init__(self, symbol, freq):
        self.symbol = symbol
        self.freq = freq
        self.left = None
        self.right = None
    
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(symbols, probabilities):
    heap = [Node(symbols[i], probabilities[i]) for i in range(len(symbols))]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        
        merged = Node(None, left.freq + right.freq)
        merged.left = left
        merged.right = right
        
        heapq.heappush(heap, merged)
    
    return heap[0]

def generate_codes(node, prefix="", code_map={}):
    if node:
        if node.left is None and node.right is None:
            code_map[node.symbol] = prefix
        else:
            generate_codes(node.left, prefix + "0", code_map)
            generate_codes(node.right, prefix + "1", code_map)
    return code_map

def calculate_entropy(probabilities):
    entropy = -sum(prob * math.log2(prob) for prob in probabilities)
    return entropy

def calculate_average_code_length(codes, probabilities, symbols):
    avg_length = sum(len(codes[symbols[i]]) * probabilities[i] for i in range(len(symbols)))
    return avg_length

def huffman_encoding(symbols, probabilities):
    entropy = calculate_entropy(probabilities)
    root = build_huffman_tree(symbols, probabilities)
    codes = generate_codes(root)
    avg_code_length = calculate_average_code_length(codes, probabilities, symbols)
    
    return codes, entropy, avg_code_length

if __name__ == "__main__":
    symbols = input("Enter symbols separated by space: ").split()
    probabilities = list(map(float, input("Enter corresponding probabilities separated by space: ").split()))
    
    if len(symbols) != len(probabilities) or abs(sum(probabilities) - 1.0) > 1e-6:
        print("Invalid input: Ensure probabilities sum to 1 and lengths match.")
    else:
        codes, entropy, avg_code_length = huffman_encoding(symbols, probabilities)
        print("Huffman Codes:", codes)
        print("Entropy:", entropy)
        print("Efficiency:",(entropy/avg_code_length)*100)
        print("Average Code Length:", avg_code_length)
