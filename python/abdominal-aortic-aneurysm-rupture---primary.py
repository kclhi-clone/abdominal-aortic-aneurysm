# caliber, 2021.

import sys, csv, re

codes = ["G714.00","G714.11","G716.00","G716000"];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('abdominal-aortic-aneurysm-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["abdominal-aortic-aneurysm-rupture---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in codes): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["abdominal-aortic-aneurysm-rupture---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["abdominal-aortic-aneurysm-rupture---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
