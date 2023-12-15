file = "data.txt"


with open(file, 'r') as f:
    next(f)
    lines = f.readlines()
founded_in_oman = []
working_in_lv = []
working_in_telecom = []
org_lv = []
lv_ssl = []
for i in range(len(lines)):
    parts = lines[i].rstrip().split(",")
    country = parts[4]

    founded = parts[6]
    industry = parts[7]
    num_of_employees = parts[8]
    website = parts[3]


    if country == "Oman":
        founded_in_oman.append(int(founded))

    
    if country == "Latvia":
        working_in_lv.append(int(num_of_employees))
        
        if industry == "Telecommunications":
            working_in_telecom.append(int(num_of_employees))

        domain = website.split(".")
        domain_end = domain[-1].strip("/")
        if domain_end == "org":
            org_lv.append(domain_end)

    
    ssl = website.split(":") 
    if ssl[0] == "https" and country == "Latvia":
        lv_ssl.append(website)
     
    
print("founded:", min(founded_in_oman))
print("num of Lv employyes:", sum(working_in_lv))
print("num of telecom employes:", sum(working_in_telecom))
print("org for lv:", len(org_lv))
print("ssl in lv:", len(lv_ssl))

f.close()