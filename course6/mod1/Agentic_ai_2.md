# When to (and NOT to) Use AI Agents 🤖

## Learning Goal

Understand:

* When AI Agents are useful
* When workflows are better
* How to decide using the 4-Criteria Framework
* Risks and limitations of agents
* Best practices for deployment

---

# AI System Spectrum

AI systems exist on a spectrum of increasing complexity.

| Type               | Description                        | Best Use Cases                         |
| ------------------ | ---------------------------------- | -------------------------------------- |
| Simple AI Features | Single AI task execution           | Summarization, Classification          |
| Workflows          | Predefined multi-step process      | Document processing, Routing           |
| Agents             | Autonomous planning and adaptation | Research, Strategy, Complex Automation |

---

## Easy Way to Remember

### Simple AI

```text
Question
   ↓
Answer
```

### Workflow

```text
Step 1
 ↓
Step 2
 ↓
Step 3
```

### Agent

```text
Goal
 ↓
Plan
 ↓
Act
 ↓
Observe
 ↓
Repeat
```

---

# The 4-Criteria Framework

Before building an agent, ask 4 questions.

---

# 1. Is the Task Ambiguous or Predictable?

## Use Agents When

The solution path is unclear.

Examples:

* Research
* Troubleshooting
* Strategic Planning
* Creative Tasks

```text
Problem
   ↓
Unknown Path
   ↓
Agent Figures It Out
```

---

## Use Workflows When

Everything can be predefined.

Examples:

* Form Processing
* Invoice Validation
* Order Routing

```text
Input
 ↓
Known Steps
 ↓
Output
```

---

## Exam Shortcut

### Ambiguous = Agent

### Predictable = Workflow

---

# 2. Is the Value Worth the Cost?

Agents are expensive.

They may consume:

```text
10x – 100x
more tokens
than workflows
```

because they:

* Think
* Plan
* Replan
* Call tools repeatedly

---

## Good Candidate

### Strategic Planning

High business value.

```text
High Value
+
High Complexity
=
Use Agent
```

---

## Bad Candidate

### FAQ Support

```text
Low Value
+
Repeatable Task
=
Use Workflow
```

---

# 3. Does the Agent Meet Minimum Capabilities?

Before deployment, test essential skills.

---

## Research Agent

Must:

* Find sources
* Filter sources
* Summarize findings

---

## Coding Agent

Must:

* Write code
* Fix code
* Validate code

---

## Customer Support Agent

Must:

* Classify issues
* Resolve common problems
* Escalate difficult cases

---

## Data Analysis Agent

Must:

* Clean data
* Detect anomalies
* Summarize trends

---

## Rule

If the agent cannot reliably perform core skills:

```text
Redesign
or
Simplify
```

---

# 4. What Happens if the Agent Makes a Mistake?

Most important question.

---

## Safe Situation

Errors can be:

* Detected quickly
* Reversed easily

```text
Mistake
 ↓
Detected
 ↓
Fixed
```

Agent may be acceptable.

---

## Dangerous Situation

Errors are:

* Hard to detect
* Expensive
* Harmful

```text
Mistake
 ↓
Nobody Notices
 ↓
Major Damage
```

Avoid agents.

---

# Current Challenges of AI Agents

---

## 1. Reasoning Inconsistency

Agent succeeds today.

Fails tomorrow.

```text
Same Task
 ↓
Different Result
```

---

## 2. Unpredictable Costs

Resource usage varies dramatically.

```text
Simple Task → Cheap

Complex Task → Expensive
```

---

## 3. Tool Integration Problems

Agents depend on:

* APIs
* Databases
* External Systems

Failures can break workflows.

---

# When NOT to Use Agents

Important interview question.

---

## Avoid Agents For

### High-Volume Low-Margin Tasks

Example:

* Basic FAQ Support
* Password Reset

Use workflows.

---

### Real-Time Systems

Example:

* Fraud Detection
* High-frequency decisions

Agents are often too slow.

---

### Zero-Error Systems

Example:

* Medical Diagnosis
* Security Decisions

Mistakes are unacceptable.

---

### Highly Regulated Industries

Need deterministic outcomes.

Examples:

* Compliance
* Legal Processing
* Critical Finance

Use workflows instead.

---

# Effective Agent Architecture

Every agent depends on 3 major components.

---

## 1. Environment

Where the agent operates.

Examples:

* Browser
* Database
* Enterprise System

---

## 2. Tools

What the agent can use.

Examples:

* Search
* APIs
* Calculators
* Databases

---

## 3. System Prompt

Defines:

* Goals
* Rules
* Constraints
* Behavior

---

## Formula

```text
Environment
+
Tools
+
System Prompt
=
Agent
```

---

# Risk Management Strategy

---

## High Risk + Hard to Notice

Use:

* Human Review
* Multiple Validation Layers

Example:

```text
Medical Reports
Financial Decisions
```

---

## High Risk + Visible

Use:

* Automated Checks
* Monitoring

Example:

```text
Customer Facing Decisions
```

---

## Low Risk

Use:

* Monitoring
* User Feedback
* Lightweight Validation

---

# Agent Deployment Best Practices

---

## Start Read-Only

Initially allow:

```text
Read
✅

Write
❌
```

Avoid giving dangerous permissions early.

---

## Add Human Approvals

Critical actions should require approval.

```text
Agent
 ↓
Recommendation
 ↓
Human Approval
 ↓
Execution
```

---

## Use Staged Deployment

### Phase 1

Proof of Concept

Low-risk tasks.

---

### Phase 2

Pilot Program

Moderate-risk tasks.

Human supervision enabled.

---

### Phase 3

Production Scaling

Only after proving reliability.

---

## Enable Logging

Track:

* Actions
* Tool Calls
* Decisions
* Errors

This makes debugging easier.

---

# Future of Agents

Expected improvements:

### Better Reasoning

More consistent decisions.

---

### Smarter Architectures

Lower cost.

Higher efficiency.

---

### Better Monitoring

Automatic error detection.

Better safety.

---

# Interview Cheat Sheet 🚀

## When Should You Use an Agent?

Use agents when:

* Task is ambiguous
* Requires planning
* Needs adaptation
* Has manageable risk
* Provides high business value

---

## When Should You NOT Use an Agent?

Avoid agents when:

* Task is repetitive
* Workflow is predictable
* Real-time response is needed
* Mistakes are unacceptable
* Compliance requires deterministic behavior

---

# Golden Rule 🌟

Don't ask:

> "Can I build an agent?"

Ask:

> "Do I actually NEED an agent?"

Most business problems are solved by:

```text
Workflow
+
LLM
```

not

```text
Agent
```

Use agents only when adaptability and autonomous decision-making provide clear value.
