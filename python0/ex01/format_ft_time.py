from datetime import datetime


def main() -> None:
    dt = datetime.today()
    s = dt.timestamp()
    formatted_date = f"{dt.strftime('%b %d %Y')}"
    intro = "Seconds since January 1, 1970:"
    content = f"{s:,.4f} or {s:.2e}"
    outro = "in scientific notation"
    print(f"{intro} {content} {outro}")
    print(formatted_date)


if __name__ == "__main__":
    main()
