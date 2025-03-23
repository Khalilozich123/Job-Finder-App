# This script collect data concerning IT that referee to Information Technology
from bs4 import BeautifulSoup
import requests

# Collecting url
url_list = ["https://www.timesjobs.com/candidate/job-search.html?searchType=Home_Search&from=submit&asKey=OFF&txtKeywords=&cboPresFuncArea=35"]
j = 1
while j < 25:  # 100 is the number of pages every page contain 25 job that
    url = "https://www.timesjobs.com/candidate/job-search.html?from=submit&searchType=Home_Search&luceneResultSize=25&postWeek=60&cboPresFuncArea=35&pDate=Y&sequence=" + str(j)
    url_list.append(url)
    j = j + 1
# Collecting data
# Data list
IT_job = []
IT_camp = []
IT_exp = []
IT_location = []
IT_skill = []
IT_link = []
IT_Data = []
y= []
# Start of the collecting
for i in url_list:
    webpage = requests.get(i)
    soup = BeautifulSoup(webpage.content, "html.parser")
    # Collecting jobs 
    jobs = soup.find_all("h2")
    for i in jobs:
        x = i.text.replace("\n\r\n      ", "").strip()
        IT_job.append(x)
    IT_job.remove(IT_job[-1])
    # Collecting the company name 
    camp = soup.find("ul", class_="new-joblist").find_all("h3")
    for i in camp:
        x = i.text.replace("\r\n    ", "").replace(".\r\n     (More Jobs) \n", "").replace(" (More Jobs)", "").strip()
        IT_camp.append(x)
        # Collecting the experience required and location of the job
    exp_loc = soup.find_all("ul", class_="top-jd-dtl clearfix")
    for i in exp_loc:
        x = i.find("li").text.replace("card_travel", "")
        IT_exp.append(x)
    for i in exp_loc:
        x = i.find("span").text
        IT_location.append(x)
    # collecting the skills required
    skill = soup.find_all("li", class_="clearfix job-bx wht-shd-bx")
    
    for i in skill:
        x = i.find("span", class_="srp-skills").text.replace("\r\n      \r\n          ", "").replace(
            "\r\n        \r\n      ", "").strip()
        y.append(x)
        for i in y:
           z = i.split(" , ")
           c =[]
        for i in z:
           c.append(i.replace('"',""))

        c = c[:8]
        k=c[0]
        for i in c[1:]:
           k =k+" , "+i

        IT_skill.append(k)

    # Collecting job links
    link = soup.find_all("ul", class_="list-job-dtl clearfix")
    for i in link:
        x = i.find("li").find("a")["href"]
        IT_link.append(x)
# Collecting all the data in same list  
j = 0

while j < len(IT_job):
    x = IT_job[j] + "\n" + IT_camp[j] + "\n" + IT_exp[j] + "\n" + IT_location[j] + "\n" + IT_skill[j] + "\n" + IT_link[j]
    IT_Data.append(x)
    j = j + 1
# Saving the data
with open("IT Data.txt", "w") as file:
    for i in IT_Data:
        file.write(str(i) + "\n==========\n")
