"""_summary_

Returns:
    _type_: _description_
"""

from pathlib import Path
import pathlib
import pdfplumber

# Project Utility Functions
import helper.project_utility as Util

SCRIPT_DIR = str(pathlib.Path(__file__).parent.resolve())


def extract_raw_text_from_pdf(pdf_path: str) -> str:
    """
    Extract raw text from a PDF file.

    Args:
        pdf_path (str): Path to the PDF file.

    Raises:
        FileNotFoundError:  If the file does not exist.

    Returns:
        str: The extracted raw text.
    """
    file_path = Path(pdf_path)

    # Check if the file exists; raise an error if not
    if not file_path.exists() or not file_path.is_file():
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")

    text = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            text += page.extract_text()

    return text


def preprocess_raw_text(
    raw_text: str,
    llm_instance: object,
) -> str:
    # TODO: Add the rule-based manual preprocessing steps here
    # =================================================
    #
    # =================================================

    promot_template_path = SCRIPT_DIR + "/prompt_templates/01_raw_text_cleansing.txt"
    promot_param_dict = {
        "raw_text": raw_text,
    }
    promot_input = Util.get_promot_from_file(promot_template_path, promot_param_dict)

    # Get the preprocessed text
    preprocessed_text = llm_instance.invoke(promot_input).content

    return preprocessed_text


def segment_preprocessed_text(
    preprocessed_text,
    llm_instance,
):

    promot_template_path = SCRIPT_DIR + "/prompt_templates/02_segment_text.txt"
    promot_param_dict = {
        "preprocessed_text": preprocessed_text,
    }
    promot_input = Util.get_promot_from_file(promot_template_path, promot_param_dict)

    # Get the preprocessed text
    preprocessed_text = llm_instance.invoke(promot_input).content

    return preprocessed_text
