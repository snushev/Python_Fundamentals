import re

number_of_barcodes = int(input())

for i in range(0, number_of_barcodes):
    barcode = input()
    regex = r"@#+[A-Z][a-zA-Z0-9]{4,}[A-Z]@#+"
    matches = re.findall(regex, barcode)

    if matches:
        new_regex = r"\d"
        new_matches = re.findall(new_regex, barcode)
        if new_matches:
            asd = "".join(new_matches)
            print(f"Product group: {asd}")
        else:
            print("Product group: 00")
    else:
        print("Invalid barcode")