# AI System Designs - Quick Revision Notes 🚀

## Learning Goal

Different AI system designs ko samajhna:

1. Single LLM Features
2. Structured Workflows
3. Autonomous Agents

Aur kab kis approach ko use karna chahiye.

---

# 1. Single LLM Features

## Idea

Ek input do, ek output lo.

```text
Input → LLM → Output
```

No memory.
No planning.
No multi-step reasoning.

---

## Key Characteristics

* Stateless processing
* Direct input-output flow
* Predefined task execution

---

## Best Use Cases

Simple aur well-defined tasks:

* Text Summarization
* Translation
* Sentiment Analysis
* Information Extraction

---

## Advantages

### ✅ Fast

Sabse quick solution.

### ✅ Cheap

Minimum compute cost.

### ✅ Easy to Build

Almost no orchestration required.

---

## Limitations

### ❌ No Memory

Har request independent hoti hai.

### ❌ No Adaptability

Context ya changing situations handle nahi kar sakta.

---

## Example

```text
News Article
      ↓
     GPT
      ↓
 Summary
```

---

# 2. Structured Workflows

## Idea

Fixed sequence of predefined steps.

```text
Input
  ↓
Step 1
  ↓
Step 2
  ↓
Step 3
  ↓
Output
```

System exactly jaanta hai next kya karna hai.

---

## Key Characteristics

### Deterministic Execution

Same input → same output.

### Explicit Control Flow

Saare steps pehle se defined.

### Fixed Tool Usage

Tools predefined hote hain.

---

## Best Use Cases

* Multi-step business processes
* Compliance-heavy applications
* Repetitive tasks
* Audit requirements

---

## Examples

### Insurance Claims

```text
Claim
 ↓
Validation
 ↓
Verification
 ↓
Approval/Rejection
```

### Document Processing

```text
OCR
 ↓
Data Extraction
 ↓
Validation
 ↓
Database Storage
```

### Financial Transactions

### Healthcare Workflows

### Batch Report Generation

---

## Advantages

### ✅ Predictable

Behavior consistent hota hai.

### ✅ Easy Debugging

Step-by-step monitoring possible.

### ✅ Audit Friendly

Compliance requirements meet karta hai.

### ✅ Cost Efficient

No unnecessary reasoning.

---

## Limitations

### ❌ Rigid

Unexpected situations handle karna difficult.

### ❌ Development Overhead

Har exception manually code karna padta hai.

---

# 3. Autonomous Agents

## Idea

Goal do, solution path khud figure out kare.

Agent continuously:

```text
Plan → Act → Observe → Repeat
```

---

## Agent Loop

```text
Goal
 ↓
Plan
 ↓
Act
 ↓
Observe
 ↓
Re-plan
 ↓
Act
 ↓
Final Result
```

---

## Core Capabilities

### Dynamic Planning

Task ko smaller steps mein break karta hai.

### Context Awareness

Previous actions aur feedback remember karta hai.

### Tool Orchestration

Required tools dynamically choose karta hai.

---

## Best Use Cases

* Open-ended tasks
* Complex reasoning
* Research
* Personalized automation
* Dynamic environments

---

## Examples

### Research Agent

Information gather + analyze + summarize.

### Travel Planning Agent

Flights + Hotels + Budget + Preferences.

### AI Customer Support

Issue ke hisab se troubleshooting path decide karta hai.

### Coding Agent

Code likhna, test karna, debug karna.

---

## Advantages

### ✅ Highly Adaptable

New situations handle kar sakta hai.

### ✅ Dynamic Decision Making

Situation ke according strategy change kar sakta hai.

### ✅ Less Human Intervention

Complex workflows automate kar sakta hai.

---

## Limitations

### ❌ Less Predictable

Output vary kar sakta hai.

### ❌ Expensive

More LLM calls + tool usage.

### ❌ Harder to Debug

Decision path complex hota hai.

---

# Side-by-Side Comparison

| Feature          | Single LLM | Workflow  | Agent   |
| ---------------- | ---------- | --------- | ------- |
| Memory           | ❌          | Limited   | ✅       |
| Multi-Step Tasks | ❌          | ✅         | ✅       |
| Adaptability     | ❌          | Low       | High    |
| Cost             | Low        | Medium    | High    |
| Predictability   | High       | Very High | Lower   |
| Complexity       | Low        | Medium    | High    |
| Tool Usage       | Fixed/None | Fixed     | Dynamic |

---

# Quick Interview Answer

## Difference Between Workflow and Agent?

### Workflow

Predefined steps follow karta hai.

```text
Known Process
     ↓
Fixed Execution
     ↓
Result
```

### Agent

Goal achieve karne ke liye khud planning karta hai.

```text
Goal
 ↓
Reasoning
 ↓
Tool Selection
 ↓
Adaptation
 ↓
Result
```

---

# Easy Analogy 🎯

## Single LLM = Calculator

Question do → Answer milega.

---

## Workflow = Recipe

Saare steps pehle se written hain.

```text
Step 1
Step 2
Step 3
Serve
```

---

## Agent = Personal Chef

Bol do:

> "Mujhe tasty dinner bana do."

Chef khud decide karega:

* Kya banana hai
* Kya ingredients chahiye
* Kis order mein cook karna hai

---

# Real Industry Practice (Most Important)

Pure agents rarely used alone.

Most companies use:

```text
Workflow + Agent
```

Example:

```text
User Query
     ↓
Workflow
     ↓
Agent Reasoning
     ↓
Validation Workflow
     ↓
Final Output
```

Benefits:

* Workflow Reliability ✅
* Agent Flexibility ✅

---

# Modern Standards

## MCP (Model Context Protocol)

Helps AI systems connect with tools and data sources.

---

## ACP (Agent Communication Protocol)

Helps agents communicate, coordinate, and operate at scale.

---

# Exam Shortcut 🚀

### Single LLM

"Answer the question."

---

### Workflow

"Follow these steps."

---

### Agent

"Achieve this goal."

---

# Final Rule for Choosing

### Use Single LLM

When task is simple and atomic.

### Use Workflow

When predictability, compliance, and efficiency matter.

### Use Agent

When adaptability, reasoning, and dynamic planning are required.

### Industry Standard

```text
Single LLM < Workflow < Agent
```

More Power ↑
More Cost ↑
More Complexity ↑
