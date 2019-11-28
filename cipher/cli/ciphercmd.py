import argparse
import os
import sys
import cipher

KEY_FILE_DEFAULT = os.path.join(os.path.expanduser("~"), ".cipher_key")


def parse_args():
    description = "ciphercmd: encryption and decryption tool"
    parser = argparse.ArgumentParser(description=description)
    parser.add_argument("-v",
                        "--version",
                        action="version",
                        version=cipher.__version__)
    mode = parser.add_subparsers()
    encr = mode.add_parser("encrypt",
                           description="encrypt",
                           help="encryption mode")
    encr.set_defaults(func=encrypt)
    encr_gin = encr.add_mutually_exclusive_group()
    encr_gkey = encr.add_mutually_exclusive_group()
    decr = mode.add_parser("decrypt",
                           description="decrypt",
                           help="decryption mode")
    decr.set_defaults(func=decrypt)
    decr_gin = decr.add_mutually_exclusive_group()
    decr_gkey = decr.add_mutually_exclusive_group()
    optional_args = [
        {
            "args": ("-i",),
            "kwargs": {
                "dest": "input",
                "help": "input to %s"
            }
        }, {
            "args": ("-f",),
            "kwargs": {
                "dest": "file",
                "help": "file to %s"
            }
        }, {
            "args": ("-k",),
            "kwargs": {
                "dest": "key_file",
                "help": "file with the key to %s, default: ~/.cipher_key"
            }
        }, {
            "args": ("-s",),
            "kwargs": {
                "dest": "key_str",
                "help": "key to %s"
            }
        }, {
            "args": ("-o",),
            "kwargs": {
                "dest": "output",
                "help": "%sed output file"
            }
        },
    ]
    subparsers = (encr, decr)
    groups = {
        "encrypt": [encr_gin, encr_gkey],
        "decrypt": [decr_gin, decr_gkey]
    }
    for mode in subparsers:
        desc = mode.description
        for arg in optional_args:
            args = arg["args"]
            kwargs = arg["kwargs"].copy()
            kwargs["help"] = kwargs["help"] % desc
            if args[0] in ("-i", "-f"):
                groups[desc][0].add_argument(*args, **kwargs)
            elif args[0] in ("-k", "-s"):
                groups[desc][1].add_argument(*args, **kwargs)
            else:
                mode.add_argument(*args, **kwargs)

    return parser


def read_path(path):
    with open(path, "r") as fd:
        return fd.read()


def get_str(string, path, var, read_file=False):
    if string:
        return string
    if path and os.path.isfile(path):
        return read_path(path) if read_file else path

    print("%s not found: %s" % (var, path))
    sys.exit(1)


def encrypt(to_proc, key, is_file, out=None):
    if is_file:
        to_proc = read_path(to_proc)

    if out:
        cipher.write(out, key, to_proc)
    else:
        print(cipher.encrypt(key, to_proc))


def decrypt(to_proc, key, is_file, out=None):
    if is_file:
        txt = cipher.read(to_proc, key)
    else:
        txt = cipher.decrypt(key, to_proc)

    if out:
        with open(out, "w") as fd:
            fd.write(txt)
    else:
        print(txt)


def main():
    parser = parse_args()
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    args = parser.parse_args()

    to_proc = get_str(args.input, args.file, "FILE")
    key = get_str(args.key_str, args.key_file, "KEY_FILE", True)

    args.func(to_proc, key, not args.input, args.output)


if __name__ == "__main__":
    main()
