"""_summary_

Example:
    $ export PYTHONPATH="${PYTHONPATH}:$(pwd)"
    $ python -m step.s01_extract_pdf_text --file_name test_1
"""

# standard
import argparse
import warnings

# project modules
from helper.project_config import ProjectConfig as Config
from helper.project_config import ProjectChatLLMConfig as LLMConfig
from src import pdf_to_text as pdf_to_text_handler

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

    print("# ======================================== #")
    print("# Step 1. Extracting text from PDF         #")
    print("# ======================================== #")
    file_path = Config.INPUT_DATA_PATH / f"{file_name}.pdf"
    raw_txt = pdf_to_text_handler.extract_raw_text_from_pdf(file_path)

    # Save the raw_txt to the file
    raw_txt_path = Config.EXTRACT_RAW_DATA_PATH / f"{file_name}.txt"
    with open(raw_txt_path, "w", encoding="utf-8") as file:
        file.write(raw_txt)

    print("# ======================================== #")
    print("# Step 2. Preprocessing raw text           #")
    print("# ======================================== #")
    preprocessed_txt = pdf_to_text_handler.preprocess_raw_text(
        raw_txt,
        LLMConfig.ChatLLM,
    )

    # Save the preprocessed_txt to the file
    preprocessed_txt_path = Config.PREPROCESSED_DATA_PATH / f"{file_name}.txt"
    with open(preprocessed_txt_path, "w", encoding="utf-8") as file:
        file.write(preprocessed_txt)

    print("# ======================================== #")
    print("# Step 3. Segment preprocessed text        #")
    print("# ======================================== #")
    seg_txt = pdf_to_text_handler.segment_preprocessed_text(
        preprocessed_txt,
        LLMConfig.ChatLLM,
    )

    # Save the preprocessed_txt to the file
    preprocessed_txt_path = Config.PREPROCESSED_DATA_PATH / f"{file_name}_seg.txt"
    with open(preprocessed_txt_path, "w", encoding="utf-8") as file:
        file.write(seg_txt)


if __name__ == "__main__":
    params = parse_args()
    main(**params)
