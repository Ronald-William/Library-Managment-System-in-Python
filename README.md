
# **GUI Library Management System**  

## **Overview**  
The **GUI Library Management System** is a Python-based application that provides an easy-to-use graphical interface for managing library operations. It allows administrators to manage book stock and customer records, while customers can browse, search, and rent books. The application uses **Tkinter** for the GUI and **MySQL** for database management.  

---

## **Features**  

### **Admin Features**  
- **Login System:** Secure access for administrators with username and password.  
- **Book Stock Management:**  
  - Add new books to the library.  
  - Delete books from the stock.  
  - View all available books.  
- **Customer Record Management:**  
  - Add new customer records.  
  - View all customer records.  
  - Search for specific customer records by ID.  
  - Update customer information (phone number, rented book).  
  - Delete customer records.  

### **Customer Features**  
- View all available books in the library.  
- Search for specific books by name or author.  
- Rent a book.  

---

## **Technologies Used**  
- **Python** – Core programming language.  
- **Tkinter** – For creating the graphical user interface (GUI).  
- **MySQL** – Backend database for storing book and customer information.  

---

## **Prerequisites**  
- **Python 3.x** installed on your system.  
- **MySQL server** installed and running.  
- Required Python libraries:  
  ```bash
  pip install mysql-connector-python
  ```  

---

## **Installation**  

### **1. Clone the Repository**  
```bash
git clone (https://github.com/Ronald-William/Library-Managment-System-in-Python.git)
```  

### **2. Install Dependencies**  
```bash
pip install mysql-connector-python
```  

### **3. Set Up the MySQL Database**  
- Create a database named **project**.  
- Run the following SQL commands to create the necessary tables:  

```sql
CREATE TABLE projectstock (
    name VARCHAR(255),
    author VARCHAR(255),
    status VARCHAR(50)
);

CREATE TABLE projcustomer (
    name VARCHAR(255),
    customerId INT PRIMARY KEY,
    dateOfRenting DATE,
    bookRented VARCHAR(255),
    phoneNumber VARCHAR(15)
);
```  

### **4. Update Database Connection Details**  
Modify the connection details in the Python script:  
```python
mycon = ms.connect(host='localhost', user='root', passwd='qwerty')
```  

---

## **How to Run**  
1. Open a terminal or command prompt.  
2. Navigate to the project directory.  
3. Run the main script:  
   ```bash
   python main.py
   ```  
4. The GUI window will open, allowing you to select between **Admin** or **Customer** functionalities.  

---

## **Usage**  

### **Admin Workflow**  
1. Log in using the admin credentials (**username: r, password: q**).  
2. Manage book stock or customer records using the provided options.  

### **Customer Workflow**  
1. Browse available books or search for specific ones.  
2. Rent a book by entering the required details.  

---

## **Limitations**  
- No encryption is implemented for admin credentials (stored in plain text).  
- Error handling for invalid inputs can be improved.  

---

## **Future Enhancements**  
- Add encryption for passwords and sensitive data.  
- Implement a more robust search functionality for books and customers.  
- Add support for generating reports (e.g., rented books, due dates).  

---

