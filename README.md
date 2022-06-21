# Radio Frequency ID (RFID) data
## Steps for analyzing RFID data
1. Pull Raw XML (Maja) files from the storage device to your local computer.
2. Convert XML files to CSV using python script (convert_XML_to_CSV.py)
3. Use Rmarkdown file (RFID_Analyses_2021.rmd) to read in raw csv "pings" and wrangle data for Track a Forager input
4. Use Track-a-forager software to turn raw "pings" into trips. Note: file must be 250MB or less. If your file size is over this amount refer to the the Rmarkdown (RFID_Analyses_2021.rmd) for instructions on using the _feedr_ R package. 
5. Once you have sucessfully run Track-a-Forager, continue through the Rmarkdown (RFID_Analyses_2021.rmd) to calculate your time activity budgets and parameters. 
