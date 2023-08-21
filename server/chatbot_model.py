import os

from dotenv import load_dotenv

load_dotenv()

OPENAI_API_TYPE = os.getenv("OPENAI_API_TYPE")
OPENAI_API_VERSION = os.getenv("OPENAI_API_VERSION")
OPENAI_API_BASE = os.getenv("OPENAI_API_BASE")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

def run_model(promptt):
    
    import json
    from langchain import OpenAI, SQLDatabase, SQLDatabaseChain

    import os
    import os

    # from dotenv import load_dotenv
    os.environ["OPENAI_API_TYPE"] = OPENAI_API_TYPE
    os.environ["OPENAI_API_VERSION"] = OPENAI_API_VERSION
    os.environ["OPENAI_API_BASE"] = OPENAI_API_BASE
    os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
    # load_dotenv()
    
    from langchain.llms import AzureOpenAI

    llm = AzureOpenAI(
        deployment_name="gpt35turbo",
        model_name="gpt-35-turbo",
        temperature=0.8,

    )

    db = SQLDatabase.from_uri("sqlite:////home/aditya/Cryptography/llllllll.db")
    
    from langchain.prompts.prompt import PromptTemplate

    _DEFAULT_TEMPLATE = """Given an input question,first create a syntactically correct {dialect} query to run, the limit of the sql is 5.Also give a detailed answer of the question.
    Use the following format:

            Question: "Question here"

            SQLQuery: "SQL Query to run"

            SQLResult: "Result of the SQLQuery"

            Answer: "Give the final answer"

            Only use the following tables:

            {table_info}

            If someone asks for table foobar, they really mean the REAL_LARGE_DATABSE table.

            Question: {input}"""

    PROMPT = PromptTemplate(

        input_variables=["input", "table_info", "dialect"], template=_DEFAULT_TEMPLATE

    )

    db_chain = SQLDatabaseChain.from_llm(llm, db, prompt=PROMPT, verbose=True, return_intermediate_steps=True,top_k = 3)

    result = db_chain(promptt)
    ans = result["intermediate_steps"]
    # print(ans)
    x = ans[len(ans) - 1]
    print(x)
    return x
    # json_data = json.loads(x)
    # print(json_data)
    # print(type(json_data))
    # return json_data

# res = run_model("what are the different type machines")
