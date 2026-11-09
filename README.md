# 🔑 Meta-Knowledge Prompt Translator

> **Stop using vague colloquial prompts.** Translate everyday plain-language pain points into high-density **Domain Terms & Meta-Knowledge Keys** (`Ablation Study`, `Progressive Disclosure`, `Monte Carlo Simulation`, `Pyramid Principle`, `Silhouette Rule`, etc.) to unlock expert-level AI outputs in 1 second.

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](./LICENSE)
[![Agent Skills Standard](https://img.shields.io/badge/Standard-Agent%20Skills-blue.svg)](./SKILL.md)
[![Lexicon Keys](https://img.shields.io/badge/Meta--Knowledge%20Keys-34%2B%20Verified-brightgreen.svg)](./references/)

[简体中文文档](./README_ZH.md) | [Before vs. After Showcase](./examples/before-after-showcase.md) | [Contributing Guide](./CONTRIBUTING.md)

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

A single domain-specific term (**Meta-Knowledge Key**) encapsulates decades of battle-tested methodologies. You don't need to know how to implement every detail from scratch—you just need the **key** that unlocks the right knowledge cluster inside the LLM.

---

## 🔥 Core 7 Benchmark Keys (Colloquial Pain Point $\rightarrow$ Expert Key)

| Colloquial Complaint | Activated Meta-Knowledge Key | Domain | What It Unlocks in the LLM |
| :--- | :--- | :--- | :--- |
| *"I stuffed 35 rules into my prompt and now the AI output is a mess"* | **Ablation Study** | ML / Experimental Science | Leave-one-out variable testing to prune redundant/conflicting rules down to $\le 10$ orthogonal principles |
| *"I gave the AI all team stats and asked who will win, but it just hedges"* | **Monte Carlo Simulation** | Statistics / Physics | Builds a probabilistic baseline and runs 10,000+ stochastic simulations to output exact win-rate distributions |
| *"AI-generated PPT slides look pretty but ramble with no clear takeaway"* | **Pyramid Principle & MECE** | Management Consulting | Answer-first (top-down in slides 1–3), Action Titles, and Mutually Exclusive / Collectively Exhaustive grouping |
| *"AI video storyboards/posters are super cluttered on mobile screens"* | **F-Shaped Pattern** | Eye-Tracking / Visual Design | Anchors high-value hooks at the top and left axes following Nielsen's eye-tracking trajectory, keeping $\ge 35\%$ negative space |
| *"AI product promo animations feel stiff and robotic like flat PPT slides"* | **Disney's 12 Principles of Animation** | Animation Industry | Injects *Squash & Stretch*, *Anticipation*, non-linear spring physics, and parabolic *Arcs* for tactile realism |
| *"When generating 4+ characters, they all have the same generic face/body"* | **Silhouette Rule & Shape Language** | Character Concept Art | Ensures instant recognition even as pure black silhouettes via contrasting Circle/Square/Triangle body proportions |
| *"Vibe-coded tools dump 60 inputs on the homepage, overwhelming users"* | **Progressive Disclosure** | UI/UX Interaction | Shows only the top 80% core workflow ($\le 18$ elements) up front; defers the remaining 20% to secondary drawers |

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

---

## 📄 License

Released under the [MIT License](./LICENSE).
