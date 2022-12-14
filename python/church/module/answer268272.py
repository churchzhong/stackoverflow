#!/usr/bin/python3

import operator
import timeit


d1 = {
    1: 1,
    2: 2,
    3: 8,
    4: 3,
    5: 6,
    6: 9,
    7: 17,
    8: 4,
    9: 20,
    10: 7,
    11: 15,
    12: 10,
    13: 10,
    14: 18,
    15: 18,
    16: 5,
    17: 13,
    18: 21,
    19: 21,
    20: 8,
    21: 8,
    22: 16,
    23: 16,
    24: 11,
    25: 24,
    26: 11,
    27: 112,
    28: 19,
    29: 19,
    30: 19,
    3077: 36,
    32: 6,
    33: 27,
    34: 14,
    35: 14,
    36: 22,
    4102: 39,
    38: 22,
    39: 35,
    40: 9,
    41: 110,
    42: 9,
    43: 30,
    44: 17,
    45: 17,
    46: 17,
    47: 105,
    48: 12,
    49: 25,
    50: 25,
    51: 25,
    52: 12,
    53: 12,
    54: 113,
    1079: 50,
    56: 20,
    57: 33,
    58: 20,
    59: 33,
    60: 20,
    61: 20,
    62: 108,
    63: 108,
    64: 7,
    65: 28,
    66: 28,
    67: 28,
    68: 15,
    69: 15,
    70: 15,
    71: 103,
    72: 23,
    73: 116,
    74: 23,
    75: 15,
    76: 23,
    77: 23,
    78: 36,
    79: 36,
    80: 10,
    81: 23,
    82: 111,
    83: 111,
    84: 10,
    85: 10,
    86: 31,
    87: 31,
    88: 18,
    89: 31,
    90: 18,
    91: 93,
    92: 18,
    93: 18,
    94: 106,
    95: 106,
    96: 13,
    9232: 35,
    98: 26,
    99: 26,
    100: 26,
    101: 26,
    103: 88,
    104: 13,
    106: 13,
    107: 101,
    1132: 63,
    2158: 51,
    112: 21,
    113: 13,
    116: 21,
    118: 34,
    119: 34,
    7288: 45,
    121: 96,
    122: 21,
    124: 109,
    125: 109,
    128: 8,
    1154: 32,
    131: 29,
    134: 29,
    136: 16,
    137: 91,
    140: 16,
    142: 104,
    143: 104,
    146: 117,
    148: 24,
    149: 24,
    152: 24,
    154: 24,
    155: 86,
    160: 11,
    161: 99,
    1186: 76,
    3238: 49,
    167: 68,
    170: 11,
    172: 32,
    175: 81,
    178: 32,
    179: 32,
    182: 94,
    184: 19,
    31: 107,
    188: 107,
    190: 107,
    196: 27,
    197: 27,
    202: 27,
    206: 89,
    208: 14,
    214: 102,
    215: 102,
    220: 115,
    37: 22,
    224: 22,
    226: 14,
    232: 22,
    233: 84,
    238: 35,
    242: 97,
    244: 22,
    250: 110,
    251: 66,
    1276: 58,
    256: 9,
    2308: 33,
    262: 30,
    263: 79,
    268: 30,
    269: 30,
    274: 92,
    1300: 27,
    280: 17,
    283: 61,
    286: 105,
    292: 118,
    296: 25,
    298: 25,
    304: 25,
    310: 87,
    1336: 71,
    319: 56,
    322: 100,
    323: 100,
    325: 25,
    55: 113,
    334: 69,
    340: 12,
    1367: 40,
    350: 82,
    358: 33,
    364: 95,
    376: 108,
    377: 64,
    2429: 46,
    394: 28,
    395: 77,
    404: 28,
    412: 90,
    1438: 53,
    425: 59,
    430: 103,
    1456: 97,
    433: 28,
    445: 72,
    448: 23,
    466: 85,
    479: 54,
    484: 98,
    485: 98,
    488: 23,
    6154: 37,
    502: 67,
    4616: 34,
    526: 80,
    538: 31,
    566: 62,
    3644: 44,
    577: 31,
    97: 119,
    592: 26,
    593: 75,
    1619: 48,
    638: 57,
    646: 101,
    650: 26,
    110: 114,
    668: 70,
    2734: 41,
    700: 83,
    1732: 30,
    719: 52,
    728: 96,
    754: 65,
    1780: 74,
    4858: 47,
    130: 29,
    790: 78,
    1822: 43,
    2051: 38,
    808: 29,
    850: 60,
    866: 29,
    890: 73,
    911: 42,
    958: 55,
    970: 99,
    976: 24,
    166: 112,
}


def f1():
    '''
    Description :
    '''
    v = list(d1.values())
    k = list(d1.keys())
    return k[v.index(max(v))]


def f2():
    '''
    Description :
    '''
    d3 = {v: k for k, v in d1.items()}
    return d3[max(d3)]


def f3():
    '''
    Description :
    '''
    return list(filter(lambda t: t[1] == max(d1.values()), d1.items()))[0][0]


def f3b():
    '''
    Description :
    '''
    # same as f3 but remove the call to max from the lambda
    m = max(d1.values())
    return list(filter(lambda t: t[1] == m, d1.items()))[0][0]


def f4():
    '''
    Description :
    '''
    return [k for k, v in d1.items() if v == max(d1.values())][0]


def f4b():
    '''
    Description :
    '''
    # same as f4 but remove the max from the comprehension
    m = max(d1.values())
    return [k for k, v in d1.items() if v == m][0]


def f5():
    '''
    Description :
    '''
    return max(d1.items(), key=operator.itemgetter(1))[0]


def f6():
    '''
    Description :
    '''
    return max(d1, key=d1.get)


def f7():
    """a) create a list of the dict's keys and values;
    b) return the key with the max value"""
    v = list(d1.values())
    return list(d1.keys())[v.index(max(v))]


def f8():
    '''
    Description :
    '''
    return max(d1, key=lambda k: d1[k])


def cmpthese(funcs, c=10000, rate=True, micro=False):
    """Generate a Perl style function benchmark"""

    def pprint_table(table):
        """Perl style table output"""

        def format_field(field, fmt='{:,.0f}'):
            if type(field) is str:
                return field
            if type(field) is tuple:
                return field[1].format(field[0])
            return fmt.format(field)

        def get_max_col_w(table, index):
            return max([len(format_field(row[index])) for row in table])

        col_paddings = [get_max_col_w(table, i) for i in range(len(table[0]))]
        for i, row in enumerate(table):
            # left col
            row_tab = [row[0].ljust(col_paddings[0])]
            # rest of the cols
            row_tab += [format_field(row[j]).rjust(col_paddings[j]) for j in range(1, len(row))]
            print(' '.join(row_tab))

    results = {k.__name__: timeit.Timer(k).timeit(c) for k in funcs}
    fastest = sorted(results, key=results.get, reverse=True)
    table = [['']]
    if rate:
        table[0].append('rate/sec')
    if micro:
        table[0].append('usec/pass')
    table[0].extend(fastest)
    for e in fastest:
        tmp = [e]
        if rate:
            tmp.append('{:,}'.format(int(round(float(c) / results[e]))))

        if micro:
            tmp.append('{:.3f}'.format(1000000 * results[e] / float(c)))

        for x in fastest:
            if x == e:
                tmp.append('--')
            else:
                tmp.append('{:.1%}'.format((results[x] - results[e]) / results[e]))
        table.append(tmp)

    pprint_table(table)


if __name__ == '__main__':
    '''
    Description :
    '''
    tl = [f1, f2, f3b, f4b, f5, f6, f7, f8, f4, f3]
    cmpthese(tl, c=100)
