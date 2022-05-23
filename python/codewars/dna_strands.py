def DNA_strand(dna):
    out = ""
    for each in dna:
        if "T" in each:
            out = out + "A"
        elif "A" in each:
            out = out + "T"
        elif "C" in each:
            out = out + "G"
        elif "G" in each:
            out = out + "C"
    return out
