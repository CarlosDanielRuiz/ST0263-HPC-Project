#!/usr/bin/python
import sys
import multiprocessing as mp

from math import ceil
from Bio import SeqIO
from textwrap import wrap

CORES = mp.cpu_count()


def counting(long_string):
    count_a = count_c = count_g = count_t = count_u = count_w = count_s = count_m = count_k = count_r = count_y = count_b = count_d = count_h = count_v = count_n = count_z = 0
    for i in long_string:
        if i.upper() == 'A':
            count_a += 1
        elif i.upper() == 'C':
            count_c += 1
        elif i.upper() == 'G':
            count_g += 1
        elif i.upper() == 'T':
            count_t += 1
        elif i.upper() == 'U':
            count_u += 1
        elif i.upper() == 'W':
            count_w += 1
        elif i.upper() == 'S':
            count_s += 1
        elif i.upper() == 'M':
            count_m += 1
        elif i.upper() == 'K':
            count_k += 1
        elif i.upper() == 'R':
            count_r += 1
        elif i.upper() == 'Y':
            count_y += 1
        elif i.upper() == 'B':
            count_b += 1
        elif i.upper() == 'D':
            count_d += 1
        elif i.upper() == 'H':
            count_h += 1
        elif i.upper() == 'V':
            count_v += 1
        elif i.upper() == 'N':
            count_n += 1
        else:
            count_z += 1

    return count_a, count_c, count_g, count_t, count_u, count_w, count_s, count_m, count_k, count_r, count_y, count_b, count_d, count_h, count_v, count_n, count_z


def main():
    print("Cores de la maquina: %d \n" % CORES)
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
        print("A: {a} C: {c} G: {g} T: {t}".format(
            a=total[0], c=total[1], g=total[2], t=total[3]))
        print("OTRAS BASES")
        print("U: {u} W: {w} S: {s} M: {m} K: {k} R: {r} Y: {y} B: {b} D: {d} H: {h} V: {v} N: {n} Z: {z} \n".format(
            u=total[4], w=total[5], s=total[6], m=total[7], k=total[8], r=total[9], y=total[10], b=total[11], d=total[12], h=total[13], v=total[14], n=total[15], z=total[16]))


if __name__ == "__main__":
    main()
