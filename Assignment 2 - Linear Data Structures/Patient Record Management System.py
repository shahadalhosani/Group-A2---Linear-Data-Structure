class Patient: # define a class to store each patients information
    def __init__(self, name, age, id, gender, medical_history, current_condition, admission_date): # all attributes associated with a patient record
        self.name = name
        self.age = age
        self.id = id
        self.gender = gender
        self.medical_history = medical_history
        self.current_condition = current_condition
        self.admission_date = admission_date

    def __str__(self): # a function to display the patients records
        return f"Patient Name: {self.name}, Patient Age: {self.age}, Patient ID: {self.id}, Patient Gender: {self.gender}, Patient Medical History: {self.medical_history}, Patient Current Condition: {self.current_condition}, Patient Admission Date: {self.admission_date}"

class Appointment: # define a class to store each appointment made by a patient
    def __init__(self, patient, doctor, time): # all attributes associates with an appointment
        self.patient = patient
        self.doctor = doctor
        self.time = time

    def __str__(self): # a function to display the appointment information
        return f"Patient Name: {self.patient}, Doctor Name: {self.doctor}, Time: {self.time}"

class Prescription:
    def __init__(self, patient_name, medications):
        self.patient_name = patient_name
        self.medications = medications

    def __str__(self):
        return f"Prescription for Patient {self.patient_name}: {self.medications}"

class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0
class Node: # a class to define a node
    def __init__(self, patient):
        self.left = None
        self.right = None
        self.patient = patient

def insert(root, patient):
    if root is None:
        return Node(patient)
    else:
        if root.patient.id < patient.id:
            root.right = insert(root.right, patient)
        else:
            root.left = insert(root.left, patient)
    return root


def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print("Name:", root.patient.name)
        print("Age:", root.patient.age)
        print("ID:", root.patient.id)
        print("Gender:", root.patient.gender)
        print("Medical History:", root.patient.medical_history)
        print("Current Condition:", root.patient.current_condition)
        print("Admission Date:", root.patient.admission_date)
        print()
        inorder_traversal(root.right)

class PatientRecordManagementSystem: # defines a class for the hospital system, specifically patient record management
    def __init__(self):
        self.patient_record = {} # dictionary to store patient record
        self.appointments = [] # list to store appointments
        self.queue = [] # queue to maintain waiting line for consulatation, ensuring a FIFO order
        self.stack = Stack() # we used the stack to manage the description of the patient's
        self.root = None

    def add_patient_record(self, name, age, id, gender, medical_history, current_condition, admission_date): # Adding a new patient record using BST data structure
        new_patient = Patient(name, age, id, gender, medical_history, current_condition, admission_date)
        self.root = insert(self.root, new_patient)
        self.patient_record[id] = new_patient

    def update_patient_record(self, root, id, new_medical_history, new_current_condition):  # Updating a patient record using BST data structure
        if root is None:
            return
        if root.patient.id == id:
            root.patient.medical_history = new_medical_history
            root.patient.current_condition = new_current_condition
        elif root.patient.id < id:
            self.update_patient_record(root.right, id, new_medical_history, new_current_condition)
        else:
            self.update_patient_record(root.left, id, new_medical_history, new_current_condition)

    def remove_patient_record(self, root, id): # Removing a patient record using BST data structure
        if root is None: # If the root is None, meaning the tree is empty or the patient record with the given ID does not exist, the function returns None.
            return root
        if id < root.patient.id: # If the ID to be removed is less than the current root's patient ID, the function recursively calls itself on the left subtree.
            root.left = self.remove_patient_record(root.left, id)
        elif id > root.patient.id: # If the ID to be removed is greater than the current root's patient ID, the function recursively calls itself on the right subtree.
            root.right = self.remove_patient_record(root.right, id)
        else: # If the ID matches the current root's patient ID, there are three cases to consider:
            if root.left is None: # If the root has no left child, the right child replaces the root.
                return root.right
            elif root.right is None: # If the root has no right child, the left child replaces the root.
                return root.left
            # Find the minimum value in the right subtree
            successor = root.right
            while successor.left is not None:
                successor = successor.left
            root.patient = successor.patient
            root.right = self.remove_patient_record(root.right, successor.patient.id)
        return root

    def schedule_appointment(self, patient, doctor, time): # Scheduling an appointment for a patient with a specific doctor.
        appointment = Appointment(patient, doctor, time)
        self.appointments.append(appointment)
        # Print the details of the newly added appointment
        print(f"Appointment scheduled for {appointment.patient} with {appointment.doctor} at {appointment.time}")

    def sort_records_by_date(self): # Create a hash table to organize patient records by admission date
        hash_table = {}
        for patient_id, patient in self.patient_record.items():
            if patient.admission_date in hash_table:
                hash_table[patient.admission_date].append(patient)
            else:
                hash_table[patient.admission_date] = [patient]

        # Sort the keys of the hash table (admission dates)
        sorted_keys = sorted(hash_table.keys())

        # Retrieve the records in sorted order
        sorted_records = []
        for key in sorted_keys:
            sorted_records.extend(hash_table[key])

        return sorted_records

    # Maintaining a line of patients waiting for consultations ensuring FIFO (First-In-First-Out) order using the Queue data structure.
    def enqueue(self, patient): # Adding patients to the consultation queue
        sorted_patients = self.sort_records_by_date()
        for patient in sorted_patients:
            if patient not in self.queue:  # Check if patient is already in the queue
                self.queue.append(patient)
                print(f"{patient.name} has been added to the queue.")

    def dequeue(self): # Removing patients from consultation queue
        if not self.is_empty():
            removed_patient = self.queue.pop(0)
            print(f"{removed_patient.name} has been called for consultation.")
            return removed_patient
        else:
            print("The queue is empty.")

    def is_empty(self): # checks if the queue is empty
        return len(self.queue) == 0

    def display_queue(self): # displaying all patients records within the queue
        for patient in self.queue:
            print(f"Name: {patient.name}, Age: {patient.age}, ID: {patient.id}, Gender: {patient.gender}, Medical History: {patient.medical_history}, Current Condition: {patient.current_condition}")

    def issue_prescription(self, patient_name, medications):
        for patient_id, patient in self.patient_record.items():
            if patient.name == patient_name:
                prescription = Prescription(patient_name, medications)
                self.stack.push(prescription)
                return prescription
        else:
            print("Patient not found in records. Prescription cannot be issued.")
            return None

    def display_prescription_stack(self): #Here we added a function
        if not self.stack.is_empty():
            for prescription in self.stack.items:
                print(prescription)
        else:
            print("Prescription stack is empty.")

    def dispense_prescription(self):
        if not self.stack.is_empty():
            prescription = self.stack.pop()
            print(f"Prescription dispensed for Patient {prescription.patient_name}.")
            return prescription
        else:
            print("Prescription stack is empty. No prescription to dispense.")
            return None
            
# Test Cases:
if __name__ == "__main__":
    # Creating an instance of PatientRecordManagementSystem
    prms = PatientRecordManagementSystem()

    # Adding new patient records
    prms.add_patient_record("Shahad", 19, 101, "Female", "Fever", "Non-Stable", "2024-04-15")
    prms.add_patient_record("Zainab", 20, 102, "Female", "Headache", "Stable", "2024-02-01")
    prms.add_patient_record("Ahmed", 30, 103, "Male", "Cough", "Non-Stable", "2024-02-10")


    print("All Patient Records:")
    inorder_traversal(prms.root)

    # Updating patient records
    prms.update_patient_record(prms.root, 101, "Dizzy", "Stable")
    prms.update_patient_record(prms.root, 102, "Stomach ache", "Stable")
    prms.update_patient_record(prms.root, 103, "Back Pain", "Stable")

    print("\nUpdated Patient Records:")
    inorder_traversal(prms.root)

    # Removing a patient record
    prms.root = prms.remove_patient_record(prms.root, 101)

    print("\nRemoving Shahad Record:")
    inorder_traversal(prms.root)

    # Scheduling appointment
    print("\nScheduling Appointments:")
    prms.schedule_appointment("Shahad", "Dr. Smith", "12.00 PM")
    prms.schedule_appointment("Zainab", "Dr. Johnson", "2.00 PM")
    prms.schedule_appointment("Ahmed", "Dr. Khaled", "10.00 AM")

    #Sorting patients record based on admission date
    sorted_records_by_date = prms.sort_records_by_date()
    print("\nSorting patients by admission date:")
    for record in sorted_records_by_date:
        print(record)

    print("\nAdding patients to waiting ling for consultation: ")

    # Patients arrive and join the queue - added based on admission date
    prms.enqueue(Patient("Shahad", 19, 101, "Female", "Fever", "Non-Stable", "2024-04-15"))
    prms.enqueue(Patient("Zainab", 20, 102, "Female", "Headache", "Stable", "2024-02-01"))
    prms.enqueue(Patient("Ahmed", 30, 103, "Male", "Cough", "Non-Stable", "2024-02-10"))

    print("\nPatients in the queue: ")
    # Displaying the current queue
    prms.display_queue()

    # Consulting patients (dequeuing)
    print("\nConsulting patients:")
    prms.dequeue()
    prms.dequeue()
    prms.dequeue()

    # Trying to consult from an empty queue
    prms.dequeue()

        # Issue prescriptions for patients during consultation
    print("\nIssue Prescriptions to Patients during consultation:")
    prms.issue_prescription("Zainab", ["Paracetamol", "Antibiotics"])
    prms.issue_prescription("Ahmed", ["Ibuprofen", "Cough Syrup"])
    prms.issue_prescription("Shahad", ["Throat Lozenges", "Antibiotics"])

    # Display prescription stack
    prms.display_prescription_stack()

    # Dispense prescriptions, ensuring Last in first out order (stack)
    prms.dispense_prescription()
    prms.dispense_prescription()
    prms.dispense_prescription()

#Test 2 the menu interface (users input)

patient_records = []
while True: 
    print("\n The patient records manegments system")
    print("1. Add patients record")
    print("2. Update patients records")
    print("3. Remove a patient record")
    print("4. Schedule an appointment")
    print("5. Sorting patients records by admission dates")
    print("6. Add the patients to the waiting line for the consultation")
    print("7. Displaying Consultation queue")
    print("8. Consulting the patients")
    print("9. Issue Prescription")
    print("10. Display priscription stack")
    print("11. Distribute Prescription")
    print("12. Search for a patient and display a summary of their records")
    print("0. Exit")
        
    opt = input("\n write your choice")
    
    if opt == "1":
        print("\n Adding in the patients record: ")
        name = input("write the patients name: ")
        age = int(input("write the patients age: "))
        patient_id = int(input("write patients ID: "))
        gender = input("write the patients gender: ")
        medical_history = input("write the patients medical history: ") 
        current_condition = input("write the patients condition: ") 
        admission_date = input("write the patients admission date: ")
        prms.add_patient_record(name, age, patient_id, gender, medical_history, current_condition, admission_date)
        patient_records.append(prms.prms.patient_record[patient_id])
        
    elif opt == "2":
        print("\n Update a patient record: ")
        patient_id = int(input("write patients ID to update the record: ")
        new_medical_history = input("write the new medical history: ")
        new_current_condition = input("write the new condition: ")
        prms.update_patient_record(prms.root, patient_id, new_medical_history, new_current_condition)
        print("\n All the updated patient records: ")
        inorder_traversal(prms.root)
    elif opt == "3":
        print("\n Removing the record: ")
        patient_id = int(input("write ID to remove patient record: ")
        prms.root = prms.remove_patient_record(prms.root, patient_id)
        print("\n patients record after removing some pationt: ")
        inorder_traversal(prms.root) 
    elif opt == "4":
        print("\n Scheduling an appointment: ")
        patient_name = input("write the patients name: ")
        patient_id = int(input("write patients ID: ") 
        doctor_name = input("write the doctors name: ")
        appointment_time = input("write the appintment time: ")
        print("\n Appintment done!: ")
        prms.schedule_appointment(patient_name, patient_id, doctor_name, appointment_time)
  
    elif opt == "5":
         print("\n All patient records sorted by admission dates: ")
         sorted_records_by_date = prms.sort_records_by_date()
         for record in sorted_records_by_date:
             print(record)
    elif opt == "6":
         prms.enqueue(Patient(name, age, patient_id, gender, medical_history, current_condition, admission_date)
    elif opt == "7":
         print("\n Consultation queue: ")
         prms.display_queue()
    elif opt == "8":
         print("\n consulting patiemts: ")
         prms.dequeue()
         prms.dequeue()
         prms.dequeue()
    elif opt == "9":
         patient_name = input("write the patients name: ")
         patient_id = int(input("write patients ID: ")
         medications = input("write the medications (seperated by comma): ").split(",") 
         prms.issue_prescription(patient_name, patient_id, medications)
    elif opt == "10": 
         print("\n prescription stack: ")
         prms.display_prescription_stack()
    elif opt == "11":
         print("\n dispincing prescription: ")
         prms.distribute_prescription()
         prms.distribute_prescription()
         prms.distribute_prescription()
    elif opt =="12":
         patient_id = int(input("write patients ID for searching: ")
         prms.search_patient(patient_id)
    elif opt == "0":#Exiting the programm and showing all data inputs
         print("\n All patient records: ")
         for record in patient_records:
             print(record)
         print("exiting the programm!")
         break
    else:
        print("incorrect choice, make sure to pick numbers from 0-12")






        
   




        
    
        
        






