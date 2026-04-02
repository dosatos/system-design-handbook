# Technical Targets: Practical Engineering Focus

Specific, measurable goals for technical preparation optimized for **Anthropic** and **OpenAI** practical interview styles.

**Last Updated**: March 30, 2026  
**Timeline**: 8 weeks  
**Philosophy**: Practical engineering demonstrations over algorithm memorization

---

## Overall Technical Readiness Goal

**Target State**: Demonstrate practical engineering ability through deployed projects, solve real-world problems efficiently, and master ML infrastructure design.

**Timeline**: 8 weeks

**Key Insight**: Both Anthropic and OpenAI value **practical engineering over theoretical algorithms**.

---

## Portfolio Projects Targets

### Project #1: AI-Web Ecosystem Research
**Timeline**: Week 1-3  
**Status**: [ ] Not Started (Starts TODAY - March 31, 2026)

**Research Goals**:
- [ ] Research question defined and methodology documented
- [ ] 100+ major sites analyzed (news, tech blogs, platforms)
- [ ] Protection mechanisms cataloged and categorized
- [ ] Effectiveness analysis completed
- [ ] Proposed framework for sustainable AI-web ecosystem
- [ ] 3,000+ word research report/blog post written
- [ ] Dataset published with findings

**Technical Goals** (Scraper as Research Tool):
- [ ] Robots.txt parser and checker implemented
- [ ] Token bucket rate limiter with per-domain limits
- [ ] Site accessibility checker (detects paywalls, CAPTCHAs, etc.)
- [ ] Claude Agent SDK integration for intelligent crawling
- [ ] Batch analyzer for 100+ sites
- [ ] Robots.txt analyzer tool (public utility)
- [ ] Data collection and aggregation pipeline
- [ ] GitHub repo with research/ and tools/ directories

**Success Metrics**: 
- Published research with novel insights
- 100+ sites analyzed with statistical findings
- Working scraper demonstrating ethical practices
- Technical framework proposal that could influence industry

---

### Project #2: RLHF Reward Model Trainer (or Alternative)
**Timeline**: Week 3-5  
**Status**: [ ] Not Started

**Decision Point**: End of Week 3 based on scraper progress

**Option A: RLHF Technical Goals**:
- [ ] Reward model training pipeline set up
- [ ] Anthropic HH-RLHF dataset processed
- [ ] Model trained on preference pairs
- [ ] Evaluation metrics computed (agreement with humans)
- [ ] Clean GitHub repo with training logs
- [ ] Technical write-up on RLHF implementation

**Option B: Alternative Project Goals**:
- [ ] TBD based on Week 3 insights and interests
- [ ] Could be: Inference optimization, interpretability tool, or another agent

**Success Metric**: Technically impressive ML project relevant to Anthropic/OpenAI

---

### Project #3: OPTIONAL - Additional Project
**Timeline**: Week 5-6  
**Status**: [ ] TBD - Likely Skip

**Note**: Two strong projects may be sufficient. Focus on applications and interviews over third project.

**If Pursued** (only if ahead of schedule):
- [ ] Choose relevant ML or agent project
- [ ] Complete implementation
- [ ] Document and deploy
- [ ] Add to resume if time permits

**Success Metric**: Optional - prioritize quality of 2 projects over quantity of 3

---

## Practical Coding Targets

### Problem Count Goals (75-100 Total)

| Milestone | Count | Target Week | Focus | Status |
|-----------|-------|-------------|-------|--------|
| Foundations | 20 | Week 2 | Real-world patterns, string/list ops | [ ] |
| Build Phase | 30 | Week 4 | Graph/tree, concurrency, ML patterns | [ ] |
| Polish Phase | 30 | Week 6 | Timed practice, company-style | [ ] |
| **Total Goal** | **75-100** | **Week 6** | **Practical engineering** | [ ] |

### Practical Pattern Mastery

| Pattern Category | Target Problems | Real-World Use Cases | Status |
|------------------|-----------------|---------------------|--------|
| String/Parsing | 10 | Log processing, data cleaning | [ ] |
| Dict/HashMap | 10 | Caching, frequency counting, indexing | [ ] |
| List Operations | 8 | Filtering, transformations, pipelines | [ ] |
| File I/O & Data | 8 | Data processing, ETL | [ ] |
| Error Handling | 5 | Robust production code | [ ] |
| Concurrency | 8 | Async APIs, threading | [ ] |
| API Design | 8 | REST endpoints, request handling | [ ] |
| Graph/Tree | 12 | Dependency resolution, recommendations | [ ] |
| Dynamic Programming | 10 | Caching, optimization | [ ] |
| Stream Processing | 8 | Real-time data, pipelines | [ ] |

**NOT** focusing on: Algorithm theory, memorizing Big O proofs, competitive programming tricks

### Speed Goals (Practical Focus)

| Difficulty | Current | Target | Measurement |
|------------|---------|--------|-------------|
| Easy Practical | - min | 15 min | Build + test working solution |
| Medium Practical | - min | 30 min | Build + test working solution |
| Hard Practical | - min | 45 min | Build + test working solution |

**Key**: "Working solution" = runs, handles edge cases, can be explained clearly

---

## System Design Targets

### Core ML Infrastructure Designs (10 Total)

| System | Week | Priority | Target Rating (1-5) | Status |
|--------|------|----------|---------------------|--------|
| URL Shortener | 1 | Foundation | 4 | [ ] |
| Rate Limiter | 2 | Foundation | 4 | [ ] |
| Chat System | 3 | Anthropic Focus | 5 | [ ] |
| ML Training Pipeline | 3 | Core ML | 5 | [ ] |
| Feature Store | 4 | ML Infrastructure | 5 | [ ] |
| Model Serving Infrastructure | 4 | Core ML | 5 | [ ] |
| RLHF Pipeline | 5 | Anthropic/OpenAI Focus | 5 | [ ] |
| Conversational AI System | 5 | Anthropic Focus | 5 | [ ] |
| ChatGPT-scale API | 5 | OpenAI Focus | 5 | [ ] |
| Real-time Inference | 6 | Production ML | 5 | [ ] |

### Framework Mastery Goals

- [ ] Can run system design framework without notes
- [ ] Capacity estimation quick and reasonable (within 10x)
- [ ] Trade-off discussions natural and thoughtful
- [ ] Can deep-dive on any component when asked
- [ ] **ML infrastructure is a strength** (critical for both companies)
- [ ] Can explain distributed systems concepts clearly
- [ ] Performance optimization patterns second nature

### Mock Interview Targets

| Type | Target Count | Min Pass Rate | Week Achieved |
|------|-------------|---------------|---------------|
| Mock System Design | 5+ | 80% positive | Week 6 |
| Full 45-min simulations | 5+ | All pass | Week 6 |

---

## ML Knowledge Targets

### Core ML Fundamentals

| Topic | Target Understanding Level | Status |
|-------|---------------------------|--------|
| **Transformer Architecture** | Can whiteboard and explain each component | [ ] |
| **Attention Mechanism** | Explain math intuitively, scaled dot-product | [ ] |
| **Positional Encoding** | Know why needed, absolute vs relative | [ ] |
| **Tokenization** | BPE, SentencePiece, vocabulary size trade-offs | [ ] |
| **Training Basics** | Loss functions, optimizers (Adam, SGD), learning rates | [ ] |
| **Distributed Training** | Data parallel, model parallel, pipeline parallel | [ ] |
| **Mixed Precision** | FP16/BF16 training, why faster, stability | [ ] |

### RLHF Pipeline (Critical for Both Companies)

| Stage | Target Understanding | Status |
|-------|---------------------|--------|
| **Supervised Fine-Tuning** | Purpose, data requirements, process | [ ] |
| **Reward Modeling** | Preference learning, Bradley-Terry model | [ ] |
| **PPO Training** | High-level algorithm, policy optimization | [ ] |
| **Constitutional AI** | How it differs from RLHF (Anthropic focus) | [ ] |
| **Failure Modes** | Reward hacking, distribution shift, safety | [ ] |

### Inference Optimization (Production ML)

| Topic | Target Understanding | Status |
|-------|---------------------|--------|
| **KV Caching** | Memory trade-offs, when to use | [ ] |
| **Quantization** | INT8, FP16, accuracy vs speed | [ ] |
| **Batching Strategies** | Static vs continuous batching | [ ] |
| **Model Optimization** | ONNX, TensorRT, pruning | [ ] |
| **Latency Optimization** | Request coalescing, caching | [ ] |

### Company-Specific ML Topics

#### Anthropic Focus
- [ ] Constitutional AI approach thoroughly understood
- [ ] Claude architecture and capabilities
- [ ] AI safety research (alignment, interpretability)
- [ ] Can discuss AI safety thoughtfully and genuinely

#### OpenAI Focus
- [ ] GPT architecture evolution (GPT-2 → GPT-4)
- [ ] Scaling laws and implications
- [ ] ChatGPT and API products
- [ ] RLHF implementation at scale

---

## Behavioral Story Targets

### Story Bank (8-10 Total)

| Story Type | Target Count | Quality Goal | Status |
|------------|-------------|--------------|--------|
| **Ownership Stories** | 2-3 | Led end-to-end, shipped, impact | [ ] |
| **Technical Depth** | 2-3 | Solved hard problem, deep dive | [ ] |
| **Collaboration** | 2-3 | Cross-functional, team success | [ ] |
| **Failure/Learning** | 1-2 | What you learned, growth | [ ] |
| **AI Safety** | 1-2 | Thought about implications | [ ] |

### Story Quality Criteria

Each story should:
- [ ] Follow STAR format (Situation, Task, Action, Result)
- [ ] Be told in 2-3 minutes
- [ ] Include specific technical details
- [ ] Show ownership and impact
- [ ] Demonstrate company value alignment
- [ ] Have follow-up details ready for deep-dives

### Company-Specific Preparation

**Anthropic Focus**:
- [ ] Stories emphasize careful thinking and safety
- [ ] Can discuss trade-offs thoughtfully
- [ ] Show independent work (open source, blog posts)
- [ ] Demonstrate long-term thinking

**OpenAI Focus**:
- [ ] Stories emphasize ownership and speed
- [ ] Can discuss large-scale impact
- [ ] Show end-to-end execution
- [ ] Demonstrate product thinking

---

## Weekly Technical Targets

### Week 1-2: Foundations
- [ ] RAG system 60% complete
- [ ] 20 practical problems solved
- [ ] 2 system designs (URL shortener, rate limiter)
- [ ] Transformer architecture understood
- [ ] Company research started

### Week 3-4: Deep Build
- [ ] RAG system deployed ✅
- [ ] Distributed trainer 60% complete
- [ ] 50 practical problems total
- [ ] 6 system designs total (4 new)
- [ ] RLHF pipeline understood
- [ ] 4 STAR stories drafted

### Week 5-6: Polish & Apply
- [ ] All 3 projects deployed ✅
- [ ] 75-100 practical problems solved
- [ ] 10 system designs mastered
- [ ] 6 mock interviews completed
- [ ] Resume finalized (projects at TOP)
- [ ] Applications submitted Week 5 ✅
- [ ] Referrals secured
- [ ] 8-10 behavioral stories polished

### Week 7-8: Interview Mode
- [ ] Daily warm-up routine established
- [ ] Company-specific prep for each interview
- [ ] Portfolio projects demo-ready
- [ ] At least one offer received
- [ ] Dual offers for negotiation leverage

---

## GitHub Profile Targets

### Repository Organization
- [ ] 3 portfolio projects pinned
- [ ] Each repo has clear README with:
  - [ ] Project overview and motivation
  - [ ] Architecture diagram
  - [ ] Setup instructions
  - [ ] Performance benchmarks
  - [ ] Technologies used
- [ ] Clean commit history (meaningful messages)
- [ ] Code is well-documented and formatted
- [ ] No secrets or credentials in repos

### Profile Quality
- [ ] Profile README highlights key projects
- [ ] Contributions show consistent activity (especially Weeks 1-6)
- [ ] Projects demonstrate practical engineering
- [ ] Languages: Python prominently featured

---

## Resume Targets

### Structure (Anthropic Guidance)
- [ ] Independent projects and open source at **TOP**
- [ ] Portfolio projects with impact metrics
- [ ] Technical skills section clear and honest
- [ ] Work experience emphasizes ownership
- [ ] Education present but not emphasized over practical work

### Content Quality
- [ ] Each project has impact metric (latency, throughput, scale)
- [ ] Action verbs: "Built", "Designed", "Implemented", "Deployed"
- [ ] Technical depth visible (specific technologies)
- [ ] Mission alignment signals where appropriate
- [ ] 1 page maximum, clean formatting

### Company-Specific Versions
- [ ] Anthropic version: Safety, independent work, practical engineering
- [ ] OpenAI version: Scale, ownership, product impact

---

## Reading & Research Targets

### Essential Reading

| Material | Target Week | Priority | Status |
|----------|-------------|----------|--------|
| Anthropic blog posts | Week 1-2 | HIGH | [ ] |
| Constitutional AI papers | Week 3-4 | HIGH | [ ] |
| OpenAI GPT papers | Week 2-3 | HIGH | [ ] |
| RLHF papers (InstructGPT) | Week 4 | HIGH | [ ] |
| Attention Is All You Need | Week 1 | MEDIUM | [ ] |
| Relevant DDIA chapters (5,6,9) | Week 2-4 | MEDIUM | [ ] |

### Company News & Culture
- [ ] Read all Anthropic blog posts from 2025-2026
- [ ] Read OpenAI blog posts from 2025-2026
- [ ] Understand AI safety landscape and debates
- [ ] Know recent product launches and features
- [ ] Familiar with company culture (Glassdoor, Blind, etc.)

---

## Verification Methods

### Portfolio Projects
✅ **Deployed and accessible** via public URL  
✅ **GitHub repo public** with professional README  
✅ **Can demo live** in <5 minutes  
✅ **Can explain technical decisions** clearly  
✅ **Performance metrics documented**

### Practical Coding
✅ **Can solve Medium in 30 min** consistently  
✅ **Can explain approach** before coding  
✅ **Code runs and passes tests**  
✅ **Can handle edge cases**  
✅ **Speed improving week over week**

### System Design
✅ **Can complete 45-min design** without notes  
✅ **Receives positive feedback** in mocks  
✅ **Can handle deep-dive questions**  
✅ **Trade-off discussions natural**  
✅ **ML infrastructure is comfortable**

### ML Knowledge
✅ **Can explain to non-expert** clearly  
✅ **Can answer "why" not just "what"**  
✅ **Can discuss trade-offs** thoughtfully  
✅ **Can connect concepts** to real systems

---

## Success Indicators by Week

### ✅ Week 2 Success
- RAG system showing visible progress
- Comfortable solving practical easy/medium problems
- System design framework internalized
- Transformer architecture clear

### ✅ Week 4 Success
- RAG system deployed and working
- 50+ problems solved with improving speed
- System design confidence growing
- RLHF pipeline understood
- Behavioral stories drafted

### ✅ Week 6 Success
- All 3 projects deployed and documented
- 75-100 problems solved, speed targets met
- System design fluent (10 designs practiced)
- Mock interview feedback positive
- Applications submitted, referrals secured

### ✅ Week 8 Success
- Active in interview processes
- Projects demo-ready and impressive
- Technical discussions confident
- At least one offer in hand
- Ready to negotiate

---

## Daily Habits for Success

### During Build Phase (Weeks 1-6)
- **Morning**: 1-2 practical problems (45-60 min)
- **Midday/Evening**: Portfolio project work (1-2 hrs)
- **Evening**: System design or ML reading (30-60 min)

### During Interview Phase (Weeks 7-8)
- **Morning**: Warm-up problems (30 min)
- **Midday**: Interviews as scheduled
- **Evening**: Review and company-specific prep (30-60 min)

---

## Tracking Progress

### Weekly Review Questions
1. Are portfolio projects on schedule?
2. Is coding speed improving?
3. Is system design confidence growing?
4. Are behavioral stories polished?
5. Is GitHub profile professional?
6. Is resume highlighting practical engineering?

### Files to Update
- `projects/` - Project documentation and progress
- `practice/coding/problems-log.md` - Problem tracking
- `practice/system-designs/` - Design practice records
- `practice/behavioral/story-bank.md` - STAR stories
- `progress/weekly/week-XX.md` - Weekly progress
- `memory/journey-log.md` - Session summaries

---

## Adjustment Criteria

**Accelerate** if:
- Projects completing ahead of schedule
- Coding speed hitting targets early
- System design already fluent
- Recruiter reaches out early

**Slow down** if:
- Projects taking longer than expected
- Coding speed not improving
- System design still unclear
- Need more depth in ML fundamentals

**Pivot focus** if:
- Recruiter gives specific feedback
- Interview schedule changes
- Weak areas identified in mocks

---

## Final Success Criteria

By end of Week 6, you should:
✅ Have 3 impressive deployed projects  
✅ Solve practical Medium problems in 30 min  
✅ Design ML systems confidently  
✅ Discuss AI safety thoughtfully  
✅ Tell compelling behavioral stories  
✅ Have applications submitted with referrals  
✅ Be ready to interview and impress

**The difference**: Not algorithm patterns memorized, but **real systems built**.

---

<!-- Track your progress by checking off boxes as you go -->
