import argparse
import os
import sys
import cipher

KEY_FILE_DEFAULT = os.path.join(os.path.expanduser("~"), ".cipher_key")


def parse_args():
    description = "encryption and decryption tool"
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
                "nargs": "?",
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


def get_input(text, path):
    if text:
        return text
    if not sys.stdin.isatty():
        if not path:
            return sys.stdin.read()
        else:
            print("ciphercmd error: argument -i: not allowed with argument -f")
            sys.exit(1)
    if path:
        return path
    print("ciphercmd error: one of the arguments -i -f is required")
    sys.exit(1)


def get_key(text, path):
    if text:
        return text
    if path:
        if os.path.isfile(path):
            return read_path(path)
        else:
            print("ciphercmd error: key file not found: %s" % path)
    if os.path.isfile(KEY_FILE_DEFAULT):
        return read_path(KEY_FILE_DEFAULT)
    print("ciphercmd error: one of the arguments -k -s is required")
    sys.exit(1)


def encrypt(to_proc, key, is_file, out=None):
    if is_file:
        to_proc = read_path(to_proc)

    if out:
        cipher.write(out, key, to_proc)
    else:
        sys.stdout.write(cipher.encrypt(key, to_proc))


def decrypt(to_proc, key, is_file, out=None):
    if is_file:
        txt = cipher.read(to_proc, key)
    else:
        txt = cipher.decrypt(key, to_proc)

    if out:
        with open(out, "w") as fd:
            fd.write(txt)
    else:
        sys.stdout.write(txt)


def main():
    parser = parse_args()
    if len(sys.argv) == 1:
        parser.print_help(sys.stderr)
        sys.exit(1)
    args = parser.parse_args()

    to_proc = get_input(args.input, args.file)
    key = get_key(args.key_str, args.key_file)

    args.func(to_proc, key, not not args.file, args.output)


if __name__ == "__main__":
    main()
