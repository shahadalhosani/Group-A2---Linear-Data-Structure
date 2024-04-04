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
    def __init__(self, patient_name, patient_id, doctor, time): # all attributes associates with an appointment
        self.patient_name = patient_name
        self.patient_id = patient_id
        self.doctor = doctor
        self.time = time

    def __str__(self): # a function to display the appointment information
        return f"Patient Name: {self.patient_name}, Patient ID: {self.patient_id}, Doctor Name: {self.doctor}, Time: {self.time}"

class Prescription: # define a class to store each prescription a doctor have issued for a patient
    def __init__(self, patient_name, patient_id, medications): # all attributes associated with a prescription
        self.patient_name = patient_name
        self.patient_id = patient_id
        self.medications = medications

    def __str__(self): # a function to display the prescription information
        return f"Prescription for Patient {self.patient_name} with ID {self.patient_id}: {self.medications}"

class Doctor: # define a class to store each doctor for a specific pateitn
    def __init__(self, name, specialty): # all attributes associated with a doctor
        self.name = name
        self.specialty = specialty

class Stack: # define a class for the stack to be used as a data structure when issuing and distributing prescriptions to patients
    def __init__(self):
        self.items = []

    def push(self, item): # adds an item
        self.items.append(item)

    def pop(self): # removes an item
        if not self.is_empty():
            return self.items.pop()

    def is_empty(self): # checks if the stack is empty
        return len(self.items) == 0
class Node: # a class to define a node
    def __init__(self, patient): # constructor method for Node class
        self.left = None # initialize left child pointer
        self.right = None # initialize right child pointer
        self.patient = patient # store patient data in the node

def insert(root, patient): # function to insert a patient node into the binary search tree
    if root is None:  # if the root is empty
        return Node(patient) # create a new node with the patient data
    else: # if the root is not empty
        if root.patient.id < patient.id: # if the patient ID of the root is less than the new patient's ID
            root.right = insert(root.right, patient) # insert the new patient node into the right subtree
        else: # if the patient ID of the root is greater than or equal to the new patient's ID
            root.left = insert(root.left, patient)  # insert the new patient node into the left subtree
    return root # return the root of the modified subtree


def inorder_traversal(root): # function to perform an inorder traversal of the binary search tree
    if root:  # if the root is not empty
        inorder_traversal(root.left)  # recursively traverse the left subtree
        print("Name:", root.patient.name)
        print("Age:", root.patient.age)
        print("ID:", root.patient.id)
        print("Gender:", root.patient.gender)
        print("Medical History:", root.patient.medical_history)
        print("Current Condition:", root.patient.current_condition)
        print("Admission Date:", root.patient.admission_date)
        print()
        inorder_traversal(root.right) # recursively traverse the right subtree

class PatientRecordManagementSystem: # defines a class for the hospital system, specifically patient record management
    def __init__(self):
        self.patient_record = {} # dictionary to store patient record
        self.appointments = [] # list to store appointments
        self.prescriptions = [] # list to store prescriptions
        self.queue = [] # queue to maintain waiting line for consultation, ensuring a FIFO order
        self.stack = Stack() # stack to manage prescriptions
        self.patients = [] # list to store patients
        self.root = None # root of the binary search tree to store patient records

    def add_patient_record(self, name, age, id, gender, medical_history, current_condition, admission_date): # Adding a new patient record using BST data structure
        new_patient = Patient(name, age, id, gender, medical_history, current_condition, admission_date) # create a new Patient object
        self.root = insert(self.root, new_patient) # insert the new patient record into the binary search tree
        self.patient_record[id] = new_patient # add the new patient record to the patient_record dictionary by their id

    def update_patient_record(self, root, id, new_medical_history, new_current_condition):  # Updating a patient record using BST data structure
        if root is None: # if the root is None, return
            return
        if root.patient.id == id: # if the root's patient ID matches the given ID
            root.patient.medical_history = new_medical_history # update the medical history
            root.patient.current_condition = new_current_condition # update the current condition
        elif root.patient.id < id:  # if the root's patient ID is less than the given ID
            self.update_patient_record(root.right, id, new_medical_history, new_current_condition) # traverse right subtree
        else: # if the root's patient ID is greater than the given ID
            self.update_patient_record(root.left, id, new_medical_history, new_current_condition) # traverse left subtree

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
            while successor.left is not None: # Traverse left until reaching the leftmost node of the right subtree
                successor = successor.left
            root.patient = successor.patient # Replace the root's patient with the successor's patient
            root.right = self.remove_patient_record(root.right, successor.patient.id) # Remove the successor node
        return root

    def schedule_appointment(self, patient_name, patient_id, doctor, time): # Scheduling an appointment for a patient with a specific doctor.
        appointment = Appointment(patient_name, patient_id, doctor, time) # Create a new Appointment object
        self.appointments.append(appointment)  # Add the appointment to the list of appointments
        # Print the details of the newly added appointment
        print(f"Appointment scheduled for {appointment.patient_name} with {appointment.doctor} at {appointment.time}")

    def sort_records_by_date(self): # Create a hash table to organize patient records by admission date
        hash_table = {} # Initialize an empty hash table
        for patient_id, patient in self.patient_record.items(): # Iterate through each patient record
            if patient.admission_date in hash_table: # If the admission date is already a key in the hash table
                hash_table[patient.admission_date].append(patient) # Append the patient record to the corresponding list
            else: # If the admission date is not yet a key in the hash table
                hash_table[patient.admission_date] = [patient] # Create a new key-value pair with the admission date as the key and a list containing the patient record as the value

        # Sort the keys of the hash table (admission dates)
        sorted_keys = sorted(hash_table.keys())

        # Retrieve the records in sorted order
        sorted_records = []
        for key in sorted_keys:
            sorted_records.extend(hash_table[key])

        return sorted_records

    # Implementing a Queue data structure to maintain a line of patients waiting for consultations ensuring FIFO (First-In-First-Out).
    def enqueue(self, patient): # Adding patients to the consultation queue
        sorted_patients = self.sort_records_by_date()
        for patient in sorted_patients:
            if patient not in self.queue:  # Check if patient is already in the queue
                self.queue.append(patient) # add patient to queue
                print(f"{patient.name} has been added to the queue.")

    def dequeue(self): # Removing patients from consultation queue
        if not self.is_empty():
            removed_patient = self.queue.pop(0) # remove patients from queue in a FIFO order
            print(f"{removed_patient.name} has been called for consultation.")
            return removed_patient
        else:
            print("The queue is empty.")

    def is_empty(self): # checks if the queue is empty
        return len(self.queue) == 0

    def display_queue(self): # displaying all patients records within the queue
        for patient in self.queue:
            print(f"Name: {patient.name}, Age: {patient.age}, ID: {patient.id}, Gender: {patient.gender}, Medical History: {patient.medical_history}, Current Condition: {patient.current_condition}")

    def issue_prescription(self, patient_name, patient_id, medications): # Issue medical prescriptions to patients during consultation
        for patient_id, patient in self.patient_record.items(): # Iterate through each patient record
            if patient.name == patient_name:  # Check if the patient's name matches the provided patient_name
                prescription = Prescription(patient_name, patient_id, medications)  # Create a new Prescription object
                self.stack.push(prescription)  # Push the prescription onto the prescription stack
                return prescription  # Return the prescription that was issued
        else:
            print("Patient not found in records. Prescription cannot be issued.")
            return None

    def display_prescription_stack(self): # displaying prescription using the stack data structure (applied above class Stack), to ensure LIFO order
        if not self.stack.is_empty():
            for prescription in self.stack.items:
                print(prescription)
        else:
            print("Prescription stack is empty.")

    def distribute_prescription(self): # distributing prescription to patients in a LIFO order
        if not self.stack.is_empty():
            prescription = self.stack.pop()
            print(f"Prescription dispensed for Patient {prescription.patient_name}.")
            return prescription
        else:
            print("Prescription stack is empty. No prescription to distribute.")
            return None

    def search_patient(self, patient_id): # Search for a patient and display a summary of their essential information
        for _, patient in self.patient_record.items():
            if patient.id == patient_id:

                # Finding appointment details
                for appointment in self.appointments:
                    if appointment.patient_id == patient_id:
                        appointment = appointment
                        break

                # Finding medication details
                medications = []
                for prescription in self.stack.items:
                    if prescription.patient_id == patient_id:
                        medications.extend(prescription.medications)

                prescription_info = medications if medications else "Not prescribed"

                # dictionary to display a summary of all essential information
                patient_dict = {
                    'Patient Name': patient.name,
                    'Age': patient.age,
                    'ID': patient.id,
                    'Gender': patient.gender,
                    'Medical Condition': patient.medical_history,
                    'Current Condition': patient.current_condition,
                    'Doctor': appointment.doctor,
                    'Appointment Date': patient.admission_date,
                    'Appointment Time': appointment.time,
                    'Medications': prescription_info
                }
                print(patient_dict)
                return

        print(f"Patient with ID '{patient_id}' not found.")


# Test Case 1 without menu-based interface to ensure that everything is working:
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
    prms.schedule_appointment("Shahad", 101, "Dr. Smith", "12.00 PM")
    prms.schedule_appointment("Zainab", 102, "Dr. Johnson", "2.00 PM")
    prms.schedule_appointment("Ahmed", 103, "Dr. Khaled", "10.00 AM")

    #Sorting patients record based on admission date
    sorted_records_by_date = prms.sort_records_by_date()
    print("\nSorting patients by admission date:")
    for record in sorted_records_by_date:
        print(record)

    print("\nAdding patients to waiting line for consultation: ")

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

    # Issue prescriptions for patients during consultation
    print("\nIssue Prescriptions to Patients during consultation:")
    prms.issue_prescription("Zainab", 102, ["Paracetamol", "Antibiotics"])
    prms.issue_prescription("Ahmed", 103, ["Ibuprofen", "Cough Syrup"])
    prms.issue_prescription("Shahad", 101, ["Throat Lozenges", "Antibiotics"])

    # Display prescription stack
    prms.display_prescription_stack()

    # Dispense prescriptions, ensuring Last in first out order (stack)
    prms.distribute_prescription()
    prms.distribute_prescription()
    prms.distribute_prescription()


    prms.issue_prescription("Zainab", 102, ["Paracetamol", "Antibiotics"])
    prms.issue_prescription("Ahmed", 103, ["Ibuprofen", "Cough Syrup"])
    prms.issue_prescription("Shahad", 101, ["Throat Lozenges", "Antibiotics"])

    # Searching for a patient and displaying a summary of essential information
    print("\nSearch and display patient summary:")
    prms.search_patient(101)
    prms.search_patient(102)
    prms.search_patient(103)

# Test case 2 with menu-based interface:
if __name__ == "__main__":
    # Creating an instance of PatientRecordManagementSystem
    prms = PatientRecordManagementSystem()

    # Initialize lists to store input data
    patient_records = []

    while True:
        print("\n==== Patient Record Management System ====")
        print("1. Add a Patient Record")
        print("2. Update a Patient Record")
        print("3. Remove a Patient Record")
        print("4. Schedule an Appointment")
        print("5. Sort Patient Records by Admission Date")
        print("6. Add patient to waiting line for consultation")
        print("7. Display Consultation Queue")
        print("8. Consult Patients")
        print("9. Issue Prescription")
        print("10. Display Prescription Stack")
        print("11. Distribute Prescription")
        print("12. Search for a patient and display a summary of their records:")
        print("0. Exit")

        choice = input("\nEnter your choice: ")


        if choice == "1":
            print("\nAdding a Patient Record:")
            name = input("Enter patient name: ")
            age = int(input("Enter patient age: "))
            patient_id = int(input("Enter patient ID: "))
            gender = input("Enter patient gender: ")
            medical_history = input("Enter patient medical history: ")
            current_condition = input("Enter patient current condition: ")
            admission_date = input("Enter admission date (YYYY-MM-DD): ")
            prms.add_patient_record(name, age, patient_id, gender, medical_history, current_condition, admission_date)
            patient_records.append(prms.patient_record[patient_id])

        elif choice == "2":
            print("\nUpdating a Patient Record:")
            patient_id = int(input("Enter patient ID to update: "))
            new_medical_history = input("Enter new medical history: ")
            new_current_condition = input("Enter new current condition: ")
            prms.update_patient_record(prms.root, patient_id, new_medical_history, new_current_condition)
            print("\nAll updated records of patients")
            inorder_traversal(prms.root)


        elif choice == "3":
            print("\nRemoving a Patient Record:")
            patient_id = int(input("Enter patient ID to remove: "))
            prms.root = prms.remove_patient_record(prms.root, patient_id)
            print("Patient record after removing a certain patient")
            inorder_traversal(prms.root)


        elif choice == "4":
            print("\nScheduling an Appointment:")
            patient_name = input("Enter patient name: ")
            patient_id = input("Enter patient ID: ")
            doctor_name = input("Enter doctor name: ")
            appointment_time = input("Enter appointment time: ")
            print("\nAppointment scheduled successfully")
            prms.schedule_appointment(patient_name, patient_id, doctor_name, appointment_time)

        elif choice == '5':
            print("\nAll Patient Records Sorted by Admission Date")
            sorted_records_by_date = prms.sort_records_by_date()
            for record in sorted_records_by_date:
                print(record)

        elif choice == '6':
            # Add identified patients to waiting line
            prms.enqueue(Patient(name, age, patient_id, gender, medical_history, current_condition, admission_date))


        elif choice == "7":
            print("\nConsultation Queue:")
            prms.display_queue()


        elif choice == "8":
            print("\nConsulting Patients:")
            prms.dequeue()
            prms.dequeue()
            prms.dequeue()


        elif choice == "9":
            print("\nIssuing Prescription:")
            patient_name = input("Enter patient name: ")
            patient_id = input("Enter patient ID: ")
            medications = input("Enter medications (comma-separated): ").split(",")
            prms.issue_prescription(patient_name, patient_id, medications)


        elif choice == "10":
            print("\nPrescription Stack:")
            prms.display_prescription_stack()


        elif choice == "11":
            print("\nDispensing Prescription:")
            prms.distribute_prescription()
            prms.distribute_prescription()
            prms.distribute_prescription()


        elif choice == "12":
            patient_id = int(input("Enter patient id you are searching for: "))
            prms.search_patient(patient_id)


        elif choice == "0":
            # Exit the program and display all information input from the user
            print("\nAll Patient Records:")
            for record in patient_records:
                print(record)


            print("Exiting the program. Thank you!")
            break


        else:
            print("Invalid choice. Please enter a valid option.")






        
   




        
    
        
        






