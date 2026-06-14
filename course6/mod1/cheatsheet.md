# Foundations of Function Calling, Tool Calling, Agents & LCEL

---

# 1. Tool Calling Fundamentals

Tool Calling allows an LLM to use external functions (tools) for tasks beyond its built-in knowledge.

Important:

> The model does not execute the tool itself. It only generates the tool name and arguments required for execution.

The application is responsible for:

* Running the tool
* Getting the result
* Sending the result back to the model

---

# 2. Tool Calling Workflow

## Step 1: Tool Setup + User Question

Define tools and provide them to the model.

Example Query:

```text
What's the weather in Paris?
```

Example Tool:

```python
def get_weather(location):
    pass
```

---

## Step 2: Tool Call

The model determines which tool should be used.

Example:

```python
get_weather("Paris")
```

Generated Tool Call:

```json
{
  "tool": "get_weather",
  "location": "Paris"
}
```

---

## Step 3: Tool Execution

Application executes the tool.

```python
result = get_weather("Paris")
```

Example Result:

```python
{
    "temperature": 14
}
```

---

## Step 4: Result Passing

Tool output is sent back to the model.

```python
{
    "temperature": 14
}
```

This becomes part of the model's context.

---

## Step 5: Final Response

Model generates a natural language answer.

```text
It's currently 14°C in Paris.
```

---

# 3. LangChain Tool Hierarchy

All LangChain tools inherit from:

```python
BaseTool
```

Hierarchy:

```text
BaseTool
│
├── Tool
├── StructuredTool
└── Custom Tools
```

---

# 4. Tool Creation Methods

## 4.1 Subclassing BaseTool

Most flexible approach.

Example:

```python
from langchain.tools import BaseTool

class CalculatorTool(BaseTool):
    name = "calculator"
    description = "Performs calculations"

    def _run(self, expression):
        return eval(expression)
```

Advantages:

* Maximum control
* Custom behavior
* Sync and async support

Disadvantage:

* More code

---

## 4.2 Using Tool Class

Traditional method.

```python
from langchain.tools import Tool

def add_numbers(text):
    return str(eval(text))

tool = Tool(
    name="Calculator",
    func=add_numbers,
    description="Performs addition"
)
```

Best for:

* Simple string inputs
* Legacy projects

---

## 4.3 Using @tool Decorator

Recommended modern approach.

```python
from langchain.tools import tool

@tool
def add_numbers(a: int, b: int):
    """
    Add two numbers.
    """
    return a + b
```

Automatically generates:

* Name
* Description
* Argument Schema

Advantages:

* Less code
* Cleaner syntax
* Agent-friendly

---

## 4.4 StructuredTool

Supports multiple inputs and complex schemas.

```python
from langchain.tools import StructuredTool

def calculate(a: int, b: int):
    return a + b

tool = StructuredTool.from_function(calculate)
```

Best for:

* Multiple parameters
* Named arguments
* Function-calling models

---

# 5. Tool Inspection & Usage

## Tool Schema

Inspect tool metadata.

```python
print(tool.name)
print(tool.description)
print(tool.args)
```

---

## Direct Invocation

Testing tools without agents.

```python
tool.invoke({
    "a": 10,
    "b": 20
})
```

Output:

```python
30
```

---

## Tool Binding to Models

Provide tools to an LLM.

```python
llm_with_tools = llm.bind_tools([tool])
```

Now the model knows:

* Available tools
* Parameters
* Descriptions

---

## Tool Invocation Through Model

```python
response = llm_with_tools.invoke(
    "Add 10 and 20"
)
```

Model may generate:

```json
{
  "tool": "add_numbers",
  "a": 10,
  "b": 20
}
```

---

# 6. LangChain Built-in Tools

## Search

```text
SerpAPI
Wikipedia
Tavily
```

Purpose:

* Web Search
* Knowledge Retrieval

---

## Math & Code

```text
LLMMathChain
Python REPL
Pandas Toolkit
```

Purpose:

* Computation
* Data Analysis

---

## Web & APIs

```text
Requests Toolkit
Playwright
```

Purpose:

* Web Requests
* Browser Automation

---

## Productivity

```text
Gmail
Google Calendar
Slack
GitHub
```

Purpose:

* Scheduling
* Messaging
* Repository Management

---

## Files & Documents

```text
FileSystem
Google Drive
VectorStoreQA
```

Purpose:

* Document Access
* File Operations
* Retrieval

---

## Finance

```text
Stripe
Yahoo Finance
Polygon IO
```

Purpose:

* Payments
* Market Data

---

## ML Tools

```text
DALL-E
HuggingFace Hub
```

Purpose:

* Image Generation
* Model Access

---

# 7. Agents in LangChain

## Definition

Agent = LLM + Tools + Reasoning + Memory

Agents can:

* Think
* Use tools
* Observe results
* Generate answers

---

## Components of an Agent

### LLM

Reasoning engine.

### Tools

External capabilities.

### Memory

Stores conversation context.

### Executor

Runs the reasoning loop.

---

## Agent Workflow

```text
Question
 ↓
Thought
 ↓
Action
 ↓
Observation
 ↓
Thought
 ↓
Final Answer
```

This is called:

```text
ReAct (Reason + Act)
```

---

## Agent Types

### zero-shot-react-description

Uses tool descriptions to decide actions.

```python
agent="zero-shot-react-description"
```

Best for:

* Simple tools
* Text inputs

---

### chat-zero-shot-react-description

Chat-optimized version of ReAct.

```python
agent="chat-zero-shot-react-description"
```

---

### OpenAI Function Agent

```python
create_openai_functions_agent(...)
```

Best for:

* Function Calling
* Structured JSON inputs
* Structured JSON outputs

---

### LangGraph Agents

```python
create_react_agent(...)
```

Modern approach.

Advantages:

* Better orchestration
* Memory support
* Multi-step workflows

---

# 8. LCEL (LangChain Expression Language)

LCEL allows building chains using the pipe operator.

```python
|
```

Output of one component becomes input of the next.

---

## Why LCEL?

Benefits:

* Cleaner syntax
* Faster execution
* Easier chaining
* Better readability

---

# 9. Runnable Architecture

LCEL is built on:

```python
Runnable
```

Everything in LCEL follows a common interface.

Examples:

```python
Prompt
LLM
Parser
Retriever
```

All are runnables.

---

# 10. Simple LCEL Chain

Example:

```python
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt = ChatPromptTemplate.from_template(
    "Explain {topic}"
)

chain = (
    prompt
    | llm
    | StrOutputParser()
)

result = chain.invoke(
    {"topic": "Tool Calling"}
)

print(result)
```

Flow:

```text
Input
 ↓
Prompt
 ↓
LLM
 ↓
Output Parser
 ↓
Final Output
```

---

# Quick Revision

```text
Function
 ↓
Tool
 ↓
Agent
 ↓
Tool Calling
 ↓
Function Calling
 ↓
LangGraph
 ↓
LCEL Chains
```

Important Formulas:

Tool Calling:
LLM → Tool Request → Tool Execution → Result → Final Answer

Agent:
LLM + Tools + Memory + Reasoning

ReAct:
Reason → Act → Observe → Answer

LCEL:
Component1 | Component2 | Component3

```
```
