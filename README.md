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

# Google Scholar BibTeX Veri Toplama Otomasyonu [TR]

Bu proje, akademisyenlerin makale yazarken referans aldıkları diğer makalelerin BibTeX verilerini otomatik olarak toplar. Google Scholar veritabanı üzerinde arama yaparak, sonuçları BibTeX formatında düzenler.

## Nasıl Kullanılır?

Projeyi kullanmak için şu adımları izleyin:

1. **Projeyi bilgisayarınıza indirin**.
2. `ArticlesTitles.txt` dosyasını açın ve her satıra **bir makale başlığı** yazarak BibTeX verilerinin toplanacağı başlıkları girin.
3. **Projenin Python kodunu çalıştırın**. Tarayıcı otomatik olarak açılacaktır.
4. **Önemli**: Tarayıcıda işlem bitene kadar herhangi bir şeye tıklamayın.
5. İşlem tamamlandığında, `Results.txt` adında bir dosya oluşturulacak ve BibTeX verileri bu dosya içinde listelenmiş olacaktır.

---

## Features

- Automatically collects BibTeX entries from Google Scholar based on article titles.
- The collected data is formatted and saved into a `Results.txt` file.
- Simple and easy-to-use interface by modifying a text file (`ArticlesTitles.txt`).

---

## Requirements

- Python 3.6 or higher
- Required Python packages: `requests`, `beautifulsoup4`, etc. (These can be installed using `pip`).

---

## Installation

1. Clone the repository to your local machine:
    ```bash
    git clone https://github.com/yourusername/your-repository.git
    ```
2. Navigate to the project directory:
    ```bash
    cd your-repository
    ```
3. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
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

If you have any questions or need assistance, feel free to reach out via [email@example.com](mailto:email@example.com) or open an issue on the [GitHub repository](https://github.com/yourusername/your-repository/issues).

---

## Contributing

Contributions are welcome! If you’d like to contribute, please fork the repository and submit a pull request. Be sure to follow the guidelines for making contributions.

---

## Acknowledgements

- Thanks to [Google Scholar](https://scholar.google.com/) for providing the data.
- Special thanks to the [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) library for simplifying web scraping.

---

### Additional Information

- **File Structure:**
    - `ArticlesTitles.txt`: Contains the article titles for which you want to collect BibTeX entries.
    - `Results.txt`: Contains the collected BibTeX entries after running the script.
    - `requirements.txt`: Contains a list of Python dependencies.

---

Feel free to modify the code or expand the project as needed. Happy coding!
