"""_summary_

Returns:
    _type_: _description_
"""

from langchain_community.vectorstores import Chroma
from langchain_google_genai.chat_models import ChatGoogleGenerativeAI

from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain


def load_vectorestore(
    vectorestore_path,
    embedding_llm,
):
    """Load vectorestore

    Args:
        vectorestore_path (_type_): _description_
        embedding_llm (_type_): _description_

    Returns:
        _type_: _description_
    """
    vectorstore = Chroma(
        embedding_function=embedding_llm,
        persist_directory=vectorestore_path,
    )
    return vectorstore


def search_and_generate_report(
    query: str,
    vectorstore: Chroma,
    chatllm: ChatGoogleGenerativeAI,
) -> str:
    """Search and Generate Reports from Chroma Database

    Args:
        query (str): _description_
        vectorstore (Chroma): _description_
        llm (ChatGoogleGenerativeAI): _description_

    Returns:
        str: _description_
    """

    # Search Chroma database for relevant chunks
    search_results = vectorstore.similarity_search(query, k=10)

    # Extract matching chunks
    matching_chunks = [result.page_content for result in search_results]

    # Combine matching chunks into a single text
    combined_text = "\n".join(matching_chunks)

    # Define the report prompt
    # TODO: move the prompt template to a file, this is only to show that I know how to use PromptTemplate :)
    report_prompt = PromptTemplate(
        input_variables=["input_text"],
        template="Generate a detailed financial summary report highlighting the financial health of the company. based on the following text:\n{input_text}",
    )

    # Generate the report using the LLM
    chain = LLMChain(llm=chatllm, prompt=report_prompt)
    report = chain.run(input_text=combined_text)

    return report
