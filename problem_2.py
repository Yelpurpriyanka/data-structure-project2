#File Recursion problem
import os


def find_files(suffix='', path='.'):
    """
    Find all files beneath path with file name suffix.
    Note that a path may contain further subdirectories
    and those subdirectories may also contain further subdirectories.
    There are no limit to the depth of the subdirectories can be.
    Args:
      suffix(str): suffix of the file name to be found
      path(str): path of the file system
    Returns:
       a list of paths
    """
    if path is None:
        return "No path specified"
    elif not isinstance(path, str):
        return "Path isn't a valid path"

    files = []
    for file in os.listdir(path):

        file_path = os.path.join(path, file)

        if os.path.isfile(file_path):

            if file.endswith(suffix):
            
                files.append(file_path)

        if os.path.isdir(file_path):
            
            new_files = find_files(suffix, file_path)

            files.extend(new_files)

    return files


# Edge test cases
print("find_files(, None):", find_files('', None), '\n')
print("find_files(, -1):", find_files('', -1), '\n')

# General test cases
print("find_files(\"\", .):", find_files("", "."), '\n')
print("find_files(\".py\", .):", find_files(".py", "."), '\n')
print("find_files(\".pdf\", .):", find_files(".pdf", "."), '\n')
print("find_files(\".c\", .):", find_files(".c", "."), '\n')
print("find_files(\".gitkeep\", .):", find_files(".gitkeep", "."), '\n')