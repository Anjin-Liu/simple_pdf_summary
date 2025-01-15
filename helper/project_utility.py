"""
Project Utility Functions
"""

import os


def get_promot_from_file(
    promot_file_path: str,
    params: dict,
) -> str:
    """Get promot command from local txt file and render it with a parameter dictionary

    Args:
        promot_file_path (str): local txt file path
        params (dict): a dictionary mapping the variables in the local txt file.

    Raises:
        FileNotFoundError: Raise file not found error

    Returns:
        str: Promot command as string
    """

    if not os.path.exists(promot_file_path):
        raise FileNotFoundError(
            f"Failed to locate promot template file: {promot_file_path}"
        )

    with open(promot_file_path, mode="r", encoding="utf-8") as file:
        query = file.read().format(**params)

    return query
