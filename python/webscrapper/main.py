# required packages
# pip install requests beautifulsoup4 selenium

from extractors.indeed import extract_indeed_jobs
from extractors.wwr import extract_wwr_jobs

keyword = input("What do you want to search for?")

indeed = extract_indeed_jobs(keyword)
wwr = extract_wwr_jobs(keyword)

jobs = indeed + wwr

# write results to file
file = open(f"{keyword}.csv", "w")

rownum = 0
for job in jobs:
    data = f"{job['position']},{job['company']}, {job['location']}, {job['link']}\n"
    file.write(data)

    # log
    rownum += 1
    print(f"[{rownum}] {data}")

file.close()
