---
title: "Classical System Design Topics"
category: "System Design"
last_updated: "January 2026"

summary: |
  Comprehensive guide to classical system design concepts. Covers scalability (horizontal vs
  vertical), load balancing, caching strategies, database design (SQL vs NoSQL, sharding,
  replication), CAP theorem, message queues, and API design. Includes practice problems
  (URL shortener, rate limiter, notification system) and estimation techniques.

outline:
  - Must-Know Concepts (Scalability, Load Balancing, Caching, Databases, CAP, Queues, APIs)
  - Practice Design Problems
  - Estimation Practice
  - Resources
---

# Classical System Design Topics

## Table of Contents

- [Must-Know Concepts](#must-know-concepts)
- [Practice Design Problems](#practice-design-problems)
- [Estimation Practice](#estimation-practice)
- [Resources](#resources)

---

## Must-Know Concepts

### 1. Scalability

**Horizontal vs Vertical Scaling**
```
Vertical (Scale Up):      Horizontal (Scale Out):
┌─────────────────┐       ┌──────┐ ┌──────┐ ┌──────┐
│                 │       │      │ │      │ │      │
│   Bigger Box    │  vs   │ Box1 │ │ Box2 │ │ Box3 │
│                 │       │      │ │      │ │      │
└─────────────────┘       └──────┘ └──────┘ └──────┘
```

**When to Use Each:**
| Approach | Pros | Cons | Use When |
|----------|------|------|----------|
| Vertical | Simple, no code changes | Limited, expensive, SPOF | Starting out, simple apps |
| Horizontal | Unlimited scale, redundancy | Complex, state management | Production systems at scale |

### 2. Load Balancing

**Strategies:**
| Algorithm | Description | Use When |
|-----------|-------------|----------|
| Round Robin | Cycle through servers | Homogeneous servers |
| Weighted RR | Weight by capacity | Heterogeneous servers |
| Least Connections | Route to least busy | Variable request times |
| IP Hash | Consistent by client IP | Session affinity needed |
| Consistent Hashing | Minimize redistribution | Caching, partitioning |

**Layer 4 vs Layer 7:**
```
Layer 4 (Transport):       Layer 7 (Application):
- Faster                   - Content-based routing
- Less features            - SSL termination
- TCP/UDP aware            - HTTP aware
```

### 3. Caching

**Cache Strategies:**
```
Write-Through:           Write-Back:              Write-Around:
┌─────┐   ┌─────┐       ┌─────┐   ┌─────┐       ┌─────┐   ┌─────┐
│ App │──▶│Cache│──▶DB  │ App │──▶│Cache│       │ App │──▶│ DB  │
└─────┘   └─────┘       └─────┘   └──┬──┘       └─────┘   └─────┘
                                     │ async           ↓
                                     ▼ DB         Cache on read
```

**Cache Eviction Policies:**
- LRU (Least Recently Used) - Most common
- LFU (Least Frequently Used)
- FIFO (First In First Out)
- TTL (Time To Live)

**Caching Technologies:**
| Technology | Use Case |
|------------|----------|
| Redis | In-memory, data structures |
| Memcached | Simple K/V, distributed |
| CDN | Static content, edge |
| Local cache | Single-node, low latency |

### 4. Database Design

**SQL vs NoSQL:**
| Aspect | SQL | NoSQL |
|--------|-----|-------|
| Schema | Fixed | Flexible |
| Scaling | Vertical (typically) | Horizontal |
| ACID | Yes | Varies |
| Joins | Yes | Limited |
| Use case | Complex queries, transactions | Scale, flexibility |

**Partitioning/Sharding:**
```
Horizontal (Sharding):
┌─────────────────────────────────────┐
│            Original Table           │
└─────────────────────────────────────┘
              │ Shard by user_id % 3
              ▼
┌───────────┐ ┌───────────┐ ┌───────────┐
│  Shard 0  │ │  Shard 1  │ │  Shard 2  │
│ id%3 == 0 │ │ id%3 == 1 │ │ id%3 == 2 │
└───────────┘ └───────────┘ └───────────┘
```

**Replication:**
| Type | Consistency | Availability | Use Case |
|------|-------------|--------------|----------|
| Single Leader | Strong | Lower | OLTP |
| Multi-Leader | Eventual | Higher | Geo-distributed |
| Leaderless | Eventual | Highest | High availability |

### 5. CAP Theorem

```
      Consistency
          ▲
         / \
        /   \
       /     \
      /   CP  \
     /    systems
    /     (Postgres)
   ▼───────────────▶
Availability       Partition Tolerance

AP systems: Cassandra, DynamoDB
CP systems: PostgreSQL, MongoDB (default)
```

**In Practice:**
- Partition tolerance is mandatory (networks fail)
- Choose between Consistency and Availability
- Most systems offer tunable consistency

### 6. Message Queues

**Use Cases:**
- Decoupling services
- Async processing
- Load leveling
- Event sourcing

**Technologies:**
| Queue | Throughput | Ordering | Features |
|-------|------------|----------|----------|
| Kafka | Very High | Partition | Log-based, replay |
| RabbitMQ | High | Queue | Routing, DLQ |
| SQS | High | Partial | Managed, simple |
| Redis Streams | Very High | Consumer group | In-memory |

**Patterns:**
```
Pub/Sub:                    Queue:
┌──────┐                    ┌──────┐
│Pub   │                    │Prod  │
└──┬───┘                    └──┬───┘
   │                           │
   ▼                           ▼
┌──────┐                    ┌──────┐
│Topic │───────────────────▶│Queue │
└──────┘                    └──┬───┘
   │                           │
   ├───▶ Sub1                  ▼
   ├───▶ Sub2               Consumer
   └───▶ Sub3               (one gets each msg)
```

### 7. API Design

**REST vs gRPC:**
| Aspect | REST | gRPC |
|--------|------|------|
| Protocol | HTTP/1.1 | HTTP/2 |
| Format | JSON | Protobuf |
| Performance | Lower | Higher |
| Browser support | Native | Limited |
| Use case | Public APIs | Internal services |

**Rate Limiting Algorithms:**

```python
# Token Bucket
class TokenBucket:
    def __init__(self, rate, capacity):
        self.rate = rate          # tokens per second
        self.capacity = capacity  # max tokens
        self.tokens = capacity
        self.last_update = time.time()

    def allow_request(self):
        now = time.time()
        elapsed = now - self.last_update
        self.tokens = min(self.capacity,
                         self.tokens + elapsed * self.rate)
        self.last_update = now

        if self.tokens >= 1:
            self.tokens -= 1
            return True
        return False
```

---

## Practice Design Problems

### Problem 1: URL Shortener

**Requirements:**
- Shorten long URLs
- Redirect short → long
- 100M URLs/month writes
- 10B reads/month

**Key Design Decisions:**
1. **ID Generation:** Counter, Random, Base62
2. **Storage:** NoSQL for K/V pattern
3. **Caching:** Redis for hot URLs
4. **Read path:** Cache → DB

```
Write Path:
URL → Generate ID → Store (DB + Cache) → Return short URL

Read Path:
Short URL → Cache hit? → Return long URL
                     ↓ miss
            DB lookup → Cache update → Return
```

### Problem 2: Rate Limiter

**Requirements:**
- Limit requests per user
- Multiple rate limits (1/sec, 100/min, 1000/day)
- Distributed across servers

**Key Design Decisions:**
1. **Algorithm:** Sliding window counter
2. **Storage:** Redis (atomic operations)
3. **Sync:** Async for performance

```
Request → Get user limits from Redis
       → Check all windows
       → Allow/Reject
       → Update counters (async)
```

### Problem 3: Notification System

**Requirements:**
- Push, Email, SMS channels
- Millions of notifications/day
- At-least-once delivery
- Rate limiting per user

**Components:**
```
API Gateway → Notification Service → Message Queue → Workers
                    │                                   │
                    └── Template Service                ├── Push (APNS, FCM)
                                                        ├── Email (SendGrid)
                                                        └── SMS (Twilio)
```

---

## Estimation Practice

### Back-of-Envelope Calculations

**Common Numbers:**
| Metric | Value |
|--------|-------|
| DAU → Writes/day | DAU × 5-10 |
| Writes/sec | Writes/day ÷ 86400 |
| Storage (1 year) | Writes × size × 365 |
| Memory (cache) | Hot data × size |

**Example: Twitter-like Service**
```
DAU: 100M
Tweets/user/day: 0.5
Tweets/day: 50M
Tweets/sec: ~600

Tweet size: 1KB (text + metadata)
Storage/year: 50M × 1KB × 365 = ~18TB

Read:Write ratio: 100:1
Reads/sec: 60,000
```

---

## Resources

### Books
- **Designing Data-Intensive Applications** - Martin Kleppmann
- **System Design Interview** Vol 1 & 2 - Alex Xu

### Online
- [System Design Primer](https://github.com/donnemartin/system-design-primer)
- [Grokking System Design](https://www.designgurus.io/)
- [Hello Interview](https://www.hellointerview.com/)
