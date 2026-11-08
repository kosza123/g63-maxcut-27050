#!/usr/bin/env python3
"""Independent Max-Cut verifier for G-set graphs (pure Python 3, no dependencies).

Usage:
    python3 verify_cut.py G63 ../solution/G63_maxcut_27050.txt
    python3 verify_cut.py G63 ../solution/G63_maxcut_27050.hex --hex

G63 is the original G-set file (first line "n m", then one edge "i j w" per line, 1-based),
available from https://web.stanford.edu/~yyye/yyye/Gset/G63 .
The partition file holds n characters '0'/'1'; character k (0-based) is the side of vertex k+1.
The --hex form expands each hexadecimal digit to 4 bits, most significant bit first
(reading the hexadecimal string of arXiv:2510.21105 this way reproduces its value of 27,047).
"""
import hashlib
import sys


def main():
    if len(sys.argv) < 3:
        sys.exit(__doc__)
    graph_path, part_path = sys.argv[1], sys.argv[2]
    raw = open(graph_path, "rb").read()
    lines = raw.decode("ascii").split("\n")
    n, m = map(int, lines[0].split()[:2])
    edges = []
    for line in lines[1:]:
        f = line.split()
        if len(f) == 3:
            i, j, w = int(f[0]), int(f[1]), int(f[2])
            if not (1 <= i <= n and 1 <= j <= n) or i == j:
                sys.exit(f"invalid edge line: {line!r}")
            edges.append((i - 1, j - 1, w))
    if len(edges) != m:
        sys.exit(f"edge count {len(edges)} != header m {m}")
    text = "".join(open(part_path, encoding="ascii").read().split())
    if "--hex" in sys.argv:
        text = "".join(format(int(c, 16), "04b") for c in text)[:n]
    if len(text) != n or set(text) - {"0", "1"}:
        sys.exit("partition must contain exactly n characters '0'/'1'")
    side = [c == "1" for c in text]
    cut = sum(w for i, j, w in edges if side[i] != side[j])
    complement_cut = sum(w for i, j, w in edges if (not side[i]) != (not side[j]))
    print(f"graph sha256     : {hashlib.sha256(raw).hexdigest()}")
    print(f"graph            : n={n} m={m} total_weight={sum(w for _, _, w in edges)}")
    print(f"partition sha256 : {hashlib.sha256(text.encode()).hexdigest()}")
    print(f"vertices on side 1: {sum(side)}")
    print(f"CUT              : {cut}")
    print(f"CUT (complement) : {complement_cut}")


if __name__ == "__main__":
    main()
