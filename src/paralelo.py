#!/usr/bin/python
import sys
import multiprocessing as mp

from math import ceil
from Bio import SeqIO
from textwrap import wrap

CORES = mp.cpu_count()

def counting(long_string):
    count_a = count_c = count_g = count_t = count_n = 0
    for i in long_string:
        if i == 'A':
            count_a += 1
        elif i == 'C':
            count_c += 1
        elif i == 'G':
            count_g += 1
        if i == 'T':
            count_t += 1
        else:
            count_n += 1

    return count_a, count_c, count_g, count_t, count_n


def main():
    print("Cores de la maquina: %d" % CORES)
    file_name = sys.argv[1]
    for record in SeqIO.parse(file_name, 'fasta'):
        POOL = mp.Pool(CORES)
        print("Longitud de la cadena: %d" % len(record))
        _string = record.seq
        part_length = ceil(len(_string)/CORES)
        print("Longitud de las particiones: %d" % part_length)
        string_parts = wrap(str(_string), part_length)
        results = POOL.map(counting, [part for part in string_parts])
        POOL.close()
        total = tuple(map(sum, zip(*results)))
        print("A: {a} C: {c} G: {g} T: {t}".format(a = total[0], c = total[1], g = total[2], t = total[3]))
        print("Cantidad de N: {n} \n".format(n=total[4]))

if __name__ == "__main__":
    main()
