
from logstats import parse_event, count_levels, top_errors, format_report


def main():
    file_name = input().strip()

    with open(file_name, encoding="utf-8") as log:
        counts = count_levels(log)

    with open(file_name, encoding="utf-8") as log:
        errors = top_errors(log, 3)

    total = sum(counts.values())
    error_count = counts.get("ERROR", 0)    
    broken_count = counts.get("BROKEN", 0)

    print(total)
    print(error_count)
    print(broken_count)

    report = format_report(counts, errors)

    with open("report.txt", "w", encoding="utf-8") as file:
        file.write(report)


if __name__ == "__main__":
    main()
