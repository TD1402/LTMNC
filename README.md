# pdftoword
![image](https://github.com/Anshidanshi/pdftoword/assets/87684031/3d5ef5c9-94b3-43b5-a76a-79c6cd9b43e0)
![image](https://github.com/Anshidanshi/pdftoword/assets/87684031/e380bec0-2511-4419-b899-2422590a5f5f)

### note estimated conversion time is a dummy 
# PDF to Word Conversion using Django

This is a Django project that provides a simple web interface to convert PDF files to Word documents. The project utilizes the `pdf2docx` library for PDF conversion and allows users to upload PDF files, perform the conversion, and download the resulting Word documents.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/your-pdf-to-word-conversion-project.git
   cd your-pdf-to-word-conversion-project
Create and activate a virtual environment:

```bash
Copy code
python -m venv venv
source venv/bin/activate
Install the project dependencies:

```bash
Copy code
pip install -r requirements.txt
Apply migrations to set up the database:

```bash
Copy code
python manage.py migrate
Start the development server:

bash
Copy code
python manage.py runserver
Access the web application at http://localhost:8000.

Usage
Upload a PDF file using the provided form.
After successful conversion, you'll receive a short code and a download link for the corresponding Word document.
Use the short code to download the converted Word document.
Project Structure
home/ - Django app directory containing the main project logic.
views.py - Contains views for PDF to Word conversion and related functionality.
models.py - Defines the ConvertedFile model for storing PDF and converted Word files.
templates/ - HTML templates for rendering the user interface.
media/ - Directory for storing uploaded and converted files.
yourpdf2wordproject/ - Django project directory.
settings.py - Project settings including configurations.
urls.py - URL routing for the project.
venv/ - Virtual environment directory (not included in the repository).
Contributing
Contributions are welcome! If you find any issues or want to enhance the project, feel free to create a pull request.

License
This project is licensed under the MIT License.

javascript
Copy code

Replace `Anshidanhhi`, `pdf-to-word`, and other placeholders with the appropriate information. Also, make sure to include your `LICENSE` file if you choose a different open-source license.

# LTMNC
