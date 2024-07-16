import argparse

def main():
    parser = argparse.ArgumentParser(description="A program to demonstrate command-line argument parsing.")

    parser.add_argument('-i', required=True, type=str, help="Input string (required)")
    parser.add_argument('-o', required=True, type=str, help="Output string (required)")
    parser.add_argument('-a', required=True, type=str, choices=['windows', 'linux'], help="Platform (required, either 'windows' or 'linux')")
    parser.add_argument('-s', type=str, default="/src", help="Source directory (optional, defaults to '/src')")

    args = parser.parse_args()

    input_str = args.i
    output_str = args.o
    platform = args.a
    source_dir = args.s

    # Example processing based on the platform
    if platform == 'windows':
        print(f"Processing for Windows with input '{input_str}', output '{output_str}', and source '{source_dir}'")
    elif platform == 'linux':
        print(f"Processing for Linux with input '{input_str}', output '{output_str}', and source '{source_dir}'")
    else:
        print("Invalid platform. This should never happen due to argparse validation.")

if __name__ == "__main__":
    main()
