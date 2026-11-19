
import json


def csv_to_records(text):
    lines = text.strip().splitlines()

    if not lines:
        return []

    headers = [item.strip() for item in lines[0].split(",")]

    result = []

    for line in lines[1:]:
        if not line.strip():
            continue

        values = [item.strip() for item in line.split(",")]

        record = dict(zip(headers, values))
        result.append(record)

    return result


def parse_settings(lines):
    result = {}
    current_list = None

    def convert_value(value):
        if value in ("true", "yes"):
            return True

        if value in ("false", "no"):
            return False

        try:
            return int(value)
        except ValueError:
            pass

        try:
            return float(value)
        except ValueError:
            return value

    for line in lines:
        line = line.split("#")[0].strip()

        if not line:
            continue

        if line.startswith("- "):
            if current_list is not None:
                value = line[2:].strip()
                result[current_list].append(convert_value(value))
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
                result[key] = convert_value(value)

    return result


def merge_by_key(rows: list[dict], extra: dict, key: str = "id") -> list[dict]:
    result = []

    for row in rows:
        record = {}

        if key in row:
            extra_record = extra.get(row[key], {})
            record.update(extra_record)

        record.update(row)

        result.append(record)

    return result


def records_to_json(records):
    return json.dumps(records,ensure_ascii=False,indent=2,sort_keys=True)
