#Enjoy :D

import tkinter as tk
from tkinter import filedialog, ttk
import pandas as pd 
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class CSVDashboard:
    def __init__(self, root,):
        self.root = root
        self.root.title("Converter")

        self.data = None #Place holder for the loaded DataFrame

        #Creating the upload button
        self.upload_btn = tk.Button(root, text="Upload  CSV", command=self.load_csv)
        self.upload_btn.pack(pady=10)

        #Column selectors
        self.column_selector = ttk.Combobox(root, state='readoly')
        self.column_selector.pack(pady=5)

        #Creating the button to plot the chart
        self.plot_btn = ttk.Button(root, text="Show Plot", command=self.plot_column)
        self.plot_btn.pack(pady=5)

        #Graph area
        self.canvas_frame = tk.Frame(root)
        self.canvas_frame.pack(fill=tk.BOTH, expand=True)  

    #Open a file dialog for selecting a csv file
    def load_csv(self,):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files", "*.csv")])#Open's the file search window and filters only the ".csv" files
        if not file_path:
            return  #If user cancels, exit the function

        try:
            #Load the CSV into a pandas DataFrame 
            self.data = pd.read_csv(file_path)

            #Extract column names and update the dropdown
            columns = self.data.columns.tolist()
            self.column_selector['values'] = columns
            self.column_selector.set('Select Column to Plot') #Set default text
        except Exception as e:
            #Handle errors (e.g., bad file format)
            print("Failed to load CSV:", e)

   
    def plot_column(self, event=None):
        #Get the selected column name from the dropdown
        column = self.column_selector.get()
        
        #Check if data is loaded and column is valid
        if self.data is None or column not in self.data.columns:
            print("Invalid or missing column.")
            return
        
        #Clear previous plots   
        for widget in self.canvas_frame.winfo_children():
            widget.destroy()
        
        #Create a new matplotlib figur and axes
        fig, ax = plt.subplots(figsize=(6, 4))

        #Plot logic: depends column type
        #     
        #Auto-coose plot based on data type
        if pd.api.types.is_numeric_dtype(self.data[column]):
            #Line plot for numeric data
            self.data[column].plot(kind='line', ax=ax)
            ax.set_title(f"Line Plot of {column}")
            ax.set_ylabel(column)
            ax.set_xlabel("Index")

        else:
            #Bar plot for categorical/text data - show value counts as bar plots
            value_counts = self.data[column].value_counts().head(10)
            value_counts.plot(kind='bar', ax=ax)
            ax.set_title(f"Bar plot of top categories in '{column}'")
            ax.set_ylabel("Count")
            ax.set_xlabel("Category")

        ax.grid(True) # Add gridlines for readability

        #Embed th matplotlib figure into the tkinter frame
        canvas = FigureCanvasTkAgg(fig, master=self.canvas_frame)
        canvas.draw()
        canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)           


#Start the GUI app
if __name__ == "__main__":
    root = tk.Tk()
    app = CSVDashboard(root)
    root.mainloop()                




