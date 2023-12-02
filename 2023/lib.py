from loguru import logger
import typing
import os


def get_data_path(filename: str) -> str:
    """
    Creates flexible paths for input files to ensure
    they execute at any folder level.
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))

    while True:
        # Check for data file in current directory
        data_path = os.path.join(current_dir, "data", filename)
        if os.path.exists(data_path):
            return data_path

        # Check for the data file in subdirectory
        for sub_dir in os.listdir(current_dir):
            sub_dir_path = os.path.join(current_dir, sub_dir)
            if os.path.isdir(sub_dir_path):
                data_path = os.path.join(sub_dir_path, "data", filename)
                if os.path.exists(data_path):
                    return data_path

        # Move up one directory level
        new_dir = os.path.dirname(current_dir)
        if new_dir == current_dir:
            # We have reached the root directory without finding the file
            raise FileNotFoundError(f"Data file '{filename}' not found")
        current_dir = new_dir


def read_files(fn):
    f = get_data_path(fn)
    data = []
    for line in open(f, "r"):
        data.append(line.rstrip())
    return data
