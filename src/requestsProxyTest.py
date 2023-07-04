import requests
import URLs

proxies = {
    'http':'http://wwwproxykanazawa-it.ac.jp:8080',
    'https':'https://wwwproxykanazawa-it.ac.jp:8080'
}

res = requests(URLs.AllprojectURL,proxies=proxies)
