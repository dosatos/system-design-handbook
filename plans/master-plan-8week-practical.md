# Master Plan: 8-Week Practical Engineering Preparation

## Overview

An 8-week intensive practical engineering program targeting Senior SWE roles at **Anthropic** and **OpenAI**.

**Updated**: March 30, 2026  
**Start Date**: [To be set]  
**Target Interview Window**: Weeks 6-8  
**Weekly Time Commitment**: 25-30 hours

## Critical Insight: Why This Plan is Different

Both Anthropic and OpenAI emphasize **practical engineering over algorithm theory**:

**Anthropic**: *"You can look things up—just be comfortable with basic syntax"*  
**OpenAI**: *"Practical engineering focus over theoretical algorithms"*

This plan reflects that reality: **40% portfolio projects, 30% system design, 20% targeted coding, 10% behavioral/company prep**.

---

## Phase Summary

| Phase | Weeks | Focus | Key Deliverables |
|-------|-------|-------|------------------|
| 1: Build Foundations | 1-2 | Core patterns, Project 1 setup, ML basics | RAG system started, 20 problems |
| 2: Deep Build | 3-4 | Project 1 complete, Project 2, system design | RAG deployed, distributed trainer started, 30 problems |
| 3: Polish & Apply | 5-6 | Project 3, applications, mocks | Model serving deployed, apps submitted, referrals |
| 4: Interview Mode | 7-8 | Active interviewing, maintain sharpness | Offers secured, negotiation |

---

## Phase 1: Build Foundations (Weeks 1-2)

### Goals
- Establish practical Python proficiency
- Start Portfolio Project #1 (RAG System)
- Learn core coding patterns (not LeetCode grinding)
- Begin ML fundamentals
- Start company research

### Portfolio Project #1: AI-Web Ecosystem Research (Week 1-3)
**Goal**: Research project on AI-web tensions + ethical scraper as research tool

**Research Question**: How are content creators protecting against AI crawlers, how effective are these protections, and what's a sustainable path forward?

**Tech Stack**: Python, Claude Agent SDK, robots.txt parser, BeautifulSoup, data analysis

**Components**:
1. **Ethical Web Scraper** (research tool) - collects data from 100+ sites
2. **Data Analysis** - categorize protection strategies, measure effectiveness  
3. **Research Report** - 3,000+ word blog post with findings and framework
4. **Robots.txt Analyzer Tool** - public tool for site analysis

**Why This Matters**: 
- **Incredibly timely** - NYT lawsuit, licensing deals, GEO emergence
- **Directly relevant to Anthropic/OpenAI** - they face this problem daily
- Shows ethical thinking (Constitutional AI alignment)
- Research + technical + analysis (not just coding)
- Novel insights vs following tutorials
- Could generate real-world impact

**Deliverables**:
- Research report/blog post (3,000+ words)
- Ethical scraper using Claude Agent SDK
- Dataset of 100+ site protection strategies
- Proposed technical framework for sustainable AI-web ecosystem

**Time**: 20-25 hours over 3 weeks

### Practical Coding (20 problems)
**Focus**: Real-world patterns, not algorithm theory

**Week 1 (10 problems)**:
- String manipulation and parsing (log processing, data cleaning)
- Dictionary/hash map patterns (caching, frequency counting)
- List operations (filtering, transformations)
- API design problems

**Week 2 (10 problems)**:
- File I/O and data processing
- Error handling patterns
- Concurrency basics (threading, async)
- Testing and debugging scenarios

**Resource**: Python coding interview patterns, practical engineering problems (not Blind 75)

### System Design (2 sessions)
- Week 1: URL Shortener (distributed systems basics)
- Week 2: Rate Limiter (API design, distributed caching)

**Reference**: `roadmap/05-system-design/framework.md`

### ML Fundamentals (Week 1-2)
- Transformer architecture deep dive
- Attention mechanisms and positional encoding
- Training fundamentals (loss functions, optimization)
- RLHF overview

**Reference**: `roadmap/02-technical-preparation/ml-fundamentals.md`

### Company Research (Week 1-2)
- Read Anthropic: Constitutional AI papers, Claude blog posts
- Read OpenAI: GPT papers, ChatGPT case studies
- Understand AI safety landscape
- Draft "Why Anthropic?" and "Why OpenAI?" answers

### Weekly Time Breakdown
- **12 hrs**: Portfolio Project #1
- **6 hrs**: Practical coding (10 problems)
- **4 hrs**: System design (2 sessions)
- **4 hrs**: ML fundamentals reading
- **2 hrs**: Company research
- **Total**: 28 hours/week

---

## Phase 2: Deep Build (Weeks 3-4)

### Goals
- Complete and deploy Project #1
- Start and make progress on Project #2
- Deepen system design skills (ML focus)
- Build stronger coding proficiency
- RLHF deep dive

### Portfolio Project #1: Web Scraping Agent (Complete Week 3)
**Goal**: Finish, deploy, document

**Week 3 Deliverables**:
- Full implementation with robots.txt compliance
- Rate limiting and backoff working
- Clean GitHub repo with README
- Demonstration of ethical scraping (100+ URLs)
- Technical blog post on implementation choices
- Production-quality code

**Time**: 8-10 hours Week 3

### Portfolio Project #2: TBD - RLHF or Alternative (Week 3-4 Start)
**Goal**: Build technically deep ML project

**Option A: RLHF Reward Model Trainer**
**Tech Stack**: PyTorch, HuggingFace transformers, Anthropic HH dataset

**Features**:
- Reward model training on preference data
- Preference dataset processing (Anthropic HH-RLHF)
- Model evaluation and benchmarking
- Comparison to human preferences
- **Simplified scope**: Reward modeling only, not full PPO pipeline

**Why This Matters**:
- Directly relevant to Anthropic/OpenAI's core work
- Shows deep understanding of RLHF
- Few candidates have built this
- Great interview talking points

**Time**: 15-20 hours over 2 weeks

---

**Option B: Alternative ML Project** (Decide after Week 3)
- Transformer interpretability tool
- Inference optimization benchmark
- Or other technically impressive project

**Decision Point**: End of Week 3 based on:
- Scraper completion status
- Your comfort with ML training
- GPU access availability
- Interview timeline

**Time**: 15-20 hours over 2 weeks

### Practical Coding (30 problems total, 15 per week)
**Week 3 (15 problems)**:
- Graph traversal (dependency resolution, recommendation systems)
- Tree structures (parsing, hierarchical data)
- Dynamic programming (practical caching, optimization)
- API integration patterns

**Week 4 (15 problems)**:
- Stream processing (real-time data)
- Distributed systems patterns (consensus, replication)
- ML pipeline problems (data transforms, feature engineering)
- Performance optimization (profiling, bottleneck fixing)

### System Design (4 sessions, 2 per week)
**Week 3**:
- Chat System design
- ML Training Pipeline design

**Week 4**:
- Model Serving Infrastructure
- Feature Store design

**Reference**: `roadmap/05-system-design/ml-infrastructure.md`

### ML Deep Dive (Week 3-4)
- Week 3: RLHF pipeline end-to-end
- Week 4: Constitutional AI, reward modeling
- Inference optimization (KV caching, quantization)
- Scaling laws and distributed training

### Behavioral Stories (Week 3-4)
- Week 3: Audit work history, draft 4 core STAR stories
- Week 4: Refine stories for ownership, mission alignment, AI safety

### Weekly Time Breakdown
- **10-12 hrs**: Portfolio projects (finish #1, start #2)
- **8 hrs**: Practical coding (15 problems)
- **4 hrs**: System design (2 sessions)
- **4 hrs**: ML deep dive
- **2 hrs**: Behavioral stories
- **Total**: 28-30 hours/week

---

## Phase 3: Polish & Apply (Weeks 5-6)

### Goals
- Complete Project #2, start and finish Project #3
- Submit applications to both companies
- Secure referrals
- Mock interview practice
- Resume polished with projects at TOP

### Portfolio Project #2: RLHF or Alternative (Complete Week 5)
**Deliverables** (if doing RLHF):
- Trained reward model on preference data
- Evaluation metrics and comparisons
- Clean GitHub repo with training logs
- Technical write-up on RLHF implementation

**Deliverables** (if alternative project):
- Working implementation of chosen project
- Benchmarks or performance metrics
- Clean documentation
- Technical blog post

**Time**: 8-10 hours Week 5

### Portfolio Project #3: OPTIONAL - Additional Project (Week 5-6)
**Goal**: Third project if time permits

**Options**:
- Model serving API with optimization
- Distributed training infrastructure
- Another agent using Claude Agent SDK
- Whatever is most relevant based on Week 5 insights

**Decision**: This is OPTIONAL. Two strong projects may be enough.

**Priority**: Focus on applications, mocks, and interview prep over third project

**Time**: 10-12 hours IF pursued (likely skip)

### Practical Coding (30 problems total, 15 per week)
**Week 5 (15 problems)**:
- Anthropic-style practical problems
- OpenAI-style hard but practical problems
- Timed practice (45 min per problem)

**Week 6 (15 problems)**:
- Company-tagged problems if available
- Weak area review
- Mock interview simulations

### System Design (4 sessions)
**Week 5**:
- Full mock: Design a conversational AI system (Anthropic focus)
- Full mock: Design ChatGPT-scale API infrastructure (OpenAI focus)

**Week 6**:
- Full mock: Design real-time model inference system
- Full mock: Design RLHF training pipeline

### Mock Interviews (Week 5-6)
- Week 5: 2 mock coding interviews (practical focus)
- Week 6: 2 mock system design, 2 mock behavioral

### Application Activities (Week 5)
**Critical Week!**

- [ ] Resume finalized (projects at TOP per Anthropic guidance)
- [ ] LinkedIn profile updated
- [ ] GitHub cleaned and organized (3 projects pinned)
- [ ] Referrals secured at both companies
- [ ] "Why Anthropic?" answer perfected
- [ ] "Why OpenAI?" answer perfected
- [ ] **Applications submitted to both companies**

### Behavioral Prep (Week 5-6)
- Week 5: 8-10 STAR stories complete
- Week 6: AI safety discussion prep, mission alignment prep

### Weekly Time Breakdown
- **10 hrs**: Portfolio projects (finish #2, complete #3)
- **8 hrs**: Practical coding (15 problems)
- **4 hrs**: System design mocks
- **4 hrs**: Mock interviews
- **4 hrs**: Application prep (resume, referrals, company research)
- **Total**: 30 hours/week

---

## Phase 4: Interview Mode (Weeks 7-8)

### Goals
- Active interviewing at both companies
- Maintain technical sharpness
- Secure offers
- Negotiate compensation

### Daily Routine (While Interviewing)
**Morning (1 hr)**:
- 2-3 practical coding warm-up problems
- Review one system design pattern

**Midday**:
- Interviews as scheduled
- Company-specific research before each interview

**Evening (1-2 hrs)**:
- Review interview performance
- Prepare for next rounds
- Continue light coding practice

### Portfolio Maintenance
- Projects deployed and demo-ready
- Practice explaining technical decisions
- Prepare for deep technical discussions
- Have GitHub open and ready to show

### Interview Preparation (Company-Specific)
**Before Anthropic Interviews**:
- Review Constitutional AI approach
- Practice explaining RAG system with Claude integration
- Prepare AI safety discussion points
- Review Colab environment

**Before OpenAI Interviews**:
- Review GPT architecture and RLHF
- Practice ownership and end-to-end stories
- Prepare scaling and product thinking examples
- Be ready for "very hard" practical problems

### Negotiation (Week 7-8)
- Week 7: Review compensation data (levels.fyi March 2026)
- Week 8: Active negotiation as offers arrive
- Practice negotiation scripts
- Leverage dual offers

### Weekly Time Breakdown
- **7 hrs**: Daily coding warm-up (1 hr/day)
- **10-15 hrs**: Active interviews
- **5 hrs**: Interview prep and research
- **3 hrs**: Negotiation prep
- **Total**: 25-30 hours/week

---

## Key Success Metrics by Week

### End of Week 2
- [ ] Web scraping agent 60% complete (robots.txt + rate limiting working)
- [ ] 20 practical problems solved
- [ ] 2 system designs practiced
- [ ] Transformer architecture understood
- [ ] Company research started

### End of Week 4
- [ ] Web scraping agent deployed and documented ✅
- [ ] Project #2 started (RLHF or alternative 60% complete)
- [ ] 50 practical problems solved
- [ ] 6 system designs practiced
- [ ] RLHF pipeline understood (whether building it or not)
- [ ] 4 STAR stories drafted

### End of Week 6
- [ ] 2 strong projects deployed and demo-ready ✅ (3rd optional)
- [ ] 80 practical problems solved
- [ ] 10 system designs practiced
- [ ] 6 mock interviews completed
- [ ] Resume finalized with projects at TOP
- [ ] **Applications submitted to both companies** ✅
- [ ] Referrals secured

### End of Week 8
- [ ] Active in interview processes at both companies
- [ ] At least one offer received
- [ ] Dual offers for negotiation leverage
- [ ] Decision made

---

## Portfolio Projects: Detailed Specs

### Project #1: AI-Web Ecosystem Research
**Timeline**: Week 1-3  
**Deliverables**: Research report + ethical scraper + analyzer tool + dataset  
**GitHub**: [repo link with research/ and tools/ directories]

**Research Highlights**:
- Analyzed 100+ major sites' protection strategies (news, tech blogs, platforms)
- Categorized protection mechanisms: robots.txt (60%+ block AI bots), paywalls, rate limits
- Measured effectiveness of current protections
- Proposed technical framework for sustainable AI-web ecosystem
- Published 3,000+ word research report/blog post

**Technical Highlights**:
- Built ethical scraper using Claude Agent SDK as research tool
- Robots.txt analyzer - scans sites and categorizes protections
- Token bucket rate limiting respecting Crawl-delay
- Data collection pipeline: 100+ sites analyzed
- Statistical analysis of protection patterns

**Resume Bullets**:
- *"Researched AI-generated traffic impact on content creators, analyzing 100+ major sites' protection strategies and publishing findings"*
- *"Proposed technical framework for sustainable AI-web ecosystem balancing training data access with creator attribution"*
- *"Built ethical web scraper using Claude Agent SDK to collect research data while respecting all site protections"*

**Interview Talking Points**:
- "I researched the tension between AI companies needing training data and content creators needing attribution - directly relevant to Anthropic/OpenAI's challenges"
- "My analysis shows 60%+ of major sites now block GPTBot/ClaudeBot, but protections are inconsistent and often ineffective"
- "I proposed a technical framework for sustainable relationships, similar to how SEO evolved"
- "This demonstrates Constitutional AI thinking - balancing competing interests rather than ignoring one side"
- "The scraper was my research tool, demonstrating how AI companies SHOULD interact with content"

---

### Project #2: RLHF Reward Model Trainer (Option A)
**Timeline**: Week 3-5  
**GitHub**: [repo link]

**Technical Highlights**:
- Trained reward model on Anthropic HH-RLHF dataset
- PyTorch + HuggingFace transformers
- Preference learning with Bradley-Terry model
- Evaluation metrics: accuracy vs human preferences
- Simplified scope: Reward modeling (not full PPO)

**Resume Bullet**: "Implemented RLHF reward model trainer using Anthropic's preference dataset, achieving X% agreement with human preferences"

**Interview Talking Points**:
- "I focused on reward modeling to understand preference learning deeply"
- "Used Anthropic's HH-RLHF dataset to stay relevant"
- "Implemented Bradley-Terry model for pairwise comparisons"
- "Could extend to full PPO loop but prioritized depth over breadth"

---

### Project #2: Alternative (Option B)
**Decision**: End of Week 3 based on progress and interests

**Options**:
- Transformer interpretability visualization tool
- Inference optimization benchmark (quantization, batching)
- Another Claude Agent SDK project (code analysis agent)

**Will spec once we decide**

---

## Practical Coding Strategy

### NOT Traditional LeetCode Grinding

**What We're Doing Differently**:
- 75-100 problems total (vs 200+)
- Focus on **practical patterns** not algorithm theory
- Real-world scenarios (log parsing, API design, data pipelines)
- Speed and correctness over Big O memorization
- Timed practice (45 min realistic)

### Problem Sources
1. **Real coding tasks** from past projects
2. **System implementation problems** (build a cache, implement rate limiter)
3. **Debugging scenarios** (find and fix bugs)
4. **API design problems** (design a REST endpoint)
5. **Data processing** (parse logs, transform data)
6. **Selected LeetCode Medium-Hard** (practical patterns only)

### Weekly Practice Routine
- **Daily**: 1-2 problems (45 min max)
- **Focus**: Speed and correct implementation
- **Tools**: Can look things up (matches Anthropic style)
- **Review**: Learn patterns, don't memorize solutions

---

## System Design Focus Areas

### Core ML Infrastructure Patterns
1. **Model Training Pipeline** (data → training → checkpoints)
2. **Model Serving Infrastructure** (inference, batching, caching)
3. **Feature Store** (data processing, feature engineering)
4. **RLHF Pipeline** (reward model, PPO, human feedback loop)
5. **Chat System with RAG** (conversation, context, retrieval)
6. **Distributed Training** (data parallelism, model parallelism)
7. **Real-time Inference** (latency optimization, scaling)

### System Design Framework
1. **Requirements** (functional, non-functional, scale)
2. **High-level design** (components, data flow)
3. **Deep dive** (bottlenecks, optimizations)
4. **Trade-offs** (consistency vs availability, latency vs cost)

**Reference**: `roadmap/05-system-design/ml-infrastructure.md`

---

## Behavioral Interview Strategy

### Core Themes for Both Companies
1. **Ownership & End-to-End Thinking** (OpenAI emphasis)
2. **Mission Alignment** (AI safety, impact)
3. **Speed & Execution** (move fast, ship)
4. **Technical Depth** (can go deep when needed)
5. **Collaboration** (cross-functional work)

### Story Bank (8-10 stories)
- 2-3 **ownership stories** (led project end-to-end)
- 2-3 **technical depth stories** (solved hard problem)
- 2-3 **collaboration stories** (worked across teams)
- 1-2 **failure stories** (what you learned)
- 1-2 **AI safety stories** (thought about implications)

### AI Safety Preparation
- Understand Constitutional AI (Anthropic)
- Understand RLHF and alignment (OpenAI)
- Have thoughtful opinions on AI safety
- Show you care about impact and responsibility

---

## Company-Specific Preparation

### Anthropic Focus
**Culture**: High-trust, low-politics, safety-first  
**Interview Style**: Progressive difficulty, can look things up  
**What They Value**: Independent work (blog posts, open source), practical ability

**Prep Priorities**:
1. Read Constitutional AI papers thoroughly
2. Understand Claude's architecture and capabilities
3. Prepare safety-focused discussion points
4. Showcase independent projects prominently
5. Practice explaining technical decisions clearly

**Resume Strategy**: Projects and independent work at TOP

---

### OpenAI Focus
**Culture**: High-intensity, impact-driven, ambitious  
**Interview Style**: Very hard but practical, ownership emphasis  
**What They Value**: End-to-end ownership, speed, large-scale systems

**Prep Priorities**:
1. Read GPT papers and understand architecture evolution
2. Study recent ChatGPT and API product updates
3. Prepare ownership and impact stories
4. Practice hard practical coding problems (timed)
5. Show you can move fast and ship

**Resume Strategy**: Impact metrics, scale, ownership

---

## Timeline: Application to Offer

### Week 5: Application Week
- **Monday-Tuesday**: Finalize resume, secure referrals
- **Wednesday-Thursday**: Submit applications
- **Friday**: Follow up with referrers

### Week 6: Phone Screens
- **Anthropic**: 20-30 days timeline → expect contact Week 6
- **OpenAI**: 20-30 days timeline → expect contact Week 6
- Continue prep, do mock interviews

### Week 7: Onsite/Virtual Onsites
- **Anthropic**: 4 coding rounds (progressive difficulty)
- **OpenAI**: Multiple rounds (coding, system design, behavioral)
- Maintain daily practice routine

### Week 8: Offers & Negotiation
- Receive offers
- Use dual offers for leverage
- Negotiate using compensation data
- Make decision

---

## Tracking & Accountability

### Weekly Reviews (Sunday)
- [ ] Review week's progress against plan
- [ ] Adjust next week's priorities
- [ ] Update `progress/weekly/week-XX.md`
- [ ] Update `memory/journey-log.md`

### Progress Files
- **Projects**: `projects/` directory with detailed docs
- **Coding**: `practice/coding/problems-log.md`
- **System Design**: `practice/system-designs/`
- **Behavioral**: `practice/behavioral/story-bank.md`
- **Applications**: `applications/`

### Key Metrics to Track
- Portfolio projects: completion percentage
- Practical problems: count and weak areas
- System designs: count and confidence level
- Mock interviews: feedback and scores
- Applications: status and next steps

---

## Adjustments & Flexibility

This plan should be adjusted based on:
- **Interview scheduling** (if Anthropic responds Week 5, accelerate prep)
- **Project complexity** (if RAG system takes longer, adjust timeline)
- **Weak areas** (spend more time where needed)
- **Recruiter feedback** (take their guidance seriously)
- **Life circumstances** (maintain sustainable pace)

**Golden Rule**: Focus on practical engineering demonstrations over algorithm grinding.

---

## Resources

### Code Practice
- Python practical problems (not Blind 75)
- System implementation exercises
- Real-world debugging scenarios
- Timed mock interviews

### System Design
- `roadmap/05-system-design/framework.md`
- `roadmap/05-system-design/ml-infrastructure.md`
- Real system design case studies

### ML Fundamentals
- `roadmap/02-technical-preparation/ml-fundamentals.md`
- Transformer papers
- RLHF papers (OpenAI, Anthropic)
- Constitutional AI (Anthropic)

### Company Research
- `roadmap/01-company-research/2026-hiring-intelligence.md`
- `roadmap/01-company-research/anthropic.md`
- `roadmap/01-company-research/openai.md`

---

## Success Indicators

You're on track if:
- ✅ Projects are deploying on schedule
- ✅ Can explain technical decisions clearly
- ✅ Coding speed improving (solve Medium in 30-45 min)
- ✅ System design confidence growing
- ✅ Mock interview feedback is positive
- ✅ Resume clearly shows practical engineering
- ✅ GitHub looks professional and active
- ✅ Can discuss AI safety thoughtfully
- ✅ Applications submitted Week 5
- ✅ Interviews scheduled Week 6-7

---

## Final Notes

This plan is optimized for **Anthropic and OpenAI's actual interview styles**, not theoretical algorithm preparation. 

**The difference**: 
- Traditional prep: Grind 200+ LeetCode problems
- This plan: Build 3 deployed projects, solve 75-100 practical problems, master ML system design

**Why it works**: Both companies explicitly value **practical engineering over theoretical algorithms**. Show them real systems you've built, not algorithm patterns you've memorized.

**Compensation target**: With dual offers from Anthropic ($550K-$759K) and OpenAI ($655K-$1.43M), your $550K-$760K target is highly achievable.

Let's build. 🚀
