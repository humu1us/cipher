import argparse
import os.path as path
import cipher


def parse_args():
    parser = argparse.ArgumentParser(
                 description="ciphercmd: encryption and decryption tool"
            )

    parser.add_argument("-f",
                        "--file",
                        dest="file",
                        type=str,
                        required=True,
                        help="File to encrypt")

    parser.add_argument("-k",
                        "--key",
                        dest="key",
                        type=str,
                        required=False,
                        default=path.join(path.expanduser("~"), ".passwd"),
                        help="Key used to encrypt the file")

    parser.add_argument("-o",
                        "--output",
                        dest="out",
                        type=str,
                        required=False,
                        default="file.out",
                        help="File name for the result file")

    parser.add_argument("-e",
                        "--encrypt",
                        dest="enc",
                        action="store_true",
                        help="Use ciphercmd in encryption mode")

    parser.add_argument("-d",
                        "--decrypt",
                        dest="dec",
                        action="store_true",
                        help="Use ciphercmd in decryption mode")

    return parser


def read_path(path):
    with open(path, "r") as fd:
        return fd.read()


def encrypt(fname, key_path, out):
    key = read_path(key_path)
    txt = read_path(fname)
    cipher.write(out, key, txt)


def decrypt(fname, key_path, out):
    key = read_path(key_path)
    txt = cipher.read(fname, key)

    with open(out, "w") as fd:
        fd.write(txt)


def main():
    parser = parse_args()
    args = parser.parse_args()

    if args.enc and args.dec:
        print("Error, encrypt and decrypt flags are exclusives")
        parser.print_help()

    if args.enc:
        encrypt(args.file, args.key, args.out)
    elif args.dec:
        decrypt(args.file, args.key, args.out)
    else:
        print("Need an action ('--encrypt' or '--decrypt')")
        parser.print_help()


if __name__ == "__main__":
    main()
