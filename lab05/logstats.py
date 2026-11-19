
def parse_event(line): 
    parts = line.strip().split(maxsplit=2)

    if len(parts) != 3:
        raise ValueError("Неверный формат строки")

    time, level, message = parts

    if level not in ("DEBUG", "INFO", "WARNING", "ERROR"):
        raise ValueError("Неизвестный уровень")

    return {"time": time,"level": level,"message": message}


def count_levels(lines):
    counts = {}

    for line in lines:
        try:
            event = parse_event(line)
            level = event["level"]
            counts[level] = counts.get(level, 0) + 1
        except ValueError:
            continue

    return counts

def top_errors(lines: list[str], n: int) -> list[list]:
    errors = {}

    for line in lines:
        if not line.strip():
            continue

        try:
            event = parse_event(line)

            if event["level"] == "ERROR":
                message = event["message"]
                errors[message] = errors.get(message, 0) + 1

        except ValueError:
            continue

    sorted_errors = sorted(errors.items(),key=lambda item: (-item[1], item[0]))

    return [[message, count] for message, count in sorted_errors[:n]]

def format_report(counts: dict, errors: list[list]) -> str:
    report = "Отчёт по журналу\n\n"

    for level in sorted(counts):
        report += f"{level}: {counts[level]}\n"

    report += "\nЧастые ошибки:\n"

    for message, count in errors:
        report += f"- {message} — {count}\n"

    return report
