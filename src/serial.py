#!/usr/bin/python
import sys
from Bio import SeqIO
from time import time

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
    start_time = time()
 
    file_name = sys.argv[1]
    for record in SeqIO.parse(file_name, "fasta"):
        print("Longitud de la cadena: %d" % len(record))
        _string = record.seq
        a, c, g, t, u, w, s, m, k, r, y, b, d, h, v, n, z = counting(_string)
        print("A: {} C: {} G: {} T: {}".format(a, c, g, t))
        print("OTRAS BASES")
        print("U: {} W: {} S: {} M: {} K: {} R: {} Y: {} B: {} D: {} H: {} V: {} N: {} Z: {} \n".format(
            u, w, s, m, k, r, y, b, d, h, v, n, z))
    elapsed_time = (time() - start_time)/60
    print("tiempo transcurrido: %0.10f minutos." % elapsed_time)


if __name__ == "__main__":
    main()
