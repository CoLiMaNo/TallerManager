# TallerManager

Taller Manager is an mobile application designed to manage the information of clients, vehicles, spare parts, and the repair history of a mechanical workshop. This tool enables workshops to keep accurate records of the vehicles admitted, the repairs performed, and the spare parts used, facilitating cost management and customer service.

Features
•	Client Management: Register and update client information, including name, phone number, address, and email.
•	Vehicle Management: Store information about clients' vehicles, including make, model, license plate, and mileage.
•	Admission History: Track vehicle admissions to the workshop, detailing the admission date, reported fault, and diagnosis.
•	Spare Parts Management: Record spare parts used in repairs, including their name, description, and cost.
•	Service Records: Assign spare parts and services to vehicles, allowing for a detailed repair history.

Installation

Requirements
•	Python 3.8+
•	SQLAlchemy (for database management)
•	SQLite (can be adapted to other database systems if needed)

Dependencies
Install the required dependencies with the following command:
pip install -r requirements.txt

Database Setup
The database is designed using SQLAlchemy. To configure the database, ensure you have SQLite installed or set up another database system if you wish to use a different database management system.
You can initialize the database by running:
python initialize_db.py
This file will create the necessary tables in your database.

Usage
Running the Application
To start using Taller Manager, run the following command:
python app.py
This will start the application, and you can interact with the client, vehicle, admission, and spare parts management functions.

Main Features
1.	Client Management
o	Create a new client by providing the following details:
	Name
	Phone Number
	Address
	Email
2.	Vehicle Management
o	Vehicles can be associated with an existing client. When creating a vehicle, you need to specify:
	Make
	Model
	License Plate
	Mileage
3.	Admission Management
o	When a vehicle is admitted to the workshop, you can record the following details:
	Admission Date
	Mileage at Admission
	Reported Fault
	Workshop Diagnosis
4.	Spare Parts Management
o	Spare parts used in repairs can be recorded with:
	Spare Part Name
	Description
	Spare Part Cost
Contributing
If you want to contribute to Taller Manager, please follow these steps:
1.	Fork this repository.
2.	Create a branch with the name of your new feature (git checkout -b new-feature).
3.	Commit your changes (git commit -m 'Add new feature').
4.	Push to your branch (git push origin new-feature).
5.	Open a Pull Request.
License
This project is licensed under the MIT License. See the LICENSE file for details.

![01-inicio](https://github.com/user-attachments/assets/49226904-41d9-4ce6-9234-4475d17617c0)

