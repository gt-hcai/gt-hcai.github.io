import csv

csv_file = "HCAI labs.csv"

print('<table id="sortable-table">')
print("<thead>")
print("<tr>")

with open(csv_file, newline='', encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)

    for col in header:
        if "People" in col:
            print(f"<th data-sort="numeric">{col}</th>")
        else:
            print(f"<th>{col}</th>")

print("</tr>")
print("</thead>")
print("<tbody>")

with open(csv_file, newline='', encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)

    for row in reader:
        print("<tr>")
        for col, cell in zip(header, row):

            if col.lower() == "url" and cell.strip():
                if "None" not in cell: 
                    print(f'<td><a href="{cell}" target="_blank">{cell}</a></td>')
                else:
                    print(f"<td>{cell}</td>")
            else:
                print(f"<td>{cell}</td>")

        print("</tr>")

print("</tbody>")
print("</table>")