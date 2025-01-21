### README

# Selenium Web Scraper with Proxy Support

This Python script demonstrates how to scrape data from a website using Selenium while leveraging proxy rotation for anonymity. The script specifically targets [Books to Scrape](https://books.toscrape.com/) to collect book titles and their prices.

---

## Features
- Uses Selenium WebDriver to scrape data.
- Implements proxy rotation by selecting a random proxy from a list.
- Navigates through all pages on the website and extracts book titles and prices.
- Handles dynamic page loading and navigation with Selenium's wait functionality.

---

## Prerequisites

### **1. Required Tools and Libraries**
- **Python 3.7 or later**
- **Google Chrome**
- **ChromeDriver** (compatible with your Chrome version)
- Python libraries:
  - `selenium`

Install Selenium using:
```bash
pip install selenium
```

### **2. Proxy List**
- Create a `proxies_list.txt` file in the same directory as the script.
- Add your proxies in the following format:
  ```
  192.168.1.1:8080
  192.168.1.2:8080
  ```

### **3. ChromeDriver Path**
- Ensure `chromedriver.exe` is downloaded and the correct path is set in the script:
  ```python
  path = "C:/Users/agham/chromedriver-win64/chromedriver.exe"
  ```

---

## How to Use

1. Clone or download the repository.
2. Add your list of proxies to `proxies_list.txt`.
3. Update the `path` variable with the correct path to your `chromedriver.exe`.
4. Run the script:
   ```bash
   python scraper.py
   ```

---

## Workflow

1. **Load Proxies**: Reads proxies from `proxies_list.txt` and selects one at random.
2. **Configure WebDriver**: Sets up ChromeDriver to use the selected proxy.
3. **Scrape Website**:
   - Opens [Books to Scrape](https://books.toscrape.com/).
   - Navigates through all pages.
   - Extracts book titles and prices.
4. **Output**: Prints the first 5 book details to the console and saves all data in a Python dictionary.

---

## Error Handling

- **Proxy Errors**: If a proxy fails, the script terminates with an error message.
- **WebDriver Timeout**: The script uses explicit waits to handle dynamic elements.

---

## Example Output

```text
Using proxy: 192.168.1.1:8080
Title: A Light in the Attic, Price: £51.77
Title: Tipping the Velvet, Price: £53.74
Title: Soumission, Price: £50.10
Title: Sharp Objects, Price: £47.82
Title: Sapiens: A Brief History of Humankind, Price: £54.23
```

---

## Notes
- The script currently extracts up to **Page 50** of the website.
- Adjust the `current_page` and pagination logic if the target website changes.
- Use ethically and in compliance with the target website's terms of service.

---

## License
This project is open-source and available under the MIT License.
