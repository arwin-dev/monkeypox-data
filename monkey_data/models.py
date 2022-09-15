from pickle import TRUE
from pyexpat import model
from django.db import models

class Monkey(models.Model):
    ID = models.CharField(max_length=50,primary_key=True)
    Status = models.CharField(max_length=50,blank=True)
    Location = models.CharField(max_length=50,blank=True)
    City = models.CharField(max_length=100,blank=True)
    Country = models.CharField(max_length=100,blank=False)
    Age = models.CharField(max_length=10,blank=True,null=True)
    Gender = models.CharField(max_length=100,blank=True)
    Date_onset = models.CharField(max_length=10,blank=True,null=True)
    Date_confirmation = models.CharField(max_length=10,blank=True)

    Symptoms = models.CharField(max_length=200,blank=True,null=True)
    Hospitalised = models.BooleanField(null=True,blank=True)
    Date_hospitalisation = models.CharField(max_length=10,blank=True)
    Isolated = models.BooleanField(null=True,blank=True)
    Date_Isolation = models.CharField(max_length=10,blank=True)
    Outcome = models.CharField(max_length=200,blank=True,null=True)
    Date_death = models.CharField(max_length=10,blank=True)

    Contact_comment = models.CharField(max_length=100,blank=True,null=True)
    Contact_ID = models.CharField(max_length=100,blank=True)
    Contact_location = models.CharField(max_length=100,blank=True)
    Travel_history = models.BooleanField(null=True,blank=True)
    Travel_history_entry = models.CharField(max_length=100,blank=True)
    Travel_history_start = models.CharField(max_length=100,blank=True)
    Travel_history_location = models.CharField(max_length=100,blank=True)
    Travel_history_country = models.CharField(max_length=100,blank=True)
    Genomics_Metadata = models.CharField(max_length=100,blank=True)
    Confirmation_method = models.CharField(max_length=100,blank=True)
    Source = models.CharField(max_length=300,blank=True)
    Source_II = models.CharField(max_length=300,blank=True)
    Date_entry = models.CharField(max_length=10,blank=True)
    Date_last_modified = models.CharField(max_length=10,blank=True)
    Source_III = models.CharField(max_length=300,blank=True)
    Source_IV = models.CharField(max_length=300,blank=True)
    Country_ISO3 = models.CharField(max_length=50,blank=False)


    def __str__(self):
        return self.ID



#{"ID": "N49624", "Status": "confirmed", "Location": "Vermont", "City": "", "Country": "United States", "Age": "", "Gender": "", "Date_onset": "", "Date_confirmation": "2022-08-29", "Symptoms": "", "Hospitalised (Y/N/NA)": "", "Date_hospitalisation": "", "Isolated (Y/N/NA)": "", "Date_isolation": "", "Outcome": "", "Date_death": "", "Contact_comment": "", "Contact_ID": "", "Contact_location": "", "Travel_history (Y/N/NA)": "", "Travel_history_entry": "", "Travel_history_start": "", "Travel_history_location": "", "Travel_history_country": "", "Genomics_Metadata": "", "Confirmation_method": "", "Source": "https://www.cdc.gov/poxvirus/monkeypox/response/2022/us-map.html", "Source_II": "", "Date_entry": "2022-08-29", "Date_last_modified": "2022-08-29", "Source_III": "", "Source_IV": "", "Country_ISO3": "USA"}