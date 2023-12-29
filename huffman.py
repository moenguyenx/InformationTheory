from heapq import heappush, heappop, heapify
from collections import defaultdict
from bitarray import bitarray

def build_huffman_tree(freq_lib):
    """
    Build Huffman tree and return the Huffman dictionary.

    Parameters:
        freq_lib (defaultdict): A dictionary containing the frequency of each symbol.

    Returns:
        dict: Huffman dictionary mapping symbols to their Huffman codes.
    """
    heap = [[fq, [sym, ""]] for sym, fq in freq_lib.items()]
    heapify(heap)

    while len(heap) > 1:
        right = heappop(heap)
        left = heappop(heap)

        for pair in right[1:]:
            pair[1] = '0' + pair[1]
        for pair in left[1:]:
            pair[1] = '1' + pair[1]
        heappush(heap, [right[0] + left[0]] + right[1:] + left[1:]) 

    huffman_list = right[1:] + left[1:]
    huffman_dict = {a[0]: bitarray(str(a[1])) for a in huffman_list}

    return huffman_dict

def huffman_encode(text, huffman_dict):
    """
    Encode a text using Huffman encoding.

    Parameters:
        text (str): The input text to be encoded.
        huffman_dict (dict): Huffman dictionary mapping symbols to their Huffman codes.

    Returns:
        bitarray: Encoded message.
    """
    encoded_text = bitarray()
    encoded_text.encode(huffman_dict, text)
    return encoded_text

def huffman_decode(encoded_text, huffman_dict):
    """
    Decode a text using Huffman decoding.

    Parameters:
        encoded_text (bitarray): The encoded message.
        huffman_dict (dict): Huffman dictionary mapping symbols to their Huffman codes.

    Returns:
        str: Decoded message.
    """
    decoded_text = bitarray()
    decoded_text.extend(encoded_text)
    decoded_text = decoded_text.decode(huffman_dict)
    decoded_text = ''.join(decoded_text)
    return decoded_text

def huffman_main_func():
    """
    Main function to take user input, perform Huffman encoding and decoding, and print the results.
    """
    # Input data to be compressed
    text = input("Input message: ")

    # Create a library with frequency of each symbols
    freq_lib = defaultdict(int)
    for ch in text:
        freq_lib[ch] += 1

    # Create Huffman tree
    huffman_dict = build_huffman_tree(freq_lib)

    # Huffman Encoding 
    encoded_text = huffman_encode(text, huffman_dict)
    print("Encoded message:", encoded_text)

    # Decoding
    decoded_text = huffman_decode(encoded_text, huffman_dict)
    print("Decoded message:", decoded_text)

