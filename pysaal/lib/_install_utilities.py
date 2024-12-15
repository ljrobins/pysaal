from pathlib import Path
from shutil import copyfile


def install_linux_library():
    LIB_PATH = Path(__file__).parent
    usr_ld_library_path = Path("/usr/lib/")

    all_files = list(LIB_PATH.glob("*"))

    for file in all_files:
        if ".py" not in file.suffix and ".dylib" not in file.suffix and ".DLL" not in file.suffix:
            copyfile(file, usr_ld_library_path / file.name)
