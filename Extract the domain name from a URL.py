def domain_name(url):
    return url.split("://")[-1].split("www.")[-1].split(".")[0]

################

def domain_name(url):
    url = url.split("://")[-1]


    url = url.split("www.")[-1]

    domain_split = url.split(".")
    return domain_split[0]


url = "http://github.com/francerivera/python"
print(f"domain name = {domain_name(url)}")
