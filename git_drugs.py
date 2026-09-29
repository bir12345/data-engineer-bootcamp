def window_function(spark):
    pharmaData = (("Omeprazole", "PPI", "GERD", "20 mg", "PO OD before breakfast", 12, "Headache"), \
                  ("Pantoprazole", "PPI", "Erosive esophagitis", "40 mg", "PO OD", 18, "Diarrhea"), \
                  ("Esomeprazole", "PPI", "GERD", "40 mg", "PO OD", 25, "Headache"), \
                  ("Omeprazole", "PPI", "GERD", "20 mg", "PO OD before breakfast", 12, "Headache"), \
                  ("Famotidine", "H2 blocker", "Duodenal ulcer", "40 mg", "PO at bedtime", 10, "Headache"), \
                  ("Ondansetron", "Antiemetic", "Chemotherapy-induced nausea", "8 mg", "PO q8h PRN", 22, "Constipation"), \
                  ("Metoclopramide", "Prokinetic", "Diabetic gastroparesis", "10 mg", "PO QID (AC & HS)", 14, "Extrapyramidal symptoms"), \
                  ("Loperamide", "Antidiarrheal", "Acute diarrhea", "2 mg", "PO PRN after loose stool", 8, "Constipation"), \
                  ("Lactulose", "Laxative", "Chronic constipation", "15 mL", "PO OD", 14, "Flatulence"), \
                  ("Bisacodyl", "Laxative", "Constipation", "5 mg", "PO at bedtime", 6, "Abdominal cramps"))

    columns = ["drug_name", "drug_class", "indication", "dosage", "regimen", "price_usd", "side_effect"]
    df = spark.createDataFrame(data=pharmaData, schema=columns)
    df.printSchema()
    df.show(truncate=False)

    ppi_df = df.filter(df.drug_class == "PPI")
    ppi_df.show(truncate=False)
