# TODO: not used at the moment
import argparse

def main(mapping_file):
    print(mapping_file)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Process some files.')
    parser.add_argument('mapping_file', type=str, help='The input file to process')

    args = parser.parse_args()

    main(args.mapping_file)
