import csv
from reportlab.pdfgen import canvas


def save_csv(filename, data):
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=list(data))
        writer.writeheader()
        writer.writerow(data)


def load_csv(filename, field_names):
    with open(filename, newline="", encoding="utf-8-sig") as file:
        rows = list(csv.DictReader(file))

    if len(rows) != 1:
        raise ValueError("Use a CSV containing one product.")

    data = rows[0]

    for name in field_names:
        if name not in data or data[name] is None:
            raise ValueError("Use the same columns as an exported CSV.")

    return data


def save_pdf(filename, text):
    pdf = canvas.Canvas(filename)
    pdf.setFont("Helvetica", 12)
    y = 800

    for line in text.splitlines():
        pdf.drawString(50, y, line)
        y = y - 22

    pdf.save()
