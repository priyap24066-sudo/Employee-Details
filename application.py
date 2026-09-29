from tkinter import *
import pyqrcode
from PIL import Image,ImageTk
from tkinter import filedialog,messagebox
class Employee():
    def __init__(self):
        self.emp_id=""
        self.emp_name=""
        self.emp_dept=""
        self.salary=0
        self.phone_no=""
        self.email=""
    def add_employee(self):
        self.emp_id=input("Employee Id:")
        self.emp_name=input("Employee Name:")
        self.emp_dept=input("Employee Department:")
        self.salary=float(input("Employee Salary:"))
        self.phone_no=input("PhoneNumber:")
        self.email=input("EmailId:")
    def display(self):
        print(f'Employee Id:{self.emp_id}')
        print(f'Employee Name:{self.emp_name}')
        print(f'Employee Department:{self.emp_dept}')
        print(f'Employee Salary:{self.salary}')
        print(f'PhoneNumber:{self.phone_no}')
        print(f'EmailId:{self.email}')
emp1=[]
while True:
    print("Employee Details")
    print("---------------")
    print("1.Add employee")
    print("2.Display employee")
    print("3.Search_id")
    print("4.Update employee")
    print("5.Delete")
    print("6.QR code")
    print("7.Exit")
    choice=int(input())
    if choice==1:
        emp=Employee()
        emp.add_employee()
        emp1.append(emp)
    elif choice==2:
        if len(emp1)==0:
            print("No employees")
        else:
            for emp in emp1:
                emp.display()
    elif choice==3:
        search_id=input("Enter id")
        found=False
        for emp in emp1:
            if emp.emp_id == search_id:
                emp.display()
                found=True
        if found==False:
                print("No id found")
    elif choice==4:
        update_id = input("Enter Employee ID to Update: ")
        found = False
        for emp in emp1:
            if emp.emp_id == update_id:
                print("Employee Found")
                emp.emp_name = input("Enter New Name: ")
                emp.emp_dept = input("Enter New Department: ")
                emp.salary = float(input("Enter New Salary: "))
                emp.phone_no = input("Enter New Phone Number: ")
                emp.email = input("Enter New Email: ")
                print("Employee Updated Successfully")
                found = True
                break
        if found==False:
                print("Employee Not Found")
    elif choice == 5:
        delete_id = input("Enter Employee ID to Delete: ")
        found = False
        for emp in emp1:
            if emp.emp_id == delete_id:
                emp1.remove(emp)
                print("Employee Deleted Successfully")
                found = True
                break
        if not found:
            print("Employee Not Found")
    elif choice == 6:
        root = Tk()
        root.title("QR Code")
        width = root.winfo_screenwidth()
        height = root.winfo_screenheight()
        root.geometry(f"{width}x{height}")
        root.state("zoomed")
        qr_id = input("Enter Employee ID for QR Code: ")
        found = False
        for emp in emp1:
            if emp.emp_id == qr_id:
                data = f"""Employee ID : {emp.emp_id}
                        Employee Name : {emp.emp_name}
                        Department : {emp.emp_dept}
                        Salary : {emp.salary}
                        Phone : {emp.phone_no}
                        Email : {emp.email}"""

                qr = pyqrcode.create(data)
                filename = f"{emp.emp_id}.png"
                qr.png(filename, scale=8)
                image = Image.open(filename)
                image = image.resize((250, 250))
                photo = ImageTk.PhotoImage(image)
                Label(root,
                  text="Employee QR Code",
                  font=("Times New Roman", 16, "bold")).pack(pady=10)
                lbl = Label(root, image=photo)
                lbl.image = photo
                lbl.pack()
                Label(root,
                  text=f"Employee ID : {emp.emp_id}",
                  font=("Times New Roman", 12)).pack(pady=10)
                found = True
                break
        if not found:
            messagebox.showerror("Error", "Employee Not Found")
            root.destroy()
        else:
            root.mainloop()
    elif choice == 7:
        break
    
