from bs4 import BeautifulSoup
import requests

html_req = requests.get("https://uk.indeed.com/jobs?q=bioinformatics&l=&from=searchOnHP&vjk=39ec3b3b0af918e2").text




