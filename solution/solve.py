import math

def main():
    with open("/root/task/alignment.fasta", "r") as f:
        lines = f.read().splitlines()
        
    seqs, curr = [], ""
    for line in lines:
        if line.startswith(">"):
            if curr: seqs.append(curr)
            curr = ""
        else:
            curr += line.strip()
    if curr: seqs.append(curr)
    
    n, l = len(seqs), len(seqs[0])
    
    ents = []
    for i in range(l):
        col = [s[i] for s in seqs]
        counts = {c: col.count(c) for c in set(col)}
        ent = sum(-(c/n) * math.log2(c/n) for c in counts.values())
        ents.append(ent)
        
    min_ent = float('inf')
    min_idx = 0
    for i in range(l - 14):
        avg = sum(ents[i:i+15]) / 15
        if avg < min_ent:
            min_ent = avg
            min_idx = i
            
    with open("/root/solution/conservation_report.txt", "w") as f:
        f.write(f"Most conserved 15-bp window starts at: {min_idx} with entropy: {min_ent:.4f}")

if __name__ == "__main__":
    main()