# Phase 3: Company-Specific Preparation (Weeks 7-9)

## Goals

- Practice company-style coding challenges
- Master ML system design
- Prepare behavioral stories and AI safety knowledge
- Start mock interview practice

---

## Week 7: AI Company Coding Style

### Coding Focus: Company-Style Problems

**Anthropic-Style Progressive Challenges:**

Practice building iteratively complex systems:

1. **In-Memory Database Challenge**
   ```
   Level 1: Basic SET/GET/DELETE operations
   Level 2: Add filtered scans (WHERE clauses)
   Level 3: Add TTL with timestamps
   Level 4: Add compression/decompression
   ```

2. **Bank Application Challenge**
   ```
   Level 1: Basic deposit/withdraw
   Level 2: Add transfers between accounts
   Level 3: Add transaction history
   Level 4: Add concurrent transaction handling
   ```

3. **Package Manager Challenge**
   ```
   Level 1: Install single packages
   Level 2: Handle dependencies
   Level 3: Detect circular dependencies
   Level 4: Optimize installation order
   ```

**Practice Platforms:**
- [CodeSignal](https://codesignal.com/) - Anthropic uses this
- [LeetCode](https://leetcode.com/) - General practice

**Timed Practice (90 min sessions):**
- Simulate real assessment conditions
- No IDE help, no looking up solutions
- Track completion time for each level

### OpenAI/xAI-Style Hard Problems

Focus on LeetCode Hard with these patterns:
- Complex DP with multiple states
- Graph algorithms with constraints
- Concurrency and thread safety

**Example Problems:**
1. Word Ladder II (BFS + Backtracking)
2. Median of Two Sorted Arrays (Binary Search)
3. Trapping Rain Water (Multiple approaches)
4. LRU Cache (Hash + Doubly Linked List)

**Concurrency Practice (xAI focus):**
```python
import threading
from collections import defaultdict

class ConcurrentHashMap:
    def __init__(self, num_shards=16):
        self.num_shards = num_shards
        self.shards = [defaultdict(int) for _ in range(num_shards)]
        self.locks = [threading.RLock() for _ in range(num_shards)]

    def _get_shard(self, key):
        return hash(key) % self.num_shards

    def get(self, key):
        shard = self._get_shard(key)
        with self.locks[shard]:
            return self.shards[shard].get(key)

    def put(self, key, value):
        shard = self._get_shard(key)
        with self.locks[shard]:
            self.shards[shard][key] = value
```

### System Design: RAG System

**Full Design: Document Q&A System**

Requirements:
- Upload documents (PDF, docs, text)
- Ask questions about content
- Get accurate, cited answers
- Handle 1M documents, 10K queries/day

**Architecture:**
```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│   Document   │────▶│   Chunking   │────▶│  Embedding   │
│    Upload    │     │   Service    │     │   Service    │
└──────────────┘     └──────────────┘     └──────┬───────┘
                                                  │
                                                  ▼
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│    Query     │────▶│   Retriever  │◀────│   Vector     │
│   Service    │     │              │     │   Database   │
└──────┬───────┘     └──────┬───────┘     └──────────────┘
       │                    │
       ▼                    ▼
┌──────────────┐     ┌──────────────┐
│   Reranker   │────▶│     LLM      │────▶ Answer
│              │     │  Generation  │
└──────────────┘     └──────────────┘
```

**Key Decisions:**

| Component | Options | Trade-offs |
|-----------|---------|------------|
| Chunking | Fixed size, Semantic, Sliding window | Accuracy vs simplicity |
| Embeddings | OpenAI ada-002, Cohere, local | Cost vs quality |
| Vector DB | Pinecone, Weaviate, Milvus | Managed vs self-hosted |
| Retrieval | Top-K, Hybrid (dense + sparse) | Recall vs precision |
| Reranking | Cross-encoder, LLM-based | Latency vs accuracy |

### Mock Interviews

**Schedule 2 coding mock interviews this week:**

- [Pramp](https://www.pramp.com/) - Free peer-to-peer
- [Interviewing.io](https://interviewing.io/) - Paid, FAANG engineers
- Friends/colleagues - Most realistic

**Mock Interview Protocol:**
1. 5 min: Introductions
2. 45 min: Problem solving
3. 10 min: Feedback

### Week 7 Deliverables

- [ ] Complete 2 timed 90-min coding assessments
- [ ] Design RAG system end-to-end (45 min)
- [ ] Complete 2 mock coding interviews
- [ ] Implement concurrent data structure

---

## Week 8: System Design & ML Design Focus

### Coding Maintenance

- Review weak areas from Weeks 1-7
- 3-4 hard problems per day
- Focus on production-ready code
- Practice explaining while coding

### ML System Design Deep Dive

**Design 1: Recommendation System**

Requirements:
- Personalized content recommendations
- 100M users, 10M items
- Real-time recommendations
- Cold start handling

**Architecture:**
```
┌─────────────────────────────────────────────────────────┐
│                    Online Serving                        │
│  ┌─────────┐   ┌───────────┐   ┌──────────────────┐    │
│  │ Feature │──▶│ Candidate │──▶│    Ranking       │    │
│  │  Store  │   │ Generation│   │    Model         │    │
│  └─────────┘   └───────────┘   └──────────────────┘    │
│                                                          │
├─────────────────────────────────────────────────────────┤
│                    Offline Training                      │
│  ┌─────────┐   ┌───────────┐   ┌──────────────────┐    │
│  │  Data   │──▶│  Feature  │──▶│    Model         │    │
│  │  Lake   │   │Engineering│   │   Training       │    │
│  └─────────┘   └───────────┘   └──────────────────┘    │
└─────────────────────────────────────────────────────────┘
```

**Design 2: Model Serving Infrastructure**

Requirements:
- Serve 10K+ requests/second
- P99 latency < 100ms
- Multi-model support
- A/B testing capability

**Key Components:**
1. **Load Balancer** - Traffic distribution
2. **Model Registry** - Version management
3. **Inference Servers** - GPU-optimized serving
4. **Feature Store** - Online features
5. **Monitoring** - Latency, accuracy, drift

**Design 3: Distributed Training System**

Requirements:
- Train 100B+ parameter models
- Multi-node, multi-GPU
- Fault tolerance
- Efficient checkpointing

**Topics to Cover:**
- Data parallelism with gradient sync
- Model parallelism strategies
- Pipeline parallelism
- Mixed precision training
- Checkpointing strategies

### Company Research Deep Dive

**Read engineering blogs (past 6 months):**

| Company | Blog | Key Posts |
|---------|------|-----------|
| OpenAI | [developers.openai.com/blog](https://developers.openai.com/blog/) | Codex, voice models |
| Anthropic | [anthropic.com/engineering](https://www.anthropic.com/engineering) | Multi-agent, context engineering |
| DeepMind | [deepmind.google/blog](https://deepmind.google/blog/) | Gemini, AlphaFold |

**Watch technical talks from each company**

### Mock Interviews

**Schedule 2 system design mock interviews:**
- Focus on ML system design
- Practice 45-minute structured discussions
- Get feedback on communication

### Week 8 Deliverables

- [ ] Complete 3 ML system design exercises
- [ ] Read 5+ engineering blog posts per target company
- [ ] Complete 2 mock system design interviews
- [ ] Document key learnings from company research

---

## Week 9: Behavioral & Culture Deep Dive

### Coding Maintenance

- 2-3 medium problems daily
- Focus on explaining thought process aloud
- Time yourself strictly

### Behavioral Preparation

**Prepare 10 STAR Stories:**

| Theme | Story Prompt |
|-------|--------------|
| Technical Leadership | Led a complex project |
| Conflict Resolution | Disagreed with teammate/manager |
| Failure & Learning | Project that didn't succeed |
| Ambiguity | Unclear requirements |
| Impact at Scale | Biggest technical impact |
| Mentoring | Helped someone grow |
| Safety/Ethics | Raised a concern |
| Cross-Team | Worked with other teams |
| Initiative | Did something without being asked |
| Learning | Quickly learned new technology |

**STAR Framework:**
```
S - Situation: Set the context (brief)
T - Task: Your specific responsibility
A - Action: What YOU did (be specific)
R - Result: Quantified outcome + learnings
```

**Example:**
```
S: "Our ML pipeline was taking 8 hours to run, blocking daily deployments."

T: "As the tech lead, I was responsible for improving our iteration speed."

A: "I profiled the pipeline and found the bottleneck was in data loading.
    I implemented parallel data loading with Ray, added caching for
    preprocessed features, and redesigned the pipeline to use incremental
    processing."

R: "Pipeline time dropped to 45 minutes (10x improvement). This enabled
    daily model updates, which improved our recommendation accuracy by 5%.
    I documented the approach and it's now used by 3 other teams."
```

### AI Safety & Ethics Study

**Required Reading:**

1. **Anthropic's Constitutional AI paper**
   - How Claude is trained with AI feedback
   - Principles-based approach to safety

2. **RLHF papers**
   - InstructGPT (OpenAI)
   - Fine-tuning language models from human preferences

3. **Alignment Science Blog** (Anthropic)
   - Sabotage risk reports
   - Interpretability research

**Topics to Understand:**

- [ ] Why is RLHF used over just supervised learning?
- [ ] What is Constitutional AI?
- [ ] What are the limitations of current alignment techniques?
- [ ] What is deceptive alignment?
- [ ] How do you evaluate model safety?

**Sample Safety Questions:**

1. "What are the biggest risks of deploying LLMs at scale?"
2. "How would you design safety evaluations for a new model?"
3. "What's your view on the pace of AI development vs safety research?"
4. "How do you balance capability improvements with safety?"
5. "Describe a time you prioritized safety over shipping"

### Mission Alignment Practice

**For each company, be able to articulate:**
1. What is their mission?
2. Why does it matter to you personally?
3. How does your background align?
4. What would you contribute?

**OpenAI Alignment:**
> "I want to ensure AGI benefits humanity. My experience in [X] taught me
> the importance of [Y]. I believe we need to move fast on capabilities
> while being thoughtful about safety."

**Anthropic Alignment:**
> "AI safety is deeply important to me because [personal reason]. I'm drawn
> to Anthropic's approach of making safety a core part of the research, not
> an afterthought. I can contribute [specific skills]."

### Week 9 Deliverables

- [ ] Write and practice 10 STAR stories
- [ ] Read 3 AI safety papers
- [ ] Articulate each target company's mission
- [ ] Complete 2 behavioral mock interviews
- [ ] Prepare questions for interviewers

---

## Phase 3 Summary

### Skills Developed

| Area | Status |
|------|--------|
| Company-style coding | Practiced progressive challenges |
| ML system design | 3+ designs completed |
| Behavioral stories | 10 STAR stories ready |
| AI safety knowledge | Papers read, positions formed |
| Mock interviews | 6+ completed |

### Mock Interview Progress

| Week | Type | Count |
|------|------|-------|
| 7 | Coding | 2 |
| 8 | System Design | 2 |
| 9 | Behavioral | 2 |
| **Total** | | **6** |

### Readiness Checklist

**Coding:**
- [ ] Can complete 90-min progressive challenge
- [ ] Handle LeetCode Hard in 45 min
- [ ] Write production-quality code

**System Design:**
- [ ] Design ML systems end-to-end in 45 min
- [ ] Discuss trade-offs fluently
- [ ] Connect designs to company context

**Behavioral:**
- [ ] 10 polished STAR stories
- [ ] Articulate company missions
- [ ] Discuss AI safety intelligently

---

## Next Steps

Continue to [Phase 4: Interview Mode](./phase4-interview-mode.md)
