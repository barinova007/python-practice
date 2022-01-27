import sys
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('--name', type=str)
parser.add_argument('--age', type=str)

args = parser.parse_args()
print("Name")
