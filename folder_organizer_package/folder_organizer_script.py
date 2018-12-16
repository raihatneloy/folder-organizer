from os import listdir, mkdir, rename
from os.path import isfile, join, exists, expanduser, abspath

import click


source_folder = '/home/raihatneloy/Downloads'
items_list = listdir(source_folder)
extension_to_folder_mapper = {
    'jpeg jpg png gif svg': 'images',
    'app dmg pkg deb': 'applications',
    'txt xlsx xls doc docx pdf': 'text_files',
    'zip tar gz bz2': 'compressed_files',
    'py pyc whl sh': 'programming_files',
    'mp3': 'audio_files'
}


def get_file_extension(file_name):
    split_name = file_name.split('.')
    return split_name[-1]


def create_folder(name):
    if not exists(join(source_folder, name)):
        mkdir(join(source_folder, name))


def move_file_to_folder(file_name, folder_name):
    old_path = join(source_folder, file_name)
    new_path = join(source_folder, folder_name, file_name)

    print old_path, '|#|', new_path
    # rename(old_path, new_path)


def map_extension_to_folder(extension, name):
    folder_name = 'others'

    for extension_list, destination_folder in extension_to_folder_mapper.iteritems():
        if extension in extension_list.split(' '):
            folder_name = destination_folder
            break

    create_folder(folder_name)
    move_file_to_folder(name, folder_name)


@click.command()
@click.argument('sourcefolder')
def main(sourcefolder):
    global source_folder, items_list

    source_folder = abspath(expanduser(sourcefolder))
    items_list = listdir(source_folder)

    for item_name in items_list:
        if isfile(join(source_folder, item_name)):
            extension = get_file_extension(item_name)
            map_extension_to_folder(extension, item_name)


if __name__ == "__main__":
    main()