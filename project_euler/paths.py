import pathlib

def package_root_directory() -> str:
    return pathlib.Path(__file__).parent

def data_root_directory() -> str:
    return package_root_directory() / 'data'

def data_file_path(filename: str) -> str:
    return data_root_directory() / filename