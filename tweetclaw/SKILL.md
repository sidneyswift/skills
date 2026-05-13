---
name: tweetclaw
description: X/Twitter automation with @xquik/tweetclaw for OpenClaw. Use when users want to search tweets, search tweet replies, post approved tweets or replies, export followers, look up users, handle media, monitor accounts, manage webhooks, send DMs, or run giveaway draws.
---

# TweetClaw

Use TweetClaw when the user wants X/Twitter automation from OpenClaw through the `@xquik/tweetclaw` plugin.

## Setup

Read `~/.config/tweetclaw/.env`. If it does not exist, ask:

- "What default read limit should I use for searches and exports?" Suggested: `50`
- "Should all visible X actions require a final approval prompt?" Suggested: `yes`

Write:

```bash
SETUP_COMPLETE=true
DEFAULT_READ_LIMIT=50
REQUIRE_APPROVAL_FOR_VISIBLE_ACTIONS=yes
```

Install the OpenClaw plugin:

```bash
openclaw plugins install @xquik/tweetclaw
```

Useful links:

- GitHub: https://github.com/Xquik-dev/tweetclaw
- npm: https://www.npmjs.com/package/@xquik/tweetclaw
- ClawHub: https://clawhub.ai/kriptoburak/xquik-tweetclaw

## Workflow

1. Use `explore` first to find the matching endpoint, parameters, response shape, and cost.
2. Use `tweetclaw` only for a catalog-listed endpoint.
3. Apply `DEFAULT_READ_LIMIT` to searches, exports, timelines, media reads, and extraction jobs unless the user asks for a specific limit.
4. Before posting, replying, deleting, liking, retweeting, following, unfollowing, sending DMs, uploading media, creating monitors, managing webhooks, or running giveaway draws, summarize the exact action and wait for approval.
5. For public tweets or replies, show the final text and media list before calling `tweetclaw`.
6. Never ask the user to paste private setup values into chat. Point them to the TweetClaw README for local configuration.

## Use Cases

- Search tweets about a topic, account, product, or competitor
- Search tweet replies to understand objections, bugs, or giveaway entries
- Post approved tweets or post approved tweet replies
- Export followers, following, verified followers, list members, and people search results
- Look up users, tweets, threads, favoriters, retweeters, communities, and X Articles
- Upload media, download tweet media, and create gallery links
- Monitor accounts for new tweets, replies, quotes, and retweets
- Manage webhooks and review monitor events
- Send direct messages after explicit approval
- Run giveaway draws from tweet replies

## Examples

- "Search tweets about AI agents from the last 24 hours"
- "Find replies to this tweet and group the common questions"
- "Export up to 500 followers of @example"
- "Draft a reply to this tweet and wait for my approval before posting"
- "Monitor @example for new tweets and replies"
- "Pick 3 giveaway winners from replies to this tweet"

## Verify

After install or update:

```bash
openclaw plugins inspect tweetclaw --runtime
openclaw skills info tweetclaw
```
