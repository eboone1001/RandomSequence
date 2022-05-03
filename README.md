# RandomSequence
### Package for easily generating sequences based on a predefined alphabet with frequencies.

Created by 
Eric Boone, 5/2/2022

## About

The purpose of this package is to allow for easy generation of arbitrary numbers and lengths
of sequences. I wanted to make this tool because this was something that was showing up a lot in
my Bioinformatics algorithm classes, and I got sick of coding it. It's final form will have both command
line as well as python scripting functionality.

## Documentation

##### randomDNA.py
Usage: python randomDNA.py <output file> <number of seq.> <length of seq.>

Generates *n* sequences of length *m* and stores them in the user defined file. Uses an alphabet of
A, T, C, and G, each with equal expected proportion in the output string(s)
