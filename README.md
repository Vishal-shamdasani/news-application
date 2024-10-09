# News Website

This project is a Flask-based web application that displays news articles fetched from the News API. It features a dark-themed interface with horizontally scrollable news cards.

## Prerequisites

Before you begin, ensure you have met the following requirements:
* You have installed Python 3.7 or later.
* You have a Windows/Linux/Mac machine.
* You have obtained an API key from [News API](https://newsapi.org/).

## Installing News Website

To install the News Website, follow these steps:

1. Clone the repository:
   ```
   git clone https://github.com/yourusername/news-website.git
   cd news-website
   ```

2. Create a virtual environment (optional but recommended):
   ```
   python -m venv venv
   ```

3. Activate the virtual environment:
   - On Windows:
     ```
     venv\Scripts\activate
     ```
   - On macOS and Linux:
     ```
     source venv/bin/activate
     ```

4. Install the required dependencies:
   ```
   pip install flask requests
   ```

## Configuration

To configure the News API key:

1. Open the `app.py` file in a text editor.

2. Look for a line that says:
   ```python
   apikey = 'add your api key'
   ```

3. Replace `'add your api key'` with your actual News API key. For example:
   ```python
   apikey = 'abcdef1234567890abcdef1234567890'
   ```

4. Save the file.

## Running News Website

To run News Website, follow these steps:

1. Ensure you're in the project directory and your virtual environment is activated (if you're using one).

2. Run the application:
   ```
   python app.py
   ```

3. Open a web browser and navigate to `http://127.0.0.1:5000/`.

## Additional Information

- The website fetches news articles using the News API. If you want to modify the news sources or categories, you can edit the API request in the `app.py` file.
- The dark theme is implemented using custom CSS. You can modify the styles in `static/css/style.css`.
- The horizontally scrollable news cards are implemented using CSS flexbox. You can adjust the card layout in the CSS file as well.

## Contributing to News Website

To contribute to News Website, follow these steps:

1. Fork this repository.
2. Create a branch: `git checkout -b <branch_name>`.
3. Make your changes and commit them: `git commit -m '<commit_message>'`
4. Push to the original branch: `git push origin <project_name>/<location>`
5. Create the pull request.

Alternatively, see the GitHub documentation on [creating a pull request](https://help.github.com/articles/creating-a-pull-request/).

## Contact

If you want to contact me, you can reach me at `shamdasani46@gmail.com>`.

