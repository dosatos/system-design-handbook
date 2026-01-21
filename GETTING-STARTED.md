# Getting Started

Welcome to your AI coaching ecosystem for Senior SWE interview preparation at top AI labs.

---

## Quick Start (15 minutes)

### Step 1: Understand the System

This ecosystem transforms Claude into a team of 6 expert coaches:

| Expert | Specialization | Invoke With |
|--------|---------------|-------------|
| Coding Coach | LeetCode, algorithms, Python | `@coding-coach` |
| System Design Architect | Distributed systems, ML infra | `@system-design-architect` |
| ML Specialist | Transformers, RLHF, inference | `@ml-specialist` |
| Behavioral Coach | STAR stories, culture fit | `@behavioral-coach` |
| Career Strategist | Resume, networking, applications | `@career-strategist` |
| Negotiation Advisor | Compensation, offers, scripts | `@negotiation-advisor` |

### Step 2: Review Your Plan

1. Open `plans/master-plan.md` for the 12-week overview
2. Open `plans/weekly-plans/week-01.md` for Day 1 activities
3. Understand the phase structure (Foundations → Intermediate → Company-Specific → Interview Mode)

### Step 3: Start Your Journey Log

Open `memory/journey-log.md` and add your first entry:

```markdown
## [Today's Date] - Journey Begins

**Duration**: Setup session

### Accomplished
- Reviewed the coaching ecosystem
- Set up tracking systems
- Committed to 12-week preparation

### Goals
- Target companies: Anthropic, OpenAI, DeepMind, xAI
- Target compensation: $500K-$700K
- Target start date: [Your date]

### Next Session
- Complete Week 1 Day 1 checklist
- Solve first 3 coding problems
```

### Step 4: Begin Your First Practice Session

Start a conversation with Claude and say:

```
@coding-coach I'm starting my interview preparation today.
Let's begin with Week 1 - Arrays and Two Pointers.
I'm ready to solve my first three problems.
```

---

## Directory Overview

```
system-design-handbook/
├── CLAUDE.md                    # Core project brief (Claude reads this)
├── GETTING-STARTED.md           # You are here
│
├── roadmap/                     # Technical preparation content (reference)
├── experts/                     # 6 expert persona definitions
├── plans/                       # Master plan and weekly schedules
├── progress/                    # Progress tracking files
├── memory/                      # Session logs and learnings
├── practice/                    # Coding problems and design practice
├── mock-interviews/             # Mock interview records
├── projects/                    # Portfolio projects
├── applications/                # Resume, networking, tracker
├── negotiations/                # Compensation research and scripts
├── targets/                     # Goals across all dimensions
├── templates/                   # Reusable templates
└── notes/                       # Quick references and cheat sheets
```

---

## How the System Works

### Memory Persistence
Claude reads `memory/journey-log.md` at the start of each session to understand your context. At the end of each session, update:
- `memory/journey-log.md` - Session summary
- `memory/learnings.md` - Key insights
- `memory/challenges.md` - Difficulties encountered
- `memory/wins.md` - Achievements

### Progress Tracking
Track your progress in:
- `progress/completed-topics.md` - What you've mastered
- `progress/statistics.md` - Numeric progress
- `practice/coding/problems-log.md` - Problems solved

### Expert Switching
Switch experts as needed:
- `@coding-coach` for algorithm practice
- `@system-design-architect` for system design
- `@ml-specialist` for ML deep dives
- `@behavioral-coach` for story preparation
- `@career-strategist` for applications
- `@negotiation-advisor` for offers

---

## First Week Checklist

### Day 1: Setup
- [ ] Read this Getting Started guide
- [ ] Review `CLAUDE.md` to understand the system
- [ ] Review `plans/master-plan.md` for overview
- [ ] Write first entry in `memory/journey-log.md`
- [ ] Complete baseline self-assessment
- [ ] Solve 3 Easy array problems with `@coding-coach`

### Day 2-5: Build Momentum
- [ ] Solve 4-5 problems per day
- [ ] Focus: Arrays → Two Pointers → Sliding Window
- [ ] Start DDIA Chapter 1
- [ ] Log each session in journey log

### Day 6: Deep Work
- [ ] Practice URL Shortener design with `@system-design-architect`
- [ ] Complete DDIA Chapter 2
- [ ] Tackle 2 Hard problems

### Day 7: Review
- [ ] Review week's problems
- [ ] Complete `templates/weekly-review.md`
- [ ] Update `progress/statistics.md`
- [ ] Plan Week 2

---

## Key Files to Know

| Purpose | File |
|---------|------|
| See your plan | `plans/master-plan.md` |
| Today's tasks | `plans/weekly-plans/week-XX.md` |
| Track progress | `progress/statistics.md` |
| Session continuity | `memory/journey-log.md` |
| Compensation data | `negotiations/compensation-research.md` |
| Problem solving template | `templates/problem-solving.md` |
| System design template | `templates/system-design.md` |
| STAR story template | `templates/behavioral-star.md` |

---

## Using Custom Commands

### `/status`
Get a progress summary:
```
/status
```

### `/expert [name]`
Switch to a specific expert:
```
/expert coding-coach
/expert system-design-architect
/expert ml-specialist
/expert behavioral-coach
/expert career-strategist
/expert negotiation-advisor
```

### `/review [type]`
Conduct a review:
```
/review daily
/review weekly
/review topic dynamic-programming
```

### `/mock [type]`
Run a mock interview:
```
/mock coding
/mock system-design
/mock behavioral
```

---

## Tips for Success

### Be Consistent
- Show up every day, even if just for 30 minutes
- 20-25 hours/week is the target
- Consistency beats intensity

### Use the System
- Update memory files after each session
- Track every problem you solve
- Complete weekly reviews

### Trust the Process
- Follow the 12-week structure
- Don't skip phases
- The compound effect works

### Ask for Help
- Use experts for their specialties
- Ask clarifying questions
- Be honest about struggles

---

## Troubleshooting

### Claude Doesn't Seem to Know the Project
- Make sure you're in the right directory
- Claude reads `CLAUDE.md` for context
- Remind Claude to check `memory/journey-log.md`

### Lost Track of Progress
- Check `progress/statistics.md`
- Review `progress/completed-topics.md`
- Look at recent entries in `memory/journey-log.md`

### Feeling Overwhelmed
- Focus on just today's tasks
- Talk to `@behavioral-coach` about stress
- Review `memory/wins.md` for motivation
- Adjust pace if needed (sustainable > fast)

### Not Sure What to Work On
- Check current week's plan
- Ask any expert for suggestions
- Default to coding practice (highest ROI)

---

## Sample First Session

```
You: @coding-coach I'm starting my interview prep journey.
     Let's begin with Week 1. What should we work on?

Claude: [Reads journey log, reviews Week 1 plan]
        Welcome! Let's start building your foundation.
        Today we'll tackle Arrays & Hashing - the most
        common patterns in interviews.

        Let's start with "Contains Duplicate" - an Easy
        problem that introduces hash set thinking.

        Here's the problem: [Problem description]

        Take a moment to understand it. What's your
        initial approach?

You: [Describe your thinking]

Claude: [Provides hints, guides to solution]
        ...

You: [At end of session]
     Great session! Let me update my logs.

Claude: Perfect! Here's what we accomplished today:
        - 3 problems solved (Contains Duplicate, Valid Anagram, Two Sum)
        - Learned: Hash set pattern for O(n) lookups
        - Struggled with: Optimizing space in Two Sum

        For your journey log:
        [Suggested entry]

        Tomorrow: Continue with Top K Frequent Elements
        and Group Anagrams.
```

---

## Ready to Begin?

1. Open `memory/journey-log.md`
2. Add your first entry
3. Start a session with `@coding-coach`
4. Solve your first problems
5. Update your logs

**Your journey to a Senior SWE role at a top AI lab starts now.**

Good luck!
