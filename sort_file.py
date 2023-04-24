import os
from pathlib import Path
from time import time

lst_extensions = []


def create_dir(new_path: Path):
    if not new_path.exists():
        Path.mkdir(new_path)


def check_empty_dir(name_dir: Path):
    for el in name_dir.iterdir():
        if el.is_dir():
            check_empty_dir(el)
            lists = os.listdir(el)
            if not lists:
                os.rmdir(el)


def move_file(file_path: Path, new_path: Path):
    if file_path.exists():
        file_path.replace(new_path)


def sort_directory(path_for_sorting: Path, new_path: Path):
    for el in path_for_sorting.iterdir():
        if el.is_dir():
            sort_directory(el, new_path)
        elif el.is_file():
            type_file = el.suffix[1:]
# create path to directory for file this type
            new_directory = new_path.joinpath(type_file)
            if type_file not in lst_extensions:
                lst_extensions.append(type_file)
                create_dir(new_directory)
            move_file(el, new_directory.joinpath(el.name))


def main():
    before = time()
    my_path = Path('C:\\Users\\Natali\\Desktop\\Motloh')
    new_path = Path('C:\\Users\\Natali\\Desktop\\SortedM')
    sort_directory(my_path, new_path)
    check_empty_dir(my_path)
    after = time()
    print(f'{after-before=}')


if __name__ == '__main__':
    exit(main())

# after-before=0.10467362403869629 - result of execution