import requests
import json
import csv
from parse_data import parse_data

with open('converted_links.csv', 'r') as file:
    links = [row[0] for row in csv.reader(file)]


querystring = {"rnd":"1707907923186","userId":"113"}

headers = {
    "Accept": "application/json, text/plain, */*",
    "Accept-Language": "en-US,en;q=0.9",
    "Authorization": "bearer KXdOU2-cvU44Nyu0YG11P5VEbZK_bZ7ZqT7-f5ypO2G-5nljcV9fYwCVFeqiYiKXLI0SVm0xpuXTB3EYAQt1heIjbNXge57VU7u2mml7xcaqm0VTrDgViHZ0IEimgQKFxXZWssQNdc23np1ycYX5zKqYnDONgglaydHlie3HStsFROaLS3jLaFHCVdtksjXhSim8hUv77fj3yAkxjGC6Fsyzoz1_GOclLFzvClI_pl8dl71J2g_JUmlRgRkoe8LK4UvC877it76wcNzeUtiY8WDBXUTCw9xxG1cK6_j8KDlrgtqQtyYR8fJp1VICX7wja-9YISB93dbMrFD-o9aW5f8ELI-LiTLre19We84sWCTidoimnrHQ1QJdbmtbug5m",
    "Cache-Control": "no-cache",
    "Connection": "keep-alive",
    "Content-Type": "application/json",
    "Cookie": "ajs_user_id=113; ajs_anonymous_id=9e716235-4bdf-42c1-a69a-f23320569f6a; ajs_group_id=113; _fw_crm_v=14e58dbf-a9d6-434a-d817-78ced5f834e1; ASQME-TOKEN=KXdOU2-cvU44Nyu0YG11P5VEbZK_bZ7ZqT7-f5ypO2G-5nljcV9fYwCVFeqiYiKXLI0SVm0xpuXTB3EYAQt1heIjbNXge57VU7u2mml7xcaqm0VTrDgViHZ0IEimgQKFxXZWssQNdc23np1ycYX5zKqYnDONgglaydHlie3HStsFROaLS3jLaFHCVdtksjXhSim8hUv77fj3yAkxjGC6Fsyzoz1_GOclLFzvClI_pl8dl71J2g_JUmlRgRkoe8LK4UvC877it76wcNzeUtiY8WDBXUTCw9xxG1cK6_j8KDlrgtqQtyYR8fJp1VICX7wja-9YISB93dbMrFD-o9aW5f8ELI-LiTLre19We84sWCTidoimnrHQ1QJdbmtbug5m; ASQME-USERID=113; ASQME-EMAIL=r.kouwenberg@tulser.com; ASQME-USERROLE=Administrator; ASQME-ORGANISATIONID=tulser; _gid=GA1.2.852134315.1707821465; il-dat-session-id=e232e9e2-4535-491b-aa08-8c877e48ee4f; _gat_gtag_UA_120068409_3=1; _ga=GA1.1.339349451.1707213589; _ga_X5DPDLGXH3=GS1.1.1707905549.16.1.1707907922.40.0.0",
    "Pragma": "no-cache",
    "Referer": "https://tulser.askme.nl/app3/",
    "Sec-Fetch-Dest": "empty",
    "Sec-Fetch-Mode": "cors",
    "Sec-Fetch-Site": "same-origin",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
    "sec-ch-ua": '''"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"''',
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": '"Windows"',
}

for link in links[:1]:
    print(link)

    response = requests.request("GET", link, headers=headers, params=querystring)

    data = json.loads(response.text)
    
    parse_data(data)
       

