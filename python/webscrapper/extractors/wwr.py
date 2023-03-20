from bs4 import BeautifulSoup
from requests import get


def extract_wwr_jobs(keyword):
    base_url = "https://weworkremotely.com/remote-jobs/search?utf8=%E2%9C%93&term="
    search_term = "python"

    response = get(f"{base_url}{keyword}")

    if response.status_code != 200:
        print("Can't request website")
    else:
        results = []
        # [REF] https://www.crummy.com/software/BeautifulSoup/bs4/doc/
        # Objective : find section class="jobs" > ul > (all) li
        soup = BeautifulSoup(response.text, 'html.parser')
        jobs = soup.find_all('section', class_="jobs")
        for job_section in jobs:
            # go to first section, get two li from ul
            job_posts = job_section.find_all('li')
            # remove second li // <li class="view-all">
            job_posts.pop(-1)
            # go to next section get all li in ul
            for post in job_posts:
                anchors = post.find_all('a')
                # get second anchor only
                anchor = anchors[1]
                link = anchor['href']
                # approach span inside anchor
                company, kind, region = anchor.find_all(
                    'span', class_="company")
                title = anchor.find('span', class_='title')
                job_data = {
                    'link': f"https://weworkremotely.com{link}",
                    'company': company.string.replace(",", " "),
                    'location': region.string.replace(",", " "),
                    'position': title.string.replace(",", " ")
                }
                results.append(job_data)
        return results
