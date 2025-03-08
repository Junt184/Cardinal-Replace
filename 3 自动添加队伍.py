# coding=utf-8
import json
import requests


def add_team(team_num):
    team_name = [str(i) for i in range(1, team_num + 1)] # 用1-13命名
    # team_name = [input(f"队名{_}:") for _ in range(1, team_num)] # 手动input命名
    token = "fd6de30f-a595-4264-8786-883188dc94ee"
    url = "http://127.0.0.1:19999/api/manager/teams"

    headers = {"Authorization" : token}
    json_data = [
        {"Name" : name,
         "Login": ''} for name in team_name
    ]
    res = requests.post(url, json=json_data, headers=headers)
    reponse = json.loads(res.content.decode())
    if reponse['msg'] == "Duplicated Team Found!":
        print("有已经存在的用户名")
        exit()

    user_pass = reponse['data']
    for i in user_pass:
        print(i)

if __name__ == '__main__':
    team_num = 13
    add_team(team_num)