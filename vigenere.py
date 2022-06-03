import caesar


def get_index_of_coincidence(text):
    freqs = caesar.get_frequencies(text)
    numerator = 0
    for j in freqs:
        numerator += j*(j - 1)
    return numerator*26/len(text)/(len(text)-1)


def decipher(text):
    # Deduce the key using the index of coincidence
    if len(text) < 28:
        Exception("Cipher text is too short")
    columns = []
    ics = []
    for x in range(1, 14):
        delta_bar_ic = 0
        cols = []
        for i in range(x):
            column = "".join([text[j] for j in range(len(text)) if j % x == i])
            cols.append(column)
            delta_bar_ic += get_index_of_coincidence(column)
        delta_bar_ic /= x
        ics.append(delta_bar_ic)
        if 1.5 < delta_bar_ic:
            columns = cols
            break

    if len(columns) == 0:
        raise Exception("Data doesn't follow expected distribution")

    plaintext_cols = [list(caesar.decipher(i)) for i in columns]
    out = ""
    for j in range(max([len(i) for i in plaintext_cols])):
        for col in plaintext_cols:
            if len(col) > 0:
                out += col.pop(0)
    return out


if __name__ == "__main__":
    ciphertext = "".join(x for x in input("Enter ciphertext: ") if x.isalpha()).upper()
    print(decipher(ciphertext))
