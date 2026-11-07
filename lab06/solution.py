paths = ["docs/report.PDF", "notes.txt", "docs/img/logo.png", "Makefile"]

def count_by_extension(paths):
    extensions = {}
    for path in paths:
        if "." in path:
            extension = path.split(".")[-1].lower()
        else:
            extension = ""
        
        extensions[extension] = extensions.get(extension, 0) + 1
    return extensions
print(count_by_extension(paths))

def deepest_path(paths):
    if len(paths) == 0:
        return ""
    deepest = paths[0]
    for path in paths:
        if len(path.split("/")) > len(deepest.split("/")):
            deepest = path
        elif len(path.split("/")) == len(deepest.split("/")):
            if path < deepest:
                deepest = path
    return deepest
print(deepest_path(paths))


def human_size(n_bytes):
    if n_bytes < 1024:
        return str(n_bytes) + "Б"
    elif n_bytes < 1024 * 1024:
        return str(round(n_bytes / 1024, 1)) + "КБ"
    elif n_bytes < 1024 * 1024 * 1024:
        return str(round(n_bytes / 1024 / 1024, 1)) + "МБ"
    elif n_bytes < 1024 * 1024 * 1024 * 1024:
        return str(round(n_bytes / 1024 / 1024 / 1024, 1)) + "ГБ"
    else:
        return str(round(n_bytes / 1024 / 1024 / 1024 / 1024, 1)) + "ТБ"
print(human_size(900))
print(human_size(1536))
print(human_size(5 * 1024 * 1024))



