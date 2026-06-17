# LangChain Expression Language (LCEL) - Complete Cheat Sheet

---

# 1. What is LCEL?

LCEL (LangChain Expression Language) is a declarative way to build chains in LangChain.

Instead of writing step-by-step logic, you connect components together and LangChain handles execution.

Key Idea:

```text
Input
 ↓
Prompt
 ↓
LLM
 ↓
Parser
 ↓
Output
```

LCEL uses the pipe operator:

```python
|
```

to connect components.

---

# 2. Benefits of LCEL

| Capability           | Benefit                                  |
| -------------------- | ---------------------------------------- |
| Parallel Execution   | Reduces latency and improves performance |
| Async Support        | Enables non-blocking workflows           |
| Streaming            | Provides partial responses immediately   |
| LangSmith Tracing    | Debugging and monitoring                 |
| Shared API           | Consistent interface for all chains      |
| LangServe Deployment | Easy production deployment               |
| Concise Syntax       | Cleaner and readable code                |

---

# 3. Runnable Interface

Every LCEL component follows the Runnable interface.

A Runnable transforms input into output.

Common Runnable Methods:

```python
invoke()
batch()
stream()
```

All LCEL components implement these methods.

---

# 4. Types of Runnables

## ChatModel

Used to interact with LLMs.

Example:

```python
from langchain_openai import ChatOpenAI

llm = ChatOpenAI()
```

Use Case:

```text
Generate conversational responses
```

---

## PromptTemplate

Creates prompts dynamically.

Example:

```python
from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate.from_template(
    "Explain {topic}"
)
```

Use Case:

```text
Create structured prompts
```

---

## OutputParser

Converts raw model output into structured data.

Example:

```python
from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()
```

Use Case:

```text
Convert response into clean text
```

---

## RunnableLambda

Wraps custom Python functions.

Example:

```python
from langchain_core.runnables import RunnableLambda

square = RunnableLambda(
    lambda x: x*x
)
```

Use Case:

```text
Add custom business logic
```

---

## RunnableSequence

Chains multiple runnables together.

Example:

```python
chain = prompt | llm | parser
```

Use Case:

```text
Multi-step processing
```

---

# 5. Runnable Chains

Runnable chains pass output of one component to the next.

General Flow:

```text
Component1
 ↓
Component2
 ↓
Component3
```

Equivalent LCEL:

```python
component1 | component2 | component3
```

---

# 6. Simple Question Answering Chain

Components:

```text
PromptTemplate
 ↓
ChatModel
 ↓
StrOutputParser
```

Code:

```python
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

prompt = PromptTemplate.from_template(
    "What is {topic}?"
)

chain = (
    prompt
    | llm
    | StrOutputParser()
)

result = chain.invoke(
    {"topic": "LCEL"}
)

print(result)
```

Workflow:

```text
Question
 ↓
Prompt Formatting
 ↓
LLM
 ↓
Text Output
```

---

# 7. RAG Chain

Components:

```text
Retriever
 ↓
PromptTemplate
 ↓
ChatModel
 ↓
OutputParser
```

Workflow:

```text
User Query
 ↓
Retrieve Documents
 ↓
Add Context
 ↓
LLM
 ↓
Answer
```

Example:

```python
retriever | prompt | llm | parser
```

---

# 8. Function Calling Chain

Components:

```text
PromptTemplate
 ↓
ChatModel
 ↓
Tool
```

Workflow:

```text
Prompt
 ↓
Generate Tool Call
 ↓
Execute Tool
```

Example:

```python
prompt | llm_with_tools
```

---

# 9. Structured Output Chain

Components:

```text
PromptTemplate
 ↓
ChatModel
 ↓
JsonOutputParser
```

Workflow:

```text
Prompt
 ↓
LLM
 ↓
JSON Output
```

Example:

```python
prompt | llm | json_parser
```

---

# 10. Basic Operations

## invoke()

Single input → Single output

```python
result = chain.invoke(
    {"topic":"AI"}
)
```

---

## ainvoke()

Async version.

```python
result = await chain.ainvoke(
    {"topic":"AI"}
)
```

---

## batch()

Multiple inputs together.

```python
results = chain.batch([
    {"topic":"AI"},
    {"topic":"ML"}
])
```

---

## abatch()

Async batch execution.

```python
results = await chain.abatch(
    inputs
)
```

---

## stream()

Returns output incrementally.

```python
for chunk in chain.stream(
    {"topic":"AI"}
):
    print(chunk)
```

Useful for chat streaming.

---

## astream()

Async streaming.

```python
async for chunk in chain.astream(
    {"topic":"AI"}
):
    print(chunk)
```

---

# 11. Composition Patterns

## Pipe Operator

Most important LCEL feature.

```python
prompt | llm | parser
```

Meaning:

```text
Prompt
 ↓
LLM
 ↓
Parser
```

---

## .pipe()

Alternative syntax.

```python
prompt.pipe(llm).pipe(parser)
```

---

## RunnableParallel

Runs multiple runnables simultaneously.

Example:

```python
from langchain_core.runnables import RunnableParallel

parallel = RunnableParallel(
    summary=summary_chain,
    keywords=keyword_chain
)
```

Workflow:

```text
Input
 ├── Summary
 └── Keywords
```

Benefits:

* Faster execution
* Parallel processing

---

## RunnableLambda

Custom Python logic.

```python
from langchain_core.runnables import RunnableLambda

double = RunnableLambda(
    lambda x: x*2
)
```

---

# 12. Data Manipulation

## RunnablePassthrough

Returns original input.

```python
RunnablePassthrough()
```

Example:

```python
Input
 ↓
Same Input
```

---

## RunnablePassthrough.assign()

Adds fields.

```python
RunnablePassthrough.assign(
    length=lambda x: len(x)
)
```

Output:

```python
{
    "text":"hello",
    "length":5
}
```

---

## .pick()

Select specific fields.

```python
chain.pick("answer")
```

Output:

```python
{
   "answer":"..."
}
```

---

# 13. Advanced Patterns

## .bind()

Fix default parameters.

```python
llm.bind(
    temperature=0
)
```

---

## .with_fallbacks()

Backup runnable.

```python
primary.with_fallbacks(
    [backup]
)
```

Use Case:

```text
If primary fails,
use backup
```

---

## .with_retry()

Retry on failure.

```python
chain.with_retry()
```

Useful for:

```text
Network errors
API failures
```

---

# 14. Configuration

## config parameter

Control execution.

Example:

```python
chain.invoke(
    input,
    config={
        "max_concurrency":5
    }
)
```

---

## .with_config()

Apply default configuration.

```python
chain.with_config(
    tags=["production"]
)
```

---

# 15. Streaming & Batching

## astream_events()

Detailed event stream.

```python
async for event in chain.astream_events():
    print(event)
```

Shows:

* Start
* Intermediate steps
* End

---

## batch_as_completed()

Returns results immediately when completed.

```python
for result in chain.batch_as_completed(
    inputs
):
    print(result)
```

Benefit:

```text
No need to wait for all tasks
```

---

# 16. Orchestration Recommendations

## Single LLM Call

Use When:

* Simple prompt
* Single response

Example:

```python
llm.invoke(prompt)
```

Recommended:

```text
LLM Directly
```

---

## Simple Pipelines

Use When:

* Prompt + LLM + Parser
* Basic Retrieval

Example:

```python
prompt | llm | parser
```

Recommended:

```text
LCEL
```

---

## Complex Workflows

Use When:

* Conditional Logic
* Loops
* Multi-Agent Systems
* State Management

Recommended:

```text
LangGraph
```

Example:

```python
create_react_agent()
```

---

# Quick Revision

## LCEL Formula

```text
Runnable1
 |
Runnable2
 |
Runnable3
```

---

## Common Runnable Types

```text
ChatModel
PromptTemplate
OutputParser
RunnableLambda
RunnableSequence
```

---

## Most Important Methods

```python
invoke()
batch()
stream()
```

Async Versions:

```python
ainvoke()
abatch()
astream()
```

---

## Orchestration Rule

```text
Single Prompt
   ↓
LLM

Simple Chain
   ↓
LCEL

Complex Workflow
   ↓
LangGraph
```
