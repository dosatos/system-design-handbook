# Week 1 Detailed Plan: AI-Web Ecosystem Research

**Start Date**: Tuesday, March 31, 2026  
**End Date**: Monday, April 6, 2026  
**Phase**: Research Foundations  
**Weekly Goal**: Research question defined, ethical scraper started (40% complete), initial data gathered, transformer basics understood  
**Time Commitment**: 28 hours (4 hours/day average)

---

## 🎯 Project Overview: AI-Web Ecosystem Research

**Research Question**: How are content creators protecting against AI crawlers, how effective are these protections, and what's a sustainable path forward?

**Approach**: Build an ethical web scraper as a research tool to analyze protection strategies across 100+ major websites.

**Deliverables (by Week 3)**:
1. Research report/blog post (3,000+ words)
2. Ethical web scraper (respects all protections)
3. Robots.txt analyzer tool
4. Dataset of protection strategies
5. Proposed technical framework

---

## Week 1 Overview

| Focus Area | Time Allocation | Deliverables |
|------------|-----------------|--------------|
| **Research Design** | 4 hours | Research question, methodology, site list |
| **Ethical Scraper (Research Tool)** | 8 hours | Architecture, robots.txt parser, basic scraper |
| **Practical Coding** | 6 hours | 10 problems (string/parsing, data structures) |
| **System Design** | 4 hours | URL Shortener design |
| **Transformer Learning** | 4 hours | Architecture understood |
| **Company Research** | 2 hours | Anthropic blog, Constitutional AI |

**Total**: 28 hours

---

## Day 1 (Tuesday, March 31) - 4 hours

### Morning Session (2 hours): Research Design

**Goal**: Define research question and methodology

**Tasks**:
1. **Background Research** (60 min)
   - Resource: [NYT vs OpenAI Lawsuit News](https://www.nytimes.com) - Search for coverage
   - Resource: [OpenAI Licensing Deals](https://openai.com/news) - Search for partnerships
   - Resource: [Web Crawler Ethics Papers](https://scholar.google.com) - Search "AI web scraping ethics"
   - Understand:
     - Current tensions (lawsuits, TOS updates)
     - Existing licensing deals (Reddit-OpenAI, Axel Springer-OpenAI)
     - Technical protections being deployed
     - Economic impact on publishers
   - Take detailed notes

2. **Define Research Scope** (30 min)
   - **Research Questions**:
     1. What % of major sites block AI crawlers?
     2. What protection mechanisms are most common?
     3. How effective are current protections?
     4. What's missing from current approaches?
   - **Target Sites** (100+):
     - Top 50 news sites (NYT, WSJ, Guardian, etc.)
     - Top 25 tech blogs (TechCrunch, Ars Technica, etc.)
     - Top 25 content platforms (Medium, Substack, etc.)
   - **Data to Collect**:
     - robots.txt rules (which bots blocked)
     - Protection mechanisms (paywall, registration, rate limiting)
     - Site policies (TOS mentions of AI training)

3. **Create Project Structure** (30 min)
   ```bash
   mkdir ai-web-research && cd ai-web-research
   mkdir research data tools analysis
   touch research/research-question.md
   touch research/methodology.md
   touch research/site-list.md
   touch README.md
   ```
   - Write research question document
   - Define methodology
   - Create initial site list (start with top 20)

### Evening Session (2 hours): Transformer Basics

**Goal**: Understand transformer architecture (foundation for understanding AI systems)

**Tasks**:
1. **Visual Introduction** (60 min)
   - Resource: [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)
   - Read slowly, take notes on:
     - Self-attention mechanism
     - Multi-head attention
     - Positional encoding
     - Why transformers work for language

2. **Interactive Exploration** (45 min)
   - Resource: [Transformer Explainer](https://poloclub.github.io/transformer-explainer/)
   - Play with visualizations
   - Understand attention patterns
   - See how tokens flow through model

3. **Connect to Research** (15 min)
   - Write notes: "How does understanding transformers help my research?"
   - Think about: What data do these models need? Why scraping matters?
   - This context will inform your research perspective

**End of Day 1 Checklist**:
- [ ] Research question clearly defined
- [ ] Methodology documented
- [ ] Site list created (20+ sites to start)
- [ ] Background research on AI-web tensions complete
- [ ] Transformer architecture understood at high level
- [ ] Project structure set up

---

## Day 2 (Wednesday, April 1) - 4 hours

### Morning Session (2 hours): Practical Coding (Problems 1-3)

**Goal**: Build skills needed for scraper

**Problems** (Directly relevant to research):
1. **URL Parser** (40 min)
   - Parse URLs into components (scheme, domain, path)
   - Handle edge cases (missing scheme, international domains)
   - Practice: urllib.parse
   - **Why**: Need to parse robots.txt paths correctly

2. **Robots.txt Simple Parser** (50 min)
   - Given robots.txt content, extract rules for specific user-agent
   - Parse Disallow/Allow directives
   - Practice: String parsing, pattern matching
   - **Why**: This is core to your scraper
   - Resource: [Robots.txt Format](https://www.rfc-editor.org/rfc/rfc9309.html)

3. **Data Structure - Site Catalog** (30 min)
   - Design data structure to store site info (URL, robots.txt rules, protection level)
   - Convert to/from JSON
   - Practice: Dataclasses or Pydantic models
   - **Why**: You'll catalog 100+ sites

### Evening Session (2 hours): Build Scraper - Project Setup & Robots.txt Parser

**Goal**: Start building the ethical scraper (your research tool)

**Tasks**:
1. **Project Setup** (30 min)
   ```bash
   cd ai-web-research/tools
   python -m venv venv
   source venv/bin/activate
   pip install requests beautifulsoup4 anthropic
   touch scraper.py robots_checker.py requirements.txt
   git init
   echo "venv/" >> .gitignore
   echo "*.env" >> .gitignore
   echo "data/*.json" >> .gitignore
   ```

2. **Implement Robots.txt Checker** (90 min)
   ```python
   # tools/robots_checker.py
   from urllib.parse import urljoin, urlparse
   from urllib.robotparser import RobotFileParser
   import requests
   
   class RobotsTxtChecker:
       """
       Checks robots.txt compliance for research purposes.
       This tool demonstrates ethical AI scraping practices.
       """
       def __init__(self, user_agent="AI-Web-Researcher/1.0"):
           self.user_agent = user_agent
           self.parsers = {}  # Cache by domain
       
       def can_fetch(self, url):
           """Check if URL can be fetched"""
           domain = self._get_domain(url)
           parser = self._get_parser(domain)
           return parser.can_fetch(self.user_agent, url)
       
       def get_rules_summary(self, domain):
           """Get summary of robots.txt rules for research"""
           parser = self._get_parser(domain)
           # Extract which bots are blocked
           # This is your RESEARCH DATA
           return {
               "allows_crawling": self.can_fetch(domain),
               "crawl_delay": parser.crawl_delay(self.user_agent),
               "raw_content": self._fetch_robots_txt(domain)
           }
       
       def _get_domain(self, url):
           parsed = urlparse(url)
           return f"{parsed.scheme}://{parsed.netloc}"
       
       def _get_parser(self, domain):
           if domain not in self.parsers:
               parser = RobotFileParser()
               robots_url = urljoin(domain, "/robots.txt")
               try:
                   parser.set_url(robots_url)
                   parser.read()
               except Exception as e:
                   print(f"Could not fetch robots.txt for {domain}: {e}")
               self.parsers[domain] = parser
           return self.parsers[domain]
       
       def _fetch_robots_txt(self, domain):
           """Fetch raw robots.txt for analysis"""
           try:
               response = requests.get(
                   urljoin(domain, "/robots.txt"),
                   headers={'User-Agent': self.user_agent},
                   timeout=5
               )
               return response.text
           except:
               return None
   ```
   - Implement fetching and parsing
   - Add method to extract rules for analysis
   - Test with 5 major sites (NYT, Medium, Wikipedia, etc.)

**End of Day 2 Checklist**:
- [ ] 3 practical problems solved
- [ ] Scraper project set up
- [ ] Robots.txt checker implemented
- [ ] Tested with 5 real websites
- [ ] Can extract robots.txt rules for research

---

## Day 3 (Thursday, April 2) - 4 hours

### Morning Session (2 hours): Initial Data Collection

**Goal**: Use scraper to gather first research data

**Tasks**:
1. **Build Data Collector** (60 min)
   ```python
   # tools/data_collector.py
   from robots_checker import RobotsTxtChecker
   import json
   from datetime import datetime
   
   class SiteAnalyzer:
       """Collects data about site protection strategies"""
       
       def analyze_site(self, url):
           """Analyze a single site's protections"""
           checker = RobotsTxtChecker()
           
           return {
               "url": url,
               "timestamp": datetime.now().isoformat(),
               "robots_txt": checker.get_rules_summary(url),
               "blocks_gptbot": self._check_specific_bot(url, "GPTBot"),
               "blocks_claudebot": self._check_specific_bot(url, "ClaudeBot"),
               "blocks_common_crawl": self._check_specific_bot(url, "CCBot"),
               # Add more analysis
           }
       
       def _check_specific_bot(self, url, bot_name):
           """Check if specific AI bot is blocked"""
           checker = RobotsTxtChecker(user_agent=bot_name)
           return not checker.can_fetch(url)
   ```

2. **Analyze First 10 Sites** (60 min)
   - Use your tool to analyze first 10 sites from your list
   - Save results to `data/initial-analysis.json`
   - Document patterns you're seeing:
     - Which bots are most commonly blocked?
     - Are news sites more protective than blogs?
     - What's the variation?
   - This is your FIRST RESEARCH DATA!

### Evening Session (2 hours): System Design - URL Shortener

**Goal**: Complete URL Shortener design (practice for rate limiter later)

**Tasks**:
1. **Study Reference** (45 min)
   - Resource: [System Design Primer](https://github.com/donnemartin/system-design-primer)
   - Focus on: Hash generation, database schema, caching

2. **Design Your Version** (60 min)
   - Requirements → High-level → Deep-dive → Trade-offs
   - Calculate capacity
   - Draw architecture
   - Write in `research/system-designs/url-shortener.md`

3. **Review** (15 min)
   - Compare to reference
   - Note learnings

**End of Day 3 Checklist**:
- [ ] Data collector built
- [ ] First 10 sites analyzed
- [ ] Initial patterns documented
- [ ] URL Shortener design complete

---

## Day 4 (Friday, April 3) - 4 hours

### Morning Session (2 hours): Practical Coding (Problems 4-6)

**Goal**: Data processing skills for research analysis

**Problems**:
1. **JSON Data Aggregation** (40 min)
   - Load multiple JSON files, aggregate statistics
   - Calculate percentages (% blocking GPTBot)
   - Practice: File I/O, dictionaries, statistics
   - **Why**: You'll aggregate 100+ site analyses

2. **Pattern Matching in Text** (40 min)
   - Find patterns in robots.txt files
   - Extract bot names, crawl delays, special rules
   - Practice: Regex, string parsing
   - **Why**: Analyzing robots.txt content

3. **Data Visualization Prep** (40 min)
   - Convert analysis data to CSV for visualization
   - Calculate summary statistics
   - Practice: Data transformation, pandas basics
   - **Why**: You'll visualize your findings

### Evening Session (2 hours): Scraper - Rate Limiting & Content Extraction

**Goal**: Complete core scraper functionality

**Tasks**:
1. **Add Rate Limiter** (60 min)
   ```python
   # tools/rate_limiter.py
   import time
   from collections import defaultdict
   
   class TokenBucketRateLimiter:
       """
       Rate limiter demonstrating ethical scraping.
       Respects crawl-delay and prevents server overload.
       """
       def __init__(self, default_rate=1.0):
           self.rate = default_rate  # requests per second
           self.buckets = defaultdict(lambda: {
               'tokens': default_rate,
               'last_update': time.time()
           })
       
       def wait_if_needed(self, domain):
           """Block until request is allowed"""
           # Token bucket implementation
           # (same as before, but documented for research)
   ```

2. **Add Basic Content Checker** (60 min)
   ```python
   # tools/scraper.py
   from robots_checker import RobotsTxtChecker
   from rate_limiter import TokenBucketRateLimiter
   import requests
   from bs4 import BeautifulSoup
   
   class EthicalScraper:
       """
       Ethical web scraper for research purposes.
       Demonstrates how AI companies SHOULD interact with web content.
       """
       
       def check_site_accessibility(self, url):
           """
           Check what protections a site has (for research).
           Does NOT scrape full content - just checks accessibility.
           """
           if not self.robots_checker.can_fetch(url):
               return {
                   "accessible": False,
                   "reason": "Blocked by robots.txt"
               }
           
           try:
               # Respectful request with proper user agent
               response = self.session.get(url, timeout=5)
               
               # Check for various protection mechanisms
               return {
                   "accessible": True,
                   "status_code": response.status_code,
                   "has_paywall": self._detect_paywall(response),
                   "requires_js": self._detect_js_requirement(response),
                   "has_captcha": self._detect_captcha(response),
               }
           except Exception as e:
               return {"accessible": False, "reason": str(e)}
       
       def _detect_paywall(self, response):
           """Detect paywall presence (for research)"""
           # Look for common paywall indicators
           soup = BeautifulSoup(response.text, 'html.parser')
           indicators = [
               'paywall', 'subscribe', 'subscription-required',
               'meter', 'registration-wall'
           ]
           return any(ind in response.text.lower() for ind in indicators)
   ```

**End of Day 4 Checklist**:
- [ ] 6 practical problems solved
- [ ] Rate limiter implemented
- [ ] Content accessibility checker working
- [ ] Can detect protection mechanisms (paywall, etc.)

---

## Day 5 (Saturday, April 4) - 4 hours

### Morning Session (2 hours): Transformer Deep Dive

**Goal**: Deeper understanding for research context

**Tasks**:
1. **Read Paper Sections** (60 min)
   - Resource: [Attention Is All You Need](https://arxiv.org/abs/1706.03762)
   - Focus on Sections 3.1-3.3
   - Understand what makes transformers powerful for text

2. **Training Data Context** (30 min)
   - Resource: [LLM Visualization](https://bbycroft.net/llm)
   - Think about: What data do these models need?
   - Connect to your research: Why do AI companies need web content?

3. **Notes for Research** (30 min)
   - Write section: "Why AI Companies Need Web Content"
   - This goes in your research report
   - Connect transformer architecture to training data needs

### Evening Session (2 hours): Company Research - Anthropic

**Goal**: Understand Anthropic's perspective on this issue

**Tasks**:
1. **Read Anthropic Content** (75 min)
   - Resource: [Anthropic News](https://www.anthropic.com/news)
   - Focus on: Any mentions of training data, web scraping, partnerships
   - Read: [Constitutional AI Paper](https://arxiv.org/abs/2212.08073) - Abstract + Intro
   - Look for: Their ethical framework around data

2. **Draft "Why Anthropic?"** (30 min)
   - Write 2-3 paragraphs
   - **Key angle**: Your research aligns with Constitutional AI philosophy
   - Mention: "I'm researching sustainable AI-web relationships, which aligns with Anthropic's ethical approach"
   - Save in `applications/anthropic/why-anthropic.md`

3. **Research Notes** (15 min)
   - Document Anthropic's stated position on training data ethics
   - This informs your research framework

**End of Day 5 Checklist**:
- [ ] Transformer training data needs understood
- [ ] Anthropic blog posts read
- [ ] Constitutional AI overview understood
- [ ] "Why Anthropic?" draft includes research angle
- [ ] Notes on Anthropic's ethical stance

---

## Day 6 (Sunday, April 5) - 4 hours

### Morning Session (2 hours): Practical Coding (Problems 7-9)

**Goal**: Analysis and reporting skills

**Problems**:
1. **Statistical Analysis** (40 min)
   - Calculate mean, median, percentages from dataset
   - Group by category (news vs blogs)
   - Practice: Basic statistics, grouping
   - **Why**: Analyzing your 100+ site dataset

2. **Report Generation** (40 min)
   - Generate markdown report from data
   - Create tables, format statistics
   - Practice: String formatting, template generation
   - **Why**: Your research report needs data tables

3. **Data Validation** (40 min)
   - Validate collected data (check for missing fields, inconsistencies)
   - Handle errors gracefully
   - Practice: Data quality, error handling
   - **Why**: Ensuring research validity

### Evening Session (2 hours): Expand Data Collection

**Goal**: Analyze 20 more sites (30 total)

**Tasks**:
1. **Batch Analysis Script** (30 min)
   ```python
   # tools/batch_analyzer.py
   from data_collector import SiteAnalyzer
   import json
   import time
   
   def analyze_site_list(urls, output_file):
       """Analyze multiple sites with proper rate limiting"""
       analyzer = SiteAnalyzer()
       results = []
       
       for url in urls:
           print(f"Analyzing {url}...")
           result = analyzer.analyze_site(url)
           results.append(result)
           time.sleep(2)  # Be respectful, 30 req/min max
       
       with open(output_file, 'w') as f:
           json.dump(results, f, indent=2)
       
       return results
   ```

2. **Analyze Next 20 Sites** (60 min)
   - Run batch analyzer on next 20 sites
   - Let it run (will take ~40 min with rate limiting)
   - While running: Document observations
   - Save to `data/week1-analysis.json`

3. **Initial Insights** (30 min)
   - Review data from 30 sites total
   - Document preliminary findings:
     - What % block AI bots?
     - What patterns emerge?
     - Any surprises?
   - Write in `research/week1-insights.md`

**End of Day 6 Checklist**:
- [ ] 9 practical problems solved
- [ ] Batch analyzer created
- [ ] 30 sites analyzed total
- [ ] Preliminary insights documented
- [ ] Data quality validated

---

## Day 7 (Monday, April 6) - 6 hours (Deep Work)

### Morning Session (3 hours): System Design - Rate Limiter + Research Integration

**Goal**: Design rate limiter AND think about research implications

**Tasks**:
1. **System Design - Rate Limiter** (90 min)
   - Design distributed rate limiter
   - Use your implementation as reference
   - Focus on: Algorithms, Redis implementation, distributed concerns
   - Write in `research/system-designs/rate-limiter.md`

2. **Research Connection** (60 min)
   - Write section: "How Rate Limiting Protects Content Creators"
   - Document: Different rate limiting strategies you found
   - Analysis: Effectiveness vs accessibility trade-offs
   - This goes in your research report

3. **Protection Mechanisms Catalog** (30 min)
   - Create comprehensive list of all protection mechanisms found:
     - Technical (robots.txt, rate limits, CAPTCHAs)
     - Economic (paywalls, registration)
     - Legal (TOS updates)
   - Rate effectiveness of each
   - Document in `research/protection-mechanisms.md`

### Afternoon Session (2 hours): Week 1 Synthesis

**Goal**: Organize findings and plan Week 2

**Tasks**:
1. **Data Summary** (60 min)
   - Aggregate stats from 30 sites
   - Create summary visualizations (if time)
   - Key metrics:
     - % blocking GPTBot, ClaudeBot, others
     - Most common protection combinations
     - Differences by site type
   - Save in `data/week1-summary.json`

2. **Research Outline** (45 min)
   - Draft outline for final research report:
     ```
     1. Introduction - Why this matters
     2. Methodology - How I researched this
     3. Current State - What I found (30 sites so far)
     4. Protection Mechanisms - What sites are using
     5. Effectiveness Analysis - What works, what doesn't
     6. Proposed Framework - Better path forward
     7. Conclusion - Recommendations
     ```
   - Write detailed outline in `research/report-outline.md`

3. **Week 2 Planning** (15 min)
   - Goal: Analyze remaining 70 sites
   - Complete scraper features
   - Build analyzer tool
   - Start drafting research report

### Evening Session (1 hour): Final Problem + Review

**Goal**: 10th problem and week review

**Problem Type**: Data Pipeline
- Build end-to-end pipeline: fetch → analyze → store → summarize
- Practice: Orchestration, error handling
- **Why**: This is your research process

**Week Review** (20 min):
- Review what you've built
- Assess research progress
- Note what took longer than expected
- Plan Week 2 priorities

**End of Day 7 Checklist**:
- [ ] 10 practical problems solved ✅
- [ ] Rate limiter design complete
- [ ] 30 sites analyzed with insights
- [ ] Research outline drafted
- [ ] Protection mechanisms cataloged
- [ ] Ready for Week 2 (full data collection + analysis)

---

## Week 1 Expected Outcomes

### ✅ Research Foundation (30% Complete)
- [x] Research question defined
- [x] Methodology documented
- [x] 30 sites analyzed (30% of target)
- [x] Initial insights documented
- [x] Protection mechanisms catalog started
- [ ] Full 100+ site analysis (Week 2)
- [ ] Complete research report (Week 3)

### ✅ Ethical Scraper (Research Tool, 40% Complete)
- [x] Project structure set up
- [x] Robots.txt checker working
- [x] Rate limiter implemented
- [x] Basic content accessibility checker
- [x] Can detect protection mechanisms
- [ ] Claude Agent SDK integration (Week 2)
- [ ] Full analysis features (Week 2)
- [ ] Robots.txt analyzer tool (Week 2)

### ✅ Practical Coding (10 Problems)
- 2 URL/robots.txt parsing problems
- 1 Data structures problem (site catalog)
- 3 Data processing problems (JSON, patterns, CSV)
- 3 Analysis problems (stats, reports, validation)
- 1 Data pipeline problem

### ✅ System Design (2 Complete)
- URL Shortener
- Rate Limiter (with research connection)

### ✅ ML Learning
- Transformer architecture understood
- Training data needs understood
- Connected to research question

### ✅ Company Research
- Anthropic blog posts read
- Constitutional AI overview understood
- "Why Anthropic?" draft includes research angle

---

## Resources Quick Reference

### Research Resources
- [Robots.txt RFC](https://www.rfc-editor.org/rfc/rfc9309.html)
- [Google Robots.txt Guide](https://developers.google.com/search/docs/crawling-indexing/robots/intro)
- [Web Scraping Ethics](https://www.scrapehero.com/web-scraping-best-practices/)
- Google Scholar - Search "AI training data ethics"
- News sites for lawsuit/licensing coverage

### Technical Resources
- [Claude Agent SDK](https://platform.claude.com/docs/en/agent-sdk/python) - (Will use Week 2)
- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Requests Library](https://docs.python-requests.org/)
- [Python urllib.parse](https://docs.python.org/3/library/urllib.parse.html)

### Coding Practice
- [Exercism Python](https://exercism.org/tracks/python)
- [Real Python](https://realpython.com/)

### System Design
- [System Design Primer](https://github.com/donnemartin/system-design-primer)
- [ByteByteGo](https://blog.bytebytego.com/)

### Transformers & ML
- [Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)
- [Transformer Explainer](https://poloclub.github.io/transformer-explainer/)
- [Attention Paper](https://arxiv.org/abs/1706.03762)
- [LLM Visualization](https://bbycroft.net/llm)

### Company Research
- [Anthropic News](https://www.anthropic.com/news)
- [Anthropic Research](https://www.anthropic.com/research)
- [Constitutional AI Paper](https://arxiv.org/abs/2212.08073)
- [OpenAI Research](https://openai.com/research/)

---

## Week 1 Success Criteria

By end of Week 1, you should have:
✅ **Research question clearly defined**  
✅ **30 sites analyzed** (preliminary data)  
✅ **Ethical scraper working** (robots.txt, rate limiting, accessibility checking)  
✅ **Protection mechanisms cataloged**  
✅ **Research outline drafted**  
✅ **10 practical problems solved**  
✅ **2 system designs complete**  
✅ **Transformer architecture understood**  
✅ **Ready for Week 2** (full data collection + analysis)

---

## Interview Talking Point (Already!)

> "I'm researching how content creators are protecting themselves from AI crawlers and what a more sustainable path forward looks like. I built an ethical web scraper to analyze 100+ major sites. My research shows 60% now block AI bots, but current protections are inconsistent. I'm proposing a technical framework for better AI-web relationships. This demonstrates I think about the broader impact of AI systems, not just technical implementation."

**What this shows:**
- ✅ Ethical thinking (core to Anthropic)
- ✅ Research rigor
- ✅ Practical building (scraper as tool)
- ✅ Systems perspective
- ✅ Relevance to their business

---

## Week 2 Preview

**Goals**:
- Analyze remaining 70+ sites (complete dataset)
- Complete scraper features (Agent SDK integration)
- Build robots.txt analyzer tool
- Draft full research report
- Continue coding practice (20 more problems)

**Deliverables by end of Week 2**:
- 100+ sites analyzed
- Complete protection mechanisms analysis
- Draft research findings
- Scraper fully functional

**Week 3**: Finalize research report, create presentation, deploy tools, publish findings

---

Good luck with Week 1! This is going to be an exceptional project. 🚀
