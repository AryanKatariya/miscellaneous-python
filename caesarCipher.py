from __future__ import print_function
import os
import string
import argparse

try:
    maketrans = string.maketrans  # python2
except AttributeError:
    maketrans = str.maketrans  # python3


def caeser_cipher(string_: str, offset: int, decode: bool, file_: string):
    if file_ and os.path.exists(file_):
        with open(file_, "r") as f:
            string_ = f.read()

    if decode:
        offset *= -1

    lower_offset_alphabet = (
        string.ascii_lowercase[offset:] + string.ascii_lowercase[:offset]
    )
    lower_translation_table = maketrans(
        string.ascii_lowercase, lower_offset_alphabet)

    upper_offset_alphabet = (
        string.ascii_uppercase[offset:] + string.ascii_uppercase[:offset]
    )
    upper_translation_table = maketrans(
        string.ascii_uppercase, upper_offset_alphabet)

    lower_converted = string_.translate(lower_translation_table)
    final_converted = lower_converted.translate(upper_translation_table)

    if file_:
        extension = "dec" if decode else "enc"
        with open("{}.{}".format(file_, extension), "w") as f:
            print(final_converted, file=f)
    else:
        print(final_converted)


def check_offset_range(value: int) -> int:
    value = int(value)
    if value < -25 or value > 25:
        raise argparse.ArgumentTypeError(
            "{} is an invalid offset".format(value))
    return value


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Simple Caeser Cipher Encoder and Decoder"
    )

    parser.add_argument(
        "-d",
        "--decode",
        action="store_true",
        dest="decode",
        help="decode ciphertext (offset should equal what was used to encode)",
        default=False,
    )
    parser.add_argument(
        "-o",
        "--offset",
        dest="offset",
        default=13,
        type=check_offset_range,
        help="number of characters to shift",
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-f", "--file", dest="file",
                       help="file to encode", default=None)
    group.add_argument(
        "-s", "--string", dest="string", help="string to encode", default=None
    )

    args = parser.parse_args()

    caeser_cipher(args.string, args.offset, args.decode, args.file)
