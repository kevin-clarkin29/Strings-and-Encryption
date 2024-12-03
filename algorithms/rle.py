"""
Module for Run-Length Encoding (RLE) functionality.
"""

def run_length_encode(message):
    """
    Compress a string using run-length encoding.
    :param message: The string to compress.
    :return: The run-length encoded string.
    """
    if not message:
        return ""

    encoded = []
    count = 1

    # Iterate through the string and count consecutive characters
    for i in range(1, len(message)):
        if message[i] == message[i - 1]:
            count += 1
        else:
            encoded.append(f"{count}{message[i - 1]}")
            count = 1

    # Append the last character and its count
    encoded.append(f"{count}{message[-1]}")

    return ''.join(encoded)


def run_length_decode(encoded_message):
    """
    Decompress a run-length encoded string.
    :param encoded_message: The run-length encoded string.
    :return: The original uncompressed string.
    """
    if not encoded_message:
        return ""

    decoded = []
    i = 0

    while i < len(encoded_message):
        count = int(encoded_message[i])  # The count of characters
        char = encoded_message[i + 1]  # The character itself
        decoded.append(char * count)  # Append the character repeated 'count' times
        i += 2  # Move to the next pair (count, character)

    return ''.join(decoded)

if __name__ == "__main__":
    # Test cases for run_length_encode
    print(run_length_encode("AAAABBBCCDAA"))  # Expected: "4A3B2C1D2A"
    print(run_length_encode(""))             # Expected: ""
    print(run_length_encode("A"))            # Expected: "1A"

    # Test cases for run_length_decode
    print(run_length_decode("4A3B2C1D2A"))   # Expected: "AAAABBBCCDAA"
    print(run_length_decode(""))             # Expected: ""
    print(run_length_decode("1A"))           # Expected: "A"
