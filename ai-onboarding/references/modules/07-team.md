# Module 07: Team Rollout

Teaches managers how to bring what they've learned to their teams — without making the same mistakes onboarding tools usually make.

## When This Fires

- User manages others and asks about rolling out AI to their team
- User demonstrates personal competence (3+ modules completed, consistent usage)
- User says "how do I get my team doing this?" or "my reports should be using AI too"

## Prerequisites

The user should have completed at least Modules 01, 03, and 05. If they haven't gone through the journey themselves, they can't guide others through it. Don't shortcut this — a manager who hasn't experienced the learning curve will underestimate it for their team.

## The Core Insight

Rolling out AI to a team is not a training session. It's a culture change. The manager's job is not to teach prompting — it's to create an environment where experimentation is safe, wins are visible, and AI becomes part of how work gets done.

## The Approach

### 1. Assess Their Team

- How many direct reports?
- What's the team's general tech comfort?
- Has anyone already been using AI on their own?
- What's one workflow the whole team does that AI could improve?

### 2. The Cascade Pattern

Instead of training everyone at once:

1. **Pick one team member** who's curious or already experimenting
2. **Run them through the onboarding** (this skill — have them start with the opening question)
3. **Get them one win** on a real task the team recognizes
4. **Make the win visible** — share it in standup, Slack, wherever the team communicates
5. **Let demand pull** — other team members will ask "how did you do that?"
6. **Repeat** with the next person

This is slower than a group training session but dramatically more effective. Each person's "first workflow" is real work, not a demo.

### 3. Team Workspace Considerations

If the team wants shared context:

```
team-ai/
├── CLAUDE.md           # team-level context: tools, conventions, projects
├── shared-workflows/   # recipes the whole team uses
├── knowledge/          # shared learnings
└── members/
    ├── person-a/       # individual PROGRESS.md files
    └── person-b/
```

But don't start here. Start with individual workspaces. Merge into a team workspace only when there's real shared work that benefits from it.

### 4. The Manager's Ongoing Role

After rollout:

- **Weekly check-ins.** "What did you use AI for this week?" in standups or 1:1s. Normalize it.
- **Win sharing.** Slack channel or standup slot for "AI helped me do X." Social proof drives adoption.
- **Blocker resolution.** When someone hits a wall (connector blocked, IT issue), the manager unblocks it. That's their job.
- **Resist the urge to standardize too early.** Let people find their own workflows first. Standardize later when patterns emerge.

## Completion Criteria

- [x] Manager has a plan for which team member to start with
- [x] Manager understands the cascade pattern (one at a time, visible wins, pull not push)
- [x] At least one team member has started their own onboarding journey

## Anti-Patterns

- **Group training sessions.** Feel productive, rarely stick. People learn AI by doing their own work, not watching demos.
- **Mandating AI usage.** "Everyone must use AI for X by Friday" creates resentment. Let wins create demand.
- **Measuring adoption by volume.** "How many AI queries per week" is a vanity metric. "How many hours saved on real work" matters.
- **One-size-fits-all.** A sales rep and a designer need different first workflows. Don't template the learning path.
