from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def get_page_count(keyword):
    base_url = f"https://kr.indeed.com/jobs?q={keyword}&l=seoul&from=searchOnHP&vjk=1015284880e2ff62"
    options = Options()
    # Replit
    # options.add_argument("--no-sandbox")
    # options.add_argument("--disable-dev-shm-usage")

    browser = webdriver.Chrome(options=options)
    browser.get(base_url)

    soup = BeautifulSoup(browser.page_source, "html.parser")
    pagination = soup.find("nav", class_="css-jbuxu0")
    if pagination == None:
        return 1

    pages = pagination.find_all("div", recursive=False)
    count = len(pages)
    if count >= 5:
        # Restrictions to keep the site from being abused
        return 5
    else:
        return count


def extract_indeed_jobs(keyword):
    pages = get_page_count(keyword)
    print("Found", pages, "pages")

    results = []

    for page in range(pages):

        options = Options()
        # Replit
        # options.add_argument("--no-sandbox")
        # options.add_argument("--disable-dev-shm-usage")

        browser = webdriver.Chrome(options=options)
        base_url = f"https://kr.indeed.com/jobs?q={keyword}&start={page * 10}&l=seoul&from=searchOnHP&vjk=1015284880e2ff62"
        print("Requesting", base_url)

        # open web url
        browser.get(base_url)

        # Convert to soup type
        soup = BeautifulSoup(browser.page_source, "html.parser")
        job_list = soup.find("ul", class_="jobsearch-ResultsList")

        # job_list 내용중 모든 li를 검색(recursive=False 하위 1단계로 제한)
        jobs = job_list.find_all('li', recursive=False)

        for job in jobs:
            zone = job.find("div", class_="mosaic-zone")
            if zone == None:
                anchor = job.select_one("h2 a")
                title = anchor['aria-label']
                link = anchor['href']
                company = job.find("span", class_="companyName")
                location = job.find("div", class_="companyLocation")
                job_data = {
                    'link': f"https://kr.indeed.com{link}",
                    'company': company.string.replace(",", " "),
                    'location': location.string.replace(",", " "),
                    'position': title.replace(",", " "),
                }
                results.append(job_data)

    return results
