#!/usr/bin/env node
// Independent Max-Cut verifier (Node.js, no dependencies).
// Usage: node verify_cut.js G63 ../solution/G63_maxcut_27050.txt
// G63: original G-set file ("n m" header, then "i j w" per line, 1-based vertices).
// Partition: n characters '0'/'1'; character k is the side of vertex k+1.
"use strict";
const fs = require("fs");
const crypto = require("crypto");
const [graphPath, partPath] = process.argv.slice(2);
if (!graphPath || !partPath) { console.error("usage: node verify_cut.js GRAPH PARTITION"); process.exit(1); }
const raw = fs.readFileSync(graphPath);
const lines = raw.toString("ascii").split("\n");
const [n, m] = lines[0].trim().split(/\s+/).map(Number);
const part = fs.readFileSync(partPath, "ascii").replace(/\s+/g, "");
if (part.length !== n || /[^01]/.test(part)) { console.error("partition must contain exactly n characters 0/1"); process.exit(1); }
let edges = 0, cut = 0, total = 0;
for (let k = 1; k < lines.length; k++) {
  const f = lines[k].trim().split(/\s+/);
  if (f.length !== 3) continue;
  const i = Number(f[0]), j = Number(f[1]), w = Number(f[2]);
  if (i < 1 || i > n || j < 1 || j > n || i === j) { console.error("invalid edge: " + lines[k]); process.exit(1); }
  edges++; total += w;
  if (part[i - 1] !== part[j - 1]) cut += w;
}
if (edges !== m) { console.error(`edge count ${edges} != header m ${m}`); process.exit(1); }
console.log("graph sha256     :", crypto.createHash("sha256").update(raw).digest("hex"));
console.log("graph            :", `n=${n} m=${m} total_weight=${total}`);
console.log("partition sha256 :", crypto.createHash("sha256").update(part).digest("hex"));
console.log("CUT              :", cut);
