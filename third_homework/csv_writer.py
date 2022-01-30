import csv


def csv_writer():
    with open("raw_csv_book.csv", newline='') as csv_file:
        fieldnames = 'Title', 'Author', 'Pages', 'Genre'
        reader = csv.DictReader(csv_file)
        with open('converted_file.csv', mode='w', newline='') as outfile:
            writer = csv.DictWriter(outfile, fieldnames=fieldnames, delimiter=',')
            writer.writeheader()
            for row in reader:
                writer.writerow(
                    {'Title': row['Title'], 'Author': row['Author'], 'Pages': row['Pages'], 'Genre': row['Genre']})
