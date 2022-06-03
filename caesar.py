import string

rel_freqs = [.0817, .0149, .0278, .0425, .1270, .0223, .0202, .0609, .0697, .0015, .0077, .0402, .0241,
             .0675, .0751, .0193, .0009, .0599, .0633, .0906, .0276, .0098, .0236, .0015, .0197, .0007]


def shift_letter_reverse(letter, shift):
    return chr((ord(letter) - 65 - ord(shift) - 65) % 26 + 65)


def get_frequencies(text):
    # Count letter frequencies in the text
    alpha = [0]*26
    for i in text.upper():
        alpha[ord(i)-65] += 1
    return alpha


def decipher(text):
    correlations = []
    for char in string.ascii_uppercase:
        shifted_text = "".join(list(map(shift_letter_reverse, list(text), list(char)*len(text))))
        shifted_text_freqs = get_frequencies(shifted_text)
        correlation = sum([shifted_text_freqs[i] * rel_freqs[i] for i in range(26)])
        correlations.append(correlation)
    key = chr(correlations.index(max(correlations))+65)
    plaintext = "".join([shift_letter_reverse(i, key) for i in text])
    return plaintext


if __name__ == "__main__":
    ciphertext = input("Enter text to decipher: ").replace(" ", "").upper()
    print(decipher(ciphertext))
