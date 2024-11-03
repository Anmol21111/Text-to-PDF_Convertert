import tkinter as tk
from tkinter import filedialog, messagebox
from fpdf import FPDF

# Create the main application window
root = tk.Tk()
root.title("Text to PDF Converter")
root.geometry("700x500")
root.config(bg="#f0f0f0")

# Set the default font style
FONT = ("Arial", 12)

# Customize window frame color
frame_color = "#3e4444"  # Darker frame color

# Create a colorful header label
header_label = tk.Label(root, text="Text to PDF Converter", font=("Helvetica", 24, "bold"),
                        fg="#4CAF50", bg="#f0f0f0", pady=20)
header_label.pack()

# Frame for text input area with customized style
text_frame = tk.Frame(root, bg=frame_color, bd=2, relief="groove")
text_frame.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

# Create a Text widget for entering or displaying text
text_area = tk.Text(text_frame, font=FONT, wrap="word", bg="#ffffff", fg="#000000",
                    relief="flat", padx=10, pady=10)
text_area.pack(fill=tk.BOTH, expand=True)


# Function to convert text from the text widget to PDF
def convert_text_to_pdf():
    # Get the text from the text widget
    text_content = text_area.get(1.0, tk.END).strip()

    if not text_content:
        messagebox.showwarning("Warning", "The text area is empty.")
        return

    # Ask the user to specify the output file path
    output_file = filedialog.asksaveasfilename(defaultextension=".pdf",
                                               filetypes=[("PDF files", "*.pdf")])
    if not output_file:
        return

    try:
        # Create a PDF document
        pdf = FPDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.set_font("Arial", size=12)

        # Add text to the PDF
        pdf.multi_cell(0, 10, txt=text_content)

        # Save the PDF to the specified file
        pdf.output(output_file)
        messagebox.showinfo("Success", "Text successfully converted to PDF!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to convert text to PDF: {e}")


# Function to convert a text file to PDF
def convert_file_to_pdf():
    # Ask the user to choose a text file
    input_file = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])

    if not input_file:
        return

    # Ask the user to specify the output file path
    output_file = filedialog.asksaveasfilename(defaultextension=".pdf",
                                               filetypes=[("PDF files", "*.pdf")])
    if not output_file:
        return

    try:
        # Read the text from the file
        with open(input_file, 'r') as file:
            text_content = file.read()

        # Create a PDF document
        pdf = FPDF()
        pdf.add_page()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.set_font("Arial", size=12)

        # Add text to the PDF
        pdf.multi_cell(0, 10, txt=text_content)

        # Save the PDF to the specified file
        pdf.output(output_file)
        messagebox.showinfo("Success", "Text file successfully converted to PDF!")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to convert file to PDF: {e}")


# Frame for buttons with customized style
button_frame = tk.Frame(root, bg="#f0f0f0")
button_frame.pack(pady=20)

# Create buttons for converting text and files to PDF with modern design
convert_text_button = tk.Button(button_frame, text="Convert Text to PDF", command=convert_text_to_pdf,
                                font=("Arial", 14), bg="#4CAF50", fg="white", padx=20, pady=10,
                                activebackground="#45a049", activeforeground="white", relief="flat", borderwidth=0)
convert_text_button.grid(row=0, column=0, padx=10)

convert_file_button = tk.Button(button_frame, text="Convert File to PDF", command=convert_file_to_pdf,
                                font=("Arial", 14), bg="#2196F3", fg="white", padx=20, pady=10,
                                activebackground="#1e88e5", activeforeground="white", relief="flat", borderwidth=0)
convert_file_button.grid(row=0, column=1, padx=10)

# Add tooltips for better interactivity
def show_tooltip(event, text):
    tooltip = tk.Toplevel()
    tooltip.wm_overrideredirect(True)
    tooltip.geometry(f"+{event.x_root+20}+{event.y_root+20}")
    tooltip_label = tk.Label(tooltip, text=text, background="#FFFFE0", borderwidth=1, relief="solid", font=("Arial", 10))
    tooltip_label.pack()
    tooltip.after(1500, tooltip.destroy)

convert_text_button.bind("<Enter>", lambda e: show_tooltip(e, "Convert the text in the editor to a PDF file."))
convert_file_button.bind("<Enter>", lambda e: show_tooltip(e, "Convert a .txt file to a PDF file."))

# Run the main application loop
root.mainloop()
