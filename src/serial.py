import sys
from Bio import SeqIO


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
    file_name = sys.argv[1]
    for record in SeqIO.parse(file_name, 'fasta'):
        print("Longitud de la cadena: %d" % len(record))
        _string = record.seq
        a, c, g, t, n = counting(_string)
        print("A: {} C: {} G: {} T: {}".format(a, c, g, t))
        print("Cantidad de N: %d" % n)


if __name__ == "__main__":
    main()