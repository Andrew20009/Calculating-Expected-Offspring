# Calculating Expected Offspring

## OVERVIEW
This program calculates the expected number of offspring displaying the dominant phenotype in the next generation, given the number of couples of each genotype pairing and assuming every couple has exactly two offspring.
It is a solution to the **"Calculating Expected Offspring"** Rosalind problem **(ID: IEV)**. The tool is simple, efficient, and ideal for practicing expected value, probability, and file handling in Python.

---

## FEATURES
- Reads <u>six integers</u> from a text file (`rosalind_iev.txt`), one for each genotype pairing
- Multiplies each pairing by its <u>probability of a dominant offspring</u>
- Multiplies the total by <u>2 offspring per couple</u>
- Clean, well-commented code with proper functions and type hints

---

## ⚠️ IMPORTANT NOTE
> <u>**!!!Please put the input file with name rosalind_iev.txt in the same folder as the code, otherwise you will receive an Error File Not Found!!!**</u>

---

## EXAMPLE
**Input** (rosalind_iev.txt):
```
1 0 0 1 0 1
```
**Output:**
```
3.5
```

---

## HOW IT WORKS
1. Reads the number of couples for each pairing, in order:
   - AA×AA → **100%** dominant
   - AA×Aa → **100%** dominant
   - AA×aa → **100%** dominant
   - Aa×Aa → **75%** dominant
   - Aa×aa → **50%** dominant
   - aa×aa → **0%** dominant
2. Multiplies each number of couples by its dominant probability and adds them up
3. Multiplies the sum by 2, because every couple has exactly two offspring

**Worked example** (1 0 0 1 0 1):
```
E = 2 × (1·1 + 0·1 + 0·1 + 1·0.75 + 0·0.5 + 1·0) = 2 × 1.75 = 3.5
```

---

## TECHNOLOGIES USED
- **Python**
- **TXT File**
