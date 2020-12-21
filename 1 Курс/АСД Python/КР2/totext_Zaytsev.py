def csv_reader(file_path):
    exit_dict = {}
    head = True
    with open(file_path, "r") as f_obj:
        for line in f_obj:
            line = line.replace("\n", "")
            line = line.split(";")
            print(line)
            if head:
                for l in line:
                    exit_dict[l] = []
                head = False
            else:
                for i, key in enumerate(exit_dict.keys()):
                    try:
                        exit_dict[key].append(line[i])
                    except:
                        exit_dict[key] = ""
    return exit_dict


def totext(d, newfilename):
    exittext = ""
    exittext += f"Файл содержит следующие заголовки {d.keys()}\n"
    for key, value in d.items():
        exittext += f"заголовок {key}, содержит знаения: \n"
        for i, v in enumerate(value):
            exittext += f"строка {i + 1} - {v}\n"
    with open(newfilename, "w") as f_obj:
        f_obj.write(exittext)
