def open_file(file_name):
    with open(file_name) as file:
        lines = file.readlines()
    contents = [element.replace("\n", "").split(",") for element in lines]
    return contents


def add_new_line(file_name, new_line):
    with open(file_name, "a") as file:
        file.write(new_line)


def update_line(file_name, edited_line, story_id):
    contents = open_file(file_name)
    contents = [item if item[0] != story_id else edited_line for item in contents]
    write_to_file(file_name, contents)


def write_to_file(file_name, contents):
    with open(file_name, "w") as file:
        for row in contents:
            new_line = ",".join(row)
            file.write(new_line + "\n")
