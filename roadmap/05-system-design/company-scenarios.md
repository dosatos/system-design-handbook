# Company-Specific Design Scenarios

## OpenAI-Style Questions

### Scenario 1: RAG System for Internal Docs

> "Design a system that allows employees to ask questions about internal company documents."

**Requirements Clarification:**
- Document types: PDF, docs, wikis
- 10M documents, 100K queries/day
- Accuracy critical, latency < 5s
- Must cite sources

**High-Level Design:**
```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│   Document   │────▶│   Chunking   │────▶│  Embedding   │
│    Store     │     │   Pipeline   │     │   Service    │
└──────────────┘     └──────────────┘     └──────┬───────┘
                                                  │
                                                  ▼
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│    Query     │────▶│  Retriever   │◀────│   Vector     │
│   Service    │     │              │     │   Database   │
└──────┬───────┘     └──────┬───────┘     └──────────────┘
       │                    │
       ▼                    ▼
┌──────────────┐     ┌──────────────┐
│   Reranker   │────▶│     LLM      │────▶ Answer + Citations
│              │     │  Generation  │
└──────────────┘     └──────────────┘
```

**Deep Dive Topics:**
1. **Chunking Strategy**
   - Semantic vs fixed-size
   - Overlap considerations
   - Metadata preservation

2. **Embedding Model Selection**
   - Domain-specific fine-tuning?
   - Embedding dimensions trade-off
   - Batch processing

3. **Retrieval Accuracy**
   - Hybrid search (dense + sparse)
   - Reranking with cross-encoder
   - Query expansion

4. **Citation Tracking**
   - Chunk-to-document mapping
   - Confidence scores
   - Source highlighting

---

### Scenario 2: Distributed Training System

> "Design a distributed training system for deep learning models."

**Requirements:**
- Train 100B+ parameter models
- 1000+ GPUs
- Fault tolerance
- Efficient checkpointing

**High-Level Design:**
```
┌─────────────────────────────────────────────────────────┐
│                   Cluster Manager                        │
│            (Kubernetes / Slurm / Ray)                   │
└─────────────────────────────────────────────────────────┘
                           │
        ┌──────────────────┼──────────────────┐
        ▼                  ▼                  ▼
┌──────────────┐   ┌──────────────┐   ┌──────────────┐
│   Worker 0   │   │   Worker 1   │   │   Worker N   │
│   (GPU Pod)  │◀─▶│   (GPU Pod)  │◀─▶│   (GPU Pod)  │
└──────────────┘   └──────────────┘   └──────────────┘
        │                                      │
        └──────────────────┬───────────────────┘
                           ▼
                 ┌──────────────────┐
                 │ Gradient Sync    │
                 │ (All-Reduce /    │
                 │  Parameter Srvr) │
                 └──────────────────┘
```

**Key Discussion Points:**

1. **Parallelism Strategy**
   - Data parallelism for smaller models
   - Model parallelism for 100B+ params
   - Pipeline parallelism for throughput
   - Tensor parallelism within nodes

2. **Communication**
   - All-reduce vs parameter server
   - NCCL for GPU communication
   - Gradient compression

3. **Fault Tolerance**
   - Periodic checkpointing
   - Elastic training (handle node failures)
   - Restart from last checkpoint

4. **Efficiency**
   - Mixed precision (FP16/BF16)
   - Gradient accumulation
   - Activation checkpointing

---

## Anthropic-Style Questions

### Scenario 1: Massive Scale Search + LLM

> "Design a distributed search system for 1 billion documents at 1M QPS, with LLM inference at 10K+ RPS."

**Requirements:**
- 1B documents, growing
- 1M search QPS
- 10K LLM inference RPS
- P99 latency < 500ms

**Architecture:**
```
┌──────────────────────────────────────────────────────────────┐
│                        Load Balancer                          │
└──────────────────────────────────────────────────────────────┘
                              │
              ┌───────────────┴───────────────┐
              ▼                               ▼
┌──────────────────────┐         ┌──────────────────────┐
│    Search Cluster    │         │    LLM Cluster       │
│  (Elasticsearch/     │         │  (GPU inference      │
│   Custom sharded)    │         │   servers)           │
└──────────────────────┘         └──────────────────────┘
              │                               │
              └───────────────┬───────────────┘
                              ▼
                    ┌──────────────┐
                    │   Combiner   │
                    │   Service    │
                    └──────────────┘
```

**Scale Calculations:**
```
Documents: 1B
Shards needed: 1B / 10M per shard = 100 shards
Replicas per shard: 3 (for 1M QPS)
Total search nodes: ~300

LLM inference:
- 10K RPS at 100ms = 1K concurrent requests
- At 8 A100 GPUs per server, ~50 RPS per server
- Need: 200 inference servers
```

**Deep Dive:**

1. **Search Scaling**
   - Sharding by document ID hash
   - Scatter-gather query pattern
   - Caching hot queries

2. **LLM Scaling**
   - Batching for efficiency
   - KV-cache optimization
   - Speculative decoding

3. **Consistency**
   - Async index updates
   - Eventually consistent acceptable?
   - Cache invalidation

---

### Scenario 2: Token Generation at Scale

> "Scale a token-generating function to handle 100K RPS."

**Requirements:**
- Generate unique tokens
- 100K RPS globally
- Sub-10ms latency
- No duplicates

**Options Analysis:**

| Approach | Pros | Cons |
|----------|------|------|
| UUID | Simple, distributed | 128-bit, not sequential |
| Snowflake | 64-bit, sequential | Clock sync needed |
| Central counter | Simple | SPOF, bottleneck |
| Range allocation | Fast, distributed | Range management |

**Recommended: Snowflake-style**
```
┌────────────────────────────────────────────────────────┐
│  1 bit │  41 bits   │  10 bits  │     12 bits         │
│ unused │ timestamp  │ machine ID│    sequence         │
└────────────────────────────────────────────────────────┘

- 41 bits timestamp: ~69 years
- 10 bits machine: 1024 machines
- 12 bits sequence: 4096 per ms per machine
- Total: 4M tokens/ms = 4B tokens/sec globally
```

---

## DeepMind-Style Questions

### Scenario 1: Experiment Tracking System

> "Design a system for tracking ML experiments at scale."

**Requirements:**
- Track 1000s of experiments/day
- Store metrics, artifacts, code versions
- Support comparison and analysis
- Reproduce any experiment

**Components:**
```
Experiment Run → Tracker Client → API Server → Storage Backend
                      │                             │
                      ├── Metrics (time series)     ├── Metrics DB
                      ├── Artifacts (models, data)  ├── Object Store
                      ├── Code (git ref)            ├── Git integration
                      └── Parameters                └── Metadata DB
```

**Key Features:**
1. **Reproducibility**
   - Git commit hash
   - Environment snapshot
   - Random seeds
   - Data versioning

2. **Comparison**
   - Parallel coordinates plots
   - Metric comparison tables
   - Statistical tests

3. **Artifact Management**
   - Large file storage
   - Versioning
   - Lineage tracking

---

## xAI-Style Questions

### Scenario 1: High-Throughput Log Ingestion

> "Design a log ingestion pipeline handling 1M events/second."

**Requirements:**
- 1M events/second peak
- Each event ~1KB
- Real-time processing for alerts
- 30-day retention

**Architecture:**
```
Sources → Kafka Cluster → Stream Processing → Storage
             │                    │              │
             ├── Partitioned      ├── Flink      ├── Hot: Elastic
             ├── Replicated       └── Alerts     ├── Warm: S3
             └── Ordered                         └── Cold: Glacier
```

**Scale Math:**
```
Throughput: 1M events/sec × 1KB = 1GB/sec
Daily: 86.4TB
30 days: ~2.5PB

Kafka partitions: 1M/10K per partition = 100+ partitions
Stream processors: Based on processing time
```

---

### Scenario 2: Model Serving with A/B Testing

> "Design model serving for real-time inference with multi-version A/B testing."

**Requirements:**
- 10K RPS inference
- P99 < 100ms
- Support 10+ model versions simultaneously
- Gradual rollout capability

**Architecture:**
```
Request → Gateway → Traffic Router → Model Pool → Response
             │           │               │
             │           ├── A/B config  ├── Model A (90%)
             │           └── Sticky      ├── Model B (9%)
             │               sessions    └── Model C (1%)
             │
             └── Metrics Collector → Analysis Dashboard
```

**Key Components:**

1. **Traffic Routing**
   - Consistent hashing for stickiness
   - Weight-based distribution
   - Gradual rollout controls

2. **Model Pool**
   - Hot-swappable models
   - Graceful version transitions
   - Resource isolation

3. **Metrics**
   - Latency per model
   - Accuracy metrics
   - Business metrics
   - Statistical significance

---

## General Tips

### Framework for Any ML System Design

1. **Requirements** (5 min)
   - Functional: What does it do?
   - Non-functional: Scale, latency, accuracy
   - Constraints: Budget, team, timeline

2. **High-Level Design** (10 min)
   - Draw components
   - Show data flow
   - Identify critical path

3. **Deep Dive** (20 min)
   - Pick 2-3 components
   - Discuss trade-offs
   - Show depth of knowledge

4. **Extensions** (10 min)
   - How to scale 10x?
   - How to add new features?
   - What could go wrong?

### Common Pitfalls to Avoid

1. **Jumping to solutions** - Clarify requirements first
2. **Ignoring scale** - Always do back-of-envelope math
3. **Forgetting monitoring** - ML systems need observability
4. **Over-engineering** - Start simple, add complexity as needed
5. **Ignoring failures** - Discuss what happens when things break
