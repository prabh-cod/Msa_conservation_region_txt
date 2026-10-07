<!-- harbor-canary -->
Analyze the provided Multiple Sequence Alignment (MSA) to identify the most evolutionarily conserved genomic region.

Scoring is binary: all requirements must be satisfied as a single unit to pass.

### Requirements
1. Parse the DNA sequence alignment from `/root/task/alignment.fasta`.
2. Calculate the Shannon entropy for every column (position) in the alignment. Treat gaps (`-`) as a valid character state. Use base 2 for the logarithm.
3. Calculate a sliding window average of the entropy using a window size of 15 base pairs.
4. Identify the 0-indexed start position of the 15-bp window with the absolute lowest average entropy (highest conservation). In case of a tie, choose the first occurring window.
5. Write exactly the following string to `/root/solution/conservation_report.txt`:
   `Most conserved 15-bp window starts at: <position> with entropy: <mean_entropy>`
   Replace `<position>` with your calculated integer index and `<mean_entropy>` formatted to exactly four decimal places (e.g., 0.0251).
