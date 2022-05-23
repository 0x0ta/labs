from urllib.parse import urlparse

def domain_name(url):
    print(urlparse(url))
    return (urlparse(url).netloc.replace("www.","").split(".")[0]) if urlparse(url).netloc is not "" else urlparse(url).path.replace("www.","").split(".")[0]