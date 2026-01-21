---
title: "Quick Reference Cards"
category: "Resources"
last_updated: "January 2026"

summary: |
  Printable quick reference cards for rapid review. Covers: Transformer architecture
  (attention formula, encoder/decoder), distributed training (data/model/pipeline/tensor
  parallelism), RLHF pipeline, LLM inference optimization, algorithm complexity,
  system design numbers, AI safety topics, interview day checklist, and common coding patterns.

outline:
  - Transformer Architecture
  - Distributed Training
  - RLHF Pipeline
  - LLM Inference Optimization
  - Algorithm Complexity Cheat Sheet
  - System Design Numbers
  - AI Safety Topics
  - Interview Day Checklist
  - Common Coding Patterns
---

# Quick Reference Cards

## Table of Contents

- [Transformer Architecture](#transformer-architecture)
- [Distributed Training](#distributed-training)
- [RLHF Pipeline](#rlhf-pipeline)
- [LLM Inference Optimization](#llm-inference-optimization)
- [Algorithm Complexity Cheat Sheet](#algorithm-complexity-cheat-sheet)
- [System Design Numbers](#system-design-numbers)
- [AI Safety Topics](#ai-safety-topics)
- [Interview Day Checklist](#interview-day-checklist)
- [Common Coding Patterns](#common-coding-patterns)

---

## Transformer Architecture

```
┌─────────────────────────────────────────────────┐
│                TRANSFORMER                       │
├─────────────────────────────────────────────────┤
│                                                  │
│  Attention(Q, K, V) = softmax(QK^T / √d_k) V    │
│                                                  │
│  ┌─────────────┐        ┌─────────────┐         │
│  │   Encoder   │        │   Decoder   │         │
│  ├─────────────┤        ├─────────────┤         │
│  │ Self-Attn   │        │ Masked      │         │
│  │     ↓       │        │ Self-Attn   │         │
│  │ Add & Norm  │        │     ↓       │         │
│  │     ↓       │        │ Add & Norm  │         │
│  │ Feed Forward│        │     ↓       │         │
│  │     ↓       │        │ Cross-Attn  │         │
│  │ Add & Norm  │        │     ↓       │         │
│  └─────────────┘        │ Add & Norm  │         │
│                         │     ↓       │         │
│                         │ Feed Forward│         │
│                         │     ↓       │         │
│                         │ Add & Norm  │         │
│                         └─────────────┘         │
│                                                  │
│  GPT: Decoder only (causal mask)                │
│  BERT: Encoder only (bidirectional)             │
│  T5: Encoder-Decoder                            │
│                                                  │
└─────────────────────────────────────────────────┘
```

**Key Numbers:**
- Original: 6 layers, 8 heads, d_model=512
- Attention: O(n²) complexity where n=sequence length
- Parameters = 12 × d_model² × num_layers (approx)

---

## Distributed Training

```
┌─────────────────────────────────────────────────┐
│            DISTRIBUTED TRAINING                  │
├─────────────────────────────────────────────────┤
│                                                  │
│  DATA PARALLELISM:                              │
│  • Same model on each GPU                       │
│  • Different data batches                       │
│  • Gradient synchronization (AllReduce)         │
│  • Use when: Model fits on 1 GPU                │
│                                                  │
│  MODEL PARALLELISM:                             │
│  • Split model across GPUs                      │
│  • Each GPU has different layers                │
│  • Use when: Model > GPU memory                 │
│                                                  │
│  PIPELINE PARALLELISM:                          │
│  • Split by layers, process micro-batches       │
│  • Interleave forward/backward passes           │
│  • Use when: Very deep models                   │
│                                                  │
│  TENSOR PARALLELISM:                            │
│  • Split individual operations                  │
│  • Within attention heads/FFN layers            │
│  • Use when: Single layer > GPU memory          │
│                                                  │
│  GRADIENT ACCUMULATION:                         │
│  • Accumulate gradients over mini-batches       │
│  • Simulate larger batch size                   │
│  • Use when: Memory limited, need large batch   │
│                                                  │
└─────────────────────────────────────────────────┘
```

---

## RLHF Pipeline

```
┌─────────────────────────────────────────────────┐
│                 RLHF PIPELINE                    │
├─────────────────────────────────────────────────┤
│                                                  │
│  1. PRE-TRAINING                                │
│     └─ Train LLM on large text corpus           │
│                                                  │
│  2. SUPERVISED FINE-TUNING (SFT)                │
│     └─ Fine-tune on human demonstrations        │
│     └─ (prompt, desired_response) pairs         │
│                                                  │
│  3. REWARD MODEL TRAINING                       │
│     └─ Train on human preference comparisons    │
│     └─ Input: (prompt, response_A, response_B)  │
│     └─ Output: Which is better                  │
│                                                  │
│  4. PPO OPTIMIZATION                            │
│     └─ Generate responses with policy           │
│     └─ Score with reward model                  │
│     └─ Update policy to maximize reward         │
│     └─ KL penalty to stay close to SFT          │
│                                                  │
│  CONSTITUTIONAL AI (Alternative):               │
│     └─ AI critiques own outputs                 │
│     └─ AI revises based on principles           │
│     └─ Less human feedback needed               │
│                                                  │
└─────────────────────────────────────────────────┘
```

---

## LLM Inference Optimization

```
┌─────────────────────────────────────────────────┐
│           INFERENCE OPTIMIZATION                 │
├─────────────────────────────────────────────────┤
│                                                  │
│  QUANTIZATION:                                  │
│  • INT8: 2-4x speedup, minimal accuracy loss    │
│  • INT4: 4-8x speedup, some accuracy loss       │
│  • GPTQ, AWQ, SmoothQuant methods               │
│                                                  │
│  KV-CACHE:                                      │
│  • Cache key/value tensors for past tokens      │
│  • Avoid recomputation during generation        │
│  • Memory-bound for long sequences              │
│                                                  │
│  BATCHING:                                      │
│  • Static: Fixed batch size                     │
│  • Dynamic: Variable batch size                 │
│  • Continuous: In-flight batching (vLLM)        │
│                                                  │
│  SPECULATIVE DECODING:                          │
│  • Draft model generates candidates             │
│  • Main model verifies in parallel              │
│  • 2-3x speedup possible                        │
│                                                  │
│  OTHER:                                         │
│  • Flash Attention: O(n) memory                 │
│  • Paged Attention: Virtual memory for KV       │
│  • Pruning: Remove unnecessary weights          │
│  • Distillation: Train smaller model            │
│                                                  │
└─────────────────────────────────────────────────┘
```

---

## Algorithm Complexity Cheat Sheet

```
┌─────────────────────────────────────────────────┐
│            COMPLEXITY REFERENCE                  │
├─────────────────────────────────────────────────┤
│                                                  │
│  SORTING:                                       │
│  • QuickSort: O(n log n) avg, O(n²) worst       │
│  • MergeSort: O(n log n) always                 │
│  • HeapSort: O(n log n) always                  │
│                                                  │
│  SEARCHING:                                     │
│  • Binary Search: O(log n)                      │
│  • Hash Table: O(1) avg, O(n) worst             │
│  • BST: O(log n) avg, O(n) worst                │
│                                                  │
│  GRAPH:                                         │
│  • BFS/DFS: O(V + E)                            │
│  • Dijkstra: O((V + E) log V) with heap         │
│  • Bellman-Ford: O(VE)                          │
│  • Floyd-Warshall: O(V³)                        │
│  • Topological Sort: O(V + E)                   │
│                                                  │
│  DYNAMIC PROGRAMMING:                           │
│  • Usually O(n²) or O(n × m)                    │
│  • Can often optimize space to O(n)             │
│                                                  │
│  COMMON PATTERNS:                               │
│  • Two pointers: O(n)                           │
│  • Sliding window: O(n)                         │
│  • Binary search: O(log n)                      │
│  • Backtracking: O(2^n) or O(n!)                │
│                                                  │
└─────────────────────────────────────────────────┘
```

---

## System Design Numbers

```
┌─────────────────────────────────────────────────┐
│           ESTIMATION REFERENCE                   │
├─────────────────────────────────────────────────┤
│                                                  │
│  TIME:                                          │
│  • 1 day = 86,400 seconds ≈ 100K seconds        │
│  • 1 month = 2.5M seconds                       │
│  • 1 year = 30M seconds                         │
│                                                  │
│  STORAGE:                                       │
│  • 1 char = 1 byte                              │
│  • 1 tweet (140 char) ≈ 140 bytes               │
│  • 1 image ≈ 500KB                              │
│  • 1 video minute ≈ 50MB                        │
│                                                  │
│  THROUGHPUT:                                    │
│  • SSD read: 500MB/s                            │
│  • Network (1Gbps): 100MB/s                     │
│  • Redis: 100K ops/sec                          │
│  • MySQL: 10K queries/sec                       │
│                                                  │
│  LATENCY:                                       │
│  • L1 cache: 0.5 ns                             │
│  • L2 cache: 7 ns                               │
│  • RAM: 100 ns                                  │
│  • SSD: 150 µs                                  │
│  • Network (same DC): 0.5 ms                    │
│  • Network (cross DC): 40 ms                    │
│                                                  │
│  SCALE:                                         │
│  • 1 server = 10K-100K requests/sec             │
│  • 1M users = ~10K concurrent                   │
│                                                  │
└─────────────────────────────────────────────────┘
```

---

## AI Safety Topics

```
┌─────────────────────────────────────────────────┐
│             AI SAFETY CHECKLIST                  │
├─────────────────────────────────────────────────┤
│                                                  │
│  KEY CONCEPTS:                                  │
│  □ Alignment: AI does what we want              │
│  □ Robustness: Maintains safety under shift     │
│  □ Interpretability: Understand what it does    │
│  □ Oversight: Humans maintain control           │
│                                                  │
│  CURRENT APPROACHES:                            │
│  □ RLHF: Learning from human feedback           │
│  □ Constitutional AI: Principles-based          │
│  □ Red-teaming: Adversarial testing             │
│  □ Evals: Capability and safety testing         │
│                                                  │
│  RISKS TO DISCUSS:                              │
│  □ Near-term: Misuse, bias, misinformation     │
│  □ Long-term: Alignment failure, control loss   │
│  □ Dual-use: Research enabling harm             │
│                                                  │
│  COMPANY POSITIONS:                             │
│  □ Anthropic: Safety-first, Constitutional AI   │
│  □ OpenAI: Balance safety with capability       │
│  □ DeepMind: Long-term research focus           │
│  □ xAI: Move fast, less safety emphasis         │
│                                                  │
└─────────────────────────────────────────────────┘
```

---

## Interview Day Checklist

```
┌─────────────────────────────────────────────────┐
│            INTERVIEW DAY CHECKLIST               │
├─────────────────────────────────────────────────┤
│                                                  │
│  BEFORE:                                        │
│  □ Resume printed/accessible                    │
│  □ Company values reviewed                      │
│  □ Interviewer names researched                 │
│  □ Questions prepared                           │
│  □ Stories ready to tell                        │
│  □ Tech setup tested (camera, audio)            │
│  □ Water and snacks available                   │
│  □ Quiet environment confirmed                  │
│                                                  │
│  DURING CODING:                                 │
│  □ Clarify requirements first                   │
│  □ Discuss approach before coding               │
│  □ Think aloud throughout                       │
│  □ Test with examples                           │
│  □ Discuss complexity                           │
│                                                  │
│  DURING SYSTEM DESIGN:                          │
│  □ Clarify requirements (functional + NFR)      │
│  □ Back-of-envelope calculations                │
│  □ High-level design first                      │
│  □ Deep dive on 2-3 components                  │
│  □ Discuss trade-offs                           │
│                                                  │
│  DURING BEHAVIORAL:                             │
│  □ Use STAR format                              │
│  □ Be specific (names, numbers)                 │
│  □ Focus on YOUR contribution                   │
│  □ Include learnings                            │
│                                                  │
│  AFTER:                                         │
│  □ Thank interviewer                            │
│  □ Send thank-you note (optional)               │
│  □ Document questions asked                     │
│  □ Note what went well/poorly                   │
│                                                  │
└─────────────────────────────────────────────────┘
```

---

## Common Coding Patterns

```python
# Two Pointers
left, right = 0, len(arr) - 1
while left < right:
    # process
    left += 1  # or right -= 1

# Sliding Window
left = 0
for right in range(len(arr)):
    # add arr[right] to window
    while window_invalid:
        # remove arr[left] from window
        left += 1
    # process valid window

# Binary Search
left, right = 0, len(arr) - 1
while left <= right:
    mid = left + (right - left) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        left = mid + 1
    else:
        right = mid - 1

# BFS
from collections import deque
queue = deque([start])
visited = {start}
while queue:
    node = queue.popleft()
    for neighbor in graph[node]:
        if neighbor not in visited:
            visited.add(neighbor)
            queue.append(neighbor)

# DFS (recursive)
def dfs(node, visited):
    visited.add(node)
    for neighbor in graph[node]:
        if neighbor not in visited:
            dfs(neighbor, visited)

# Backtracking
def backtrack(path, choices):
    if is_solution(path):
        result.append(path[:])
        return
    for choice in choices:
        if is_valid(choice):
            path.append(choice)
            backtrack(path, remaining_choices)
            path.pop()

# Dynamic Programming
dp = [0] * (n + 1)
dp[0] = base_case
for i in range(1, n + 1):
    dp[i] = f(dp[i-1], ...)
return dp[n]
```
