import yaml
import requests


cookie = """
"""
cookie_dict = {}
for c in cookie.split("; "):
    c = c.strip()
    a = c[0:c.index("=")]
    b = c[c.index("=")+1:]
    cookie_dict[a.strip()] = b.strip()


body = {
    "operationName": None,
    "query": """{brightTitle currentTimestamp allContests { title titleSlug __typename}}""",
    "variables": {}
}

headers = {
    "origin": "https://leetcode.com",
    "referer": "https://leetcode.com/contest/",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-origin",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36 Edg/85.0.564.51",
    "x-csrftoken": cookie_dict["csrftoken"],
}


def get_all_contest():
    url = "https://leetcode.com/graphql"
    res = requests.post(url, json=body, cookies=cookie_dict, headers=headers)
    return res.json()["data"]["allContests"]


def get_all_question(contestSlug):
    url = f"https://leetcode.com/contest/api/info/{contestSlug}/"
    res = requests.get(url, cookies=cookie_dict, headers=headers)
    allQuest = res.json()["questions"]
    url = f"https://leetcode.com/contest/api/myranking/{contestSlug}/?region=global"
    res = requests.get(url, cookies=cookie_dict, headers=headers)
    solved = res.json()["my_solved"]
    unsolved = []
    for q in allQuest:
        if q["question_id"] not in solved:
            unsolved.append(q)
    return unsolved


def output(contests):
    """
    [
        {
            "title": "Weekly Contest 201",
            "url": "",
            "quest": [
                {
                    "title": "",
                    "url": ""
                },
                ...
            ]
        },
        ...
    ]
    """
    file_path = "Readme.md"
    with open(file_path, "w") as fi:
        fi.write("# All unsolved question")
        for cont in contests:
            fi.write(f"## [{cont['title']}]({cont['url']})\n")
            for q in cont["quest"]:
                fi.write(f"    - [{q['title']}]({q['url']})\n")
            if not cont["quest"]:
                fi.write("    - All Pass\n")
            fi.write("\n")


allContests = get_all_contest()
print(len(allContests))
# TODO give a question list and solve status for each question, 
# not only contest status
result = []
for contest in allContests[2:]:
    titleSlug = contest["titleSlug"]
    if titleSlug == "weekly-contest-199":
        break
    quest = get_all_question(titleSlug)
    obj = {"title": contest["title"]}
    obj["url"] = f"https://leetcode.com/contest/{titleSlug}"
    obj["quest"] = []
    for q in quest:
        questSlug = q["title_slug"]
        title = f"{q['question_id']}. {q['title']}"
        obj["quest"].append({
            "url": f"https://leetcode.com/contest/{titleSlug}/problems/{questSlug}",
            "title": title
        })
    result.append(obj)
output(result)
print("Done")
