# 🔑 plain-to-meta (Meta-Knowledge Prompt Translator v2.0)

> **Stop using vague colloquial prompts.** Translate everyday plain-language pain points into high-density **Domain Terms & Meta-Knowledge Keys** (`Ablation Study`, `Progressive Disclosure`, `Monte Carlo Simulation`, `Pyramid Principle`, `Silhouette Rule`, etc.) and compile them via **Tri-Track Architecture (System / User / Visual)** to unlock expert-level AI outputs.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Agent Skills Standard](https://img.shields.io/badge/Standard-Agent%20Skills-blue.svg)](./SKILL.md)
[![Lexicon Keys](https://img.shields.io/badge/Meta--Knowledge%20Keys-39%2B%20Verified-brightgreen.svg)](./references/)
[![Version](https://img.shields.io/badge/Version-v2.0%20Tri--Track-purple.svg)](./SKILL.md)

[简体中文文档](./README.md) | [Before vs. After Showcase](./examples/before-after-showcase.md) | [Contributing Guide](./CONTRIBUTING.md)

<p align="center">
  <img src="./assets/hero-banner.svg" alt="Meta-Knowledge Prompt Translator Architecture Banner" width="100%" />
</p>

<p align="center">
  <img src="./assets/ui-progressive-disclosure-comparison.svg" alt="UI Progressive Disclosure Comparison" width="100%" />
</p>

---

## 💡 Why Plain Language ("Natural Expression") Fails in Production

Most users struggle to get production-grade output from AI not because the model lacks capability, but because **plain, conversational language fails to activate the model's latent expert consensus**:

* **Colloquial Prompt**: *"Build me a video generation dashboard web app with all settings."* $\rightarrow$ AI dumps **58 buttons and inputs onto a single cluttered screen**.
* **With Meta-Knowledge Key**: Injecting **`Progressive Disclosure`** + **`Hick's Law`** $\rightarrow$ AI immediately limits the primary screen to **16 core controls** (reducing visual clutter by 69%) and tucks advanced parameters into on-demand drawers.

---

## 🚀 What's New in v2.0 (Inspired by Prompt Optimizer & LangGPT)

1. **Tri-Track Compilation (`System` / `User` / `Visual`)**: Automatically routes between reusable LangGPT System Personas, concise one-shot User Instructions, and 5-Layer Visual/Video Director Prompts (for Midjourney, Flux, Sora, Kling).
2. **Evidence Isolation & `{{Variable}}` Assetization**: Prevents meta-instruction confusion via `<prompt_evidence>` sandboxing, preserves `{{variable_name}}` placeholders with 100% fidelity, and extracts reusable parameter slots.
3. **6D Diagnostic Scorecard & Surgical Delta Iteration**: Scores prompts across 6 orthogonal dimensions (including *Meta-Knowledge Density*) and applies surgical patches during multi-round iteration without breaking previously validated rules.
4. **6 Domain Volumes with 39+ Verified Keys**: Covering UI/UX (`01`), Visual/Animation (`02`), Business/Copywriting (`03`), Data/Probability (`04`), Software/Level Design (`05`), and Prompt Engineering/Evaluation (`06`).

---

## 📦 Installation across Ecosystems

### 1. Antigravity / Claude Code (Native Agent Skill)

```bash
# Antigravity Global Skill
git clone https://github.com/Yun-BaiBai/plain-to-meta.git ~/.gemini/config/skills/plain-to-meta

# Claude Code Global Skill
git clone https://github.com/Yun-BaiBai/plain-to-meta.git ~/.claude/skills/plain-to-meta
```

### 2. Cursor / Windsurf

Copy [`adapters/cursor-windsurf-rules.mdc`](./adapters/cursor-windsurf-rules.mdc) into your workspace's `.cursor/rules/` directory.

### 3. ChatGPT / Claude Web / DeepSeek / Custom GPTs

Copy the system prompt from [`adapters/standalone-system-prompt.md`](./adapters/standalone-system-prompt.md) directly into your Custom Instructions or Project Instructions.

### 4. Prompt Optimizer (`linshenkx/prompt-optimizer`) Custom Template

Import [`adapters/prompt-optimizer-template.json`](./adapters/prompt-optimizer-template.json) into Prompt Optimizer to supercharge it with `plain-to-meta`'s 39+ domain keys.

---

## 📄 License

Released under the [MIT License](./LICENSE).
