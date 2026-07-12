import csv
from pathlib import Path

script_dir = Path(__file__).resolve().parent

project_root = script_dir.parent
data_folder = project_root / "data"

output_file = project_root/"output.csv"
# print(project_root)

for file_path in data_folder.glob("*.csv"):
    # print(f"Processing file; {file_path}")
    with open(file_path, mode='r', encoding='utf-8') as infile, open(
        output_file, mode="w", newline="", encoding="utf-8"
    ) as outfile:
        csv_reader = csv.DictReader(infile)

        csv_writer = csv.DictWriter(
            outfile, fieldnames=["Sales", "Date", "Region"])
        csv_writer.writeheader()
        match_count = 0
        for row in csv_reader:
            if row.get("product") == "pink morsel":
                match_count += 1
                clean_price = (
                    row["price"].replace("$", "").replace(",", "").strip()
                )
                sales = float(row["quantity"]) * float(clean_price)
                formatted_sales = f"${sales:,.2f}"

                output_data = {
                    "Sales": formatted_sales,
                    "Date": row["date"],
                    "Region": row["region"]
                }

                csv_writer.writerow(output_data)

        # (f"Finished {file_path} with {match_count} matches saved")
