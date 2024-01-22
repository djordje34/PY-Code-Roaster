import os
import numpy as np
from langchain.chains import LLMChain
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import PromptTemplate
from langchain_community.llms import HuggingFaceHub
from dotenv import load_dotenv
from langchain.chains.summarize import load_summarize_chain
from tqdm import tqdm
from langchain.text_splitter import RecursiveCharacterTextSplitter

map_prompt_template = """
Summarize the text enclosed in triple backticks for readers in two or three well-formed paragraphs. Ensure that your summary:
- Covers the main ideas comprehensively
- Includes supporting details
- Highlights important facts or figures
- Incorporates relevant examples or quotes

Avoid incomplete summaries or sentences ending abruptly. Ensure that each summary is cohesive and provides a full understanding of the content.

```{text}```

SUMMARY:
"""
map_prompt = PromptTemplate(template=map_prompt_template, input_variables=["text"])

combine_prompt_template = """
Synthesize the text enclosed in triple backticks into a detailed bullet-point summary. Provide at least 5 to 7 bullet points covering various aspects of the text. Ensure that each bullet point:
- Begins with '-'
- Forms a complete, coherent, and grammatically correct sentence without abrupt endings or incomplete information. If a sentence is incomplete, please attempt to provide a logical and relevant completion.
- Elaborates on key points to ensure a thorough understanding, providing additional context or explanations where necessary.
- Captures distinct key points or subtopics, avoiding repetition or redundancy.
- Is clear, concise, and free from unnecessary complexity.
- Presents a cohesive overview that ties together the main ideas of the text.

```{text}```

DETAILED BULLET POINT SUMMARY:
"""
combine_prompt = PromptTemplate(
    template=combine_prompt_template, input_variables=["text"]
)
load_dotenv()

HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")

def load_pdf(file_path):
    loader = PyPDFLoader(file_path)
    text_splitter = RecursiveCharacterTextSplitter(separators=["\n\n", "\n","."], chunk_size=5000, chunk_overlap=1000)
    docs = loader.load_and_split(text_splitter=text_splitter)
    print(len(docs))
    return docs

def get_chain(verbose=0):
    repo2_id = "NousResearch/Nous-Hermes-2-Mixtral-8x7B-DPO"
    llm1 = HuggingFaceHub(
        repo_id=repo2_id, model_kwargs={"temperature": 0.9, "max_length":4096})
    chain = load_summarize_chain(llm1, chain_type="map_reduce", map_prompt=map_prompt,combine_prompt=combine_prompt)
    return chain

def get_summary(docs,chain):
    return chain.run(docs)

#chain = get_chain()
#pdf = load_pdf("unet.pdf")
#print(get_summary(pdf,chain))