---
title: "Phase 2: Intermediate Mastery (Weeks 4-6)"
category: "Technical Preparation"
phase: 2
last_updated: "January 2026"

summary: |
  Weeks 4-6 covering advanced algorithms and ML systems (42 problems, total 89).
  Topics: Heap, Graphs, DP (1D & 2D), Greedy, Intervals, Union-Find, Dijkstra, Bit Manipulation.
  ML focus: Distributed training, RLHF pipeline, tokenization (BPE), inference optimization.
  System design: Rate limiter, Twitter feed, notification system.

outline:
  - Goals
  - Week 4 (Advanced Algorithms)
  - Week 5 (Complex Data Structures & ML Systems)
  - Week 6 (Advanced Algorithms & LLM Infrastructure)
  - Phase 2 Summary
---

# Phase 2: Intermediate Mastery (Weeks 4-6)

## Table of Contents

- [Goals](#goals)
- [Week 4: Advanced Algorithms](#week-4-advanced-algorithms)
- [Week 5: Complex Data Structures & ML Systems](#week-5-complex-data-structures--ml-systems)
- [Week 6: Advanced Algorithms & LLM Infrastructure](#week-6-advanced-algorithms--llm-infrastructure)
- [Phase 2 Summary](#phase-2-summary)

---

## Goals

- Master advanced algorithm patterns
- Understand ML systems (distributed training, RLHF)
- Practice complex system design
- Complete 42 additional coding problems

---

## Week 4: Advanced Algorithms

### Coding (18 problems)

| Topic | Problems | Key Pattern |
|-------|----------|-------------|
| Heap/Priority Queue | 5 | Top K, merge K sorted |
| Graphs | 7 | DFS, BFS, topological sort |
| 1D Dynamic Programming | 6 | Memoization, tabulation |

**Must-Solve Problems:**
1. Kth Largest Element (Heap)
2. Merge K Sorted Lists (Heap)
3. Number of Islands (Graphs)
4. Course Schedule (Graphs - Topological Sort)
5. Climbing Stairs (DP)
6. House Robber (DP)
7. Longest Increasing Subsequence (DP)

**Graph Traversal Templates:**

```python
# DFS for connected components
def dfs(graph, node, visited):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(graph, neighbor, visited)

# BFS for shortest path
from collections import deque
def bfs(graph, start):
    queue = deque([(start, 0)])
    visited = {start}
    while queue:
        node, dist = queue.popleft()
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, dist + 1))
```

**DP Framework:**
```python
# 1. Define state: dp[i] = ?
# 2. Define recurrence: dp[i] = f(dp[i-1], ...)
# 3. Base case: dp[0] = ?
# 4. Order of computation
# 5. Final answer location

# Example: Climbing Stairs
def climbStairs(n):
    if n <= 2:
        return n
    dp = [0] * (n + 1)
    dp[1], dp[2] = 1, 2
    for i in range(3, n + 1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]
```

### System Design

**Reading:**
- DDIA Chapters 8-9: Distributed Systems Trouble, Consistency

**Design Exercise: Rate Limiter**

Requirements:
- Limit API requests per user
- Support different rate limiting algorithms
- Distributed across multiple servers

Key Algorithms:
1. **Token Bucket:** Smooth traffic, allows bursts
2. **Leaky Bucket:** Consistent output rate
3. **Fixed Window:** Simple but edge cases at boundaries
4. **Sliding Window Log:** Accurate but memory-intensive
5. **Sliding Window Counter:** Good balance

### ML/AI

**Study Topics:**
- [ ] Loss functions (cross-entropy, MSE, contrastive)
- [ ] Optimizers (SGD, Adam, AdamW)
- [ ] Regularization (dropout, weight decay, batch norm)
- [ ] Learning rate schedules (warmup, cosine annealing)

**Book Progress:** Designing Machine Learning Systems (Chip Huyen)
- Chapters 1-3: ML Systems Overview

**Key Questions:**
1. Why use Adam over SGD?
2. When does dropout help?
3. What is the vanishing gradient problem?

### Week 4 Deliverables

- [ ] Complete 18 coding problems
- [ ] Read DDIA Chapters 8-9
- [ ] Design rate limiter with 3 algorithms
- [ ] Explain Adam optimizer mathematically
- [ ] Understand regularization techniques

---

## Week 5: Complex Data Structures & ML Systems

### Coding (12 problems)

| Topic | Problems | Key Pattern |
|-------|----------|-------------|
| 2D Dynamic Programming | 4 | Grid problems |
| Greedy | 4 | Local optimal choices |
| Intervals | 4 | Sorting + merging |

**Must-Solve Problems:**
1. Unique Paths (2D DP)
2. Longest Common Subsequence (2D DP)
3. Jump Game (Greedy)
4. Merge Intervals (Intervals)
5. Non-overlapping Intervals (Intervals)

**2D DP Template:**
```python
def longestCommonSubsequence(text1, text2):
    m, n = len(text1), len(text2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text1[i-1] == text2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])

    return dp[m][n]
```

**Interval Pattern:**
```python
def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = [intervals[0]]

    for start, end in intervals[1:]:
        if start <= merged[-1][1]:
            merged[-1][1] = max(merged[-1][1], end)
        else:
            merged.append([start, end])

    return merged
```

### System Design

**Design Exercise: Twitter/X Feed**

Requirements:
- Users post tweets
- Follow other users
- See timeline (home feed)
- 500M users, 10K celebrities with millions of followers

Key Decisions:
1. **Push vs Pull vs Hybrid** for feed generation
2. **Fan-out on write** for normal users
3. **Fan-out on read** for celebrities
4. **Caching** for hot content

Components:
- Tweet Service
- User Graph Service
- Timeline Service
- Search Service
- Notification Service

### ML/AI

**Distributed Training Deep Dive:**

| Approach | When to Use | Trade-offs |
|----------|-------------|------------|
| Data Parallelism | Model fits on one GPU | Gradient sync overhead |
| Model Parallelism | Model too large | Complex communication |
| Pipeline Parallelism | Very large models | Bubble overhead |
| Tensor Parallelism | Within transformer layers | Fine-grained communication |

**RLHF (Reinforcement Learning from Human Feedback):**

```
┌─────────────────┐
│ 1. Pre-train    │ → Base LLM on text data
│    LLM          │
└────────┬────────┘
         ↓
┌─────────────────┐
│ 2. Supervised   │ → Fine-tune on human demonstrations
│    Fine-tuning  │
└────────┬────────┘
         ↓
┌─────────────────┐
│ 3. Train        │ → Learn human preferences from comparisons
│    Reward Model │
└────────┬────────┘
         ↓
┌─────────────────┐
│ 4. PPO          │ → Optimize policy against reward model
│    Training     │
└─────────────────┘
```

**Resources:**
- [Educative: ML System Design Course](https://www.educative.io/courses/machine-learning-system-design)
- [Hello Interview: ML System Design](https://www.hellointerview.com/learn/ml-system-design/in-a-hurry/introduction)

### Week 5 Deliverables

- [ ] Complete 12 coding problems
- [ ] Design Twitter feed system
- [ ] Explain RLHF pipeline
- [ ] Understand data vs model parallelism trade-offs

---

## Week 6: Advanced Algorithms & LLM Infrastructure

### Coding (12 problems)

| Topic | Problems | Key Pattern |
|-------|----------|-------------|
| Advanced Graph | 3 | Dijkstra, Union-Find |
| Math & Geometry | 5 | Number theory, coordinates |
| Bit Manipulation | 4 | XOR, masks, shifts |

**Must-Solve Problems:**
1. Network Delay Time (Dijkstra)
2. Accounts Merge (Union-Find)
3. Pow(x, n) (Math)
4. Number of 1 Bits (Bit)
5. Counting Bits (Bit)

**Union-Find Template:**
```python
class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False
        if self.rank[px] < self.rank[py]:
            px, py = py, px
        self.parent[py] = px
        if self.rank[px] == self.rank[py]:
            self.rank[px] += 1
        return True
```

**Dijkstra's Algorithm:**
```python
import heapq

def dijkstra(graph, start):
    distances = {node: float('inf') for node in graph}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        dist, node = heapq.heappop(pq)
        if dist > distances[node]:
            continue
        for neighbor, weight in graph[node]:
            new_dist = dist + weight
            if new_dist < distances[neighbor]:
                distances[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))

    return distances
```

### System Design

**Design Exercise: Notification System**

Requirements:
- Multi-channel: push, email, SMS
- High throughput: millions of notifications/day
- Reliability: at-least-once delivery
- Rate limiting per user

Components:
1. **Notification Service** - Entry point, validation
2. **Message Queue** - Decouple and buffer
3. **Channel Workers** - Push/Email/SMS handlers
4. **Template Service** - Message formatting
5. **User Preferences** - Channel preferences

Event-Driven Architecture:
```
API → Kafka → Workers → Third-party APIs (APNS, FCM, Twilio, SendGrid)
```

### ML/AI

**LLM Infrastructure Topics:**

**Tokenization Strategies:**
| Algorithm | Pros | Cons |
|-----------|------|------|
| BPE | Handles rare words | Fixed vocabulary |
| WordPiece | Google's approach | Similar to BPE |
| SentencePiece | Language agnostic | Preprocessing needed |
| Unigram | Probabilistic | More complex |

**Implement BPE from scratch:**
```python
def train_bpe(texts, vocab_size):
    # 1. Initialize with characters
    vocab = set(char for text in texts for char in text)

    # 2. Count pair frequencies
    def get_pairs(text):
        pairs = {}
        for i in range(len(text) - 1):
            pair = (text[i], text[i+1])
            pairs[pair] = pairs.get(pair, 0) + 1
        return pairs

    # 3. Merge most frequent pair until vocab_size
    while len(vocab) < vocab_size:
        pairs = get_pairs(corpus)
        best_pair = max(pairs, key=pairs.get)
        # Merge best_pair in corpus
        vocab.add(''.join(best_pair))

    return vocab
```

**Inference Optimization:**
| Technique | Speedup | Trade-off |
|-----------|---------|-----------|
| Quantization (INT8) | 2-4x | Slight accuracy loss |
| Quantization (INT4) | 4-8x | More accuracy loss |
| KV-Cache | 2-3x | Memory usage |
| Speculative Decoding | 2-3x | Additional model needed |
| Continuous Batching | 2-5x | Implementation complexity |

**Vector Databases:**
- Pinecone (managed, easy to use)
- Weaviate (open source, feature-rich)
- Milvus (high performance)
- Chroma (lightweight, dev-friendly)

### Week 6 Deliverables

- [ ] Complete 12 coding problems
- [ ] Design notification system
- [ ] Implement BPE tokenizer from scratch
- [ ] Understand inference optimization techniques
- [ ] Know vector database options

---

## Phase 2 Summary

### Problems Completed: 42 (Total: 89)

| Topic | Count |
|-------|-------|
| Heap/Priority Queue | 5 |
| Graphs | 7 |
| 1D DP | 6 |
| 2D DP | 4 |
| Greedy | 4 |
| Intervals | 4 |
| Advanced Graph | 3 |
| Math & Geometry | 5 |
| Bit Manipulation | 4 |

### Knowledge Checkpoints

**Coding:**
- [ ] Can solve graph problems with appropriate algorithm
- [ ] Comfortable with 1D and 2D DP
- [ ] Know Union-Find and Dijkstra implementations

**System Design:**
- [ ] Can design rate limiter with multiple algorithms
- [ ] Understand push vs pull for feeds
- [ ] Can design notification system

**ML/AI:**
- [ ] Explain distributed training approaches
- [ ] Understand RLHF pipeline
- [ ] Know tokenization algorithms
- [ ] Understand inference optimization

---

## Next Steps

Continue to [Phase 3: Company-Specific](./phase3-company-specific.md)
