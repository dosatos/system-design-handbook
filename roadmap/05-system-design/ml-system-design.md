---
title: "ML System Design"
category: "System Design"
last_updated: "January 2026"

summary: |
  ML-specific system design covering data pipelines, feature stores, model training,
  serving, and monitoring. Deep dive into LLM topics: RAG architecture, LLM serving
  optimization (quantization, KV-cache, batching), embeddings and vector search.
  Common ML design problems: recommendation systems, search/ranking, fraud detection.

outline:
  - Overview
  - Core ML System Components (Data Pipeline, Feature Store, Training, Serving, Monitoring)
  - LLM-Specific Topics (RAG, LLM Serving, Embeddings)
  - Common ML Design Problems
  - ML System Design Framework
  - Resources
---

# ML System Design

## Table of Contents

- [Overview](#overview)
- [Core ML System Components](#core-ml-system-components)
- [LLM-Specific Topics](#llm-specific-topics)
- [Common ML Design Problems](#common-ml-design-problems)
- [ML System Design Framework](#ml-system-design-framework)
- [Resources](#resources)

---

## Overview

ML system design combines classical system design with ML-specific considerations:

```
┌─────────────────────────────────────────────────────────┐
│                    ML System Design                      │
├─────────────────┬─────────────────┬────────────────────┤
│ Classical SD    │   ML Specific   │  AI Company Focus  │
├─────────────────┼─────────────────┼────────────────────┤
│ Scalability     │ Data pipelines  │ LLM serving        │
│ Reliability     │ Feature stores  │ RAG systems        │
│ Caching         │ Model training  │ Distributed train  │
│ Load balancing  │ Model serving   │ Safety evaluation  │
│ Databases       │ Monitoring      │ Prompt engineering │
└─────────────────┴─────────────────┴────────────────────┘
```

## Core ML System Components

### 1. Data Pipeline

```
Raw Data → Collection → Validation → Transformation → Storage
              │              │              │            │
              ▼              ▼              ▼            ▼
          Streaming      Schema       Feature        Feature
          (Kafka)        checks      engineering      Store
```

**Key Considerations:**
- Data quality monitoring
- Schema evolution
- Backfill capabilities
- Lineage tracking

### 2. Feature Store

**Online vs Offline:**
| Aspect | Online Store | Offline Store |
|--------|--------------|---------------|
| Latency | < 10ms | Minutes |
| Use | Inference | Training |
| Storage | Redis, DynamoDB | S3, BigQuery |
| Data | Latest values | Historical |

**Feature Store Components:**
```
┌─────────────────────────────────────────┐
│             Feature Store                │
├──────────────────┬──────────────────────┤
│   Offline Store  │    Online Store      │
│   (Historical)   │    (Serving)         │
├──────────────────┴──────────────────────┤
│           Feature Registry              │
│      (Definitions, Metadata)            │
├─────────────────────────────────────────┤
│        Feature Transformation           │
│     (Batch + Streaming pipelines)       │
└─────────────────────────────────────────┘
```

### 3. Model Training

**Training Pipeline:**
```
Data → Preprocessing → Training → Evaluation → Registry
                          │
                          ├── Hyperparameter tuning
                          ├── Distributed training
                          └── Experiment tracking
```

**Distributed Training Strategies:**

| Strategy | When to Use | Trade-offs |
|----------|-------------|------------|
| Data Parallel | Model fits on 1 GPU | Gradient sync overhead |
| Model Parallel | Model > GPU memory | Complex implementation |
| Pipeline Parallel | Very deep models | Bubble overhead |
| Tensor Parallel | Transformer layers | Communication heavy |

### 4. Model Serving

**Serving Patterns:**

```
Online Inference:
Request → Load Balancer → Model Server → Response
                              │
                         ┌────┴────┐
                         │ Cache   │
                         └─────────┘

Batch Inference:
Data Lake → Batch Job → Predictions → Storage
```

**Optimization Techniques:**

| Technique | Speedup | Trade-off |
|-----------|---------|-----------|
| Quantization (INT8) | 2-4x | Slight accuracy loss |
| Quantization (INT4) | 4-8x | More accuracy loss |
| Distillation | Varies | Training required |
| Batching | 2-5x | Added latency |
| Caching | 10x+ | Memory usage |

### 5. Monitoring & Observability

**What to Monitor:**

| Level | Metrics |
|-------|---------|
| Infrastructure | CPU, GPU, memory, latency |
| Model | Accuracy, precision, recall |
| Data | Distribution drift, missing values |
| Business | Conversion, revenue impact |

**Drift Detection:**
- Input drift (covariate shift)
- Label drift (prior probability shift)
- Concept drift (P(Y|X) changes)

---

## LLM-Specific Topics

### 1. RAG Architecture

```
Query → Embedding → Vector Search → Reranking → Context
                        │               │          │
                        ▼               ▼          ▼
                   Top-K docs      Cross-encoder  LLM
                                                   │
                                                   ▼
                                               Response
```

**Key Design Decisions:**

| Component | Options | Trade-offs |
|-----------|---------|------------|
| Chunking | Fixed, semantic, sliding | Recall vs precision |
| Embedding | OpenAI, Cohere, local | Cost vs quality |
| Vector DB | Pinecone, Weaviate, Milvus | Managed vs control |
| Retrieval | Top-K, hybrid | Speed vs accuracy |
| Reranking | Cross-encoder, LLM | Latency vs quality |

### 2. LLM Serving

**Key Challenges:**
- Large model size (7B-70B+ params)
- Autoregressive generation (sequential)
- Memory-bound (KV cache)
- Variable output length

**Optimization Techniques:**

```
Model Level:
├── Quantization (INT8, INT4)
├── Pruning
└── Distillation

Serving Level:
├── KV-cache optimization
├── Continuous batching
├── Speculative decoding
└── Tensor parallelism

Request Level:
├── Prompt caching
├── Streaming responses
└── Early termination
```

### 3. Embeddings & Vector Search

**Embedding Models:**
| Model | Dimensions | Quality | Speed |
|-------|------------|---------|-------|
| OpenAI ada-002 | 1536 | High | API-limited |
| Cohere embed-v3 | 1024 | High | API-limited |
| BGE-large | 1024 | High | Self-hosted |
| MiniLM | 384 | Medium | Fast |

**Vector Database Selection:**
| DB | Managed | Scale | Features |
|----|---------|-------|----------|
| Pinecone | Yes | High | Simple, reliable |
| Weaviate | Both | High | Multi-modal |
| Milvus | Both | Very High | Feature-rich |
| Chroma | No | Low | Dev-friendly |
| pgvector | No | Medium | PostgreSQL native |

---

## Common ML Design Problems

### 1. Recommendation System

**Requirements:**
- Personalized recommendations
- 100M users, 10M items
- Real-time serving
- Cold start handling

**Two-Stage Architecture:**
```
┌─────────────────────────────────────────────────────────┐
│                Candidate Generation                      │
│  (Retrieve 1000s of candidates quickly)                 │
├─────────────────────────────────────────────────────────┤
│                    Ranking                               │
│  (Score and rank top candidates with complex model)     │
├─────────────────────────────────────────────────────────┤
│                 Business Rules                           │
│  (Filter, diversify, apply policies)                    │
└─────────────────────────────────────────────────────────┘
```

### 2. Search/Ranking System

**Requirements:**
- Query understanding
- Document retrieval
- Relevance ranking
- 10K QPS, <100ms latency

**Components:**
```
Query → Understanding → Retrieval → Ranking → Results
           │               │           │
           ├── Spell check ├── BM25    ├── Learning-to-rank
           ├── Expansion   ├── Vector  └── Personalization
           └── Intent      └── Hybrid
```

### 3. Fraud Detection

**Requirements:**
- Real-time detection
- High precision (minimize false positives)
- Handle evolving fraud patterns
- Explainability for investigation

**Design:**
```
Transaction → Feature Engineering → Real-time Scoring
                     │                     │
                     ├── User features     ├── Rules engine
                     ├── Device features   └── ML model
                     └── Behavior features

                     │
                     ▼
              Decision + Feedback Loop
```

---

## ML System Design Framework

### Interview Structure (45-60 min)

```
0-5 min:   Clarify requirements
5-15 min:  High-level design
15-35 min: Deep dive into components
35-45 min: Trade-offs and extensions
45-60 min: Questions
```

### Checklist

**Requirements:**
- [ ] Functional requirements clear
- [ ] Non-functional (scale, latency) defined
- [ ] Success metrics identified

**Data:**
- [ ] Data sources identified
- [ ] Data volume estimated
- [ ] Data quality considerations

**Model:**
- [ ] Model type selected
- [ ] Training approach defined
- [ ] Evaluation metrics chosen

**Serving:**
- [ ] Latency requirements
- [ ] Throughput requirements
- [ ] Caching strategy

**Monitoring:**
- [ ] Model metrics tracked
- [ ] Data drift detection
- [ ] Alerting strategy

---

## Resources

### Books
- **Designing Machine Learning Systems** - Chip Huyen
- **Machine Learning Design Patterns** - Lakshmanan et al.

### Courses
- [Educative ML System Design](https://www.educative.io/courses/machine-learning-system-design)
- [Hello Interview ML SD](https://www.hellointerview.com/learn/ml-system-design)

### GitHub
- [Machine-Learning-Interviews](https://github.com/alirezadir/machine-learning-interviews)
