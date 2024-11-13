import os
import shutil
from tkinter import Tk, Listbox, Scrollbar, Button, filedialog, messagebox

class FileViewer:
    def __init__(self, folder_path):
        self.folder_path = folder_path
        self.root = Tk()
        self.root.title("File Viewer")
        self.root.geometry("600x400")
        self.listbox = Listbox(self.root, selectmode='multiple')
        self.scrollbar = Scrollbar(self.root, command=self.listbox.yview)
        self.listbox.config(yscrollcommand=self.scrollbar.set)
        self.populate_list()
        self.listbox.pack(side="left", fill="both", expand=True)
        self.scrollbar.pack(side="right", fill="y")
        self.copy_button = Button(self.root, text="Copy Selected", command=self.copy_selected_files)
        self.copy_button.pack(fill="x")
        
    def populate_list(self):
        files = sorted(os.listdir(self.folder_path), key=lambda f: os.path.getmtime(os.path.join(self.folder_path, f)), reverse=True)
        for file in files:
            self.listbox.insert("end", file)
    
    def copy_selected_files(self):
        selected_files = [self.listbox.get(i) for i in self.listbox.curselection()]
        if not selected_files:
            messagebox.showwarning("No Selection", "Please select files to copy.")
            return
        #dest_folder = filedialog.askdirectory(title="Select Destination Folder")
        dest_folder = 'Desktop'
        if dest_folder:
            for file in selected_files:
                shutil.copy2(os.path.join(self.folder_path, file), os.path.join(dest_folder, file.split()[0] + os.path.splitext(file)[1]))
            #messagebox.showinfo("Success", f"Copied {len(selected_files)} files to {dest_folder}")
    
    def run(self):
        self.root.mainloop()

folder_path = "Desktop/backup/"
app = FileViewer(folder_path)
app.run()

