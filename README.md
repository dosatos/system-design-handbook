# Interview Preparation Ecosystem

A comprehensive AI coaching ecosystem for Senior Software Engineer interview preparation at top AI labs: **Anthropic**, **OpenAI**, **DeepMind**, and **xAI**.

## Overview

This system transforms Claude into a team of 6 expert coaches that provide personalized guidance through a structured 12-week preparation program. It includes memory persistence across sessions, progress tracking, and comprehensive resources for every aspect of the interview process.

## Features

- **6 Expert Personas**: Specialized coaches for coding, system design, ML, behavioral, career strategy, and negotiation
- **12-Week Structured Plan**: Phased approach from foundations to interview mode
- **Memory Persistence**: Session logs and learnings carry across conversations
- **Progress Tracking**: Detailed tracking of problems solved, topics mastered, and milestones hit
- **Compensation Research**: Current market data for AI lab compensation (2025-2026)
- **Negotiation Scripts**: Ready-to-use scripts for offer discussions
- **Templates**: Reusable frameworks for problem-solving, system design, and behavioral stories

## Quick Start

1. **Read the getting started guide**:
   ```
   cat GETTING-STARTED.md
   ```

2. **Start your first session** with Claude:
   ```
   @coding-coach I'm starting my interview prep journey. Let's begin with Week 1.
   ```

3. **Track your progress** by updating `memory/journey-log.md` after each session

## Directory Structure

```
├── CLAUDE.md                    # Core project brief (Claude reads this)
├── GETTING-STARTED.md           # Quick start guide
├── roadmap/                     # Technical preparation content (31 files)
├── experts/                     # 6 expert persona definitions
├── plans/                       # Master plan + 12 weekly schedules
├── progress/                    # Progress tracking files
├── memory/                      # Session logs, learnings, challenges, wins
├── practice/                    # Coding problems and design practice
├── mock-interviews/             # Mock interview records
├── projects/                    # Portfolio project templates
├── applications/                # Resume, networking, application tracker
├── negotiations/                # Compensation research and scripts
├── targets/                     # Goals across all dimensions
└── templates/                   # Reusable templates
```

## Expert Personas

| Expert | Invoke With | Specialization |
|--------|-------------|----------------|
| Coding Coach | `@coding-coach` | LeetCode patterns, algorithms, Python |
| System Design Architect | `@system-design-architect` | Distributed systems, ML infrastructure |
| ML Specialist | `@ml-specialist` | Transformers, RLHF, inference optimization |
| Behavioral Coach | `@behavioral-coach` | STAR stories, culture fit, AI safety |
| Career Strategist | `@career-strategist` | Resume, networking, applications |
| Negotiation Advisor | `@negotiation-advisor` | Compensation, offers, negotiation |

## 12-Week Program

| Phase | Weeks | Focus |
|-------|-------|-------|
| Foundations | 1-3 | Core patterns, 75 problems, DDIA, Transformers |
| Intermediate | 4-6 | Graphs, DP, RLHF, ML systems |
| Company-Specific | 7-9 | Targeted prep, applications, mocks |
| Interview Mode | 10-12 | Active interviewing, negotiation |

## Target Outcomes

- **200+** coding problems solved
- **12+** system designs mastered
- **10+** mock interviews completed
- **$500K-$700K** target total compensation
- Offers from top AI labs

## Key Files

| Purpose | File |
|---------|------|
| Start here | `GETTING-STARTED.md` |
| 12-week overview | `plans/master-plan.md` |
| This week's tasks | `plans/weekly-plans/week-XX.md` |
| Track progress | `progress/statistics.md` |
| Session continuity | `memory/journey-log.md` |
| Compensation data | `negotiations/compensation-research.md` |

## Usage with Claude Code

This ecosystem is designed for use with [Claude Code](https://claude.ai/claude-code). Claude reads `CLAUDE.md` to understand the project context and acts as your coaching team.

### Custom Commands

- `/status` - Get current preparation status
- `/expert [name]` - Switch to specific expert
- `/review [daily|weekly]` - Conduct progress review
- `/mock [coding|system-design|behavioral]` - Run mock interview

## Contributing

This is a personal interview preparation system. Feel free to fork and adapt for your own use.

## License

MIT
