# what this file basically consists of is functions to add the obtained data into the file
# functions to delete the files
# function to create the project directory

import os


def create_project(directory):
    if not os.path.exists(directory):
        print("creating directory" + directory)
        os.makedirs(directory)


def create_files(project_name, base_url):
    queue = os.path.join(project_name, 'queue.txt')
    crawled = os.path.join(project_name, 'crawled.txt')
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, '')

# to write the links inside the files


def write_file(path, data):
    with open(path, 'w') as f:
        f.write(data)


# just to delete the contents of the file not the file itself
def delete_file_contents(path):
    open(path, 'w').close()


# to append the data to the existing file ,
def append_to_file(path, data):
    with open(path, 'w') as file:
        file.write(data + '\n')


# to convert the files to a set for faster operations
def file_to_set(file_name):
    results = set()
    with open(file_name, 'rt') as file:
        for line in file:
            results.add(line.replace('\n', ''))
    return results


# to convert a set into a file later...
def set_to_file(links, file_name):
    with open(file_name, 'w') as f:
        for link in sorted(links):
            f.write(link + "\n")

