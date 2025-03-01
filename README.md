
# Google Scholar BibTeX Data Collection Automation [EN]

This project automates the process of collecting BibTeX entries for articles cited by academics when writing papers. It searches the Google Scholar database and formats the results according to the BibTeX citation style.

## How to Use?

To use this project, follow these steps:

1. **Download the project** to your computer.
2. Open the `ArticlesTitles.txt` file and **enter one article title per line**. These titles will be used to collect BibTeX entries.
3. **Run the Python code**. A browser window will automatically open.
4. **Important**: Do **not** click anything in the browser while the script is running.
5. After the process completes, a file named `Results.txt` will be created. This file will contain the collected BibTeX entries.

---

## Features

- Automatically collects BibTeX entries from Google Scholar based on article titles.
- The collected data is formatted and saved into a `Results.txt` file.
- Simple and easy-to-use interface by modifying a text file (`ArticlesTitles.txt`).

---

## Requirements

- Python 3.6 or higher
- Required Python packages: `selenium`, `time`, etc. (These can be installed using `pip`).

---

## Installation

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/cihanayindi/GoogleScholarBibTeXAutomation
    ```
2. Navigate to the project directory:
    ```bash
    cd GoogleScholarBibTeXAutomation
    ```
3. Install the Selenium Library:
    ```bash
    pip install selenium
    ```

---

## Troubleshooting

- **If the script doesn’t work properly:**
    - Make sure that the article titles in the `ArticlesTitles.txt` file are accurate.
    - Check your internet connection as the project requires web scraping from Google Scholar.
    - If the script gets stuck, try running it again after a short time.

---

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more information.

---

## Contact

If you have any questions or need assistance, feel free to reach out via [cihanayindi00@gmail.com](mailto:cihanayindi00@gmail.com) or open an issue on the [GitHub repository](https://github.com/yourusername/your-repository/issues). Also you can reach out via [LinkedIn](https://www.linkedin.com/in/cihanayindi/)

---

## Contributing

Contributions are welcome! If you’d like to contribute, please fork the repository and submit a pull request. Be sure to follow the guidelines for making contributions.

---

## Acknowledgements

- Thanks to [Google Scholar](https://scholar.google.com/) for providing the data.
- Thanks to Mehmetcan Karademir for the project idea.

---

### Additional Information

- **File Structure:**
    - `ArticlesTitles.txt`: Contains the article titles for which you want to collect BibTeX entries.
    - `Results.txt`: Contains the collected BibTeX entries after running the script.
---

Feel free to modify the code or expand the project as needed. Happy coding!
