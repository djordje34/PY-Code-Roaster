import os
import re
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_community.llms import HuggingFaceHub
from langchain.chains import load_summarize_chain
from dotenv import load_dotenv
from langchain.text_splitter import (
    Language,
    RecursiveCharacterTextSplitter,
)
load_dotenv()


HUGGINGFACEHUB_API_TOKEN = os.getenv("HUGGINGFACEHUB_API_TOKEN")

roast_prompt_template = """
<|system|>
Behold, the code you've summoned!
Prepare to witness its roasting by a master wordsmith, adept at turning flaws into fiery critique and satire.
Craft a concise, searingly funny yet insightful takedown that exposes every inefficiency and obfuscation.
Remember to use humor for roasting, and be ruthless!
No need to fabricate phantom features – the real ones are juicy enough!
When your wit has reached its peak and the roasting is done, unleash the final blow: "DONE!"
</s>
<|user|>
{code}
</s>
<|assistant|>
"""
sum_prompt_template = """
Behold, the code you've summoned! 
Prepare to witness its roasting by a master wordsmith, adept at turning flaws into fiery satire and parody. 
Craft a hilariously scathing yet insightful critique that exposes every inefficiency and obfuscation. 
Stick to the code in front of you, no need to conjure up phantom features – these real ones are juicy enough! 
When your wit reaches its peak and the roasting is done, unleash the final blow: "DONE!"
Before unleashing the final blow, make sure that the roast is done.

This is the original code snippet:
{code}

Now, pay attention, and let it be known – your task is not complete until every flaw has been dissected, every quirk exposed, and the roast is brought to its glorious conclusion. Finish what you started; leave no line unroasted.
</s>
{text}
"""
#LET HIM BE RUTHLESS!
roast_prompt = PromptTemplate(template=roast_prompt_template, input_variables=["code"])
sum_prompt = PromptTemplate(template=sum_prompt_template, input_variables=["code","text"])
def get_llm():
    return HuggingFaceHub(repo_id="openchat/openchat-3.5-0106",
                         model_kwargs={"temperature": 0.5,  
                                      "max_length": 1024,
                                      "min_length":700,
                                      "top_k": 5}) 

def get_roast(code,llm):
    chain = LLMChain(llm=llm, prompt=roast_prompt)
    cont_chain = LLMChain(llm=llm, prompt=sum_prompt)
    python_splitter = RecursiveCharacterTextSplitter.from_language(
    language=Language.PYTHON, chunk_size=500, chunk_overlap=0
    )
    
    code = preprocess_code(code)
    #python_docs = python_splitter.create_documents([code])
    fst_res = chain.invoke(code)
    iter = 0
    while('DONE' not in fst_res['text']):
        fst_res['text'] += cont_chain.invoke(fst_res)['text']
        iter +=1
        if(iter>=10):
            break

    return fst_res['text']
    
    
def preprocess_code(code:str)->str:
    lines = code.split('\n')
    cleaned_lines = [line.strip() for line in lines if line.strip()]
    code = '\n'.join(cleaned_lines)
    code = code.replace("    ","\t")
    code = re.sub(r'\n+', '\n', code)
    code = re.sub(r'\s+', ' ', code)
    return code


#llm = get_llm()
#user_pasted_code = 
"""
def getRecommendations(self,data):
        dataset = Recommender.getDataset()
        selected_cols = ['L4_SRC_PORT', 'L4_DST_PORT', 'PROTOCOL', 'L7_PROTO', 'IN_BYTES', 'OUT_BYTES', 'IN_PKTS', 'OUT_PKTS', 'TCP_FLAGS', 'FLOW_DURATION_MILLISECONDS']
        y = dataset['Encoded_Attack']
        dataset = dataset[selected_cols]
        data = data[selected_cols]
        cosine_similarities = cosine_similarity(data, dataset)
        most_similar_indices = cosine_similarities.argsort(axis=1)[:, ::-1]
        first_most_similar_indices = most_similar_indices[:, 0]
        second_most_similar_indices = most_similar_indices[:, 1]
        fst_pred = y.iloc[first_most_similar_indices]
        sec_pred = y.iloc[second_most_similar_indices]
        prediction = [fst_pred,sec_pred]
        return prediction
"""
#roast = get_roast(user_pasted_code,llm)
#print(roast)

    