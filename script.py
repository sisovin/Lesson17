# -*- coding: utf-8 -*-
"""
Created on Sat Jul 27 16:38:59 2024

@author: chien
"""
# %%
""" import argparse

# Create the parser
parser = argparse.ArgumentParser(description="Example script with positional and optional arguments.")

# Add positional argument
parser.add_argument("positional_arg", type=str, help="A positional argument.")

# Add optional argument
parser.add_argument("-o", "--optional_arg", type=str, help="An optional argument.", default="default_value")

# Parse the arguments
args = parser.parse_args()

# Use the arguments
print(f"Positional Argument: {args.positional_arg}")
print(f"Optional Argument: {args.optional_arg}")


print("Done.") """
# %%
import argparse

# Create the parser
parser = argparse.ArgumentParser(description="Example script with various use cases for command line arguments.")

# Add arguments
parser.add_argument("input_file", type=str, help="Path to the input file.")
parser.add_argument("output_file", type=str, help="Path to the output file.")
parser.add_argument("-v", "--verbose", action="store_true", help="Enable verbose mode.")
parser.add_argument("--learning-rate", type=float, default=0.01, help="Learning rate for the algorithm.")
parser.add_argument("--epochs", type=int, default=10, help="Number of epochs for training.")
parser.add_argument("--username", type=str, help="Username for authentication.")
parser.add_argument("--password", type=str, help="Password for authentication.")
parser.add_argument("--filter", type=str, help="Filter criteria for data processing.")
parser.add_argument("--version", action="version", version="%(prog)s 1.0")

# Parse the arguments
args = parser.parse_args()

# Use the arguments
print(f"Input File: {args.input_file}")
print(f"Output File: {args.output_file}")
if args.verbose:
    print("Verbose mode enabled.")
print(f"Learning Rate: {args.learning_rate}")
print(f"Epochs: {args.epochs}")
if args.username and args.password:
    print(f"Authenticated as {args.username}")
if args.filter:
    print(f"Filter: {args.filter}")