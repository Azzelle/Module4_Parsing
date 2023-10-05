import xml.etree.cElementTree as et

tree = et.parse("sample.xml")

root = tree.getroot()
job_titles = []
Company_Names = []
Categories = []
Cities = []

for title in root.iter('job_title'):
    job_titles.append(title.text)

for company in root.iter('company_name'):
    Company_Names.append(company.text)

for category in root.iter('category'):
    Categories.append(category.text)

for city in root.iter('city'):
    Cities.append(city.text)

print(job_titles)
print(Company_Names)
print(Categories)
print(Cities)