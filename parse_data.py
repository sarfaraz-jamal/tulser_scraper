import json
from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO


def parse_data(data):
    jsonblob = json.loads(data["JsonBlob"])

    title = data["Title"]

    first_level = jsonblob["Processen"]

    clean_data = {}

    for i in first_level:
        if title not in clean_data:
            clean_data[title] = {}
        for j in i["Taken"]:
            if i["Procestitel"] not in clean_data[title]:
                clean_data[title][i["Procestitel"]] = {}
            for k in j["Stappen"]:
                if j["Taaktitel"] not in clean_data[title][i["Procestitel"]]:
                    clean_data[title][i["Procestitel"]][j["Taaktitel"]] = {}
                clean_data[title][i["Procestitel"]][j["Taaktitel"]][k["Staptitel"]] = [] 
                html = k["Stapcontent"]

                try:
                    soup = BeautifulSoup(html, 'html.parser')
                
                    try:
                        # Find all <iframe> tags
                        all_iframe_tags = soup.find_all('iframe')
                        
                        for iframe_tag in all_iframe_tags:
                            # Extract the 'src' attribute from each <iframe> tag
                            src_attribute = iframe_tag.get('src')
                            
                            if src_attribute:
                                # Append the formatted URL to the fake_list
                                clean_data[title][i["Procestitel"]][j["Taaktitel"]][k["Staptitel"]].append("https://tulser.askme.nl/" + src_attribute)
                    except:
                        pass

                    try:
                        # Find all <iframe> tags
                        all_img_tags = soup.find_all('img')
                        
                        for img_tag in all_img_tags:
                            # Extract the 'src' attribute from each <iframe> tag
                            src_attribute = img_tag.get('src')
                            
                            if src_attribute:
                                
                                src_link = "https://tulser.askme.nl/" + src_attribute
                                clean_data[title][i["Procestitel"]][j["Taaktitel"]][k["Staptitel"]].append(src_link)

                                
                    except:
                        pass

                    try:
                        text = soup.findAll('p')
                        for t in text:
                            clean_data[title][i["Procestitel"]][j["Taaktitel"]][k["Staptitel"]].append(t.text)
                    except:
                        pass

                except:
                    pass        

    with open(f"data/{title}.json", "w", encoding='utf-8') as file:
        json.dump(clean_data, file, ensure_ascii=False, indent=4)