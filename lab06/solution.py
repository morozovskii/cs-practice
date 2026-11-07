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


# deepest_path(paths)         # "docs/img/logo.png"

# human_size(900)             # "900 Б"
# human_size(1536)            # "1.5 КБ"
# human_size(5 * 1024 * 1024) # "5.0 МБ"
