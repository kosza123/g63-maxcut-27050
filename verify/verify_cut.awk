# Independent Max-Cut verifier (POSIX awk).
# Usage: awk -f verify_cut.awk ../solution/G63_maxcut_27050.txt G63
# First file: partition (n characters 0/1, character k = side of vertex k).  Second file: G-set graph.
NR == FNR { gsub(/[ \t\r\n]/, ""); s = s $0; next }
FNR == 1  { n = $1; m = $2; if (length(s) != n) { print "partition length " length(s) " != n " n; exit 1 } ; next }
NF == 3   { e++; if (substr(s, $1, 1) != substr(s, $2, 1)) cut += $3 }
END       { if (e != m) { print "edge count " e " != m " m; exit 1 } ; print "n", n, "m", m, "edges", e; print "CUT", cut }
