# Python Lab: Naive vs. Optimized Algorithms
 
In this Lab i explored  how algorithmic choices — not just code-level  — determine
performance. each quetion   starts with a brute-force solution and works up to a
faster approach, timing both along the way.
## Overall Takeaway
 
Across all three problems, the same pattern repeats: brute-force solutions that
redo work per element are O(N²) or worse. Real speedups came from either
restructuring the problem (search over answers, sieve instead of retest) or
pairing the right data structure with a single pass (hash map lookups). Small
code-level tweaks (e.g. skipping even numbers) helped by a constant factor, but
never changed the growth curve — only an algorithmic change did that.