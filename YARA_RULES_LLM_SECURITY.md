# Automatically Generate YARA Rules for LLM Security at Scale

**Source:** [DeconvoluteAI Blog](https://deconvoluteai.com/blog/yara-rules-llm-prompt-security)
**Published:** Monday, January 26, 2026
**Author:** David Kirchhoff

## Abstract
This post introduces `yara-gen`, an open source CLI tool that automatically generates high-precision YARA rules for detecting prompt injections and jailbreaks in large language model systems. Given one dataset of adversarial prompts and one control dataset of benign text, yara-gen identifies statistically distinctive attack patterns and produces a compact, deployable ruleset optimized for runtime efficiency and low false positives.

## Introduction
Detecting prompt injections and jailbreaks at scale is a practical security problem. While YARA rules are a proven technique for malware detection, applying them to natural language is difficult because prompt attacks are highly variable.

To address this, `yara-gen` generates YARA rules directly from data. Getting started:

```bash
pip install yara-gen
```

## The Algorithm: Differential N-Gram Analysis
The tool transforms raw text datasets into YARA rules via four steps:

### 1. Candidate Generation
Extracts n-grams (3-10 words) from the adversarial dataset to balance specificity and generality.

### 2. Differential Scoring
Scores phrases based on their relative prevalence in adversarial vs. benign text.
`Score = P(Attack) - λ * P(Benign)`

### 3. Subsumption
Removes redundant, shorter phrases that are already captured by longer, more specific ones to keep the ruleset compact.

### 4. Rule Selection and Optimization
Uses a Greedy Set Cover strategy to reduce thousands of candidates to ~50 YARA rules that maximize coverage while keeping evaluation fast.

## Conclusion
`yara-gen` provides a deterministic, explainable defense for production LLM applications without relying on probabilistic model inference.

## References
[1] Schulhoff et al. "Ignore This Title and HackAPrompt" (arXiv:2311.16119)
[2] Liu et al. "Jailbreaking ChatGPT via Prompt Engineering" (arXiv:2305.13860)
[3] Gakh & Bahsi "Performance Evaluation of Early Detection Systems" (arXiv:2506.19109)
