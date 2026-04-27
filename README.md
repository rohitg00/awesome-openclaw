<p align="center">
  <a href="https://github.com/openclaw/openclaw">
    <picture>
      <source media="(prefers-color-scheme: light)" srcset="https://raw.githubusercontent.com/openclaw/openclaw/main/docs/assets/openclaw-logo-text-dark.svg">
      <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/openclaw/openclaw/main/docs/assets/openclaw-logo-text.svg">
      <img alt="OpenClaw" src="https://raw.githubusercontent.com/openclaw/openclaw/main/docs/assets/openclaw-logo-text.svg" width="600">
    </picture>
  </a>
</p>

<h1 align="center">Awesome OpenClaw</h1>

<p align="center">
  <a href="https://github.com/openclaw/openclaw/stargazers"><img src="https://img.shields.io/github/stars/openclaw/openclaw?style=flat&logo=github&label=Stars&color=gold" alt="Stars"></a>
  <a href="https://github.com/openclaw/openclaw/releases"><img src="https://img.shields.io/github/v/release/openclaw/openclaw?include_prereleases&label=Release&color=orange" alt="Release"></a>
  <a href="https://github.com/openclaw/openclaw/blob/main/LICENSE"><img src="https://img.shields.io/github/license/openclaw/openclaw?color=blue" alt="License"></a>
  <a href="https://discord.gg/clawd"><img src="https://img.shields.io/badge/Discord-Claw%20Crew-5865F2?logo=discord&logoColor=white" alt="Discord"></a>
  <br>
  <em>A curated, source-backed index for OpenClaw resources, docs, plugins, ecosystem projects, and community learning.</em>
</p>

---

**OpenClaw** is a self-hosted personal AI assistant and multi-channel gateway. You run one Gateway on your own machine or server; it connects chat apps, WebChat, Control UI, companion apps, mobile nodes, plugins, model providers, tools, sessions, and multi-agent routing into one always-available assistant.

This repository is a community-maintained resource index for OpenClaw. It is not the official OpenClaw documentation. For installation, configuration, security, and release details, prefer the official sources linked below.

## Contents

- [Official sources](#official-sources)
- [What OpenClaw is today](#what-openclaw-is-today)
- [Quick start](#quick-start)
- [Architecture map](#architecture-map)
- [Core capabilities](#core-capabilities)
- [Plugins and integrations](#plugins-and-integrations)
- [Ecosystem resources](#ecosystem-resources)
- [Learning resources](#learning-resources)
- [Security and operations](#security-and-operations)
- [Recent release themes](#recent-release-themes)
- [Community and contribution](#community-and-contribution)
- [Archived material](#archived-material)

## Official sources

| Resource | Link | Notes |
|---|---|---|
| OpenClaw website | [openclaw.ai](https://openclaw.ai/) | Product homepage, quick start, integrations, showcase, and blog. |
| Official repo | [github.com/openclaw/openclaw](https://github.com/openclaw/openclaw) | Source code, issues, releases, changelog, and contribution workflow. |
| Official docs | [docs.openclaw.ai](https://docs.openclaw.ai/) | Installation, channels, plugins, Gateway, Control UI, nodes, and concepts. |
| Releases | [GitHub releases](https://github.com/openclaw/openclaw/releases) | Stable and beta release notes. |
| Integrations | [openclaw.ai/integrations](https://openclaw.ai/integrations) | Current public integration list. |
| Showcase | [openclaw.ai/showcase](https://openclaw.ai/showcase) | Examples of what people are building. |
| Discord | [discord.gg/clawd](https://discord.gg/clawd) | Community discussion. |

## What OpenClaw is today

OpenClaw is best understood as two things together:

1. **A personal assistant you run yourself.** It can respond from the channels and devices you already use.
2. **A Gateway/control plane.** The Gateway connects channels, plugins, sessions, routing, tools, model providers, and surfaces.

The current official docs emphasize:

- self-hosting and user-controlled data;
- one Gateway process that connects built-in channels and plugin channels;
- WebChat, Control UI, companion apps, and mobile/headless nodes;
- multi-agent routing with isolated sessions, workspaces, and auth scopes;
- plugin-based capabilities for channels, model providers, speech, media, browser, search, memory, observability, and automation.

## Quick start

Use the official docs as the source of truth. Current upstream guidance is:

```bash
npm install -g openclaw@latest
openclaw onboard --install-daemon
openclaw dashboard
```

Runtime guidance from current docs:

- Node 24 is recommended.
- Node 22 LTS `22.14+` is also supported.
- Docker is available, but it is not the only or primary path.

Useful docs:

- [Getting started](https://docs.openclaw.ai/start/getting-started)
- [Node setup](https://docs.openclaw.ai/install/node)
- [Updating](https://docs.openclaw.ai/install/updating)
- [Docker](https://docs.openclaw.ai/install/docker)

## Architecture map

| Layer | What it does | Useful docs |
|---|---|---|
| Gateway | Single source of truth for sessions, routing, channel connections, plugin loading, and HTTP/WebSocket surfaces. | [Docs home](https://docs.openclaw.ai/) |
| Channels | Connect chat apps and message surfaces such as Telegram, WhatsApp, Discord, Slack, Signal, iMessage, Matrix, Teams, Zalo, Feishu, and more. | [Channels](https://docs.openclaw.ai/channels) |
| Surfaces | WebChat, Control UI, companion app, mobile nodes, CLI, and chat apps. | [Control UI](https://docs.openclaw.ai/web/control-ui), [Nodes](https://docs.openclaw.ai/nodes) |
| Agents and routing | One or many isolated agents with separate workspaces, sessions, state, and channel accounts. | [Multi-agent](https://docs.openclaw.ai/concepts/multi-agent) |
| Plugins | Manifest-backed capability packages for providers, channels, tools, speech, media, memory, observability, and automation. | [Plugins](https://docs.openclaw.ai/tools/plugin) |
| Tools and capabilities | Browser, shell, files, web fetch/search, media understanding, image/video/music generation, diagnostics, and provider-specific tools. | [Tools](https://docs.openclaw.ai/tools) |

## Core capabilities

| Capability | Current direction |
|---|---|
| Multi-channel assistant | One assistant reachable from multiple chat apps and web/mobile surfaces. |
| Control UI | Browser-based dashboard for chat, configuration, sessions, nodes, access, and runtime status. |
| Multi-agent routing | Run multiple isolated agents, workspaces, and channel accounts through one Gateway. |
| Plugins | Current OpenClaw leans heavily on plugin manifests, plugin registry behavior, and capability surfaces. |
| Voice and TTS | Rapidly expanding TTS, speech, realtime voice, and voice-note support across providers and channels. |
| Browser automation | Safer browser automation, role snapshots, CDP readiness, tab handling, and browser doctor checks. |
| Observability | OpenTelemetry and Prometheus-oriented diagnostics for model calls, token usage, tools, delivery, context, memory pressure, and more. |
| Mobile and nodes | iOS/Android/headless nodes for media, device, and mobile-adjacent workflows. |

## Plugins and integrations

Current upstream contains more than 100 plugin/extension directories. Present the ecosystem by capability instead of as one flat list.

### Channels and messaging

Discord, Telegram, WhatsApp, Slack, Signal, iMessage, Matrix, Microsoft Teams, Google Chat, Feishu, Zalo, QQBot, Nostr, Twitch, IRC, Mattermost, Synology Chat, Nextcloud Talk, Tlon, LINE, and related channel/runtime packages.

Community additions at the end of this category:

- [feishu-inout](https://github.com/joe960913/feishu-inout) - Lark/Feishu docs, messaging, calendar, and bitable integration for AI coding agents.
- [Nylas OpenClaw plugin](https://www.npmjs.com/package/@nylas/openclaw-nylas-plugin) - email, calendar, and contacts tools across major providers.
- [discourse-openclaw](https://github.com/pranciskus/discourse-openclaw) - Discourse forum read/search/write integration.

### Model providers and agent runtimes

OpenAI, Anthropic, Anthropic Vertex, OpenRouter, Google, xAI, DeepSeek, Qwen, Groq, Mistral, Cerebras, Together, Fireworks, Ollama, LM Studio, vLLM, SGLang, LiteLLM, Amazon Bedrock, Hugging Face, Moonshot, Kimi Coding, Codex, OpenCode, Kilocode, Copilot Proxy, Vercel AI Gateway, Cloudflare AI Gateway, Venice, Z.ai, and others.

### Voice, TTS, speech, and calling

Azure Speech, ElevenLabs, Deepgram, Inworld, Local CLI TTS, Minimax, Volcengine, Xiaomi, Talk Voice, speech core packages, realtime voice/calling plugins, and provider-specific speech integrations.

Community additions at the end of this category:

- [clawr.ing](https://clawr.ing) - phone/calling surface for OpenClaw-style voice workflows.

### Search, web, browser, and extraction

Browser, Brave, DuckDuckGo, Exa, Firecrawl, Perplexity, SearxNG, Tavily, Web Readability, and web fetch/search capability surfaces.

### Memory and knowledge

Active memory, Memory Wiki, LanceDB-backed memory, Voyage embeddings, and related knowledge/memory tooling.

### Media generation and understanding

Comfy, Fal, Runway, Gradium, image generation core, video generation core, media understanding core, and provider-specific media tools.

Community additions at the end of this category:

- [prompt-to-asset](https://github.com/MohamedAbdallah-14/prompt-to-asset) - image-generation routing through one MCP-style interface.

### Observability, diagnostics, and QA

OpenTelemetry diagnostics, Prometheus diagnostics, QA Lab, QA Matrix, synthetic/test plugins, and token/trace-related diagnostics.

Community additions at the end of this category:

- [Manifest](https://github.com/mnfst/manifest) - local cost and model-usage observability for agents.

## Ecosystem resources

High-confidence resources to start with:

| Resource | Link | Why it belongs |
|---|---|---|
| Official integrations | [openclaw.ai/integrations](https://openclaw.ai/integrations) | Current public integration surface. |
| Official showcase | [openclaw.ai/showcase](https://openclaw.ai/showcase) | Real examples from users and builders. |
| Plugin docs | [docs.openclaw.ai/tools/plugin](https://docs.openclaw.ai/tools/plugin) | Canonical plugin model and install/config rules. |
| Multi-agent docs | [docs.openclaw.ai/concepts/multi-agent](https://docs.openclaw.ai/concepts/multi-agent) | Current routing and isolation model. |
| Control UI docs | [docs.openclaw.ai/web/control-ui](https://docs.openclaw.ai/web/control-ui) | Current browser dashboard surface. |
| Release notes | [github.com/openclaw/openclaw/releases](https://github.com/openclaw/openclaw/releases) | Current shipped behavior. |
| OpenClaw introduction | [openclaw.ai/blog/introducing-openclaw](https://openclaw.ai/blog/introducing-openclaw) | Naming/history and current project framing. |
| Peter Steinberger on OpenClaw and OpenAI | [steipete.me/posts/2026/openclaw](https://steipete.me/posts/2026/openclaw) | OpenClaw foundation/OpenAI context. |

Community additions, kept at the end instead of elevated above official sources:

| Resource | Link | Why it belongs |
|---|---|---|
| Onepilot | [onepilotapp.com](https://onepilotapp.com) | iOS/iPadOS companion app for deploying, running, and chatting with remote agents. |
| openclaw-mcp | [GitHub](https://github.com/freema/openclaw-mcp), [website](https://openclaw-mcp.cloud), [npm](https://www.npmjs.com/package/openclaw-mcp) | MCP bridge and packaging links for OpenClaw workflows. |
| Awesome OpenClaw Personas | [GitHub](https://github.com/TravisLeeeeee/awesome-openclaw-personas) | Persona package collection for OpenClaw-style agents. |
| Awesome OpenClaw Agents | [GitHub](https://github.com/mergisi/awesome-openclaw-agents) | Agent template collection for OpenClaw-style workflows. |
| TurboStarter OpenClaw Kit | [turbostarter.dev/openclaw](https://www.turbostarter.dev/openclaw) | Starter kit/boilerplate for OpenClaw-adjacent applications. |

## Learning resources

Use this section for stable, high-signal learning material. Prefer official docs, talks, and tutorials that are recently verified.

- [Getting started](https://docs.openclaw.ai/start/getting-started)
- [Plugins](https://docs.openclaw.ai/tools/plugin)
- [Control UI](https://docs.openclaw.ai/web/control-ui)
- [Multi-agent routing](https://docs.openclaw.ai/concepts/multi-agent)
- [Updating](https://docs.openclaw.ai/install/updating)
- [Release policy](https://docs.openclaw.ai/reference/RELEASING)

## Security and operations

OpenClaw is powerful because it can connect to real accounts, local machines, tools, browsers, files, and model providers. Treat setup like local infrastructure, not a toy chatbot.

Good defaults:

- keep OpenClaw updated;
- prefer official docs for install and upgrade paths;
- restrict channel access with allowlists or pairing;
- use strong current-generation models for safety-sensitive workflows;
- review plugin sources before installing unknown packages;
- keep API keys and chat tokens out of public configs;
- use Control UI and diagnostics to inspect runtime state;
- avoid publishing private workspace, memory, or export data.

Useful links:

- [Updating](https://docs.openclaw.ai/install/updating)
- [Plugins](https://docs.openclaw.ai/tools/plugin)
- [Release policy](https://docs.openclaw.ai/reference/RELEASING)

Community additions at the end of this category:

- [OneCLI](https://github.com/johnnyfish/onecli) - credential vault/gateway pattern for keeping raw secrets away from agents.
- [ShellWard](https://github.com/jnMetaCode/shellward) - bilingual prompt-injection and data-exfiltration guardrails.
- [leashed](https://github.com/dormstern/leashed) - policy engine, audit log, and kill switch patterns for agents.
- [SupaClaw](https://github.com/vincenzodomina/supaclaw) - Supabase-first deployment pattern for constrained OpenClaw-style agents.
- [unslop](https://github.com/MohamedAbdallah-14/unslop) - output-cleanup utility for removing common AI writing artifacts before publishing.

## Recent release themes

OpenClaw is shipping quickly. In the recent 2026.4 release line, the largest visible themes are:

- TTS, voice replies, speech providers, and chat-scoped auto-TTS controls;
- plugin registry, plugin install/update/repair metadata, and deterministic startup behavior;
- OpenTelemetry and Prometheus diagnostics;
- safer browser automation and Browser Doctor checks;
- Control UI features such as PWA/Web Push, realtime Talk, Model Auth status, and tool access;
- installer and update hardening across macOS, Linux, Windows, Docker, and daemon/service setups.

For exact shipped behavior, use [GitHub releases](https://github.com/openclaw/openclaw/releases) and the upstream changelog.

## Community and contribution

- Open issues and PRs: [openclaw/openclaw](https://github.com/openclaw/openclaw)
- Community chat: [discord.gg/clawd](https://discord.gg/clawd)
- Contribute to this index: see [CONTRIBUTING.md](CONTRIBUTING.md)

When adding resources here:

- prefer canonical sources;
- include dates for volatile claims;
- do not add unsourced superlatives;
- do not hard-code star counts, pricing, or benchmark claims unless they are dated and cited;
- move outdated but historically useful content to archive pages instead of deleting context silently.

## Archived material

The previous long-form README mixed current resources with old hosting comparisons, pricing tables, security numbers, growth claims, and early ecosystem experiments. It has been archived for historical reference:

- [Legacy README snapshot, 2026-04-27](docs/archive/README-legacy-2026-04-27.md)

Archived material should not be treated as current unless re-verified against official docs, releases, or source code.
