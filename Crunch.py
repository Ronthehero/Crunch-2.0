import itertools
import os
import shutil
import subprocess

def estimate_size(min_len, max_len, charset):
    total = 0
    for length in range(min_len, max_len + 1):
        avg_line_len = length + 1  # includes newline
        total += (len(charset) ** length) * avg_line_len
    return total

def generate_wordlist(min_len, max_len, charset, output_file):
    with open(output_file, 'w') as f:
        for length in range(min_len, max_len + 1):
            for combo in itertools.product(charset, repeat=length):
                f.write(''.join(combo) + '\n')

def print_ascii_logo():
    if shutil.which("figlet"):
        try:
            subprocess.run(["figlet", "Crunch 2 . 0"], check=True)
        except Exception:
            print("=== Crunch 2.0, your Friendly, OP & Sexy WordList Generator ===")
    else:
        print("=== Crunch 2.0, your Friendly, OP & Sexy WordList Generator ===")

def main():
    print_ascii_logo()
    charset_input = input("Enter characters to include (e.g. abc123@^,): ")
    min_len = int(input("Enter minimum password length: "))
    max_len = int(input("Enter maximum password length: "))
    output_file = input("Enter output file name (e.g. wordlist.txt): ")

    size_bytes = estimate_size(min_len, max_len, charset_input)
    size_mb = size_bytes / (1024 ** 2)

    print(f"\nEstimated size: {size_mb:.2f} MB")
    choice = input("Continue? [Y/N]: ").strip().lower()

    if choice.startswith('y'):
        generate_wordlist(min_len, max_len, charset_input, output_file)
        print(f"Wordlist saved to: {output_file}")
    elif choice.startswith('n'):
        print("Operation cancelled")
    else:
        print("INVALID OPTION")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n[!] Operation interrupted by user. Exiting cleanly.")
