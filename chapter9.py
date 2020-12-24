import os
from pathlib import Path

def evoke_path():
    """
    Use Path from pathlib to construct a path which will work on Windows and
    Posix systems.
    """
    path = Path('path', 'to', 'something')
    print(f"The path is {str(path)} and is a {type(path).__name__} object.")

def construct_path():
    """
    Use the \ math division operator to construct paths. Python will construct
    a WindowsPath or PosixPath object. The first or second value must be a Path
    object, or you will get an error.
    """
    print(Path('path') / 'to' / 'something')
    print(Path('path') / Path('to/something'))  # posix only!
    print(Path('path') / Path('to', 'something'))
    print('path' / Path('to') / 'something')
    # print('path' / 'to' / Path('something'))  # wrong!

def get_cwd_path():
    """
    Gives you the path to the directory that you were in when you ran this
    function. This is not to be confused with the path to the file locaiton,
    which is not necessarily the same.
    """
    print(os.getcwd())
    print(Path.cwd())

def change_cwd():
    """
    Gives you cwd, then changes cwd and gives you the new one.
    """
    print(Path.cwd())
    os.chdir("..")
    print(Path.cwd())
    os.chdir(os.path.abspath("/"))
    print(Path.cwd())

def get_file_path():
    """
    Gives you the path to the file containing the code currently being run.
    """
    file_location = Path(__file__)
    print(f"File containing this line you are reading is at {file_location}")

def create_many_folders():
    """
    Creates /something directory and every intermediary.
    """
    folders = Path(os.getcwd(), 'path', 'to', 'something')
    os.makedirs(folders)
