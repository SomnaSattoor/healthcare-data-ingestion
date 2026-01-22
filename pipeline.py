import pandas as pd
from datetime import datetime
import re
from config import PARTNER_CONFIG


def format_phone(phone):
    digits = re.sub(r"\D", "", str(phone))
    if len(digits) == 10:
        return f"{digits[:3]}-{digits[3:6]}-{digits[6:]}"
    return None


def transform_row(row, config):
    try:
        dob = datetime.strptime(str(row["dob"]), config["date_format"]).strftime("%Y-%m-%d")
    except Exception:
        dob = None

    return {
        "external_id": row["external_id"],
        "first_name": str(row["first_name"]).title() if pd.notna(row["first_name"]) else None,
        "last_name": str(row["last_name"]).title() if pd.notna(row["last_name"]) else None,
        "dob": dob,
        "email": str(row["email"]).lower() if pd.notna(row["email"]) else None,
        "phone": format_phone(row["phone"]),
        "partner_code": config["partner_code"]
    }


def ingest_file(file_path, partner_key):
    config = PARTNER_CONFIG[partner_key]

    df = pd.read_csv(file_path, delimiter=config["delimiter"])
    df = df.rename(columns=config["column_mapping"])

    df = df[df["external_id"].notna()]

    transformed = [transform_row(row, config) for _, row in df.iterrows()]
    return pd.DataFrame(transformed)


def main():
    acme_df = ingest_file("acme.txt", "acme")
    bettercare_df = ingest_file("bettercare.csv", "bettercare")

    final_df = pd.concat([acme_df, bettercare_df], ignore_index=True)

    print("\n===== FINAL UNIFIED OUTPUT =====\n")
    print(final_df)

    final_df.to_csv("unified_output.csv", index=False)
    print("\nSaved unified_output.csv\n")


if __name__ == "__main__":
    main()

