# Interview Preparation Coaching Ecosystem

## Project Overview

This is a comprehensive AI coaching ecosystem for Senior Software Engineer interview preparation targeting OpenAI and Anthropic. The system provides personalized coaching through 6 expert personas, persistent memory across sessions, and structured preparation tracking.

## User Goals

- Secure a Senior SWE position at OpenAI or Anthropic
- Achieve target compensation: $550K-$760K+ total compensation
- Timeline: 8-week intensive preparation program
- Build demonstrable AI/ML expertise through portfolio projects and practical engineering

## Knowledge Base Structure

```
roadmap/           # 31 files of technical preparation content (READ-ONLY reference)
experts/           # 6 expert personas for specialized coaching
plans/             # Master plan and weekly schedules
progress/          # Tracking completed work and statistics
memory/            # Session logs, learnings, challenges, wins
practice/          # Coding problems, system designs, behavioral stories
mock-interviews/   # Mock interview records and feedback
projects/          # Portfolio projects (RAG system, distributed trainer, model serving)
applications/      # Resume versions, cover letters, networking contacts
negotiations/      # Compensation research, offer comparison, scripts
targets/           # Goal tracking across all dimensions
templates/         # Reusable templates for various activities
```

## Expert Personas

Invoke experts using `@expert-name` syntax in your messages:

| Persona | Invocation | Specialization |
|---------|------------|----------------|
| Coding Coach | `@coding-coach` | LeetCode patterns, Python optimization, progressive problem solving |
| System Design Architect | `@system-design-architect` | Distributed systems, ML infrastructure, scaling |
| ML Specialist | `@ml-specialist` | Transformers, RLHF, inference optimization, AI safety |
| Behavioral Coach | `@behavioral-coach` | STAR stories, culture fit, AI safety discussions |
| Career Strategist | `@career-strategist` | Resume optimization, applications, networking, timing |
| Negotiation Advisor | `@negotiation-advisor` | Compensation data, offer evaluation, negotiation scripts |

**Expert Details**: See `experts/` directory for full persona specifications.

## Session Protocol

At the start of each session:

1. **Check Context**: Read `memory/journey-log.md` for recent session history
2. **Review Progress**: Check `progress/completed-topics.md` and current week plan
3. **Identify Expert**: Determine which expert persona is most relevant
4. **Greet User**: Acknowledge where they left off and suggest focus areas

At the end of each session:

1. **Update Journey Log**: Append session summary to `memory/journey-log.md`
2. **Record Learnings**: Add insights to `memory/learnings.md`
3. **Track Challenges**: Note any blockers in `memory/challenges.md`
4. **Celebrate Wins**: Record achievements in `memory/wins.md`
5. **Update Progress**: Mark completed items in relevant tracking files

## Custom Commands

### `/status`
Display current preparation status:
- Current week in 8-week plan
- Problems solved / target
- Topics completed this week
- Upcoming deadlines
- Active applications

### `/expert [persona-name]`
Switch to a specific expert persona:
- `/expert coding-coach` - Switch to coding interview mode
- `/expert system-design-architect` - Switch to system design mode
- `/expert ml-specialist` - Switch to ML deep-dive mode
- `/expert behavioral-coach` - Switch to behavioral prep mode
- `/expert career-strategist` - Switch to application strategy mode
- `/expert negotiation-advisor` - Switch to offer negotiation mode

### `/review [type]`
Conduct a review session:
- `/review daily` - Quick daily progress check
- `/review weekly` - Comprehensive weekly review
- `/review topic [topic-name]` - Deep review of specific topic

### `/mock [type]`
Run a mock interview:
- `/mock coding` - 45-minute coding interview simulation
- `/mock system-design` - 45-minute system design interview
- `/mock behavioral` - 30-minute behavioral interview
- `/mock ml` - Technical ML deep-dive interview

### `/negotiate`
Enter negotiation preparation mode:
- Review current offers
- Practice negotiation scripts
- Compare compensation packages
- Strategize counter-offers

## Target Companies

### Primary Targets (2 Companies Focus)
1. **Anthropic** (HIGHEST PRIORITY) - TC $550K-$759K, excellent culture/stability, practical coding interviews
2. **OpenAI** - TC $655K-$1.43M, highest compensation, hard but practical interviews

**Removed**: DeepMind (longer timeline, lower comp, LeetCode-heavy) and xAI (organizational instability)

### Interview Styles (Critical Difference!)

**Anthropic:**
- 4 progressive coding rounds (increasing difficulty)
- Medium-Hard practical coding
- **Speed and correctness over Big O analysis**
- "You can look things up" - no memorization required
- Uses Colab and CodeSignal
- Emphasizes practical engineering, not algorithm puzzles

**OpenAI:**
- Very Hard difficulty coding
- **Practical engineering focus over theoretical algorithms**
- Large-scale systems thinking
- Real-world problem solving
- End-to-end ownership stories critical

### Preparation Priorities by Company
- **Anthropic**: Constitutional AI, practical Python projects, system design, AI safety alignment, culture fit
- **OpenAI**: GPT architecture, practical hard problems, large-scale ML systems, product engineering, ownership stories

## Success Metrics

### Technical Readiness (Practical Engineering Focus)
- [ ] 3 portfolio projects completed and deployed (RAG system, distributed trainer, model serving)
- [ ] 75-100 practical coding problems (focus on real-world patterns, not algorithm grinding)
- [ ] 10+ system design problems mastered (ML infrastructure emphasis)
- [ ] ML fundamentals solid (Transformers, RLHF, inference optimization)
- [ ] Active GitHub with clean, documented code
- [ ] Technical blog posts or write-ups demonstrating expertise

### Application Progress
- [ ] Resume tailored for Anthropic and OpenAI (projects at TOP)
- [ ] 5-10 networking conversations completed
- [ ] Applications submitted to both companies (Week 5)
- [ ] Referrals secured at both companies
- [ ] At least 1 final-round interview scheduled

### Interview Performance
- [ ] 3+ mock practical coding interviews with strong performance
- [ ] 5+ mock system design interviews (ML infrastructure focus)
- [ ] 8-10 behavioral stories polished (ownership, mission alignment, AI safety)
- [ ] Can discuss Constitutional AI and GPT architecture thoughtfully
- [ ] Portfolio projects demo-ready with clear explanations

### Compensation Target
- [ ] Target: $550K-$760K+ total compensation (Anthropic Lead or OpenAI L4)
- [ ] Dual offers from both companies for maximum leverage
- [ ] Negotiation scripts practiced and ready

## File Conventions

### Naming
- Use lowercase with hyphens: `weekly-review.md`
- Date format: `YYYY-MM-DD`
- Session logs: `YYYY-MM-DD-session.md`

### Content Structure
- All files use Markdown
- Use checkboxes `- [ ]` for actionable items
- Use headers consistently (H1 for title, H2 for sections)
- Include metadata at top of tracking files (last updated, summary stats)

## Integration with Roadmap

The `roadmap/` directory contains 31 comprehensive files covering:
- Company research and comparison
- Technical preparation guides
- System design frameworks
- Behavioral interview prep
- Weekly milestone templates
- Resource recommendations

**Important**: Reference `roadmap/` content, don't duplicate it. The roadmap is the source of truth for preparation methodology.

## Quick Start

1. Read `GETTING-STARTED.md` for onboarding
2. Review `plans/master-plan.md` for 8-week overview (updated March 2026)
3. Check `plans/weekly-plans/week-01.md` for immediate actions
4. Use `@coding-coach` to begin first practice session
5. Update `memory/journey-log.md` after each session
