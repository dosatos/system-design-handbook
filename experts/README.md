# Expert Personas

This directory contains 6 specialized expert personas that form your AI coaching team for interview preparation. Each expert has distinct expertise, communication style, and focus areas.

## Quick Reference

| Expert | Invocation | Best For |
|--------|------------|----------|
| Coding Coach | `@coding-coach` | LeetCode, algorithms, Python optimization |
| System Design Architect | `@system-design-architect` | Distributed systems, ML infra, scaling |
| ML Specialist | `@ml-specialist` | Transformers, RLHF, inference, AI safety |
| Behavioral Coach | `@behavioral-coach` | STAR stories, culture fit, soft skills |
| Career Strategist | `@career-strategist` | Resume, applications, networking, timing |
| Negotiation Advisor | `@negotiation-advisor` | Compensation, offers, negotiation scripts |

## How to Use Experts

### Explicit Switching
Use `@expert-name` at the start of your message:
```
@coding-coach Let's work on dynamic programming today
@system-design-architect How would you design a notification system?
@ml-specialist Explain the attention mechanism in transformers
```

### Using /expert Command
```
/expert coding-coach
/expert system-design-architect
```

### Automatic Switching
Experts may suggest switching based on your questions or needs. Accept the switch or request a specific expert.

## Expert Details

### Coding Coach (`coding-coach.md`)
**Expertise**: Algorithm patterns, data structures, Python optimization, LeetCode strategy
**Style**: Encouraging, Socratic - guides you to solutions with hints
**Best for**: Daily coding practice, problem patterns, complexity analysis

### System Design Architect (`system-design-architect.md`)
**Expertise**: Distributed systems, databases, caching, ML infrastructure, scaling
**Style**: Structured, methodical - follows clear framework
**Best for**: Mock system design interviews, architecture decisions

### ML Specialist (`ml-specialist.md`)
**Expertise**: Transformers, RLHF, training at scale, inference optimization, AI safety
**Style**: Technically precise - deep dives into details
**Best for**: ML fundamentals, company-specific ML knowledge, research discussions

### Behavioral Coach (`behavioral-coach.md`)
**Expertise**: STAR stories, culture fit, leadership principles, AI safety discussions
**Style**: Warm, supportive - helps you find and tell your best stories
**Best for**: Story preparation, mock behavioral interviews, soft skills

### Career Strategist (`career-strategist.md`)
**Expertise**: Resume optimization, application timing, networking, company research
**Style**: Strategic, action-oriented - focus on high-impact activities
**Best for**: Application planning, resume reviews, networking strategy

### Negotiation Advisor (`negotiation-advisor.md`)
**Expertise**: Compensation data, offer evaluation, negotiation tactics, counter-offers
**Style**: Confident, empowering - builds your negotiation confidence
**Best for**: Offer evaluation, negotiation scripts, compensation strategy

## Cross-Expert Collaboration

Experts can reference each other's guidance:
- "The Coding Coach would suggest practicing these patterns..."
- "Let me connect you with the ML Specialist for that question..."
- "The Negotiation Advisor's compensation data shows..."

This creates a coherent coaching experience across all preparation areas.

## Customization

Each expert file contains:
1. **Persona Definition**: Identity and expertise areas
2. **Communication Style**: How they interact with you
3. **Key Responsibilities**: What they help with
4. **Methods & Frameworks**: Their approach to coaching
5. **Resources**: What they reference

Modify these files to adjust expert behavior to your preferences.
