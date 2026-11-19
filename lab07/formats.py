
import json


def csv_to_records(text):
    lines = text.strip().splitlines()

    if not lines:
        return []

    headers = lines[0].split(",")

    result = []

    for line in lines[1:]:
        values = line.split(",")
        record = dict(zip(headers, values))
        result.append(record)

    return result


def parse_settings(lines):
    result = {}
    current_list = None

    for line in lines:
        line = line.split("#")[0].strip()

        if not line:
            continue

        if line.startswith("- "):
            if current_list is not None:
                value = line[2:].strip()
                result[current_list].append(value)
            continue

        if ":" in line:
            key, value = line.split(":", 1)

            key = key.strip()
            value = value.strip()

            if value == "":
                result[key] = []
                current_list = key
            else:
                current_list = None

                if value in ("true", "yes"):
                    result[key] = True
                elif value in ("false", "no"):
                    result[key] = False
                else:
                    try:
                        if "." in value:
                            result[key] = float(value)
                        else:
                            result[key] = int(value)
                    except ValueError:
                        result[key] = value

    return result


def merge_by_key(rows):
    result = []

    for row in rows:
        record = {}

        if key in row and row[key] in extra:
            record.update(extra[row[key]])

        record.update(row)

        result.append(record)

    return result


def records_to_json(records):
    return json.dumps(records,ensure_ascii=False,indent=2,sort_keys=True)
