# Tool Calling aur Agents in LangChain

## Tools Kya Hote Hain?

Tools basically functions hote hain jo LLM ko external duniya se interact karne dete hain.

Examples:
- Weather API
- Search Engine
- Calculator
- Database Query

### Tool ke Components

Har tool ke 3 important parts hote hain:

1. Name
2. Description
3. Parameters

Example:

Name: WeatherTool

Description:
Current weather batata hai.

Parameters:
- location

---

# Tool Calling

Tool Calling ka matlab hai LLM kisi external tool ko use karne ki request karta hai.

### Important Point

LLM khud tool execute nahi karta.

LLM sirf ek structured request generate karta hai jisme hota hai:

- Kaunsa tool use karna hai
- Kya parameters dene hain

Example:

User:
"New York ka weather kya hai?"

LLM output:

{
  "tool": "weather",
  "location": "New York"
}

Ab system:

1. Is request ko padhega
2. Weather API call karega
3. Result layega
4. Result LLM ko dega
5. LLM final answer generate karega

### Workflow

User Query
↓
LLM
↓
Tool Call Generate
↓
Tool Execute
↓
Result
↓
LLM
↓
Final Answer

---

# Function Calling vs Tool Calling

Dono same concept hain.

### Function Calling

- OpenAI ka term

### Tool Calling

- Industry aur LangChain ka term

### Difference

Koi technical difference nahi hai.

Sirf naam alag hai.

---

# Tools in LangChain

Tools aise utilities hote hain jo:

- Structured input lete hain
- Specific kaam karte hain
- Output wapas LLM ko dete hain

Examples:

- Web Search
- Database Query
- Code Execution
- APIs

---

# Toolkit

Toolkit = Related tools ka collection.

Matlab ek group of tools jo ek common purpose ke liye use hote hain.

---

# Tools Banane ke Tarike

## 1. Built-in Tools

Example:

- WikipediaQueryRun

---

## 2. load_tools()

Ek saath multiple tools load karne ke liye.

Examples:

- wikipedia
- serpapi
- llm-math

---

## 3. Custom Tools

Khud ke tools bana sakte ho using:

- Tool Class
- @tool Decorator

---

## 4. OpenAI Functions

LangChain tools ko OpenAI Functions me convert kar sakte hain.

Methods:

- convert_to_openai_function()
- bind_tools()
- bind_functions()

---

# Agents

## Definition

Agent ek LLM-powered system hota hai jo:

- Soch sakta hai (Reasoning)
- Tools use kar sakta hai
- Memory access kar sakta hai
- Actions perform kar sakta hai

Normal LLM sirf text generate karta hai.

Agent real-world kaam bhi kar sakta hai.

---

# Agent Architecture

AI Agent ke 6 major components hote hain.

---

## 1. AI Agent

Main controller.

Kaam:

- User input lena
- Decision lena
- Tools aur memory ko manage karna

---

## 2. LLM

Agent ka brain.

LLM decide karta hai:

- Direct answer dena hai?
- Memory use karni hai?
- Tool use karna hai?

---

## 3. Tools

External capabilities.

Examples:

- Search Engine
- Weather API
- Calculator
- Database

---

## 4. Memory

Information store aur retrieve karti hai.

### Types of Memory

### Short-Term Memory

RAM me stored hoti hai.

### SQL Memory

Database me stored hoti hai.

### Vector Database Memory

Semantic search ke liye use hoti hai.

---

## 5. Action

Jab LLM decide karta hai ki tool use karna hai tab ek action generate hota hai.

Example:

{
  "tool": "weather",
  "location": "New York"
}

Ye action execute kiya jata hai.

---

## 6. External World

Agent ke bahar ki duniya.

Examples:

- Internet
- APIs
- Operating System
- Physical Devices

---

# Complete Example

### Step 1

User poochta hai:

"What is the weather in New York?"

---

### Step 2

LLM query analyze karta hai.

Usse pata chalta hai ki real-time data chahiye.

---

### Step 3

LLM tool call generate karta hai:

{
  "tool": "weather",
  "location": "New York"
}

---

### Step 4

Agent weather tool ko invoke karta hai.

---

### Step 5

Weather API latest weather fetch karti hai.

Example:

68°F Sunny

---

### Step 6

Result LLM ko diya jata hai.

---

### Step 7

LLM final answer generate karta hai.

Example:

"Currently 68°F and sunny in New York."

---

# LangChain me Agents

## 1. Built-in Agent Types

Examples:

- zero-shot-react-description
- chat-zero-shot-react-description

Simple reasoning ke liye use hote hain.

---

## 2. OpenAI Function Agents

Banaye jaate hain:

create_openai_functions_agent()

Function calling support karte hain.

---

## 3. LangGraph Agents

Banaye jaate hain:

create_react_agent()

Features:

- Complex Reasoning
- Memory
- Action Chaining
- Streaming

---

## 4. AgentExecutor

Agent ko run karne ka kaam karta hai.

Kaam:

- LLM call karna
- Tool execute karna
- Result process karna
- Final answer generate karna

---

## 5. MemorySaver

Conversation context ko save rakhta hai.

Benefits:

- Personalization
- Context Retention
- User Preferences Remember Karna

---

# Exam Definitions

## Tool

LLM ke liye available function jo specific task perform karta hai.

## Tool Calling

Process jisme LLM structured request generate karta hai kisi tool ko use karne ke liye.

## Agent

LLM-powered system jo tools, memory aur actions use kar sakta hai.

## Memory

Information store aur retrieve karne ka mechanism.

## Action

Tool execution ke liye generate ki gayi request.

## Toolkit

Related tools ka collection.

---

# 2-Mark Shortcut

Tool = Function available to LLM.

Tool Calling = LLM generates structured request for tool usage.

Agent = LLM + Tools + Memory + Actions.

Toolkit = Collection of related tools.

Memory = Information storage system.

Action = Tool execution request.

---

# One-Line Revision

Agent = LLM + Tools + Memory + Actions

Tool Calling = LLM → Tool Request → Tool Execution → Result → Final Answer
