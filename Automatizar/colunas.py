import csv

# Open the input CSV file
with open('end2.csv', newline='') as infile:
    reader = csv.reader(infile)

    # Create a list to store the new rows
    new_rows = []

    # Iterate through each row in the input CSV file
    for row in reader:

        # Iterate through each cell in the row
        for cell in row:

            # Check if the cell begins with the word "cidade"
            if cell.startswith('Cidade:'):

                # If so, create a new row with only that cell and append it to the new_rows list
                new_row = [cell]
                new_rows.append(new_row)

                # Remove the cell from the current row
                row.remove(cell)

        # Append the current row (minus the "cidade" cells) to the new_rows list
        new_rows.append(row)

# Open the output CSV file
with open('end2.csv', 'w', newline='') as outfile:
    writer = csv.writer(outfile)

    # Write each new row to the output CSV file
    for new_row in new_rows:
        writer.writerow(new_row)
