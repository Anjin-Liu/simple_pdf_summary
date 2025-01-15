"""_summary_

Example:
    $ export PYTHONPATH="${PYTHONPATH}:$(pwd)"
    $ python -m step.s04_llm_report_geneartion --file_name test_1
"""

# standard
import argparse
import warnings

# project modules
from helper.project_config import ProjectConfig as Config
from helper.project_config import ProjectChatLLMConfig as LLMConfig
from helper.project_config import ProjectEmbeddingLLMConfig as EmbeddingLLMConfig
from src import report_generation as generation_handler

# TODO: Ignore all warnings for now
warnings.filterwarnings("ignore")


def parse_args() -> dict:
    """Parser for command-line options, arguments and sub-commands

    Returns:
        dict: a dictionary of arguments
    """

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--file_name",
        type=str,
        help="file name",
        required=True,
    )

    params_dict = vars(parser.parse_args())
    print(params_dict)

    return params_dict


def main(
    file_name: str,
    **_,
) -> None:

    vectorestore_path = f"{Config.INDEXED_VECTOR_DATA_PATH}/{file_name}.chroma_db"
    report_markdown_file_path = f"{Config.REPORT_DATA_PATH}/{file_name}_report.md"

    print("# ======================================== #")
    print("# Step 1. Load indexed preprocessed text   #")
    print("# ======================================== #")
    embedding_llm = EmbeddingLLMConfig.EmbeddingLLM
    vectorestore = generation_handler.load_vectorestore(
        vectorestore_path, embedding_llm
    )

    print("# ======================================== #")
    print("# Step 2. Query revenue, net income etc.   #")
    print("# ======================================== #")
    chat_llm = LLMConfig.ChatLLM
    query = "What are the key financial metrics such as revenue, net income, operating expenses, and cash flow?"

    report_text = generation_handler.search_and_generate_report(
        query,
        vectorestore,
        chat_llm,
    )

    # Save the report_text to the file
    with open(report_markdown_file_path, "w", encoding="utf-8") as file:
        file.write(report_text)


if __name__ == "__main__":
    params = parse_args()
    main(**params)
