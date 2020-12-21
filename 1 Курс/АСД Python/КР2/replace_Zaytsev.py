import os


def csv_reader(file_path):
    exit_dict = {}
    with open(file_path, "r") as f_obj:
        for line in f_obj:
            line = line.replace("\n", "")
            ln = line.split(";")
            exit_dict[ln[0]] = ln[1]
    return exit_dict


def text_reader(file_path):
    exit_list = []
    with open(file_path, "r") as f_obj:
        for line in f_obj:
            line = line.replace("\n", " ")
            exit_list.append(line)
    return exit_list


def save_table(text_path, line):
    name = os.path.basename(text_path)
    text_path = text_path.replace(name, f"_{name}")
    with open(text_path, "w") as f_obj:
        for l in line:
            f_obj.write(l)


def main(text_path, csv_path):
    d = csv_reader(csv_path)
    t = text_reader(text_path)
    exit_list = []
    for line in t:
        for old, new in d.items():
            line = line.replace(old, new)
        exit_list.append(line)
    return exit_list


