# Interview Preparation Coaching Ecosystem

## Project Overview

This is a comprehensive AI coaching ecosystem for Senior Software Engineer interview preparation targeting OpenAI, Anthropic, DeepMind, and xAI. The system provides personalized coaching through 6 expert personas, persistent memory across sessions, and structured preparation tracking.

## User Goals

- Secure a Senior SWE position at a top AI lab (OpenAI, Anthropic, DeepMind, or xAI)
- Achieve target compensation: $500K-$700K+ total compensation
- Timeline: 12-week intensive preparation program
- Build demonstrable AI/ML expertise through portfolio projects

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
- Current week in 12-week plan
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

### Primary Targets (Tier 1)
1. **Anthropic** - SF-based, strong safety focus, TC $470K-$630K
2. **OpenAI** - SF-based, cutting-edge research, TC $400K-$700K+

### Secondary Targets (Tier 2)
3. **DeepMind** - London/US, research-heavy, Google compensation bands
4. **xAI** - Startup equity upside, competitive base

### Preparation Priorities by Company
- **Anthropic**: Constitutional AI, RLHF, Claude architecture, safety research
- **OpenAI**: GPT architecture, scaling laws, RLHF, product focus
- **DeepMind**: Research fundamentals, AlphaFold/Gemini, theoretical depth
- **xAI**: Move fast, Grok architecture, real-time systems

## Success Metrics

### Technical Readiness
- [ ] 200+ LeetCode problems solved (75 Blind 75, 50 NeetCode 150, 75+ company-tagged)
- [ ] 15+ system design problems mastered
- [ ] 3 portfolio projects completed and deployed
- [ ] ML fundamentals solid (Transformers, RLHF, inference)

### Application Progress
- [ ] Resume tailored for each target company
- [ ] 10+ networking conversations completed
- [ ] Applications submitted to all target companies
- [ ] At least 2 final-round interviews scheduled

### Interview Performance
- [ ] 5+ mock coding interviews with 80%+ pass rate
- [ ] 5+ mock system design interviews with positive feedback
- [ ] 10+ behavioral stories polished and practiced
- [ ] Able to discuss AI safety thoughtfully

### Compensation Target
- [ ] Target: $550K-$700K total compensation
- [ ] Multiple competing offers for leverage
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
2. Review `plans/master-plan.md` for 12-week overview
3. Check `plans/weekly-plans/week-01.md` for immediate actions
4. Use `@coding-coach` to begin first practice session
5. Update `memory/journey-log.md` after each session
