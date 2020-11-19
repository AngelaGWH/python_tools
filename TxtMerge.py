'''
Created on Nov 11, 2020

@author: wgao002
'''
import os
import sys
import argparse

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Merge all files under one directory into one")
    parser.add_argument("dir", type=str, help="input the directory")
    parser.add_argument("out_file", type=str, help="the result file name")
    args = parser.parse_args()
    input_dir = args.dir
    output_file = args.out_file
    print("The directory you input is :", input_dir)
    print("Your result will be put in : ", output_file)

    files = os.listdir(input_dir)

    outfile = open(output_file, 'w')
    for file in files:
        with open(os.path.join(input_dir,file), 'r') as content:
            for line in content:
                outfile.write(line)
    print("Done!")
    pass
