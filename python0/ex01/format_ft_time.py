from datetime import datetime


def main() -> None:
    dt = datetime.today()
    seconds = dt.timestamp()
    formatted_date = f"{dt.strftime('%b %d %Y')}"
    print(
        f"Seconds since January 1, 1970: {seconds:,.4f} or {seconds:.2e} in scientific notation"
    )
    print(formatted_date)


if __name__ == "__main__":
    main()
