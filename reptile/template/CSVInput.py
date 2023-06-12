import csv

class CSVHandler:
    def __init__(self, filename, headers, encoding="utf-8"):
        self.filename = filename
        self.headers = headers
        self.encoding = encoding

        with open(self.filename, mode='w', newline='', encoding=self.encoding) as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(self.headers)

    def append_row(self, row_data):
        with open(self.filename, mode='a', newline='', encoding=self.encoding) as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(row_data)

    def insert_chinese_annotation(self, row_idx, col_idx, annotation):
        with open(self.filename, mode='r', newline='', encoding=self.encoding) as csvfile:
            reader = csv.reader(csvfile)
            rows = [row for row in reader]

        rows[row_idx][col_idx] += f"（{annotation}）"

        with open(self.filename, mode='w', newline='', encoding=self.encoding) as csvfile:
            writer = csv.writer(csvfile)
            writer.writerows(rows)