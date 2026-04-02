# Week 1 Detailed Plan: Foundations

**Start Date**: Tuesday, March 31, 2026  
**End Date**: Monday, April 6, 2026  
**Phase**: Build Foundations  
**Weekly Goal**: RAG system started (40% complete), 10 practical problems solved, transformer basics understood  
**Time Commitment**: 28 hours (4 hours/day average)

---

## Week 1 Overview

| Focus Area | Time Allocation | Deliverables |
|------------|-----------------|--------------|
| RAG System Project #1 | 12 hours | Architecture designed, document ingestion working, vector embeddings integrated |
| Practical Coding | 6 hours | 10 problems solved (string/parsing, dict/list operations) |
| System Design | 4 hours | URL Shortener design completed |
| Transformer Learning | 4 hours | Architecture understood, can explain attention |
| Company Research | 2 hours | Anthropic blog posts read, "Why Anthropic?" drafted |

**Total**: 28 hours

---

## Day 1 (Tuesday, March 31) - 4 hours

### Morning Session (2 hours): RAG System Kickoff

**Goal**: Understand RAG architecture and set up project structure

**Tasks**:
1. **Read RAG Overview** (45 min)
   - Resource: [LangChain RAG Tutorial](https://python.langchain.com/docs/tutorials/rag/)
   - Resource: [LlamaIndex Q&A Guide](https://docs.llamaindex.ai/en/stable/understanding/putting_it_all_together/q_and_a/)
   - Read both to understand different approaches
   - Take notes on architecture patterns

2. **Choose Your Stack** (30 min)
   - **Decision Point**: LangChain vs LlamaIndex
   - **ASSUMPTION**: LangChain is more flexible for production, LlamaIndex is faster to prototype
   - **Recommendation**: Start with LangChain (better for Anthropic/OpenAI API integration)
   - Alternative: Can use LlamaIndex if you prefer simpler abstractions

3. **Project Setup** (45 min)
   ```bash
   mkdir rag-system && cd rag-system
   python -m venv venv
   source venv/bin/activate
   pip install langchain chromadb openai anthropic fastapi uvicorn
   git init
   echo "venv/" >> .gitignore
   echo "*.env" >> .gitignore
   touch README.md main.py requirements.txt
   ```
   - Create basic project structure
   - Write initial README with project goals

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
- [ ] RAG project repository created
- [ ] Dependencies installed
- [ ] README drafted with project goals
- [ ] Transformer architecture understood at high level
- [ ] Can explain what attention mechanism does

---

## Day 2 (Wednesday, April 1) - 4 hours

### Morning Session (2 hours): Practical Coding (Problems 1-3)

**Goal**: Solve 3 practical string/parsing problems

**ASSUMPTION**: You have Python 3.8+ and can run code locally

**Problem Sources**:
- [Exercism Python Track](https://exercism.org/tracks/python) - Filter for "easy" difficulty
- [Real Python Tutorials](https://realpython.com/) - Look for practical exercises

**Suggested Problems** (adapt based on what you find):
1. **Log File Parser** (30 min)
   - Parse log files and extract timestamps, error levels, messages
   - Practice: String splitting, regex, dictionaries
   - **UNKNOWN**: Exact problem source - use Exercism or create your own from real logs

2. **Data Cleaning** (45 min)
   - Clean messy CSV data (handle missing values, normalize formats)
   - Practice: File I/O, string manipulation, data structures
   - **Resource**: [Real Python - Working with Files](https://realpython.com/working-with-files-in-python/)

3. **API Response Parsing** (45 min)
   - Parse JSON API responses and transform data
   - Practice: JSON handling, nested dictionaries, list comprehensions
   - **Resource**: [Real Python - JSON in Python](https://realpython.com/python-json/)

**Coding Practice Protocol**:
- Set 45-min timer per problem
- Can look things up (matches Anthropic style)
- Focus on clean, working code
- Write tests for edge cases
- Log problems in `practice/coding/problems-log.md`

### Evening Session (2 hours): RAG System - Document Ingestion

**Goal**: Build document ingestion and chunking

**Tasks**:
1. **Study Chunking Strategies** (30 min)
   - Resource: [LangChain Text Splitters](https://python.langchain.com/docs/modules/data_connection/document_transformers/)
   - Learn about different chunking methods
   - Understand chunk size vs retrieval quality trade-offs

2. **Implement Document Loader** (90 min)
   ```python
   # Example starting point (adapt from LangChain docs)
   from langchain.document_loaders import TextLoader
   from langchain.text_splitter import RecursiveCharacterTextSplitter
   
   # Load documents
   loader = TextLoader("sample_docs/")
   documents = loader.load()
   
   # Split into chunks
   text_splitter = RecursiveCharacterTextSplitter(
       chunk_size=1000,
       chunk_overlap=200
   )
   chunks = text_splitter.split_documents(documents)
   ```
   - Create sample documents to test (3-5 text files)
   - Implement document loading
   - Implement chunking with overlap
   - Test with different chunk sizes

**End of Day 2 Checklist**:
- [ ] 3 practical problems solved and logged
- [ ] Document ingestion code working
- [ ] Chunking implemented with configurable parameters
- [ ] Sample documents processed successfully

---

## Day 3 (Thursday, April 2) - 4 hours

### Morning Session (2 hours): RAG System - Embeddings & Vector Store

**Goal**: Integrate embeddings and vector database

**Tasks**:
1. **Choose Embedding Model** (20 min)
   - **Option A**: OpenAI embeddings (requires API key, costs ~$0.0001 per 1K tokens)
   - **Option B**: Sentence Transformers (free, local, slower)
   - **ASSUMPTION**: OpenAI embeddings are faster and higher quality
   - **Recommendation**: Start with OpenAI, fallback to Sentence Transformers if cost is concern
   - Resource: [Sentence Transformers](https://www.sbert.net/) for free option

2. **Set Up ChromaDB** (40 min)
   - Resource: [ChromaDB Documentation](https://docs.trychroma.com/)
   - Install ChromaDB (already in requirements from Day 1)
   - Create vector store
   - Test storage and retrieval
   ```python
   import chromadb
   from langchain.vectorstores import Chroma
   from langchain.embeddings import OpenAIEmbeddings
   
   # Initialize
   embeddings = OpenAIEmbeddings()
   vectorstore = Chroma.from_documents(
       documents=chunks,
       embedding=embeddings,
       persist_directory="./chroma_db"
   )
   ```

3. **Implement Semantic Search** (60 min)
   - Write function to query vector store
   - Test similarity search with example queries
   - Benchmark retrieval speed
   - Log sample queries and results

**Evening Session (2 hours): System Design - URL Shortener

**Goal**: Complete URL Shortener system design

**Tasks**:
1. **Study Reference Design** (45 min)
   - Resource: [System Design Primer - URL Shortener](https://github.com/donnemartin/system-design-primer)
   - Resource: [URL Shortener on SystemDesignSchool](https://systemdesignschool.io/problems/url-shortener)
   - Understand:
     - Hash generation strategies
     - Database schema
     - Caching layer
     - Scalability considerations

2. **Design Your Own Version** (60 min)
   - Use framework: Requirements → High-level → Deep-dive → Trade-offs
   - Draw architecture diagram
   - Calculate capacity estimates
   - Identify bottlenecks
   - Write design in `practice/system-designs/url-shortener.md`

3. **Review and Critique** (15 min)
   - Compare your design to reference solutions
   - Note what you missed
   - Understand why certain choices were made

**End of Day 3 Checklist**:
- [ ] Vector embeddings integrated
- [ ] ChromaDB storing and retrieving documents
- [ ] Semantic search working
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

2. **Frequency Counter** (40 min)
   - Count word/character frequencies in large text
   - Practice: Counter, defaultdict, optimization
   - Real-world use: Log analysis, data pipelines

3. **Two-Sum Style Problem** (40 min)
   - Find pairs/triplets with hash map
   - Practice: Hash map patterns, time/space trade-offs
   - **ASSUMPTION**: This is on Exercism or can adapt from System Design Primer examples

**Coding Practice Protocol** (Same as Day 2):
- 40-min timer per problem
- Can look things up
- Focus on working code
- Log in problems-log.md

### Evening Session (2 hours): RAG System - LLM Integration

**Goal**: Integrate LLM for response generation

**Tasks**:
1. **Choose LLM API** (15 min)
   - **Option A**: Anthropic Claude (recommended for Anthropic application)
   - **Option B**: OpenAI GPT-4 (faster response times)
   - **ASSUMPTION**: Using Claude shows alignment with Anthropic
   - Get API key from [Anthropic Console](https://console.anthropic.com/) or [OpenAI Platform](https://platform.openai.com/)

2. **Implement RAG Pipeline** (90 min)
   ```python
   from anthropic import Anthropic
   
   def rag_query(question, vectorstore):
       # 1. Retrieve relevant docs
       docs = vectorstore.similarity_search(question, k=3)
       context = "\n\n".join([doc.page_content for doc in docs])
       
       # 2. Generate response with context
       client = Anthropic(api_key="...")
       message = client.messages.create(
           model="claude-3-5-sonnet-20241022",
           max_tokens=1024,
           messages=[{
               "role": "user",
               "content": f"Context:\n{context}\n\nQuestion: {question}"
           }]
       )
       return message.content[0].text
   ```
   - Implement retrieval + generation pipeline
   - Test with sample questions
   - Measure end-to-end latency

3. **Test & Iterate** (15 min)
   - Try 5-10 test questions
   - Note quality issues
   - Adjust retrieval parameters (k, chunk size)

**End of Day 4 Checklist**:
- [ ] 3 more practical problems solved (6 total)
- [ ] LLM API integrated (Anthropic or OpenAI)
- [ ] End-to-end RAG pipeline working
- [ ] Test queries returning reasonable answers

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
     - Specific technical interest (e.g., Constitutional AI approach)
     - Mission alignment (AI safety)
     - Cultural fit (careful thinking, independent work)
   - Save in `applications/anthropic/why-anthropic.md`

**End of Day 5 Checklist**:
- [ ] Attention mechanism understood mathematically
- [ ] Transformer architecture can be explained to others
- [ ] 5+ Anthropic blog posts read
- [ ] Constitutional AI overview understood
- [ ] "Why Anthropic?" draft written

---

## Day 6 (Sunday, April 5) - 4 hours

### Morning Session (2 hours): Practical Coding (Problems 7-9)

**Goal**: Solve 3 list operation problems

**Problem Types**:
1. **List Filtering/Transformation** (40 min)
   - Complex filtering with multiple conditions
   - Practice: List comprehensions, filter/map/reduce
   - Real-world: Data pipelines, ETL

2. **Sliding Window** (40 min)
   - **ASSUMPTION**: Practical sliding window (e.g., moving average, not classic LeetCode)
   - Calculate rolling statistics on data stream
   - Real-world: Time series analysis, metrics

3. **Array Manipulation** (40 min)
   - In-place array operations
   - Practice: Index manipulation, edge cases
   - Real-world: Data processing, batch operations

**Resource**: Continue using Exercism or Real Python tutorials

### Evening Session (2 hours): RAG System - Polish & Test

**Goal**: Clean up code and add error handling

**Tasks**:
1. **Add Error Handling** (45 min)
   - Handle API failures gracefully
   - Validate input queries
   - Handle empty results
   - Add retry logic for API calls

2. **Add Logging** (30 min)
   ```python
   import logging
   
   logging.basicConfig(level=logging.INFO)
   logger = logging.getLogger(__name__)
   
   logger.info(f"Retrieved {len(docs)} documents")
   logger.info(f"Query latency: {latency_ms}ms")
   ```
   - Log retrieval results
   - Log API calls and latency
   - Track errors

3. **Write Tests** (45 min)
   - Test document loading
   - Test chunking with edge cases (empty docs, very long docs)
   - Test vector search
   - **UNKNOWN**: Full test coverage - aim for basic smoke tests

**End of Day 6 Checklist**:
- [ ] 9 practical problems solved total
- [ ] RAG system has error handling
- [ ] Logging implemented
- [ ] Basic tests written
- [ ] Code quality improved

---

## Day 7 (Monday, April 6) - 6 hours (Deep Work)

### Morning Session (3 hours): System Design - Rate Limiter

**Goal**: Complete Rate Limiter design

**Tasks**:
1. **Study Rate Limiting Patterns** (60 min)
   - Resource: [System Design Primer](https://github.com/donnemartin/system-design-primer)
   - Resource: [ByteByteGo Blog](https://blog.bytebytego.com/) - Search for rate limiting articles
   - Understand algorithms:
     - Token bucket
     - Leaky bucket
     - Fixed window
     - Sliding window
   - Compare trade-offs

2. **Design Rate Limiter** (90 min)
   - Requirements gathering
   - Choose algorithm (recommend: Token bucket or Sliding window)
   - Database/cache design (Redis typically)
   - Distributed considerations
   - Draw architecture
   - Calculate capacity
   - Write design in `practice/system-designs/rate-limiter.md`

3. **Review & Critique** (30 min)
   - Compare to reference solutions
   - Note gaps in your understanding
   - Research anything unclear

### Afternoon Session (2 hours): RAG System - Simple UI

**Goal**: Add basic web interface

**Tasks**:
1. **Build FastAPI Endpoint** (60 min)
   - Resource: [FastAPI Documentation](https://fastapi.tiangolo.com/)
   ```python
   from fastapi import FastAPI
   
   app = FastAPI()
   
   @app.post("/query")
   async def query(question: str):
       response = rag_query(question, vectorstore)
       return {"answer": response}
   ```
   - Create POST endpoint for queries
   - Add input validation
   - Test with curl or Postman

2. **Add Simple HTML UI** (60 min)
   - Create `static/index.html` with form
   - Use Tailwind CDN for styling (optional)
   - **ASSUMPTION**: Basic HTML/CSS knowledge
   - **ALTERNATIVE**: Skip UI and just use API endpoint
   ```html
   <!DOCTYPE html>
   <html>
   <body>
       <form id="queryForm">
           <input type="text" id="question" />
           <button type="submit">Ask</button>
       </form>
       <div id="answer"></div>
       <script>
           // Basic fetch to POST /query
       </script>
   </body>
   </html>
   ```

### Evening Session (1 hour): Practical Coding (Problem 10)

**Goal**: Solve 1 challenging problem

**Problem Type**: API Design
- Design a REST endpoint for a specific use case
- Practice: HTTP methods, status codes, error handling
- Real-world: Building production APIs

**Resource**: [Microsoft API Guidelines](https://github.com/microsoft/api-guidelines) or [Zalando REST API Guidelines](https://github.com/zalando/restful-api-guidelines)

**End of Day 7 Checklist**:
- [ ] 10 practical problems solved (Week 1 goal reached!)
- [ ] Rate Limiter design completed
- [ ] RAG system has API endpoint
- [ ] Simple UI added (or API documented)
- [ ] Ready to demo RAG system

---

## Week 1 Review (Monday Evening, April 6 - Optional 1 hour)

### Reflection Session

**Tasks**:
1. **Update Progress Tracking** (20 min)
   - Update `progress/weekly/week-01.md`
   - Mark completed items
   - Note what took longer than expected

2. **Technical Review** (20 min)
   - Can you explain transformer architecture?
   - Can you demo your RAG system?
   - Can you walk through your system designs?

3. **Plan Week 2** (20 min)
   - Review Week 2 goals in master plan
   - Identify potential blockers
   - Adjust if needed based on Week 1 learnings

---

## Expected Outcomes by End of Week 1

### ✅ RAG System (40% Complete)
- [x] Project structure set up
- [x] Document ingestion working
- [x] Vector embeddings integrated
- [x] Semantic search functional
- [x] LLM integration complete
- [x] Basic API endpoint working
- [ ] Deployment (Week 2-3)
- [ ] Performance optimization (Week 2-3)
- [ ] Production polish (Week 3)

### ✅ Practical Coding (10 Problems)
- 3 String/parsing problems
- 3 Dict/hashmap problems  
- 3 List operation problems
- 1 API design problem

### ✅ System Design (1 Complete, 1 In Progress)
- URL Shortener: Complete
- Rate Limiter: Complete

### ✅ ML Learning
- Transformer architecture understood
- Attention mechanism clear
- Can explain at high level

### ✅ Company Research
- Anthropic blog posts read
- Constitutional AI overview understood
- "Why Anthropic?" drafted

---

## Resources Quick Reference

### RAG System
- [LangChain Docs](https://python.langchain.com/docs/get_started/introduction)
- [LlamaIndex Docs](https://docs.llamaindex.ai/en/stable/)
- [ChromaDB Docs](https://docs.trychroma.com/)
- [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook)
- [FastAPI Docs](https://fastapi.tiangolo.com/)

### Practical Coding
- [Exercism Python](https://exercism.org/tracks/python)
- [Real Python](https://realpython.com/)
- [Python Roadmap](https://roadmap.sh/python)

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

## Known Unknowns & Assumptions

### ⚠️ ASSUMPTIONS
1. **Python Environment**: Assumes Python 3.8+ installed locally
2. **API Keys**: Assumes you'll get OpenAI or Anthropic API keys (both have free tiers/credits)
3. **Development Tools**: Assumes basic familiarity with git, terminal, text editor
4. **Internet Access**: All resources require internet
5. **Hardware**: Assumes reasonable laptop (no GPU needed for Week 1)

### ❓ UNKNOWNS
1. **Exact Coding Problems**: Exercism and Real Python have rotating content - exact problems may vary
2. **API Costs**: OpenAI embeddings cost ~$0.0001/1K tokens, Claude API costs vary - UNKNOWN total cost for Week 1 (estimate: $5-15)
3. **Time Estimates**: Times are estimates based on average pace - adjust as needed
4. **Prior Knowledge**: Plan assumes intermediate Python knowledge - if beginner, may need extra time

### 🚨 EXPLICIT GAPS
1. **No specific LeetCode problems listed**: Intentionally avoiding LeetCode grinding per research findings
2. **UI optional**: RAG UI is optional - can focus on API only
3. **Testing minimal**: Full test coverage deferred to later weeks
4. **No deployment yet**: Deployment happens Week 2-3, not Week 1

---

## Adjustments & Flexibility

**If Behind Schedule**:
- Skip UI (Day 7) - focus on API only
- Reduce problems from 10 to 8
- Skim transformer paper instead of deep read

**If Ahead of Schedule**:
- Add simple monitoring to RAG system
- Read more Anthropic research papers
- Start Week 2 transformer training fundamentals early
- Experiment with different embedding models

**If Struggling**:
- Spend extra time on transformers (most important foundation)
- Reduce coding problems but maintain quality
- Ask for help in LangChain/LlamaIndex communities
- Extend Week 1 to 8-9 days if needed

---

## Daily Checklist Template

```markdown
## [Day X] - [Date]

### Morning Session ✅
- [ ] Task 1
- [ ] Task 2
- [ ] Task 3

### Evening Session ✅
- [ ] Task 1
- [ ] Task 2

### Notes
- What went well:
- What took longer:
- Questions for tomorrow:

### Time Tracking
- Planned: X hours
- Actual: X hours
```

---

## Week 1 Success Criteria

You're ready for Week 2 if:
✅ RAG system works end-to-end (can query and get answers)  
✅ Solved at least 8 practical problems  
✅ Completed 2 system designs  
✅ Can explain transformer architecture  
✅ Read Anthropic blog and understand Constitutional AI at high level  
✅ Have working code on GitHub

**Not required for Week 1**:
- ❌ Perfect code quality
- ❌ Full test coverage
- ❌ Production deployment
- ❌ Deep transformer math mastery
- ❌ Complete system design framework memorized

Week 1 is about **building momentum and foundational understanding**. Polish comes in Weeks 2-3.

---

Good luck with Week 1! 🚀
