def window_function(spark):
    pharmaData = (("Atorvastatin", "Cardiology", "Hyperlipidemia", "20 mg", "PO OD", 45, "Myalgia"), \
                  ("Metoprolol", "Cardiology", "Hypertension", "50 mg", "PO BID", 30, "Fatigue"), \
                  ("Lisinopril", "Cardiology", "Hypertension", "10 mg", "PO OD", 30, "Nonproductive cough"), \
                  ("Metformin", "Diabetes", "Type 2 diabetes mellitus", "500 mg", "PO BID with meals", 20, "Diarrhea"), \
                  ("Atorvastatin", "Cardiology", "Hyperlipidemia", "20 mg", "PO OD", 45, "Myalgia"), \
                  ("Insulin Glargine", "Diabetes", "Diabetes mellitus", "10 units", "subcut at bedtime", 300, "Hypoglycemia"), \
                  ("Semaglutide", "Diabetes", "Type 2 diabetes mellitus", "0.5 mg", "subcut weekly", 950, "Nausea"), \
                  ("Amoxicillin", "Antibiotics", "Acute otitis media", "500 mg", "PO q8h", 15, "Maculopapular rash"), \
                  ("Azithromycin", "Antibiotics", "Community-acquired pneumonia", "250 mg", "PO OD x 4 days", 25, "Diarrhea"), \
                  ("Amlodipine", "Cardiology", "Hypertension", "5 mg", "PO OD", 30, "Peripheral edema"))

    columns = ["drug_name", "drug_class", "indication", "dosage", "regimen", "price_usd", "side_effect"]
    df = spark.createDataFrame(data=pharmaData, schema=columns)
    df.printSchema()
    df.show(truncate=False)

    cardio_df = df.filter(df.drug_class == "Cardiology")
    cardio_df.show(truncate=False)
