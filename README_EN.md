# 🔑 plain-to-meta (Meta-Knowledge & De-Roleplayed Execution Engine v3.1 · Adaptive Slim Edition)

> **Stop using vague colloquial prompts—and stop telling AI "You are an expert in X".** `plain-to-meta` v3.1 translates everyday pain points into **42+ high-density Meta-Knowledge Keys**, enforces the **Orient $\rightarrow$ Borrow $\rightarrow$ Adaptive Ground & Falsify** execution workflow, and cuts output token overhead by **~40%** via **Adaptive Complexity Gating** and **Zero Double-Tax Output**.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Agent Skills Standard](https://img.shields.io/badge/Standard-Agent%20Skills-blue.svg)](./SKILL.md)
[![Lexicon Keys](https://img.shields.io/badge/Meta--Knowledge%20Keys-42%2B%20Verified-brightgreen.svg)](./references/)
[![Version](https://img.shields.io/badge/Version-v3.1%20Adaptive--Slim-purple.svg)](./SKILL.md)

[简体中文文档](./README.md) | [Before vs. After Showcase (7 Cases)](./examples/before-after-showcase.md) | [Contributing Guide](./CONTRIBUTING.md)

<p align="center">
  <img src="./assets/hero-banner.svg" alt="Meta-Knowledge Prompt Translator Architecture Banner" width="100%" />
</p>

<p align="center">
  <img src="./assets/ui-progressive-disclosure-comparison.svg" alt="UI Progressive Disclosure Comparison" width="100%" />
</p>

---

## 💡 The Twin Laws & Adaptive Gating of `plain-to-meta` v3.1

1. **Law 1: Break the "Plain Language" Myth (Activate Meta-Knowledge Keys)**
   - Plain language fails to trigger the LLM's latent expert consensus. Injecting a named domain methodology (`Progressive Disclosure`, `Monte Carlo Simulation`, `Ablation Study`, `Pyramid Principle`, `Silhouette Rule`) unlocks decades of battle-tested engineering frameworks in a single token cluster.
2. **Law 2: Break the "You Are an Expert" Myth (Orient $\rightarrow$ Borrow $\rightarrow$ Adaptive Ground)**
   - Telling AI *"You are a world-class expert"* often just triggers **Tone Cosplay**—the AI uses fancier buzzwords while keeping the exact same lazy workflow. Instead, v3.1 enforces three concrete operational steps:
     - **🧭 1. Orient (Reframe & Find Missing Work)**: State the ultimate decision goal and hard constraints; ask the AI to identify omitted prerequisite steps and reorganize the workflow before executing.
     - **🔑 2. Borrow (Cross-Disciplinary Action Injection)**: Borrow actionable methods from adjacent fields (e.g., applying Project Management's *Critical Path Method* and Risk Engineering's *Contingency Switching* to travel planning) and **bake the changes directly into the deliverable**—no hollow advice or multiple "expert hats".
     - **⚖️ 3. Adaptive Complexity Gating (-40% Output Token Slimming)**:
       - **Creative / UI / Code / Visual Tasks**: Keeps prompts lean (`Orient + Borrow + Negative Redlines`), automatically skipping heavy archival verification so model attention stays 100% focused on code and aesthetics.
       - **Research / Strategy / Audit / Fact-Checking Tasks**: Automatically activates **Primary Source Grounding**, **Popperian Falsification (disconfirming evidence)**, and a dedicated **Unverified Audit Log**.

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

Import [`adapters/prompt-optimizer-template.json`](./adapters/prompt-optimizer-template.json) into Prompt Optimizer to equip it with our v3.0 engine.

---

## 📄 License

Released under the [MIT License](./LICENSE).
