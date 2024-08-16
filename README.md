# File and Image Search Web Application

This is a simple web application built with Flask that allows users to search for files (PDF, DOC, DOCX, XLS, XLSX, PPT, PPTX) and images online. The application scrapes Google search results for the specified file types or images based on the user's query.

## Features

- **File Search**: Search for specific file types such as PDF, DOC, DOCX, XLS, XLSX, PPT, and PPTX using Google search.
- **Image Search**: Search for images based on a user-defined query.
- **Responsive UI**: A simple and responsive user interface with a modern gradient background and hover effects.

## How to Run

### Prerequisites

- Python 3.x installed
- `pip` (Python package installer)

### Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/file-image-search.git
    cd file-image-search
    ```

2. Install the required Python packages:

    ```bash
    pip install -r requirements.txt
    ```

### Running the Application

1. Start the Flask development server:

    ```bash
    python app.py
    ```

2. Open your web browser and navigate to `http://127.0.0.1:5000/` to access the application.

### Usage

- Enter a search query in the text input field.
- Select the type of files you want to search for from the dropdown menu.
- Click the "Search" button to see the results.

## Files Structure

- **index.html**: The main HTML file that provides the user interface.
- **app.py**: The Flask application that handles routing and search functionality.
- **requirements.txt**: A list of required Python packages.

## Notes

- This application relies on web scraping using `requests` and `BeautifulSoup4`. Be aware of the terms of service of the websites you scrape.
- The application scrapes Google search results, so performance and results may vary based on network conditions and Google's response.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
