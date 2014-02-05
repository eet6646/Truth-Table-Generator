Truth-Table-Generator
=====================

Generate a truth table for a given number of bits.

```no-highlight
usage: truthTableGen.py [-h] [-nb NBITS] [-o OUTPUTFILE] [-s SEPARATOR] [-v]

Generate a truth table

optional arguments:
  -h, --help            show this help message and exit
  -nb NBITS, --nbits NBITS
                        Number of bits the truth table should contain
  -o OUTPUTFILE, --outputfile OUTPUTFILE
                        Output to text file
  -s SEPARATOR, --separator SEPARATOR
                        Separator
  -v, --verbose         Should output to console
```

Examples
-------

```bash
$ python truthTableGen.py -nb 3 -v
000
001
010
011
100
101
110
111
```

CSV Output for quick Excel importing
```bash
$ python truthTableGen.py -nb 3 -v -o output.csv -s ,
0,0,0
0,0,1
0,1,0
0,1,1
1,0,0
1,0,1
1,1,0
1,1,1
```

License
-------

All of the code contained here is licensed by [MIT](https://github.com/eet6646/Truth-Table-Generator/blob/master/LICENSE)