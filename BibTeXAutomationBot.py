from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def google_scholar_search(file_path, output_file):
    # Chrome WebDriver'ı başlat
    driver = webdriver.Chrome()
    driver.get("https://scholar.google.com/")
    wait = WebDriverWait(driver, 10)  # Explicit wait

    # Dosyayı oku ve satırları al
    with open(file_path, "r", encoding="utf-8") as file:
        queries = file.readlines()

    # Sonuçları yazacağımız dosyayı aç
    with open(output_file, "w", encoding="utf-8") as output:
        for query in queries:
            query = query.strip()
            if not query:
                continue

            try:
                # Arama kutusunu bul ve sorguyu yaz
                search_box = wait.until(EC.presence_of_element_located((By.NAME, "q")))
                search_box.clear()
                search_box.send_keys(query)
                search_box.send_keys(Keys.RETURN)
                time.sleep(3)

                # İlk sonucu al
                first_result = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "h3.gs_rt a")))

                # "Alıntı yap" butonuna bas
                cite_button = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "a.gs_or_cit")))
                cite_button.click()
                time.sleep(2)

                # "BibTeX" butonuna bas
                bibtex_button = wait.until(EC.presence_of_element_located((By.LINK_TEXT, "BibTeX")))
                bibtex_button.click()
                time.sleep(2)

                # BibTeX içeriğini al
                bibtex_content = wait.until(EC.presence_of_element_located((By.TAG_NAME, "pre"))).text
                output.write(f"\n{bibtex_content}\n")
                
                # Geri dön (Google Scholar sonuçlarına)
                driver.back()
                time.sleep(2)
                driver.back()
                time.sleep(2)

            except Exception as e:
                output.write(f"Hata oluştu ({query}): {e}\n")
                output.write("-" * 50 + "\n\n")  # Boş satır eklemek için \n ekledik

    driver.quit()

# Kullanım
google_scholar_search("ArticleTitles.txt", "Results.txt")
