"""PDF to Text Module"""

__author__ = ("Anjin Liu anjindaily@gmail.com",)
__copyright__ = "Copyright 2025, Anjin"
__contributors__ = ["Anjin Liu"]

from .generation_handler import (
    load_vectorestore,
    search_and_generate_report,
)

llm_generation_func = [
    "load_vectorestore",
    "search_and_generate_report",
]

__all__ = llm_generation_func
