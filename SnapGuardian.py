import base64
from tkinter import filedialog
from CTkMessagebox import CTkMessagebox
import customtkinter as ctk
from PIL import Image
import io

ctk.set_appearance_mode("System")  # Modes: "System" (default), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue")





def encrypt_image(image_path, output_path):
    with open(image_path, "rb") as image_file:
        binary_data = image_file.read()
        encoded_data = base64.b64encode(binary_data).decode("utf-8")
    
    with open(output_path, "w") as text_file:
        text_file.write(encoded_data)

def decrypt_image(input_path, output_path):
    with open(input_path, "r") as text_file:
        encoded_data = text_file.read()
        binary_data = base64.b64decode(encoded_data)
    
    with open(output_path, "wb") as image_file:
        image_file.write(binary_data)

def choose_encryption():
    file_path = filedialog.askopenfilename(title="Select Image File", filetypes=[("Image Files", "*.png;*.jpg;*.jpeg;*.bmp;*.gif")])
    if file_path:
        save_path = filedialog.asksaveasfilename(defaultextension=".txt", title="Save Encrypted Text File", filetypes=[("Text Files", "*.txt")])
        if save_path:
            encrypt_image(file_path, save_path)
            CTkMessagebox(title="Info", message="File saved successfully to: " + save_path)

def choose_decryption():
    file_path = filedialog.askopenfilename(title="Select Encrypted Text File", filetypes=[("Text Files", "*.txt")])
    if file_path:
        save_path = filedialog.asksaveasfilename(defaultextension=".png", title="Save Decrypted Image File", filetypes=[("Image Files", "*.png")])
        if save_path:
            decrypt_image(file_path, save_path)
            CTkMessagebox(title="Info", message="Image saved successfully to: " + save_path)

def main():
    root = ctk.CTk()
    root.title("SnapGuardian: Secure Image Transfer")
    root.geometry("600x500")

    title_label = ctk.CTkLabel(root, text="SnapGuardian: Secure Image Transfer", font=ctk.CTkFont(size=24, weight="bold"))
    title_label.pack(pady=20)

    encrypt_button = ctk.CTkButton(root, text="Encrypt Image", command=choose_encryption, width=200, height=60, font=ctk.CTkFont(size=16))
    encrypt_button.pack(pady=20)

    decrypt_button = ctk.CTkButton(root, text="Decrypt Image", command=choose_decryption, width=200, height=60, font=ctk.CTkFont(size=16))
    decrypt_button.pack(pady=20)

    about_us_button = ctk.CTkButton(root, text="About Us", command=show_about_us, width=200, height=60, font=ctk.CTkFont(size=16))
    about_us_button.pack(pady=20)

    
    def askfor():
        msg = CTkMessagebox(title="Exit?", message="Do you want to close the program?",
                        icon="question", option_1="No", option_2="Yes")
        response = msg.get()
    
        if response=="Yes":
            root.destroy()       
    
    
    root.protocol("WM_DELETE_WINDOW",askfor)
    root.mainloop()

def show_about_us():
    about_window = ctk.CTkToplevel()
    about_window.title("About Us")
    about_window.geometry("500x400")

    about_label = ctk.CTkLabel(about_window, text="About SnapGuardian", font=ctk.CTkFont(size=20, weight="bold"))
    about_label.pack(pady=20)

    about_text = """We are a dedicated team of three members who developed SnapGuardian to address the need for secure image transfers. In an age where data privacy is paramount, SnapGuardian ensures your images are safely encrypted for transfer and storage, and easily decrypted when needed."""
    about_us_label = ctk.CTkLabel(about_window, text=about_text, wraplength=450, justify="left")
    about_us_label.pack(pady=10)

if __name__ == "__main__":
    main()
