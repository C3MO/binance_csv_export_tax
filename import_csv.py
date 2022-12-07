import csv

# Path to the Binance CSV file
binance_csv_file = "Binance_Trades.csv"

# Output file for tax report
output_file = "Binance_Tax_Report_Germany.csv"

# Dictionary mapping Binance trade types to German tax categories
trade_type_to_tax_category = {
    "TRADE": "Spekulationsgeschäft",
    "MARGIN_TRADE": "Termingeschäft",
}

# Read the Binance CSV file
with open(binance_csv_file, "r") as f:
    reader = csv.DictReader(f)

    # Create a list of dictionaries for the tax report
    tax_report = []

    # Loop through the Binance trades
    for row in reader:
        # Convert the trade type to the corresponding German tax category
        tax_category = trade_type_to_tax_category[row["Type"]]

        # Extract the trade date, coin name, and trade price
        trade_date = row["Date"]
        coin_name = row["Coin"]
        trade_price = float(row["Price"])

        # Calculate the trade amount in Euros
        trade_amount = float(row["Amount"]) * trade_price

        # Create a dictionary for the current trade with the necessary information for the tax report
        trade_data = {
            "Datum": trade_date,
            "Kategorie": tax_category,
            "Währung": coin_name,
            "Betrag in Euro": trade_amount,
        }

        # Add the trade data to the tax report
        tax_report.append(trade_data)

# Write the tax report to the output file
with open(output_file, "w") as f:
    writer = csv.DictWriter(f, fieldnames=["Datum", "Kategorie", "Währung", "Betrag in Euro"])
    writer.writeheader()
    writer.writerows(tax_report)