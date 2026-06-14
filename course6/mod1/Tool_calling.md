# AI Math Assistant - Tool Calling & Agents Summary

## Overview

Is notebook ka main objective LangChain aur LangGraph ke through Tool Calling aur Agents ko samajhna hai.

Flow:

Function → Tool → Agent → Multiple Tools → Real-world Problem Solving

---

# 1. Functions

Normal Python functions:

```python
def add_numbers(a, b):
    return a + b
```

Ye sirf Python code hai. LLM directly use nahi kar sakta.

---

# 2. Tools

Tool ek wrapper hota hai jo function ko LLM-friendly banata hai.

Tool ke components:

* Name
* Description
* Parameters

Tool banane ke do common methods:

## Method 1

```python
Tool(...)
```

## Method 2 (Recommended)

```python
@tool
```

Example:

```python
@tool
def add_numbers(a: int, b: int):
    return a + b
```

Benefits of `@tool`:

* Automatically schema generate karta hai
* Name extract karta hai
* Parameters identify karta hai
* Agent-compatible bana deta hai

---

# 3. Tool Calling

Tool Calling mein LLM tool execute nahi karta.

LLM sirf structured request generate karta hai.

Example:

User:
Add 10 and 20

LLM:

```json
{
  "tool": "add_numbers",
  "a": 10,
  "b": 20
}
```

External system tool execute karta hai aur result LLM ko return karta hai.

---

# 4. Agents

Agent = LLM + Tools + Reasoning

Agent decide karta hai:

* Tool use karna hai?
* Kaunsa tool use karna hai?
* Final answer kaise generate karna hai?

---

# 5. ReAct Framework

ReAct = Reason + Act

Flow:

Question
↓
Thought
↓
Action
↓
Observation
↓
Final Answer

Example:

User:
What is 10 + 20?

Thought:
Addition required

Action:
add_numbers

Observation:
30

Final Answer:
30

---

# 6. Agent Types

## zero-shot-react-description

* Tool descriptions use karta hai
* Examples ki zarurat nahi
* Simple input/output tools ke liye best

Example:

Input → String

Output → String

---

## structured-chat-zero-shot-react-description

* Structured inputs handle karta hai
* Multiple parameters support karta hai
* JSON-like data ke liye useful

Example:

```json
{
  "a": 10,
  "b": 20
}
```

---

## openai-functions

* Native function calling support
* Structured JSON inputs
* Structured JSON outputs
* Complex tools ke liye best

Example Output:

```json
{
  "sum": 60,
  "count": 3
}
```

---

# 7. Multiple Tools

Agent ke paas multiple tools ho sakte hain.

Example:

* add_numbers
* subtract_numbers
* multiply_numbers
* divide_numbers

Agent automatically correct tool choose karta hai.

---

# 8. Built-in Tools

LangChain already tools provide karta hai.

Examples:

* WikipediaQueryRun
* Google Search
* Python REPL
* YouTube Search
* Weather Tools

---

# 9. initialize_agent()

Old method:

```python
initialize_agent(...)
```

Used to create and run agents.

---

# 10. create_react_agent()

Modern LangGraph method:

```python
create_react_agent(...)
```

Advantages:

* Better orchestration
* Better memory support
* More flexible workflows
* Recommended approach

---

# 11. Orchestration

Orchestration = LLM, Tools, Memory aur Actions ko coordinate karna.

Example:

User:
(10 + 20) × 5

Agent:

Add Tool
↓
Multiply Tool
↓
Answer

Ye complete workflow orchestration kehlata hai.

---

# 12. Important Definitions

## Function

Normal Python code.

## Tool

LLM-usable function.

## Tool Calling

LLM generates structured request for tool usage.

## Agent

LLM-powered system that uses tools and reasoning.

## ReAct

Reason + Act framework.

## Orchestration

Coordination of tools, memory and actions.

## Toolkit

Collection of related tools.

---

# Viva One-Liners

Tool = Function wrapped for LLM usage.

Agent = LLM + Tools + Reasoning.

ReAct = Reason → Act → Observe → Answer.

@tool = Converts Python function into LangChain Tool.

zero-shot-react-description = Simple tool calling.

structured-chat-zero-shot-react-description = Structured inputs.

openai-functions = Structured inputs + structured outputs.

create_react_agent() = Modern LangGraph agent creation method.

Orchestration = Managing interaction between LLM, tools and memory.
