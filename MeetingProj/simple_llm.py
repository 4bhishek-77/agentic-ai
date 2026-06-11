from ibm_watsonx_ai.foundation_models.utils.enums import ModelTypes
from ibm_watsonx_ai import APIClient, Credentials
from ibm_watsonx_ai.metanames import GenTextParamsMetaNames as GenParams
from ibm_watsonx_ai.foundation_models.utils.enums import DecodingMethods
from langchain_ibm import WatsonxLLM, WatsonxEmbeddings
from ibm_watsonx_ai.foundation_models.utils import get_embedding_model_specs
from ibm_watsonx_ai.foundation_models.utils.enums import EmbeddingTypes

from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate

from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

from ibm_watsonx_ai.foundation_models import ModelInference
from ibm_watsonx_ai.foundation_models.schema import TextChatParameters


# ============================================================
# Model Parameters
# ============================================================

parameters = {
    GenParams.DECODING_METHOD: "sample",
    GenParams.MAX_NEW_TOKENS: 512,
    GenParams.MIN_NEW_TOKENS: 1,
    GenParams.TEMPERATURE: 0.5,
    GenParams.TOP_K: 50,
    GenParams.TOP_P: 1,
}


# ============================================================
# Granite Model Configuration
# ============================================================

model_id = "ibm/granite-3-3-8b-instruct"
project_id = "skills-network"

granite_llm = WatsonxLLM(
    model_id=model_id,
    url="https://us-south.ml.cloud.ibm.com",
    project_id=project_id,
    params=parameters,
)


# ============================================================
# Test Prompt
# ============================================================

response = granite_llm.invoke(
    "How to read a book effectively?"
)

print(response)


# ============================================================
# Utility Function
# ============================================================

def remove_non_ascii(text):
    return "".join(
        character
        for character in text
        if ord(character) < 128
    )


# ============================================================
# Financial Product Assistant
# ============================================================

def product_assistant(ascii_transcript):

    system_prompt = """
You are an intelligent assistant specializing in financial products.

Your task is to process transcripts of earnings calls,
ensuring that all references to financial products
and common financial terms are in the correct format.

For each financial product or common term that is
typically abbreviated as an acronym, the full term
should be spelled out followed by the acronym
in parentheses.

Examples:

401k
→ 401(k) retirement savings plan

HSA
→ Health Savings Account (HSA)

ROA
→ Return on Assets (ROA)

VaR
→ Value at Risk (VaR)

PB
→ Price to Book (PB) ratio

Similarly, transform spoken numbers representing
financial products into numeric representations.

Examples:

five two nine
→ 529 (Education Savings Plan)

four zero one k
→ 401(k) (Retirement Savings Plan)

Some acronyms may have different meanings
depending on context.

Example:

LTV
→ Loan to Value

OR

LTV
→ Lifetime Value

Determine the correct meaning using context.

Leave normal numerical expressions unchanged.

After processing:

1. Return corrected transcript.
2. Return list of modified terms.
"""

    prompt_input = (
        system_prompt
        + "\n\n"
        + ascii_transcript
    )

    messages = [
        {
            "role": "user",
            "content": prompt_input
        }
    ]

    model_id = (
        "meta-llama/"
        "llama-3-2-11b-vision-instruct"
    )

    params = TextChatParameters(
        temperature=0.2,
        top_p=0.6
    )

    llama32 = ModelInference(
        model_id=model_id,
        credentials=credentials,
        project_id=project_id,
        params=params
    )

    response = llama32.chat(
        messages=messages
    )

    return response["choices"][0]["message"]["content"]


# ============================================================
# Meeting Minutes Prompt
# ============================================================

template = """
Generate meeting minutes and a list of tasks
based on the provided context.

Context:
{context}

Meeting Minutes:
- Key points discussed
- Decisions made

Task List:
- Actionable items
- Assignees
- Deadlines
"""

prompt = ChatPromptTemplate.from_template(
    template
)


# ============================================================
# LangChain Pipeline
# ============================================================

chain = (
    {"context": RunnablePassthrough()}
    | prompt
    | granite_llm
    | StrOutputParser()
)


# ============================================================
# Example Usage
# ============================================================

transcript = """
We discussed launching the new product next month.
Rahul will prepare the marketing campaign.
Priya will finalize the budget by Friday.
"""

meeting_minutes = chain.invoke(
    transcript
)

print(meeting_minutes)
