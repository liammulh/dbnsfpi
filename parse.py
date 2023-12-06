import csv


FILE_NAME = "dbNSFP4.3a_variant.chrX-rg-for-152959399.tsv"


def print_columns():
    with open(FILE_NAME) as tsv:
        rows = []
        for row in csv.reader(tsv, delimiter="\t"):
            rows.append(row) 
        columns = list(zip(*rows))
        for column in columns:
            print(column)


if __name__ == "__main__":
    print_columns()
