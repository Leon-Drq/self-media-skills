---
name: x-article-personal-observation
description: Rewrite Chinese AI/tech drafts, WeChat/AI Pioneer articles, YouTube interview summaries, podcast notes, or source material into English X Articles with a personal-observation voice. Use when the user asks for an English X article, X Articles longform, personal observation, "英文 X", "发 X 的 article", or to turn a Chinese article into an English post for X.
---

# X Article Personal Observation

Turn a Chinese AI/tech draft or source package into a polished English X Article: personal, analytical, high-signal, and easy to read on X.

## Core Output

- Write in Markdown.
- Default length: 900-1600 English words unless the user asks otherwise.
- Save under the workspace draft folder when working in `~/Documents/公众号`:
  - `草稿/<English-Slug>-X-Article.md`
- Do not include WeChat banners, AI Pioneer fixed banners, Chinese captions, or公众号 publishing metadata.
- Do not publish to X unless the user explicitly asks and a posting tool/session is available.

## Workflow

1. Read the source article or notes fully.
   - If a file path is given, read it before writing.
   - If only a topic/source URL is given, gather enough source material first.
   - If the topic is current, verify fresh facts before making factual claims.

2. Extract one central thesis.
   - Prefer a sharp business or technology mechanism, not a broad summary.
   - Convert "who fought whom" into "what market mechanism is changing."
   - Keep the article about one big idea.

3. Respect user-provided title and opening.
   - If the user gives a Chinese title, translate it into natural, clickable English rather than literal English.
   - Example: `为什么大多数企业接了ai反而亏钱了` -> `Why Most Companies Lose Money After Plugging in AI`
   - If the user gives an opening angle, use it directly in English.
   - Example: `我周末看了 Palantir CEO Alex Karp 的访谈...` -> `Over the weekend, I watched Palantir CEO Alex Karp's interview...`

4. Rewrite, do not translate sentence by sentence.
   - Remove WeChat-style signposting, slogans, and section padding.
   - Rebuild the article for English readers: shorter paragraphs, clearer logic, fewer abstractions.
   - Preserve facts, sources, and the core argument.

5. Finish with references when useful.
   - Put source links at the bottom under `References:`.
   - Do not overload the body with citations.
   - Avoid quoting long passages from transcripts or articles.

## Recommended Structure

Use this structure by default:

```markdown
# <English Title>

<First-person opening scene or source encounter.>

<Immediate tension: what seemed obvious, and what turned out to be more important.>

<Core thesis in plain English.>

## <Section 1: The surface conflict>

## <Section 2: The mechanism>

## <Section 3: Why companies/users misread it>

## <Section 4: What changes next>

## The real takeaway

<Concise closing judgment.>

References:

- <source>
```

Keep sections flexible. Use 3-6 sections depending on complexity.

## Voice

Write like a thoughtful operator or investor sharing a weekend observation, not a media outlet.

Prefer:

- `Over the weekend, I watched...`
- `The problem is not AI. The problem is how companies buy AI.`
- `Tokens are not outcomes. Usage is not ROI.`
- `On paper, this looks like progress. In reality, it can become an expensive illusion.`
- `The dashboard looks more advanced. The P&L does not move.`
- `The next phase will not be judged by how much AI companies consume, but by what they get back.`

Avoid:

- `In this article, I will analyze...`
- `This title is catchy because...`
- `The interesting part is...` when it exposes writing mechanics instead of the event.
- `Let's dive in.`
- `Here is why this matters.`
- `Thread below`, hashtags, emoji, engagement bait, or "hot take" language.
- WeChat phrases such as "真正值得看的是", "更深层来看", "下面我们来分析", "这篇文章要讲的是".

## Conflict And Hook

Build conflict into the article, but keep it credible.

Good conflict layers:

- Person/company conflict: `Palantir vs OpenAI/Anthropic`
- Economic conflict: `AI usage rising while ROI remains unclear`
- Ownership conflict: `who owns data, workflows, IP, model weights, and alpha`
- Budget conflict: `first AI budget bought experimentation; second AI budget will demand outcomes`
- Reader conflict: `the company looks more AI-native, but the P&L does not move`

Do not stop at drama. Upgrade the drama into a mechanism.

Bad:

```text
Palantir blasted OpenAI. This is a big fight.
```

Better:

```text
The conflict is not simply Palantir versus OpenAI.
It is between two ways of buying enterprise AI: paying for intelligence as usage, or building AI into a controlled business system that produces measurable outcomes.
```

## English Style Rules

- Use short paragraphs. One sentence paragraphs are allowed when they create rhythm.
- Use simple verbs: buy, own, control, lose, compound, prove, switch, audit.
- Explain Chinese/industry concepts in plain English.
- Use `AI`, not `ai`.
- Use `X Articles` or `X Article`, not `Twitter article` unless the source context requires it.
- Avoid overusing em dashes; prefer periods and colons.
- Do not preserve Chinese section numbering like `01`, `02` unless the user asks.
- Keep claims proportional. Avoid `destroyed`, `killed`, `changed everything`, `the end of`.

## Title Rules

Use a clear English title with tension, usually 6-12 words.

Good patterns:

- `Why Most Companies Lose Money After Plugging in AI`
- `The AI Bill Is Rising. The Business Is Not.`
- `Enterprise AI Is Entering Its Second Budget Cycle`
- `Tokens Are Not Outcomes`
- `The Real Fight Behind Palantir's Attack on OpenAI`

Avoid:

- Literal translations that sound Chinese in English.
- Vague titles like `A Deep Analysis of Enterprise AI`.
- Clickbait that the body cannot prove.

## Final Checklist

Before finishing:

- The opening uses the user's requested first-person angle if provided.
- The first 8-12 lines contain a clear tension, not background filler.
- The article has one thesis.
- The body is not a sentence-by-sentence translation.
- No WeChat banners or Chinese publishing artifacts remain.
- No "writer backstage" phrasing remains: title discussion, article-planning language, or "this piece will explain."
- References are included when source claims depend on external material.
- The final response reports the Markdown path and approximate word count.
