# scanNsearch

scanNsearch is a web application that allows users to extract text from uploaded images using Optical Character Recognition (OCR) and search for specific keywords within the extracted text. The application is built using **Streamlit** and **EasyOCR**, providing a user-friendly interface for text extraction and search functionality in multiple languages, including English and Hindi.

## Features

- **OCR Text Extraction**: Extract text from uploaded images using EasyOCR.
- **Keyword Search**: Search for keywords in the extracted text and highlight the results.
- **Multi-language Support**: Supports text extraction in English and Hindi.
- **Web Interface**: Built using Streamlit for a simple and interactive user experience.
  
## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/scanNsearch.git
   ```
2. Navigate to the project directory:
   ```bash
   cd scanNsearch
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the application:
   ```bash
   streamlit run TheApp.py
   ```

## Usage

1. Upload an image containing text that you want to extract.
2. The application will display the extracted text.
3. Enter a keyword to search within the extracted text.
4. The application will highlight the occurrences of the keyword.

## Project Structure

- `TheApp.py`: Main application file where the OCR and keyword search logic is implemented.
- `requirements.txt`: List of Python libraries required to run the application.

## Requirements

- Python 3.8 or above
- Streamlit
- EasyOCR
- PyTorch (required for EasyOCR)

## Deployment

To deploy this app:

1. Initialize a git repository in the project directory:
   ```bash
   git init
   ```

2. Add your remote repository:
   ```bash
   git remote add origin https://github.com/yourusername/scanNsearch.git
   ```

3. Push the code to your GitHub repository:
   ```bash
   git add .
   git commit -m "Initial commit"
   git branch -M main
   git push -u origin main
   ```

You can also deploy the app on Streamlit Cloud by connecting your GitHub repository and setting up the deployment.

## Contributing

Contributions are welcome! Please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License.

---

Make sure to replace `yourusername` with your actual GitHub username when uploading this file to your repository.
