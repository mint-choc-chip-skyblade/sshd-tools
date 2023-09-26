# SSHD Object Analyser

This is a handy script for analysing objects in The Legend of Zelda: Skyward
Sword HD. It should work for the Wii version but it hasn't been tested for it
so your mileage may vary.

## Features

This script can:

* Find all objects with a given name/s, on a given stage/s, and of a given
  type/s
  * These can be mixed and matched in any combination
* Highlight a given attribute of each object
* Shift and mask the given attribute to isolate a sepecific part of the given
  attribute
* Output values in decimal (default), hexadecimal, or binary
* Display a summary of all the unique values of the given attribute (with
  shift and mask applied) that were found

## How to

You will need to obtain the `.json` files for each stage from
[lepelog](https://github.com/lepelog)'s fork of the
[skywardsword-tools](https://github.com/lepelog/skywardsword-tools)
repository. Specifically, you will need the files in the `stageHD` directory
from the `output` branch:
https://github.com/lepelog/skywardsword-tools/tree/output/stageHD

Place the `stageHD` directory in the same place as the `analyse-objects.py`
file.

### Help Command

```
usage: analyse-objects.py [-h] [--stages [STAGES ...]] [--names [NAMES ...]] [--types [TYPES ...]] [--attribute [ATTRIBUTE]] [--shift [SHIFT]] [--mask [MASK]] [--hex] [--bin] [--summary]

A tool to help analyse the properties of objects in The Legend of Zelda: Skyward Sword (HD).

options:
  -h, --help            show this help message and exit
  --stages [STAGES ...]
                        A list of stages to include in the search. If none are given, all stages will be included.
  --names [NAMES ...]   A list of object names to include in the search. If none are given, all names will be included.
  --types [TYPES ...]   A list of the object types to include in the search. If none are given, all types will be included.
  --attribute [ATTRIBUTE]
                        Only include objects with the given attribute. This attribute is the subject of any shifts or masks also defined. If no attribute is
                        given, param1 is used.
  --shift [SHIFT]       The number of bits to shift the attribute by. If no attribute is given, param1 is used.
  --mask [MASK]         The mask applied to the attribute. If no attribute is given, param1 is used.
  --hex                 Determines if integer values should be outputted in hexadecimal.
  --bin                 Determines if integer values should be outputted in binary.
  --summary             If this argument is given, print a summary of all the unique results found.
```

### Examples

Find all objects from multiple stages with one of the provided names. Get its
`params2` attribute and output it in hex for each object. Then provide a
summary of all the unique values of `params2` that were found.

Output:
```
>analyse-objects.py --stages F001r F009r --names TBox Tubo --attribute params2 --hex --summary
Tubo            F001r   l1  r00 FC 75 params2: 0xffffffff  -> 0xffffffff
Tubo            F001r   l1  r00 FC 76 params2: 0xffffffff  -> 0xffffffff
Tubo            F001r   l1  r00 FC 77 params2: 0xffffffff  -> 0xffffffff
Tubo            F001r   l1  r00 FC 78 params2: 0xffffffff  -> 0xffffffff
Tubo            F001r   l2  r00 FC 78 params2: 0xffffffff  -> 0xffffffff
Tubo            F001r   l2  r00 FC 79 params2: 0xffffffff  -> 0xffffffff
TBox            F001r   l3  r00 FC 79 params2: 0xff5fffff  -> 0xff5fffff
TBox            F001r   l3  r00 FC 80 params2: 0xff5fffff  -> 0xff5fffff
Tubo            F001r   l3  r00 FC 81 params2: 0xffffffff  -> 0xffffffff
Tubo            F001r   l3  r00 FC 82 params2: 0xffffffff  -> 0xffffffff
TBox            F001r   l4  r00 FC 7F params2: 0xff5fffff  -> 0xff5fffff
Tubo            F001r   l4  r00 FC 78 params2: 0xffffffff  -> 0xffffffff
Tubo            F001r   l4  r00 FC 79 params2: 0xffffffff  -> 0xffffffff
TBox            F001r   l0  r01 FC 09 params2: 0xff5fffff  -> 0xff5fffff
TBox            F001r   l0  r06 FC 08 params2: 0xff5fffff  -> 0xff5fffff
TBox            F009r   l0  r00 FC 00 params2: 0xff5fffff  -> 0xff5fffff
Unique Results:
0xffffffff occured 10 times
0xff5fffff occured 6 times
```


Find all the `Wind` objects in stage `D300_1`. Get the `anglez` attribute of
each object, shift it to the right by 8 and mask it with 3. Show the results
in binary and provide a summary of all the unique values of `anglez` (with the
given shift and mask) that were found.

```
>analyse-objects.py --stages D300_1 --names Wind --attribute anglez --shift 8 --mask 3 --bin --summary
Wind            D300_1  l0  r05 FC 7A anglez: 0b111111111 -> 0b1
Wind            D300_1  l0  r05 FC 7B anglez: 0b111111111 -> 0b1
Wind            D300_1  l0  r05 FC 7C anglez: 0b111111111 -> 0b1
Wind            D300_1  l0  r05 FC 7D anglez: 0b111111111 -> 0b1
Wind            D300_1  l0  r05 FC 7E anglez: 0b111111111 -> 0b1
Wind            D300_1  l0  r05 FC 7F anglez: 0b111111111 -> 0b1
Wind            D300_1  l0  r05 FC 80 anglez: 0b111111111 -> 0b1
Wind            D300_1  l0  r08 FC 52 anglez: 0b1111111111 -> 0b11
Wind            D300_1  l0  r08 FC 53 anglez: 0b1111111111 -> 0b11
Wind            D300_1  l0  r08 FC 54 anglez: 0b1111111111 -> 0b11
Wind            D300_1  l0  r08 FC 55 anglez: 0b1111111111 -> 0b11
Wind            D300_1  l0  r08 FC 56 anglez: 0b1111111111 -> 0b11
Wind            D300_1  l0  r08 FC 57 anglez: 0b1111111111 -> 0b11
Wind            D300_1  l0  r08 FC 58 anglez: 0b1111111111 -> 0b11
Unique Results:
0b1 occured 7 times
0b11 occured 7 times
```


Find all the `Smoke` objects and get each of their `angley` attributes. Shift
by `0x8` and mask with `0xFF`.

```
>analyse-objects.py --names Smoke --attribute angley --shift 0x8 --mask 0xFF
Smoke           F200    l0  -1  FC 00 angley: 0           -> 0
Smoke           F201_3  l0  -1  FC 00 angley: 32768       -> 128
Smoke           F201_4  l0  -1  FC 00 angley: 17840       -> 69
Smoke           F202    l0  -1  FC 07 angley: 0           -> 0
Smoke           S200    l2  -1  FC 00 angley: 0           -> 0
```
