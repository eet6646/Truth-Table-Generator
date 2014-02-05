
import argparse


def genTruthTable(nBits):
    """
        Generator yielding truth table row
    """
    toBin = lambda x: bin(x)[2:]
    decMax = 2**nBits
    for i in xrange(decMax):
        row = list(toBin(i).zfill(nBits))
        yield row


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Generate a truth table')
    parser.add_argument('-nb', '--nbits', type=int, help='Number of bits the truth table should contain')
    parser.add_argument('-o', '--outputfile', type=str, help='Output to text file')
    parser.add_argument('-s', '--separator', type=str, default='', help='Separator')
    parser.add_argument('-v', '--verbose', action='store_true', default=False, help='Should output to console')
    
    args = parser.parse_args()

    nBits = args.nbits
    outputFile = args.outputfile
    verbose = args.verbose
    separator = args.separator

    if not nBits: # Interactive mode enabled
        nBits = int(raw_input('Number of bits the truth table should contain: '))
        outputFile = outputFile or raw_input('Output file [none]: ')
        verbose = verbose or bool(raw_input('Should output to console [1/0]: '))
        separator = separator or raw_input('Separator: ')

    tTable = genTruthTable(nBits)

    hOutputFile = None
    if outputFile:
        hOutputFile = open(outputFile, 'w')

    for row in tTable:
        if verbose:
            print separator.join(row)

        if hOutputFile:
            hOutputFile.write(separator.join(row) + '\n')

    if hOutputFile:
        hOutputFile.close()
