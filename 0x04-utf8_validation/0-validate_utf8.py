#!/usr/bin/python3
"""
 a method that determines if a given data set represents a valid 
 UTF-8 encoding.
"""


def validUTF8(data):
    # Number of expected continuation bytes for the current character
    num_bytes = 0

    # Masks and patterns for checking the number of bytes and
    # continuation bytes
    byte_masks = [
        (0b10000000, 0b00000000),  # 1-byte character (0xxxxxxx)
        (0b11100000, 0b11000000),  # 2-byte character (110xxxxx)
        (0b11110000, 0b11100000),  # 3-byte character (1110xxxx)
        (0b11111000, 0b11110000)   # 4-byte character (11110xxx)
    ]
    # Continuation byte (10xxxxxx)
    continuation_mask = (0b11000000, 0b10000000)

    for byte in data:
        byte = byte & 0xFF  # Limit to 8 bits

        if num_bytes == 0:
            # Determine how many bytes the character should have
            for i, (mask, pattern) in enumerate(byte_masks, 1):
                if byte & mask == pattern:
                    num_bytes = i
                    break
            else:
                # If no valid starting pattern is found, return False
                return False
        else:
            # Check if the byte matches the continuation byte pattern
            if byte & continuation_mask[0] != continuation_mask[1]:
                return False

        # Reduce the expected continuation bytes
        num_bytes -= 1

    # Return True if no extra continuation bytes are expected
    return num_bytes == 0
