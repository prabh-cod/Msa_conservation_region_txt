import os
import math
import pytest

def test_conservation_report():
    """Verify independent parsing, entropy calculation, and window identification on held-out data."""
    report_path = "/root/solution/conservation_report.txt"
    assert os.path.exists(report_path), "conservation_report.txt is missing"
    
    # 1. Independent Derivation from Held-Out Data
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
        
    num_seqs = len(seqs)
    seq_len = len(seqs[0])
    
    entropies = []
    for col in range(seq_len):
        counts = {}
        for seq in seqs:
            counts[seq[col]] = counts.get(seq[col], 0) + 1
        ent = 0.0
        for count in counts.values():
            p = count / num_seqs
            ent -= p * math.log2(p)
        entropies.append(ent)
        
    min_ent = float('inf')
    min_idx = -1
    for i in range(seq_len - 14):
        window_ent = sum(entropies[i:i+15]) / 15
        if window_ent < min_ent:
            min_ent = window_ent
            min_idx = i
            
    expected_string = f"Most conserved 15-bp window starts at: {min_idx} with entropy: {min_ent:.4f}"
    
    # 2. Strict Correctness Check
    with open(report_path, "r") as f:
        agent_report = f.read().strip()
        
    assert agent_report == expected_string, f"Report mismatch. Expected: '{expected_string}', Found: '{agent_report}'"