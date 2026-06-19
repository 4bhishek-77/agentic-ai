# LangChain Built-in Agents Cheat Sheet (Hinglish)

## 🤖 Built-in Agents Kya Hote Hain?

Agents = LLM + Tools + Decision Making

Normal LLM:

```python
response = llm.invoke("What is AI?")
```

Agent:

```python
User Question
     ↓
Reasoning
     ↓
Choose Tool
     ↓
Execute Tool
     ↓
Generate Answer
```

---

# I. Core Agent Types

## 1. ZERO_SHOT_REACT_DESCRIPTION

Sabse common agent.

Features:

* Pehle reason karta hai
* Tool descriptions padhkar tool choose karta hai
* Examples ki zarurat nahi

### Code

```python
from langchain.agents import initialize_agent, AgentType

agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True
)

agent.invoke("What is the population of India?")
```

### Use Case

* Search tools
* APIs
* Calculators

---

## 2. REACT_DOCSTORE

Document store access kar sakta hai.

### Use Case

* Wikipedia
* Knowledge Base
* Documentation

---

## 3. SELF_ASK_WITH_SEARCH

Complex question ko chhote questions me todta hai.

Example:

```text
Who is the president of the country where Tesla was founded?
```

Steps:

```text
Tesla founded in?
↓
USA
↓
President of USA?
↓
Answer
```

---

## 4. CONVERSATIONAL_REACT_DESCRIPTION

Conversation memory maintain karta hai.

Example:

```text
User: CEO of Google?
Agent: Sundar Pichai

User: Where was he born?
```

Agent samajhta hai "he" = Sundar Pichai.

---

## 5. CHAT_ZERO_SHOT_REACT_DESCRIPTION

Chat models ke liye optimized.

Example:

* GPT
* Granite
* Claude

---

## 6. CHAT_CONVERSATIONAL_REACT_DESCRIPTION

Chat + Memory

Best for chatbots.

---

## 7. STRUCTURED_CHAT_ZERO_SHOT_REACT_DESCRIPTION

Multiple inputs wale tools support karta hai.

Example Tool:

```python
search_tool(
    query,
    location,
    date
)
```

---

## 8. OPENAI_FUNCTIONS

OpenAI Function Calling ke liye.

Example:

```python
get_weather(city)
```

---

## 9. OPENAI_MULTI_FUNCTIONS

Ek se jyada functions call kar sakta hai.

Example:

```text
Weather + Currency + Search
```

---

# II. Model Compatibility

Har model structured outputs support nahi karta.

Common issue:

```text
OutputParserException
ValidationError
```

Mostly hota hai:

```text
structured-chat-zero-shot-react-description
```

use karte waqt.

Granite models ke saath generally:

```python
AgentType.ZERO_SHOT_REACT_DESCRIPTION
```

safe choice hai.

---

# III. Prebuilt Agents

Ready-made agents.

---

## create_pandas_dataframe_agent()

DataFrame ke saath natural language.

### Code

```python
import pandas as pd

from langchain_experimental.agents.agent_toolkits import (
    create_pandas_dataframe_agent
)

df = pd.read_csv("sales.csv")

agent = create_pandas_dataframe_agent(
    llm,
    df,
    verbose=True
)

agent.invoke(
    "Which product has highest sales?"
)
```

### Use Cases

* Data Analysis
* Statistics
* Charts

---

## create_csv_agent()

CSV file directly query kar sakta hai.

### Code

```python
from langchain.agents.agent_toolkits import create_csv_agent

agent = create_csv_agent(
    llm,
    "sales.csv",
    verbose=True
)

agent.invoke(
    "How many rows are there?"
)
```

---

## create_sql_agent()

Database query karne ke liye.

### Code

```python
from langchain_community.utilities.sql_database import SQLDatabase

from langchain_community.agent_toolkits import create_sql_agent

db = SQLDatabase.from_uri(
    "sqlite:///sample.db"
)

agent = create_sql_agent(
    llm=llm,
    db=db,
    verbose=True
)

agent.invoke(
    "List all employees"
)
```

### Lab Favorite ⭐

Ye IBM Agent Labs me bahut use hota hai.

---

## create_openai_functions_agent()

Function calling ke liye.

### Code

```python
agent = create_openai_functions_agent(
    llm,
    tools,
    prompt
)
```

---

## create_tool_calling_agent()

Structured tools ke liye.

### Code

```python
agent = create_tool_calling_agent(
    llm,
    tools,
    prompt
)
```

---

# IV. LangGraph Agents

Traditional agent:

```text
Question
 ↓
Tool
 ↓
Answer
```

LangGraph:

```text
Question
 ↓
Reason
 ↓
Tool
 ↓
Reason
 ↓
Tool
 ↓
Answer
```

Graph based execution.

---

## create_react_agent()

Sabse common LangGraph agent.

### Code

```python
from langgraph.prebuilt import create_react_agent

agent = create_react_agent(
    model=llm,
    tools=tools
)

response = agent.invoke(
    {
        "messages": [
            ("human",
             "What is the capital of India?")
        ]
    }
)

print(response)
```

---

# Interview Questions

## Difference Between LLM and Agent?

LLM:

* Only generates text

Agent:

* Reasons
* Uses tools
* Takes actions

---

## Most Common Agent Type?

```python
ZERO_SHOT_REACT_DESCRIPTION
```

---

## Best Agent For SQL?

```python
create_sql_agent()
```

---

## Best Agent For Pandas?

```python
create_pandas_dataframe_agent()
```

---

## Best Agent For Multi-step Reasoning?

```python
create_react_agent()
```

(LangGraph)
