import pathlib

def get_package_root_directory() -> str:
    return pathlib.Path(__file__).parent

def get_data_root_directory() -> str:
    return get_package_root_directory() / 'data'

def get_data_file_path(filename: str) -> str:
    return get_data_root_directory() / filename