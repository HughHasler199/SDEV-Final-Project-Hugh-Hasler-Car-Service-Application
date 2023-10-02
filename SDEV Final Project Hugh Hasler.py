from tkinter import Button, Entry, Label, Tk, messagebox


class CarServiceApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Car Service App")
        self.current_page = 0
        
        self.pages = [self.create_time_page, self.create_problem_page, self.create_contact_page]
        
        self.create_time_page()
        
    def create_time_page(self):
        self.clear_page()
        self.root.geometry("400x200")
        self.root.title("Select Service Time")
        
        Label(self.root, text="Select Service Time:").pack(pady=10)
        
        
        Button(self.root, text="Next", command=self.next_page).pack()
    
    def create_problem_page(self):
        self.clear_page()
        self.root.geometry("400x200")
        self.root.title("Describe Car Problem")
        
        Label(self.root, text="Describe Car Problem:").pack(pady=10)
        
        
        Button(self.root, text="Next", command=self.next_page).pack()
    
    def create_contact_page(self):
        self.clear_page()
        self.root.geometry("400x200")
        self.root.title("Provide Contact Information")
        
        Label(self.root, text="Phone Number:").pack(pady=10)
        Entry(self.root).pack()
        
        Label(self.root, text="Email Address:").pack(pady=10)
        Entry(self.root).pack()
        
        Button(self.root, text="Submit", command=self.submit).pack()
    
    def clear_page(self):
        for widget in self.root.winfo_children():
            widget.destroy()
    
    def next_page(self):
        if self.current_page < len(self.pages) - 1:
            self.current_page += 1
            self.pages[self.current_page]()
    
    def submit(self):
        messagebox.showinfo("Submission", "Your information has been submitted successfully.")
        self.root.quit()

if __name__ == "__main__":
    root = Tk()
    app = CarServiceApp(root)
    root.mainloop()