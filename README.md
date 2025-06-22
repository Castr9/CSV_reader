# CSV_reader

CSV Dashboard Viewer

A simple Tkinter GUI application that allows users to upload a CSV file and visualize the data through plots. It uses Pandas for data handling and Matplotlib for plotting, with an embedded chart area directly in the GUI.
Features

    Upload a .csv file through a file dialog.

    Select a column from the dropdown menu.

    Automatically generates:

        Line plots for numeric columns.

        Bar plots for categorical/text columns.

    Embeds the plot directly into the application window.

Technologies Used

    Python tkinter (GUI)

    pandas (Data manipulation)

    matplotlib (Plotting)

Installation

    Clone the repository (or copy the script):
    
cd csv-dashboard-viewer

Install required packages (preferably in a virtual environment):

    pip install pandas matplotlib

    tkinter is included by default with most Python installations.

Usage

Run the Python script:

python your_script_name.py

Steps:

    Click "Upload CSV" to select a .csv file.

    Choose a column from the dropdown menu.

    Click "Show Plot" to view the graph.

Example

    Numeric column: Shows a line chart with index on the X-axis.

    Categorical column: Displays a bar chart of the top 10 most frequent values.

Limitations

    Only supports .csv file format.

    Bar plots limited to top 10 categories for readability.

License

This project is open-source and free to use under the MIT License.
