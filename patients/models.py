from django.db import models
import uuid

class Patient(models.Model):
    name = models.CharField(max_length = 100)
    address = models.TextField()
    medical_history = models.TextField()
    patient_id = models.UUIDField(default = uuid.uuid4, editable = False, unique = True)
