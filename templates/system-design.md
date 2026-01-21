# System Design Template

Use this template for approaching system design problems systematically.

---

## RESHADED Framework (45 minutes)

### R - Requirements (5 minutes)

**Functional Requirements** (What the system should do):
1.
2.
3.
4.

**Non-Functional Requirements** (How well it should do it):
- [ ] Scalability: ___ users/requests
- [ ] Availability: ___% uptime
- [ ] Latency: p50 ___, p99 ___
- [ ] Consistency: Strong / Eventual
- [ ] Durability: ___ data loss tolerance

**Scope Clarification**:
- In scope:
- Out of scope:

**Assumptions**:
1.
2.

---

### E - Estimations (5 minutes)

**Users**:
- DAU:
- MAU:
- Peak concurrent:
- Requests per user per day:

**Traffic**:
- Read:write ratio:
- QPS (average):
- QPS (peak):

**Storage**:
- Data per user:
- Total data:
- Growth rate:

**Bandwidth**:
- Average request size:
- Daily bandwidth:

**Quick Math Reference**:
```
1 million requests/day ≈ 12 QPS
1 billion requests/day ≈ 12,000 QPS
1 KB × 1 million = 1 GB
1 KB × 1 billion = 1 TB
```

---

### S - Storage Schema (5 minutes)

**Data Models**:

```
Entity 1:
- field_1: type
- field_2: type
- created_at: timestamp

Entity 2:
- field_1: type
- ...
```

**Database Choice**:
- [ ] SQL (PostgreSQL, MySQL) - Why:
- [ ] NoSQL Document (MongoDB) - Why:
- [ ] NoSQL Key-Value (Redis, DynamoDB) - Why:
- [ ] Wide Column (Cassandra) - Why:

**Indexing Strategy**:
-

**Partitioning/Sharding**:
- Shard key:
- Strategy:

---

### H - High-Level Design (10 minutes)

**Architecture Diagram**:
```
[Client] → [Load Balancer] → [API Servers]
                                  ↓
                            [Cache Layer]
                                  ↓
                            [Database]
```

**Key Components**:
1. **Client Layer**:
2. **API Layer**:
3. **Service Layer**:
4. **Data Layer**:
5. **Cache Layer**:

**Data Flow**:
1. User sends request to...
2. Request is processed by...
3. Data is stored/retrieved from...
4. Response is returned...

---

### A - API Design (5 minutes)

**Key Endpoints**:

```
POST /api/v1/resource
Request: { field1: "", field2: "" }
Response: { id: "", status: "" }

GET /api/v1/resource/{id}
Response: { id: "", field1: "", ... }

PUT /api/v1/resource/{id}
Request: { field1: "", field2: "" }
Response: { status: "" }

DELETE /api/v1/resource/{id}
Response: { status: "" }
```

**Authentication**:
-

**Rate Limiting**:
-

---

### D - Detailed Design (15 minutes)

**Component Deep Dive 1**: ___
- How it works:
- Data structures:
- Algorithm:
- Edge cases:

**Component Deep Dive 2**: ___
- How it works:
- Data structures:
- Algorithm:
- Edge cases:

**Caching Strategy**:
- What to cache:
- Cache invalidation:
- TTL:

**Message Queue** (if applicable):
- Use case:
- Technology:
- Consumer design:

---

### E - Error Handling (5 minutes)

**Failure Scenarios**:
| Component | Failure Mode | Mitigation |
|-----------|--------------|------------|
| Database | Down | Replica failover |
| Cache | Miss | Fall through to DB |
| API Server | Crash | LB health checks |
| Network | Partition | Circuit breaker |

**Recovery Strategy**:
-

**Monitoring & Alerting**:
- Key metrics:
- Alert thresholds:

**Graceful Degradation**:
-

---

### D - Discuss Trade-offs (5 minutes)

**Design Trade-offs Made**:

| Decision | Alternative | Why This Choice |
|----------|-------------|-----------------|
| | | |
| | | |

**CAP Theorem Position**:
- [ ] CP (Consistency + Partition Tolerance)
- [ ] AP (Availability + Partition Tolerance)
- Why:

**Scaling Considerations**:
- Current design handles: ___ QPS
- To scale 10x: ___
- To scale 100x: ___

**Future Improvements**:
1.
2.
3.

---

## Quick Reference

### Database Selection
| Use Case | Recommendation |
|----------|----------------|
| ACID transactions | PostgreSQL |
| High write throughput | Cassandra |
| Flexible schema | MongoDB |
| Caching | Redis |
| Search | Elasticsearch |

### Caching Patterns
- **Cache-Aside**: App checks cache, then DB
- **Write-Through**: Write to cache and DB
- **Write-Behind**: Write to cache, async to DB

### Load Balancing
- Round Robin: Simple, equal distribution
- Least Connections: Route to least busy
- IP Hash: Session affinity

### Consistency Models
- **Strong**: All reads see latest write
- **Eventual**: Reads may see stale data temporarily
- **Causal**: Preserves cause-and-effect

---

## Interview Tips

### Before Starting
- Clarify requirements first
- State assumptions explicitly
- Ask about scale expectations

### During Design
- Draw as you explain
- Start high-level, then deep-dive
- Always discuss trade-offs

### Common Mistakes
- Jumping to detailed design too fast
- Not discussing trade-offs
- Over-engineering simple systems
- Ignoring failure modes

---

_Practice until the framework is automatic._
