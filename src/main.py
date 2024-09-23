import sys
import help
import vars
import hexdump

def main():
    args = sys.argv
    if len(args) > 4:
        print("Error: Too many arguments")
        return
    if args[1] == "--help" or args[1] == "-h":
        if len(args) == 2:
            help.select("")
        help.select(args[2])
        return
    if args[1] == "--version" or args[1] == "-v":
        print(f"RevASM version {vars.VERSION} - 2024 Absolute Narwhal\n")
        return
    if len(args) < 3:
        print("Error: No file provided")

    if args[1] == "hexdump":
        hexdump.format(b"todo: make this fucking work.")

main()