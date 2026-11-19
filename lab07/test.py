from formats import parse_settings, merge_by_key

print(parse_settings(["rate: 3,5 # с запятой"]))

print(merge_by_key(
    [{"id": "1", "город": "Азов"}],
    {"1": {"регион": "Ростовская"}},
    "id"
))