"""Prefect related utilities."""

import inspect


def generate_flow_name() -> str:
    """Use this function to auto generate flow name."""
    current_file_path = inspect.stack()[1].filename
    current_file_name = current_file_path.split("/")[-1].split(".")[0]
    current_folder_name = current_file_path.split("/")[-2].split(".")[0]
    return f"{current_folder_name}_{current_file_name}"
