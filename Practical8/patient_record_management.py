class patient(object):
    """
    Maintain a set of records for patients who have been seen at a local hospital
    """
    def __init__(self, name, age, date_of_latest_admission, medical_history):
        self.name = name
        self.age = age
        self.date_of_latest_admission = date_of_latest_admission
        self.medical_history = medical_history
    
    def patient_record(self):
        """
        This function will print out details of a patient's record in a single line
        """
        patient_record = f"{self.name} {self.age} {self.date_of_latest_admission} {self.medical_history}"
        return patient_record
    
example_patient_record = patient('Donald Trump', 77, '2023-11-15', 'Example medical history')
print(example_patient_record.patient_record())