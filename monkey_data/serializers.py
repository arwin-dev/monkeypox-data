from dataclasses import field
from rest_framework import serializers
from .models import Monkey

class MonkeySerializer(serializers.ModelSerializer):
    class Meta:
        model = Monkey
        fields = [
                  'ID','Status','Location','City','Country','Age','Gender',
                  'Date_onset','Date_confirmation','Symptoms','Hospitalised',
                  'Date_hospitalisation','Isolated','Date_Isolation','Outcome',
                  'Date_death','Contact_comment','Contact_ID','Contact_location',
                  'Travel_history','Travel_history_entry','Travel_history_start',
                  'Travel_history_location','Travel_history_country','Genomics_Metadata',
                  'Confirmation_method','Source','Source_II','Date_entry','Date_last_modified',
                  'Source_III','Source_IV','Country_ISO3'
                ]
