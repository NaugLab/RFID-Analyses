# Importing the required libraries
import xml.etree.ElementTree as Xet
import pandas as pd
import glob

cols = ["UTCTime", "ReaderID", "Address", "UID", "ScanCount", "Type", "UTCTime_Creation", "Company", "Program_Version"]
rows = []

# Loop through xml files in directory
for filepath in glob.iglob('*.xml'):

    # Parsing the XML file
    xmlparse = Xet.parse(filepath)
    root = xmlparse.getroot()

    # Get the information dataframe
    info = root.find("Information")
    utc_creation = info.find("UTCTime_Creation").text
    company = info.find("Company").text
    version = info.find("Program_Version").text

    # Collect each data point
    for i in root.findall("Dataset"):
        utc = i.find("UTCTime").text
        readerid = i.find("ReaderID").text
        adr = i.find("Address").text
        uid = i.find("UID").text
        scan = i.find("ScanCount").text
        type = i.find("Type").text

        rows.append({"UTCTime": utc,
                     "ReaderID": readerid,
                     "Address": adr,
                     "UID": uid,
                     "ScanCount": scan,
                     "Type": type,
                     "UTCTime_Creation": utc_creation,
                     "Company": company,
                     "Program_Version": version})

df = pd.DataFrame(rows, columns=cols)

# Writing dataframe to csv
df.to_csv('RFID_raw_output_2021.csv', index=False)
