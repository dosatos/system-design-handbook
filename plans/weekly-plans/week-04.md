# Week 4: Graphs & Backtracking

**Phase**: 2 - Intermediate
**Focus**: Graph traversals, backtracking patterns, RLHF introduction
**Target Hours**: 20-25

---

## Overview

Week 4 begins Phase 2 with graph algorithms and backtracking - two of the most challenging and rewarding pattern types. Also introduces RLHF pipeline understanding.

---

## Daily Breakdown

### Day 1 (Monday) - Graph Fundamentals

**Morning (1.5 hrs)**
- [ ] Review graph representations (adjacency list, matrix)
- [ ] Solve 2 Easy graph problems (BFS/DFS)

**Evening (2.5 hrs)**
- [ ] Solve 3 Medium graph problems
- [ ] Start DDIA Chapter 7

**Problems**: Number of Islands, Clone Graph, Pacific Atlantic Water Flow, Course Schedule

---

### Day 2 (Tuesday) - Graph BFS/DFS Mastery

**Morning (1.5 hrs)**
- [ ] Solve 2 Medium graph problems
- [ ] Focus on multi-source BFS

**Evening (2.5 hrs)**
- [ ] Solve 2 more graph problems
- [ ] Begin RLHF pipeline overview
- [ ] Continue DDIA Chapter 7

**Problems**: Rotting Oranges, Walls and Gates, Course Schedule II, Redundant Connection

---

### Day 3 (Wednesday) - Advanced Graph Algorithms

**Morning (1.5 hrs)**
- [ ] Learn Union Find / Disjoint Set
- [ ] Solve 2 Union Find problems

**Evening (2.5 hrs)**
- [ ] Solve 2 more graph problems
- [ ] Deep dive: RLHF Stage 1 (SFT)
- [ ] Finish DDIA Chapter 7

**Problems**: Number of Connected Components, Graph Valid Tree, Word Ladder

---

### Day 4 (Thursday) - Backtracking Introduction

**Morning (1.5 hrs)**
- [ ] Learn backtracking template
- [ ] Solve 2 backtracking problems

**Evening (2.5 hrs)**
- [ ] Solve 3 more backtracking problems
- [ ] Start DDIA Chapter 8
- [ ] Add 2 more STAR stories to bank

**Problems**: Subsets, Combination Sum, Permutations, Subsets II, Combination Sum II

---

### Day 5 (Friday) - Backtracking Mastery

**Morning (1.5 hrs)**
- [ ] Solve 2 Medium backtracking problems

**Evening (2 hrs)**
- [ ] Solve 2 harder backtracking problems
- [ ] Week review preparation

**Problems**: Permutations II, Word Search, Palindrome Partitioning, N-Queens

---

### Day 6 (Saturday) - Deep Work Day

**Morning (3 hrs)**
- [ ] Solve 2 Hard graph/backtracking problems
- [ ] Continue DDIA Chapter 8
- [ ] Practice Chat System design

**Afternoon (2 hrs)**
- [ ] Refine Chat System design
- [ ] Deep dive: RLHF Stage 2 (Reward Modeling)
- [ ] Document design

**Problems**: Alien Dictionary, Word Ladder II

---

### Day 7 (Sunday) - Review & Planning

**Morning (2 hrs)**
- [ ] Review all problems from this week
- [ ] Graph and backtracking pattern review
- [ ] Practice behavioral stories aloud

**Afternoon (2 hrs)**
- [ ] Week 4 retrospective
- [ ] Update all tracking files
- [ ] Update memory files
- [ ] Plan Week 5

---

## Weekly Targets

### Coding (20 problems)
| Pattern | Easy | Medium | Hard | Total |
|---------|------|--------|------|-------|
| Graphs | 2 | 8 | 2 | 12 |
| Backtracking | 0 | 6 | 2 | 8 |
| **Total** | 2 | 14 | 4 | **20** |

### System Design
- [ ] DDIA Chapters 7-8 read
- [ ] Chat System design practiced

### ML Deep Dive
- [ ] RLHF pipeline overview completed
- [ ] SFT stage understood
- [ ] Reward modeling introduced

### Behavioral
- [ ] Story bank at 5+ stories
- [ ] Practice stories aloud

### Career
- [ ] Follow up on networking outreach
- [ ] Schedule 1-2 informational interviews

---

## Key Patterns to Master

### Graph Patterns
1. **BFS**: Level by level, shortest path in unweighted
2. **DFS**: Explore to depth, path finding
3. **Union Find**: Connected components, cycle detection
4. **Topological Sort**: Course schedule type problems

### Backtracking Template
```python
def backtrack(candidates, path, result):
    if is_solution(path):
        result.append(path[:])
        return

    for candidate in candidates:
        if is_valid(candidate):
            path.append(candidate)
            backtrack(remaining_candidates, path, result)
            path.pop()  # backtrack
```

---

## Completion Checklist

- [ ] 20+ coding problems solved (95 total)
- [ ] DDIA Chapters 7-8 completed
- [ ] Chat System design practiced
- [ ] RLHF overview understood
- [ ] 5+ STAR stories ready
- [ ] Networking conversations scheduled
- [ ] All tracking files updated
