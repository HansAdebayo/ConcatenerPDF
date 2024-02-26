from PyPDF2 import PdfReader, PdfWriter

# Créer une instance de PdfWriter qui sera le PDF final
writer = PdfWriter()

# Liste des fichiers PDF à concaténer
pdf_files = ['Semestre1.pdf', 'Semestre2.pdf', 'Semestre3.pdf','Semestre4.pdf','Semestre5.pdf']

# Parcourir chaque fichier PDF
for pdf_file in pdf_files:
    reader = PdfReader(pdf_file)
    # Parcourir chaque page du fichier PDF actuel et l'ajouter au writer
    for page in reader.pages:
        writer.add_page(page)

# Écrire le fichier PDF final
with open("output.pdf", "wb") as output_pdf:
    writer.write(output_pdf)

print("Les fichiers PDF ont été concaténés avec succès en 'output.pdf'")
