# TO DO:
### High priority
1. Script functionality
   1. Sequence Generator object
      1. Read in table to create alphabet and frequencies
      2. Or just use dictionary
   2. Member function to call on generator object that generates sequences
      1. Takes in dictionary, or dictionary like file to get letter freqs.
      2. Options for standard DNA, protien, binary, decimal sequences
2. Rewrite sequence generator to be alphabet agnostic

### Low Priority
1. Diagnostic output
   1. Option to print (silenced by default)
   2. Final letter frequencies
   3. Time analysis.
2. Robust Command line interface
   1. --help functionality
   2. Proper options
   3. Warn if frequencies do not add up to 1.