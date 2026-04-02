# Week 1 Detailed Plan: Foundations (Web Scraping Agent)

**Start Date**: Tuesday, March 31, 2026  
**End Date**: Monday, April 6, 2026  
**Phase**: Build Foundations  
**Weekly Goal**: Web scraping agent started (40% complete), 10 practical problems solved, transformer basics understood  
**Time Commitment**: 28 hours (4 hours/day average)

---

## Week 1 Overview

| Focus Area | Time Allocation | Deliverables |
|------------|-----------------|--------------|
| Web Scraping Agent Project #1 | 12 hours | Architecture designed, robots.txt parser working, rate limiting implemented |
| Practical Coding | 6 hours | 10 problems solved (string/parsing, dict/list operations) |
| System Design | 4 hours | URL Shortener design completed |
| Transformer Learning | 4 hours | Architecture understood, can explain attention |
| Company Research | 2 hours | Anthropic blog posts read, "Why Anthropic?" drafted |

**Total**: 28 hours

---

## Day 1 (Tuesday, March 31) - 4 hours

### Morning Session (2 hours): Web Scraping Agent Kickoff

**Goal**: Understand ethical web scraping and design architecture

**Tasks**:
1. **Study Robots.txt Protocol** (45 min)
   - Resource: [Robots.txt Specification](https://www.rfc-editor.org/rfc/rfc9309.html)
   - Resource: [Google's Robots.txt Guide](https://developers.google.com/search/docs/crawling-indexing/robots/intro)
   - Learn:
     - User-agent directives
     - Allow/Disallow rules
     - Crawl-delay directive
     - Sitemap location
     - Wildcard patterns
   - Take notes on edge cases

2. **Study Ethical Scraping Practices** (30 min)
   - Resource: [Web Scraping Best Practices](https://www.scrapehero.com/web-scraping-best-practices/)
   - Understand:
     - Rate limiting strategies
     - Backoff algorithms
     - User-agent identification
     - Respect for bandwidth
   - Note ethical considerations

3. **Design Agent Architecture** (45 min)
   - Draw architecture diagram:
     - Input: List of URLs
     - Components: Robots.txt checker → Rate limiter → Scraper → Parser → Storage
     - Agent orchestration with Claude Agent SDK
   - Define data structures:
     - RobotsTxtRules class
     - ScrapeRequest/Response
     - RateLimiter state
   - Write architecture doc in project README

### Evening Session (2 hours): Transformer Basics

**Goal**: Understand transformer architecture fundamentals

**Tasks**:
1. **Watch Visual Introduction** (60 min)
   - Resource: [The Illustrated Transformer](https://jalammar.github.io/illustrated-transformer/)
   - Read entire article slowly, take notes on:
     - Self-attention mechanism
     - Multi-head attention
     - Positional encoding
     - Encoder-decoder structure

2. **Interactive Exploration** (45 min)
   - Resource: [Transformer Explainer](https://poloclub.github.io/transformer-explainer/)
   - Play with interactive visualizations
   - Focus on understanding attention patterns
     - Try different input examples

3. **Create Study Notes** (15 min)
   - Write down: "What is a transformer in 3 sentences?"
   - Draw basic transformer architecture from memory
   - Note questions for deeper research later

**End of Day 1 Checklist**:
- [ ] Robots.txt protocol understood
- [ ] Web scraping agent architecture designed
- [ ] README with architecture diagram created
- [ ] Transformer architecture understood at high level
- [ ] Can explain what attention mechanism does

---

## Day 2 (Wednesday, April 1) - 4 hours

### Morning Session (2 hours): Practical Coding (Problems 1-3)

**Goal**: Solve 3 practical string/parsing problems

**Problem Sources**:
- [Exercism Python Track](https://exercism.org/tracks/python) - Filter for "easy" difficulty
- [Real Python Tutorials](https://realpython.com/) - Look for practical exercises

**Suggested Problems**:
1. **Log File Parser** (30 min)
   - Parse log files and extract timestamps, error levels, messages
   - Practice: String splitting, regex, dictionaries
   - This is DIRECTLY relevant to web scraping (parsing HTML/text)

2. **URL Parser** (45 min)
   - Parse URLs into components (scheme, domain, path, query params)
   - Practice: String manipulation, urllib.parse
   - Directly relevant to scraping project
   - Resource: [urllib.parse docs](https://docs.python.org/3/library/urllib.parse.html)

3. **Text Extraction** (45 min)
   - Extract structured data from semi-structured text
   - Practice: Regex, string methods, pattern matching
   - Relevant to HTML parsing

**Coding Practice Protocol**:
- Set 45-min timer per problem
- Can look things up (matches Anthropic style)
- Focus on clean, working code
- Write tests for edge cases
- Log problems in `practice/coding/problems-log.md`

### Evening Session (2 hours): Scraper - Project Setup & Robots.txt Parser

**Goal**: Set up project and implement robots.txt parser

**Tasks**:
1. **Project Setup** (30 min)
   ```bash
   mkdir ethical-web-scraper && cd ethical-web-scraper
   python -m venv venv
   source venv/bin/activate
   pip install requests beautifulsoup4 anthropic
   git init
   echo "venv/" >> .gitignore
   echo "*.env" >> .gitignore
   touch README.md scraper.py robots_parser.py rate_limiter.py
   ```
   - Create project structure
   - Initialize git repo
   - Set up basic files

2. **Implement Robots.txt Parser** (90 min)
   ```python
   # robots_parser.py
   import requests
   from urllib.parse import urljoin, urlparse
   from urllib.robotparser import RobotFileParser
   
   class RobotsTxtChecker:
       def __init__(self, user_agent="EthicalBot/1.0"):
           self.user_agent = user_agent
           self.parsers = {}  # Cache parsers by domain
       
       def can_fetch(self, url):
           """Check if URL can be fetched according to robots.txt"""
           domain = self._get_domain(url)
           parser = self._get_parser(domain)
           return parser.can_fetch(self.user_agent, url)
       
       def get_crawl_delay(self, url):
           """Get crawl delay for domain"""
           domain = self._get_domain(url)
           parser = self._get_parser(domain)
           return parser.crawl_delay(self.user_agent)
       
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
                   # If can't fetch, allow by default but be conservative
               self.parsers[domain] = parser
           return self.parsers[domain]
   ```
   - Implement robots.txt fetching
   - Parse and cache rules
   - Handle missing/malformed robots.txt
   - Test with real websites (example.com, wikipedia.org)

**End of Day 2 Checklist**:
- [ ] 3 practical problems solved and logged
- [ ] Project structure set up
- [ ] Robots.txt parser implemented
- [ ] Parser tested with real websites
- [ ] Can check if URL is allowed to be scraped

---

## Day 3 (Thursday, April 2) - 4 hours

### Morning Session (2 hours): Scraper - Rate Limiter Implementation

**Goal**: Implement token bucket rate limiter

**Tasks**:
1. **Study Rate Limiting Algorithms** (30 min)
   - Resource: [Rate Limiting Patterns](https://github.com/donnemartin/system-design-primer#rate-limiter)
   - Understand:
     - Token bucket algorithm
     - Leaky bucket
     - Fixed vs sliding window
   - Choose: Token bucket (flexible, allows bursts)

2. **Implement Rate Limiter** (90 min)
   ```python
   # rate_limiter.py
   import time
   from collections import defaultdict
   from threading import Lock
   
   class TokenBucketRateLimiter:
       def __init__(self, requests_per_second=1.0):
           self.rate = requests_per_second
           self.buckets = defaultdict(lambda: {
               'tokens': requests_per_second,
               'last_update': time.time()
           })
           self.lock = Lock()
       
       def wait_if_needed(self, domain):
           """Block until we can make a request to domain"""
           with self.lock:
               bucket = self.buckets[domain]
               now = time.time()
               
               # Refill tokens based on time passed
               time_passed = now - bucket['last_update']
               bucket['tokens'] = min(
                   self.rate,
                   bucket['tokens'] + time_passed * self.rate
               )
               bucket['last_update'] = now
               
               # Wait if no tokens available
               if bucket['tokens'] < 1.0:
                   wait_time = (1.0 - bucket['tokens']) / self.rate
                   time.sleep(wait_time)
                   bucket['tokens'] = 0
               else:
                   bucket['tokens'] -= 1.0
       
       def set_crawl_delay(self, domain, delay_seconds):
           """Set custom rate for domain (from robots.txt)"""
           if delay_seconds:
               self.buckets[domain]['rate'] = 1.0 / delay_seconds
   ```
   - Implement token bucket algorithm
   - Per-domain rate limiting
   - Respect Crawl-delay from robots.txt
   - Test with multiple domains

**Evening Session (2 hours): System Design - URL Shortener

**Goal**: Complete URL Shortener system design

**Tasks**:
1. **Study Reference Design** (45 min)
   - Resource: [System Design Primer - URL Shortener](https://github.com/donnemartin/system-design-primer)
   - Resource: [URL Shortener on SystemDesignSchool](https://systemdesignschool.io/problems/url-shortener)
   - Understand:
     - Hash generation strategies (Base62, MD5 + collision handling)
     - Database schema (URL mapping, analytics)
     - Caching layer (Redis for hot URLs)
     - Scalability considerations

2. **Design Your Own Version** (60 min)
   - Use framework: Requirements → High-level → Deep-dive → Trade-offs
   - Draw architecture diagram
   - Calculate capacity estimates:
     - 100M URLs/month = ~40 writes/sec
     - 10:1 read:write ratio = ~400 reads/sec
     - 500 bytes per URL = 50GB/year
   - Identify bottlenecks
   - Write design in `practice/system-designs/url-shortener.md`

3. **Review and Critique** (15 min)
   - Compare your design to reference solutions
   - Note what you missed
   - Understand why certain choices were made

**End of Day 3 Checklist**:
- [ ] Rate limiter implemented with token bucket
- [ ] Per-domain rate limiting working
- [ ] Crawl-delay integration complete
- [ ] URL Shortener design completed and documented

---

## Day 4 (Friday, April 3) - 4 hours

### Morning Session (2 hours): Practical Coding (Problems 4-6)

**Goal**: Solve 3 dictionary/hash map problems

**Problem Types**:
1. **Caching Implementation** (40 min)
   - Build LRU cache from scratch
   - Practice: OrderedDict or custom implementation
   - **Resource**: [Exercism - Python Track](https://exercism.org/tracks/python)
   - Relevant to rate limiter caching

2. **Frequency Counter** (40 min)
   - Count word/character frequencies in large text
   - Practice: Counter, defaultdict, optimization
   - Real-world use: Analyzing scraped content

3. **Domain Grouping** (40 min)
   - Group URLs by domain, count requests per domain
   - Practice: Hash map patterns, urllib.parse
   - Directly relevant to scraper (per-domain logic)

### Evening Session (2 hours): Scraper - Content Extraction & Error Handling

**Goal**: Implement HTML parsing and robust error handling

**Tasks**:
1. **Implement Basic Scraper** (60 min)
   ```python
   # scraper.py
   import requests
   from bs4 import BeautifulSoup
   from urllib.parse import urlparse
   import time
   
   class EthicalScraper:
       def __init__(self, user_agent="EthicalBot/1.0", rate_limit=1.0):
           self.user_agent = user_agent
           self.robots_checker = RobotsTxtChecker(user_agent)
           self.rate_limiter = TokenBucketRateLimiter(rate_limit)
           self.session = requests.Session()
           self.session.headers.update({'User-Agent': user_agent})
       
       def scrape(self, url):
           """Scrape URL if allowed, respecting robots.txt and rate limits"""
           # Check robots.txt
           if not self.robots_checker.can_fetch(url):
               return {"error": "Disallowed by robots.txt", "url": url}
           
           # Respect rate limits
           domain = urlparse(url).netloc
           crawl_delay = self.robots_checker.get_crawl_delay(url)
           if crawl_delay:
               self.rate_limiter.set_crawl_delay(domain, crawl_delay)
           self.rate_limiter.wait_if_needed(domain)
           
           # Fetch and parse
           try:
               response = self.session.get(url, timeout=10)
               response.raise_for_status()
               
               soup = BeautifulSoup(response.text, 'html.parser')
               
               return {
                   "url": url,
                   "title": soup.title.string if soup.title else "",
                   "text": soup.get_text()[:1000],  # First 1000 chars
                   "links": [a.get('href') for a in soup.find_all('a', href=True)][:20],
                   "status_code": response.status_code
               }
           except Exception as e:
               return {"error": str(e), "url": url}
   ```
   - Implement scraping with BeautifulSoup
   - Extract title, text, links
   - Integrate robots.txt checker and rate limiter

2. **Add Exponential Backoff** (60 min)
   ```python
   def scrape_with_retry(self, url, max_retries=3):
       """Scrape with exponential backoff on failures"""
       for attempt in range(max_retries):
           result = self.scrape(url)
           if 'error' not in result:
               return result
           
           # Backoff on certain errors
           if attempt < max_retries - 1:
               # Exponential backoff: 1s, 2s, 4s
               wait_time = 2 ** attempt
               print(f"Retry {attempt + 1} after {wait_time}s for {url}")
               time.sleep(wait_time)
       
       return result  # Return last result (with error)
   ```
   - Add retry logic with exponential backoff
   - Handle HTTP errors (429, 503, timeouts)
   - Add jitter to avoid thundering herd

**End of Day 4 Checklist**:
- [ ] 6 practical problems solved total
- [ ] Basic scraper implemented
- [ ] Content extraction working (title, text, links)
- [ ] Exponential backoff on errors
- [ ] Integration: robots.txt + rate limiter + scraper

---

## Day 5 (Saturday, April 4) - 4 hours

### Morning Session (2 hours): Transformer Deep Dive

**Goal**: Understand attention mechanism in detail

**Tasks**:
1. **Read Original Paper** (60 min)
   - Resource: [Attention Is All You Need](https://arxiv.org/abs/1706.03762)
   - Focus on Sections 3.1-3.3 (attention mechanism)
   - **NOTE**: Paper is technical - skim math, focus on concepts
   - Don't try to understand everything in one read

2. **Watch 3D Visualization** (30 min)
   - Resource: [LLM Visualization](https://bbycroft.net/llm)
   - See tokens flow through transformer
   - Understand attention patterns visually
   - Play with different inputs

3. **Create Cheat Sheet** (30 min)
   - Write down formulas for:
     - Scaled dot-product attention
     - Multi-head attention
     - Positional encoding
   - Draw architecture diagram from memory
   - Note questions for later research

### Evening Session (2 hours): Company Research - Anthropic

**Goal**: Deep understanding of Anthropic's approach

**Tasks**:
1. **Read Blog Posts** (60 min)
   - Resource: [Anthropic News](https://www.anthropic.com/news)
   - Read at least 5 recent posts from 2024-2026
   - Focus on:
     - Claude releases and capabilities
     - Constitutional AI explanations
     - Company culture signals
     - Technical blog posts
   - Take notes on themes

2. **Read Constitutional AI Paper** (45 min)
   - Resource: [Constitutional AI Paper](https://arxiv.org/abs/2212.08073)
   - **ASSUMPTION**: Reading abstract and introduction is enough for Week 1
   - Understand high-level approach
   - Note how it differs from RLHF

3. **Draft "Why Anthropic?"** (15 min)
   - Write 2-3 paragraphs answering: "Why do you want to work at Anthropic?"
   - Include:
     - Specific technical interest (e.g., Constitutional AI, Claude Agent SDK)
     - Mission alignment (AI safety)
     - Cultural fit (careful thinking, independent work, ethical engineering)
     - Mention your scraping agent shows ethical thinking
   - Save in `applications/anthropic/why-anthropic.md`

**End of Day 5 Checklist**:
- [ ] Attention mechanism understood mathematically
- [ ] Transformer architecture can be explained to others
- [ ] 5+ Anthropic blog posts read
- [ ] Constitutional AI overview understood
- [ ] "Why Anthropic?" draft written (mentions ethical engineering)

---

## Day 6 (Sunday, April 5) - 4 hours

### Morning Session (2 hours): Practical Coding (Problems 7-9)

**Goal**: Solve 3 list operation problems

**Problem Types**:
1. **List Filtering/Transformation** (40 min)
   - Complex filtering with multiple conditions
   - Practice: List comprehensions, filter/map/reduce
   - Real-world: Filtering scraped URLs by domain/pattern

2. **URL Deduplication** (40 min)
   - Remove duplicate URLs (handle trailing slashes, query params)
   - Practice: Sets, URL normalization
   - Directly relevant to scraper

3. **Batch Processing** (40 min)
   - Process list of URLs in batches
   - Practice: Chunking, generators
   - Relevant to scraping multiple URLs efficiently

### Evening Session (2 hours): Scraper - Claude Agent SDK Integration

**Goal**: Integrate Claude Agent SDK for agent orchestration

**Tasks**:
1. **Study Agent SDK** (30 min)
   - Resource: [Claude Agent SDK Docs](https://platform.claude.com/docs/en/agent-sdk/python)
   - Resource: [Agent SDK GitHub Examples](https://github.com/anthropics/claude-agent-sdk-python)
   - Understand:
     - Creating custom tools
     - Tool definitions
     - Agent sessions
     - How agent decides when to use tools

2. **Create Scraping Tools** (90 min)
   ```python
   from claude_agent_sdk import tool, create_sdk_mcp_server
   
   # Initialize scraper
   scraper = EthicalScraper()
   
   @tool(
       name="scrape_url",
       description="Scrape a URL ethically, respecting robots.txt and rate limits",
       parameters={"url": {"type": "string", "description": "URL to scrape"}}
   )
   async def scrape_url_tool(args):
       url = args["url"]
       result = scraper.scrape_with_retry(url)
       
       if 'error' in result:
           return {
               "content": [{
                   "type": "text",
                   "text": f"Error scraping {url}: {result['error']}"
               }]
           }
       
       return {
           "content": [{
               "type": "text",
               "text": f"Title: {result['title']}\nText: {result['text'][:500]}..."
           }]
       }
   
   @tool(
       name="check_robots",
       description="Check if a URL is allowed by robots.txt",
       parameters={"url": {"type": "string"}}
   )
   async def check_robots_tool(args):
       allowed = scraper.robots_checker.can_fetch(args["url"])
       return {
           "content": [{
               "type": "text",
               "text": f"{'Allowed' if allowed else 'Disallowed'} by robots.txt"
           }]
       }
   ```
   - Create custom tools for scraping
   - Define tool schemas
   - Test with Agent SDK

**End of Day 6 Checklist**:
- [ ] 9 practical problems solved total
- [ ] Claude Agent SDK integrated
- [ ] Custom scraping tools created
- [ ] Agent can orchestrate scraping decisions

---

## Day 7 (Monday, April 6) - 6 hours (Deep Work)

### Morning Session (3 hours): System Design - Rate Limiter

**Goal**: Complete Rate Limiter design

**Tasks**:
1. **Study Rate Limiting Patterns** (60 min)
   - Resource: [System Design Primer](https://github.com/donnemartin/system-design-primer)
   - Resource: [ByteByteGo Blog](https://blog.bytebytego.com/) - Search for rate limiting articles
   - Understand algorithms:
     - Token bucket (your implementation!)
     - Leaky bucket
     - Fixed window
     - Sliding window
   - Compare trade-offs

2. **Design Distributed Rate Limiter** (90 min)
   - Requirements gathering (API gateway, distributed system)
   - Choose algorithm: Sliding window log (Redis)
   - Database/cache design (Redis keys, TTL)
   - Distributed considerations (race conditions, clock skew)
   - Draw architecture
   - Calculate capacity
   - Write design in `practice/system-designs/rate-limiter.md`

3. **Review & Critique** (30 min)
   - Compare to reference solutions
   - Note gaps in your understanding
   - Research anything unclear

### Afternoon Session (2 hours): Scraper - Testing & Documentation

**Goal**: Add tests and polish documentation

**Tasks**:
1. **Write Tests** (60 min)
   ```python
   # test_scraper.py
   import pytest
   from scraper import EthicalScraper
   
   def test_robots_txt_disallow():
       scraper = EthicalScraper()
       # Test with known disallowed URL
       result = scraper.scrape("https://example.com/admin")
       assert 'error' in result or result.get('status_code') != 200
   
   def test_rate_limiting():
       scraper = EthicalScraper(rate_limit=2.0)  # 2 req/sec
       # Scrape same domain twice quickly
       start = time.time()
       scraper.scrape("https://example.com/page1")
       scraper.scrape("https://example.com/page2")
       elapsed = time.time() - start
       assert elapsed >= 0.5  # Should be rate limited
   
   def test_content_extraction():
       scraper = EthicalScraper()
       result = scraper.scrape("https://example.com")
       assert 'title' in result
       assert 'text' in result
       assert 'links' in result
   ```
   - Test robots.txt compliance
   - Test rate limiting
   - Test content extraction
   - Test error handling

2. **Polish Documentation** (60 min)
   - Update README with:
     - Project overview
     - Architecture diagram
     - Features (robots.txt, rate limiting, backoff)
     - Usage examples
     - Ethical considerations
     - Installation instructions
   - Add code comments
   - Document API/tool interfaces

### Evening Session (1 hour): Practical Coding (Problem 10) + Review

**Goal**: Solve 1 final problem and review week

**Problem Type**: API Design or Error Handling
- Design robust error handling for HTTP requests
- Practice: Exception handling, retry logic, logging
- Real-world: Production API design

**Week Review** (20 min):
- [ ] Review what you built (scraper demo)
- [ ] Update progress tracking
- [ ] Note what took longer than expected
- [ ] Identify improvements for Week 2

**End of Day 7 Checklist**:
- [ ] 10 practical problems solved (Week 1 goal reached!)
- [ ] Rate Limiter design completed
- [ ] Tests written for scraper
- [ ] Documentation polished
- [ ] Ready to continue Week 2

---

## Week 1 Expected Outcomes

### ✅ Web Scraping Agent (40% Complete)
- [x] Project structure set up
- [x] Robots.txt parser working
- [x] Rate limiter implemented (token bucket)
- [x] Basic scraper with content extraction
- [x] Exponential backoff on errors
- [x] Claude Agent SDK integration
- [ ] CLI interface (Week 2)
- [ ] Batch processing (Week 2)
- [ ] Full deployment (Week 3)

### ✅ Practical Coding (10 Problems)
- 3 String/parsing problems (log parser, URL parser, text extraction)
- 3 Dict/hashmap problems (LRU cache, frequency counter, domain grouping)
- 3 List operation problems (filtering, deduplication, batching)
- 1 API design/error handling problem

### ✅ System Design (2 Complete)
- URL Shortener: Complete
- Rate Limiter: Complete (you implemented one!)

### ✅ ML Learning
- Transformer architecture understood
- Attention mechanism clear
- Can explain at high level

### ✅ Company Research
- Anthropic blog posts read
- Constitutional AI overview understood
- "Why Anthropic?" drafted (includes ethical engineering angle)

---

## Resources Quick Reference

### Web Scraping Agent
- [Claude Agent SDK Docs](https://platform.claude.com/docs/en/agent-sdk/python)
- [Agent SDK GitHub](https://github.com/anthropics/claude-agent-sdk-python)
- [Robots.txt RFC](https://www.rfc-editor.org/rfc/rfc9309.html)
- [Google Robots.txt Guide](https://developers.google.com/search/docs/crawling-indexing/robots/intro)
- [BeautifulSoup Docs](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
- [Requests Library](https://docs.python-requests.org/)

### Practical Coding
- [Exercism Python](https://exercism.org/tracks/python)
- [Real Python](https://realpython.com/)
- [Python urllib.parse](https://docs.python.org/3/library/urllib.parse.html)

### System Design
- [System Design Primer](https://github.com/donnemartin/system-design-primer)
- [ByteByteGo Blog](https://blog.bytebytego.com/)
- [System Design School](https://systemdesignschool.io/)

### Transformers
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

By end of Week 1, you should:
✅ Have working web scraping agent (robots.txt + rate limiting + scraping)  
✅ Solved at least 8-10 practical problems  
✅ Completed 2 system designs  
✅ Can explain transformer architecture  
✅ Read Anthropic blog and understand Constitutional AI at high level  
✅ Have working code on GitHub

**Interview Talking Point**: 
"I built an ethical web scraping agent using Claude Agent SDK. It demonstrates my understanding of the SDK's proper use case - agentic execution - rather than forcing it into RAG where it doesn't fit. The agent respects robots.txt, implements token bucket rate limiting, and uses exponential backoff for failures."

---

Good luck with Week 1! 🚀
