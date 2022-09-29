# Radio Frequency ID (RFID)
## Steps for analyzing RFID data
1. Pull Raw XML (Maja) files from the storage device to your local computer.
2. Convert XML files to CSV using python script (convert_XML_to_CSV.py)
  - If running the python script in RStudio, the xml files must be in the same folder that the output will appear in, regardless of the location of the python script.
3. Use Rmarkdown file (RFID_Analyses_2021.rmd) to read in raw csv "pings" and wrangle data for Track a Forager input
4. Use [Track-a-forager software](https://colostate.sharepoint.com/:u:/s/Naug-Lab/EVCoVL19z8lDhjhpSVb7LU8Bj3qXQGPut9AHRHkohdFelQ?e=tH8gWa) to turn raw "pings" into trips. Note: file must be 250MB or less. If your file size is over this amount refer to the the Rmarkdown (RFID_Analyses_2021.rmd) for instructions on using the _feedr_ R package. 
5. Once you have sucessfully run Track-a-Forager, continue through the Rmarkdown (RFID_Analyses_2021.rmd) to calculate your time activity budgets and parameters. 
6. After running through RFID_Analyses_2021.rmd, move onto [RFID.MasterData.Analyses.rmd] (RFID.MasterData.Analyses.rmd)  for further model building and visualizations. 
