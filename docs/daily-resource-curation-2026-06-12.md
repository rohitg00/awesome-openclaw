# Daily resource curation, 2026-06-12

This log records the public-source checks behind the 2026-06-12 Awesome OpenClaw maintenance update.

## Summary

- Open contributor PRs reviewed: 3.
- Contributor PRs merged before new cleanup: 1.
- Existing maintainer PRs merged before new work: 1.
- Verified resources added to `README.md`: 50.
- Verified resources also added to `docs/website/directory.html`: 10.
- Primary source type: npm registry package metadata, package README content, and public package pages.
- Stopping reason: the run stopped at the daily target after 50 high-confidence candidates. Additional public packages remain, but wallet, payment, trading, adult/persona, anti-detection, risky account automation, placeholder, and thin metadata-only candidates were deferred for separate review.

## Accepted candidates

| Candidate | Type | Public evidence | Placement |
|-----------|------|-----------------|-----------|
| `@agent-vm/openclaw-agent-vm-plugin` | deployment template | npm metadata describes an OpenClaw sandbox backend delegating execution to a Gondolin-managed VM. | README |
| `@agentclub/openclaw-adapter` | companion app | npm README documents an adapter for local OpenClaw Gateway agents. | README |
| `@akalsey/openclaw-gatepass` | security tool | npm README documents a Gatepass secrets-management plugin for OpenClaw. | README |
| `@ama2/openclaw-channel` | plugin | npm README documents a self-hosted AMA2 OpenClaw channel plugin. | README |
| `@ambient-os/openclaw-channel` | plugin | npm metadata describes an Ambient iOS channel plugin for OpenClaw messaging, pairing, and push notifications. | README |
| `@aporthq/openclaw-aport` | security tool | npm README documents deterministic pre-action authorization for OpenClaw tool calls. | README, directory |
| `@archermindim/openclaw-channel` | plugin | npm README documents an OpenIM channel plugin for OpenClaw Gateway. | README |
| `@arinova-ai/openclaw-arinova-ai` | plugin | npm metadata describes Arinova Chat channel and virtual-office status events for OpenClaw. | README |
| `@artflo-ai/artflo-openclaw-plugin` | plugin | npm README documents a plugin that connects OpenClaw to Artflo canvas WebSocket runtime. | README |
| `@athenafleet/bridge` | companion app | npm README documents a CLI bridge from local OpenClaw Gateway to an Athena dashboard. | README |
| `@attest-protocol/openclaw-attest` | monitoring dashboard | npm README documents an audit-trail plugin for OpenClaw agent actions. | README |
| `@awareness-sdk/openclaw-memory` | plugin | npm README documents cross-session memory recall for OpenClaw. | README, directory |
| `@axonflow/openclaw` | security tool | npm README documents policy enforcement, PII scanning, approval gates, and audit trails for OpenClaw agents. | README, directory |
| `@beeos-ai/claw` | companion app | npm README documents a BeeOS bridge for OpenClaw Gateway file transfer and observability. | README |
| `@botschat/openclaw-plugin` | plugin | npm metadata describes a BotsChat channel plugin for OpenClaw. | README |
| `@bouncer-protocol/openclaw` | plugin | npm README documents a WebSocket channel plugin for Bouncer Protocol negotiation workflows in OpenClaw. | README |
| `@brightdeck/openclaw-deck` | workflow automation | npm README documents OpenClaw tools for managing Brightdeck presentations. | README |
| `@cfio/cohort-sync` | monitoring dashboard | npm README documents telemetry and session sync from OpenClaw to Cohort dashboards. | README |
| `@chatu-ai/webhub` | developer tool | npm README documents a channel SDK for building custom OpenClaw channel plugins. | README |
| `@clackhq/openclaw-plugin` | plugin | npm README documents a Clack workspace channel plugin for OpenClaw collaboration. | README |
| `@claw-fact-bus/openclaw-plugin` | plugin | npm metadata and package page describe a Claw Fact Bus integration for OpenClaw. | README |
| `@claw_chat/clawchat-proxy` | companion app | npm metadata describes an SSE and POST proxy server for OpenClaw Gateway. | README |
| `@clawboo/gateway-client` | developer tool | npm metadata describes a typed WebSocket client for OpenClaw Gateway RPC and events. | README |
| `@clawboo/gateway-proxy` | developer tool | npm metadata describes a same-origin WebSocket proxy for OpenClaw Gateway with server-side auth injection. | README |
| `@clawdb/openclaw` | plugin | npm README documents ClawDB-backed memory retrieval, persistence, branching, sync, and reflection for OpenClaw. | README, directory |
| `@clawmem-ai/clawmem` | backup/restore tool | npm README documents GitHub-native transcript mirroring, recall, and memory maintenance for OpenClaw. | README |
| `@clawnify/agent-control-ui` | companion app | npm README documents a control UI for OpenClaw agent sessions. | README |
| `@clawos-dev/openclaw-extensions` | developer tool | npm metadata describes a runtime and registry for user-defined ClawOS extensions inside OpenClaw. | README |
| `@compresh/openclaw-hook` | plugin | npm README documents an OpenClaw Plugin SDK hook for per-turn context compression. | README |
| `@consensus-tools/openclaw` | plugin | npm README documents an adapter from consensus-tools into OpenClaw plugins. | README |
| `@context-security/openclaw-email-guard-plugin` | security tool | npm README documents policy checks for OpenClaw email composition and sending. | README, directory |
| `@controluiclaw/sdk` | developer tool | npm README documents a TypeScript SDK for OpenClaw Gateway WebSocket APIs. | README |
| `@corev/openclaw-plugin` | plugin | npm metadata describes Corev versioned configuration operations exposed as OpenClaw tools. | README |
| `@cozeloop/openclaw-cozeloop-trace` | monitoring dashboard | npm metadata describes OpenTelemetry trace reporting from OpenClaw to CozeLoop. | README |
| `openclaw-agent-builder` | companion app | npm README documents a wizard for creating and deploying OpenClaw agents and teams. | README, directory |
| `openclaw-agent-runtime-contracts` | developer tool | npm README documents shared runtime contracts for OpenClaw planner, todo, and session-state integrations. | README |
| `openclaw-agent-sdk` | developer tool | npm README documents session management, tool registration, and streaming integrations for OpenClaw Hub. | README |
| `openclaw-agent-wake-protocol` | workflow automation | npm README documents lifecycle registration and wake-state tracking for OpenClaw multi-agent systems. | README |
| `openclaw-aegis` | monitoring dashboard | npm README documents a self-healing sidecar daemon for OpenClaw Gateway process recovery. | README, directory |
| `openclaw-code-agent` | workflow automation | npm README documents managed background-process orchestration for coding-agent sessions from OpenClaw. | README |
| `openclaw-cost-optimizer` | workflow automation | npm README documents an OpenClaw skill for auditing configuration cost-optimization opportunities. | README |
| `openclaw-daemon` | companion app | npm README documents a persistent background daemon for OpenClaw Gateway management. | README |
| `openclaw-engram` | plugin | npm README documents a persistent-memory server connection for OpenClaw. | README |
| `openclaw-gateway-chat` | companion app | npm README documents a React chat SDK for OpenClaw Gateway HTTP, SSE, and WebSocket chat surfaces. | README, directory |
| `openclaw-keeper` | monitoring dashboard | npm README documents a health monitor and auto-recovery daemon for OpenClaw Gateway. | README |
| `openclaw-mcp-tools` | plugin | npm README documents a bridge from MCP server tools into native OpenClaw tools. | README |
| `openclaw-plugin-memory-pro` | plugin | npm README documents an enhanced memory plugin with vector storage, knowledge graph, and document workflows. | README |
| `openclaw-quest` | monitoring dashboard | npm README documents an observability dashboard plugin for OpenClaw agent sessions. | README, directory |
| `openclaw-skill-boilerplate` | setup guide | npm README documents boilerplate for scaffolding, developing, and publishing OpenClaw skills. | README |
| `n8n-nodes-openclaw-chat` | workflow automation | npm README documents n8n nodes for OpenClaw Gateway chat, model, response, and tool APIs. | README, directory |

## Contributor PR triage

| PR | Classification | Decision | Reason |
|----|----------------|----------|--------|
| #186, OneClickClaw | resource-submission | merged | Public site documents OpenClaw managed VPS hosting, pricing, setup time, EU hosting, backups, updates, and supported channels. |
| #182, TWZRD Agent Intel | resource-submission | deferred | The source is public, but it is Solana and x402 payment oriented. Needs separate conservative security and payment-risk review before inclusion. |
| #99, XVARY Stock Research | resource-submission | deferred | The source is public and useful for Claude Code, but there is no clear OpenClaw-specific integration evidence and the PR adds a new top-level README section. |

## Deferred candidate classes

- Wallet, payment, trading, on-chain, and x402 packages were deferred for separate security review.
- Dating, adult/persona, selfie, and social-growth packages were skipped for safety and quality reasons.
- Browser anti-detection, scraping, and account-automation packages were skipped unless the official API-compliant OpenClaw use was clear.
- Placeholder packages, deprecated shims, and metadata-only packages with unclear setup evidence were skipped.
- Duplicate packages already present in README, directory, or use-case pages were skipped.
