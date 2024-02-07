import requests
from bs4 import BeautifulSoup
import pandas as pd

URL="https://www.payscale.com/college-salary-report/majors-that-pay-you-back/bachelors/page/"
records = []

for current_page in range(34):
    print(current_page)
    endpoint = f"{URL}{current_page + 1}"
    response = requests.get(endpoint)
    soup = BeautifulSoup(response.text, "html.parser")
    rows = soup.select("table.data-table tbody tr")
    for row in rows:
        cells = row.select("span.data-table__value")
        record = {
            "Rank": cells[0].getText(),
            "Major": cells[1].getText(),
            "Degree Type": cells[2].getText(),
            "Early Career Pay": float(
                cells[3].getText().strip("$").replace(",", "")
            ),
            "Mid-Career Median Salary": float(
                cells[4].getText().strip("$").replace(",", "")
            ),
            "High Meaning":cells[5].getText()
        }
        records.append(record)

pd.DataFrame(records).to_csv("salaries_by_college_major_updated.csv", index=False)
