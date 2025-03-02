from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def google_scholar_search(file_path, output_file):
    # Start Chrome WebDriver
    driver = webdriver.Chrome()
    driver.get("https://scholar.google.com/")
    wait = WebDriverWait(driver, 10)  # Explicit wait

    # Read the file and get the lines
    with open(file_path, "r", encoding="utf-8") as file:
        queries = file.readlines()

    # Open the file where we will write the results
    with open(output_file, "w", encoding="utf-8") as output:
        for query in queries:
            query = query.strip()
            if not query:
                continue

            try:
                # Find the search box and type your query
                search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))
                search_box.clear()
                search_box.send_keys(query)
                search_box.send_keys(Keys.RETURN)
                time.sleep(8)

                # Get first result
                first_result = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h3.gs_rt a")))

                # Press the "Quote" button
                cite_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.gs_or_cit")))
                cite_button.click()
                time.sleep(4)

                # Click the "BibTeX" button
                bibtex_button = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "BibTeX")))
                bibtex_button.click()
                time.sleep(4)

                # Get BibTeX content
                bibtex_content = wait.until(EC.presence_of_element_located((By.TAG_NAME, "pre"))).text
                output.write(f"\n{bibtex_content}\n")
                
                # Back (to Google Scholar results)
                driver.back()
                time.sleep(4)
                # Close the opened pop-up
                driver.back()
                time.sleep(4)

            except Exception as e:
                output.write(f"Hata oluştu ({query}): {e}\n")
                output.write("-" * 50 + "\n\n")

    driver.quit()

# Write txt names here for use
google_scholar_search("GoogleScholarBibTeXAutomation\ArticleTitles.txt", "Results.txt")
