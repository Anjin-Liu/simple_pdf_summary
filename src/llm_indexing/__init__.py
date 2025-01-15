"""PDF to Text Module"""

__author__ = ("Anjin Liu anjindaily@gmail.com",)
__copyright__ = "Copyright 2025, Anjin"
__contributors__ = ["Anjin Liu"]

from .llm_indexing_handler import (
    index_text_to_chroma,
)

llm_indexing_func = [
    "index_text_to_chroma",
]

__all__ = llm_indexing_func
