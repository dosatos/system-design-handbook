# Problem Solving Template

Use this template for approaching coding problems systematically.

---

## UMPIRE Framework

### U - Understand (2-3 minutes)

**Problem Restatement**:
_Write the problem in your own words_

**Inputs**:
- Type:
- Constraints:
- Size range:

**Outputs**:
- Type:
- Format:

**Clarifying Questions**:
- [ ] What if input is empty?
- [ ] What if there are duplicates?
- [ ] Are there negative numbers?
- [ ] What's the expected size/scale?
- [ ] What should we return for edge cases?

**Edge Cases**:
1.
2.
3.

---

### M - Match (1-2 minutes)

**Pattern Recognition**:
- [ ] Does this remind me of another problem?
- [ ] Which data structure fits best?
- [ ] Which algorithm pattern applies?

**Potential Patterns**:
- [ ] Two Pointers
- [ ] Sliding Window
- [ ] Hash Map
- [ ] Binary Search
- [ ] DFS/BFS
- [ ] Dynamic Programming
- [ ] Greedy
- [ ] Other: ___

**Why This Pattern**:
_Explain why the pattern fits_

---

### P - Plan (3-5 minutes)

**High-Level Approach**:
1.
2.
3.
4.

**Pseudocode**:
```
// Step 1:

// Step 2:

// Step 3:

// Return:
```

**Data Structures Needed**:
-

**Before Coding Checklist**:
- [ ] I can explain my approach
- [ ] I know the time complexity
- [ ] I've considered edge cases
- [ ] I'm confident in the plan

---

### I - Implement (10-20 minutes)

**Code**:
```python
def solution(input):
    # Implementation

    pass
```

**While Coding**:
- [ ] Talking through each step
- [ ] Handling edge cases
- [ ] Using descriptive variable names
- [ ] Not getting stuck on syntax

---

### R - Review (2-3 minutes)

**Code Walkthrough**:
_Trace through with a simple example_

**Edge Case Testing**:
| Input | Expected | Actual |
|-------|----------|--------|
| | | |
| | | |
| | | |

**Bug Check**:
- [ ] Off-by-one errors?
- [ ] Null/empty checks?
- [ ] Return statement correct?
- [ ] Variable initialization?

---

### E - Evaluate (2 minutes)

**Complexity Analysis**:
- Time: O(?) because ___
- Space: O(?) because ___

**Optimization Discussion**:
- Can we do better on time? ___
- Can we do better on space? ___
- Trade-offs? ___

**Alternative Approaches**:
1. ___ (Time: O(?), Space: O(?))
2. ___ (Time: O(?), Space: O(?))

---

## Quick Reference

### Time Complexities to Know
- O(1): Constant - hash lookup, arithmetic
- O(log n): Logarithmic - binary search
- O(n): Linear - single pass
- O(n log n): Linearithmic - efficient sorting
- O(n²): Quadratic - nested loops
- O(2ⁿ): Exponential - subsets
- O(n!): Factorial - permutations

### Common Data Structures
| Structure | Access | Search | Insert | Delete |
|-----------|--------|--------|--------|--------|
| Array | O(1) | O(n) | O(n) | O(n) |
| Hash Map | O(1) | O(1) | O(1) | O(1) |
| Linked List | O(n) | O(n) | O(1) | O(1) |
| BST | O(log n) | O(log n) | O(log n) | O(log n) |
| Heap | O(1) top | O(n) | O(log n) | O(log n) |

### Pattern Quick Checks
- **Sorted array?** → Binary search, two pointers
- **Finding pairs?** → Hash map, two pointers
- **Subarray/substring?** → Sliding window
- **Tree/graph traversal?** → BFS/DFS
- **Optimal substructure?** → DP
- **Make choices?** → Backtracking

---

## Interview Tips

### Communication
- Think out loud constantly
- Ask clarifying questions first
- Explain trade-offs
- State assumptions

### Time Management
- Don't jump to code immediately
- Don't spend too long planning
- Leave time for testing
- Know when to ask for hints

### Common Mistakes
- Not handling edge cases
- Off-by-one errors
- Forgetting to return
- Not testing with examples

---

_Use this template until the process becomes automatic._
