import re
import requests


city = ["nj", "suzhou", "wx", "xa"]


u = "http://{}.bendibao.com/ditie/linemap.shtml"


class Parser:
    def __init__(self):
        self.all_maps = []
        self.xls = []
        self.href_re = re.compile(r"(?<=href=\").*?(?=\")")
        self.name_re = re.compile(r"(?<=>).*?(?=</a>)")

    def add_tags(self, tags):
        class Zd:
            def __init__(self, name, href, xls):
                self.name = name
                self.href = href
                self.xls = xls
        
        class Xl:
            def __init__(self, name, href):
                self.name = name
                self.href = href
        
        class Map:
            def __init__(self, name, href):
                self.name = name
                self.href = href

        for tag in tags:
            hrefs = self.href_re.findall(tag)
            names = self.name_re.findall(tag)
            if not hrefs:
                print("href not found", tag)
                continue
            href = hrefs[0]
            if not names:
                print("name not found", tag)
                continue
            name = names[0]
            if href.startswith("/ditie/zd_"):
                self.all_maps[-1].append(Zd(name, href, self.xls))
                self.xls = []
            if href.startswith("/ditie/xl_"):
                self.xls.append(Xl(name, href))
            if href.startswith("/ditie/map_"):
                self.all_maps.append([Map(name, href)])


def get_sites(city, html_content):
    """[
        {"name": "", "link": "", "trans": []},
        {"name": "", "link": "", "trans": []},
    ]
    map_某个地铁线路的开始标志
    zd_某个地铁站
    xl_某个换乘线路
    """
    html_content = html_content.replace("<a", "\n<a")
    html_content = html_content.replace("</a>", "</a>\n")
    a_tags = []
    for li in html_content.split("\n"):
        if li.startswith("<a") and li.endswith("</a>") and 'href="/ditie/' in li:
            a_tags.append(li.strip())
    with open(f"{city}_.html", "w") as f:
        f.write("\n".join(a_tags))
    p = Parser()
    p.add_tags(a_tags)
    for m in p.all_maps:
        print("")
        print(m[0].name, len(m) - 1)
        print(",".join([a.name for a in m[1:]]))
    return p


for c in city:
    url = u.format(c)
    res = requests.get(url)
    get_sites(c, res.text)
