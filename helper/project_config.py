"""Project Config Class"""

# Import system Libraries
import pathlib
import json

# Import LLM Libraries
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai import GoogleGenerativeAIEmbeddings


class ProjectConfig:
    """Config Class"""

    # Project Path Config
    PROJECT_PATH = pathlib.Path(__file__).parent.parent.resolve()

    # Data Storage Paths Config
    INPUT_DATA_PATH = PROJECT_PATH / "data" / "01_input"
    EXTRACT_RAW_DATA_PATH = PROJECT_PATH / "data" / "02_extracted_raw_data"
    PREPROCESSED_DATA_PATH = PROJECT_PATH / "data" / "03_preprocessed_data"
    INDEXED_VECTOR_DATA_PATH = PROJECT_PATH / "data" / "04_indexed_vector_data"
    REPORT_DATA_PATH = PROJECT_PATH / "data" / "05_report_data"


# Load credential JSON file
llm_cred = {}
with open(
    f"{ProjectConfig.PROJECT_PATH}/credentials/llm-cred.json",
    "r",
    encoding="utf-8",
) as file:
    llm_cred = json.load(file)


class ProjectChatLLMConfig:
    """Project ChatLLM Config Class"""

    ChatLLM = ChatGoogleGenerativeAI(
        model="gemini-1.5-pro",
        temperature=0,
        max_tokens=None,
        max_retries=1,
        google_api_key=llm_cred["google-api-key"],
    )


class ProjectEmbeddingLLMConfig:
    """Project EmbeddingLLM Config Class"""

    EmbeddingLLM = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001",
        google_api_key=llm_cred.get("google-api-key"),
    )
