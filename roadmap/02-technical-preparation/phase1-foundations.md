---
title: "Phase 1: Foundations (Weeks 1-3)"
category: "Technical Preparation"
phase: 1
last_updated: "January 2026"

summary: |
  First 3 weeks covering fundamental data structures and algorithms (47 problems).
  Topics: Arrays, Hash Maps, Two Pointers, Stack, Sliding Window, Binary Search, Linked Lists,
  Trees, Tries, Backtracking. Includes Transformer architecture study and DDIA Chapters 1-7.
  Ends with URL shortener design and GPT vs BERT understanding.

outline:
  - Goals
  - Week 1 (Assessment & Core Data Structures)
  - Week 2 (Algorithms Deep Dive)
  - Week 3 (Trees, Graphs, Core ML)
  - Phase 1 Summary
---

# Phase 1: Foundations (Weeks 1-3)

## Table of Contents

- [Goals](#goals)
- [Week 1: Assessment & Core Data Structures](#week-1-assessment--core-data-structures)
- [Week 2: Algorithms Deep Dive](#week-2-algorithms-deep-dive)
- [Week 3: Trees, Graphs, Core ML](#week-3-trees-graphs-core-ml)
- [Phase 1 Summary](#phase-1-summary)

---

## Goals

- Master fundamental data structures and algorithms
- Understand Transformer architecture
- Build system design foundation
- Complete 47 coding problems

---

## Week 1: Assessment & Core Data Structures

### Coding (16 problems)

| Topic | Problems | NeetCode Link |
|-------|----------|---------------|
| Arrays & Hashing | 8 | [Link](https://neetcode.io/practice?tab=neetcode150) |
| Two Pointers | 4 | [Link](https://neetcode.io/practice?tab=neetcode150) |
| Stack | 4 | [Link](https://neetcode.io/practice?tab=neetcode150) |

**Key Patterns to Master:**
- Hash maps for O(1) lookup
- Two pointer technique for sorted arrays
- Monotonic stack for next greater element

**Must-Solve Problems:**
1. Two Sum (Arrays)
2. Valid Anagram (Arrays)
3. Valid Parentheses (Stack)
4. Container With Most Water (Two Pointers)

### System Design

**Reading:**
- DDIA Chapters 1-3: Reliable, Scalable, and Maintainable Applications

**Key Concepts:**
- Reliability vs Scalability vs Maintainability
- Data models (relational, document, graph)
- Storage and retrieval basics

### ML/AI

**Primary Task:** Read "Attention Is All You Need" paper (Vaswani et al., 2017)

**Understand:**
- [ ] Why attention replaced RNNs
- [ ] Scaled dot-product attention: Q, K, V
- [ ] Multi-head attention mechanism
- [ ] Positional encoding

**Resources:**
- [Transformer LLM Roadmap](https://mentorcruise.com/blog/transformer-llms-roadmap-and-interview-preparation-guide/)
- [3Blue1Brown: Attention in Transformers](https://www.youtube.com/watch?v=eMlx5fFNoYc)

### Week 1 Deliverables

- [ ] Complete 16 coding problems
- [ ] Set up NeetCode/LeetCode accounts
- [ ] Read DDIA Chapters 1-3
- [ ] Understand self-attention mechanism
- [ ] Create study schedule in calendar

---

## Week 2: Algorithms Deep Dive

### Coding (16 problems)

| Topic | Problems | Key Pattern |
|-------|----------|-------------|
| Sliding Window | 5 | Variable/fixed window |
| Binary Search | 5 | Search space reduction |
| Linked List | 6 | Two pointers, dummy nodes |

**Must-Solve Problems:**
1. Best Time to Buy and Sell Stock (Sliding Window)
2. Longest Substring Without Repeating Characters (Sliding Window)
3. Binary Search (Binary Search)
4. Reverse Linked List (Linked List)
5. Merge Two Sorted Lists (Linked List)

**Binary Search Template:**
```python
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = left + (right - left) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

### System Design

**Reading:**
- DDIA Chapters 4-5: Encoding, Replication

**Study Topics:**
- Load balancing strategies (round-robin, least connections, consistent hashing)
- Caching strategies (write-through, write-back, write-around)
- CDN basics

**Exercise:** Design a simple URL shortener (sketch only)

### ML/AI

**Continue Transformer Study:**
- [ ] Encoder vs Decoder architecture
- [ ] Layer normalization and residual connections
- [ ] Feed-forward networks in Transformers

**New Concept:** Position-wise Feed-Forward Networks
```
FFN(x) = max(0, xW₁ + b₁)W₂ + b₂
```

**Resources:**
- [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)

### Week 2 Deliverables

- [ ] Complete 16 coding problems
- [ ] Read DDIA Chapters 4-5
- [ ] Explain CAP theorem from memory
- [ ] Understand full Transformer architecture
- [ ] Sketch URL shortener design

---

## Week 3: Trees, Graphs, Core ML

### Coding (15 problems)

| Topic | Problems | Key Pattern |
|-------|----------|-------------|
| Trees | 8 | DFS, BFS, recursion |
| Tries | 3 | Prefix matching |
| Backtracking | 4 | Decision trees, pruning |

**Must-Solve Problems:**
1. Invert Binary Tree (Trees)
2. Validate Binary Search Tree (Trees)
3. Implement Trie (Tries)
4. Subsets (Backtracking)
5. Combination Sum (Backtracking)

**Tree Traversal Templates:**
```python
# DFS - Recursive
def dfs(node):
    if not node:
        return
    # preorder: process here
    dfs(node.left)
    # inorder: process here
    dfs(node.right)
    # postorder: process here

# BFS
from collections import deque
def bfs(root):
    queue = deque([root])
    while queue:
        node = queue.popleft()
        # process node
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)
```

**Backtracking Template:**
```python
def backtrack(candidates, path, result):
    if is_solution(path):
        result.append(path[:])
        return
    for candidate in candidates:
        if is_valid(candidate):
            path.append(candidate)
            backtrack(candidates, path, result)
            path.pop()  # backtrack
```

### System Design

**Reading:**
- DDIA Chapters 6-7: Partitioning, Transactions

**Full Design Exercise: URL Shortener**

Requirements:
- Shorten long URLs
- Redirect short URLs
- 100M URLs/month write, 10B reads/month

Key Decisions:
1. **ID Generation:** Counter vs Random vs Base62
2. **Storage:** SQL vs NoSQL
3. **Caching:** Redis for hot URLs
4. **Scaling:** Database sharding strategy

### ML/AI

**Model Architectures:**
- [ ] GPT (Decoder-only) - autoregressive, causal attention
- [ ] BERT (Encoder-only) - bidirectional, masked LM
- [ ] T5 (Encoder-Decoder) - sequence-to-sequence

**Start Reading:** [Chip Huyen's ML Interviews Book](https://huyenchip.com/ml-interviews-book/)
- Focus on Chapters 1-3 (Overview, ML Basics)

**Key Questions to Answer:**
1. Why is GPT decoder-only?
2. What's the difference between encoder and decoder attention?
3. Why use causal masking?

### Week 3 Deliverables

- [ ] Complete 15 coding problems
- [ ] Read DDIA Chapters 6-7
- [ ] Design URL shortener from scratch (45 min timed)
- [ ] Explain GPT vs BERT vs T5 differences
- [ ] Start Chip Huyen ML book

---

## Phase 1 Summary

### Problems Completed: 47

| Topic | Count |
|-------|-------|
| Arrays & Hashing | 8 |
| Two Pointers | 4 |
| Stack | 4 |
| Sliding Window | 5 |
| Binary Search | 5 |
| Linked List | 6 |
| Trees | 8 |
| Tries | 3 |
| Backtracking | 4 |

### Knowledge Checkpoints

**Coding:**
- [ ] Can solve any array/string medium in 25 min
- [ ] Know when to use each data structure
- [ ] Can explain Big O for all solutions

**System Design:**
- [ ] Understand DDIA Chapters 1-7
- [ ] Can design URL shortener end-to-end
- [ ] Know CAP theorem and its implications

**ML/AI:**
- [ ] Can explain Transformer from scratch
- [ ] Understand GPT vs BERT architectures
- [ ] Started ML interview prep book

### Recommended Self-Assessment

1. **Coding:** Solve 3 random mediums in 75 min (25 min each)
2. **System Design:** Design URL shortener in 45 min
3. **ML:** Explain Transformer attention to a peer

---

## Next Steps

Continue to [Phase 2: Intermediate](./phase2-intermediate.md)
