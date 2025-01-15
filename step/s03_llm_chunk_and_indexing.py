"""_summary_

Example:
    $ export PYTHONPATH="${PYTHONPATH}:$(pwd)"
    $ python -m step.s03_llm_chunk_and_indexing --file_name test_1
"""

# standard
import argparse
import warnings

# project modules
from helper.project_config import ProjectConfig as Config
from helper.project_config import ProjectEmbeddingLLMConfig as EmbeddingLLMConfig
from src import llm_indexing as llm_indexing_handler

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

    seg_text_file_path = f"{Config.PREPROCESSED_DATA_PATH}/{file_name}_seg.txt"
    vectorestore_path = f"{Config.INDEXED_VECTOR_DATA_PATH}/{file_name}.chroma_db"
    embedding_llm = EmbeddingLLMConfig.EmbeddingLLM

    print("# ======================================== #")
    print("# Step 1. Chunk and Indexing               #")
    print("# ======================================== #")
    with open(seg_text_file_path, "r", encoding="utf-8") as file:
        seg_text = file.read()

    llm_indexing_handler.index_text_to_chroma(
        seg_text,
        embedding_llm,
        vectorestore_path,
    )


if __name__ == "__main__":
    params = parse_args()
    main(**params)
