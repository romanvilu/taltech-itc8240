import itertools
from nltk.corpus import words

# Given ciphertext in binary.
ciphertext_bin = ["00010010", "00000111", "11101010"]

# Convert ciphertext's binaries to decimal integers.
ciphertext_ints = [int(b, 2) for b in ciphertext_bin]

# Load a set of valid 3-letter English words from the NLTK words dictionary.
words = {word.upper() for word in words.words() if len(word) == 3}

# Brute-force all possible 3-letter keys (0-255 range for each byte).
with open("generated/plaintexts.txt", "w") as f:
    # Try all possible 3-byte keys.
    for key in itertools.product(range(256), repeat=3):
        # Decrypt using XOR.
        decrypted = [ciphertext_ints[i] ^ key[i] for i in range(3)]

        # Convert to characters.
        plaintext = "".join(chr(c) for c in decrypted)

        # Check if is a valid English word.
        if plaintext in words:
            # Write the plaintext and its corresponding key to the file.
            f.write(f"{plaintext} - Key: {' '.join(map(str, key))}\n")
