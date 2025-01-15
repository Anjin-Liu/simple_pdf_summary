"""PDF to Text Module"""

__author__ = ("Anjin Liu anjindaily@gmail.com",)
__copyright__ = "Copyright 2025, Anjin"
__contributors__ = ["Anjin Liu"]

from .pdf_to_text_handler import (
    extract_raw_text_from_pdf,
    preprocess_raw_text,
    segment_preprocessed_text,
)

text_extract_func = [
    "extract_raw_text_from_pdf",
    "preprocess_raw_text",
    "segment_preprocessed_text",
]

__all__ = text_extract_func
