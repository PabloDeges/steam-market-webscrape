import json

def main():
    temp_name = []

    with open("formatted_name_output.json", "r") as f:
        data = json.load(f)
        for item in data:
            temp_name.append(item)

    temp_price = []

    with open("formatted_price_output.json", "r") as f:
        data = json.load(f)
        for item in data:
            temp_price.append(item)

    temp_img = []

    with open("formatted_img_output.json", "r") as f:
        data = json.load(f)
        for item in data:
            temp_img.append(item)

    all_items = []

    for x in range(0, (len(temp_name))):

        #dont judge this please :D

        name = temp_name[x]
        w = "" 
        c = ""

        if "Glock-18" in name:
            w = "Glock-18"
            c = "Pistol"

        elif "P200" in name:
            w = "P200"
            c = "Pistol"

        elif "USP-S" in name:
            w = "USP-S"
            c = "Pistol"

        elif "P250" in name:
            w = "P250"
            c = "Pistol"

        elif "Dual Berettas" in name:
            w = "Dual Berettas"
            c = "Pistol"

        elif "Tec-9" in name:
            w = "Tec-9"
            c = "Pistol"

        elif "Five-SeveN" in name:
            w = "Five-SeveN"
            c = "Pistol"

        elif "CZ75-Auto" in name:
            w = "CZ75-Auto"
            c = "Pistol"

        elif "Desert Eagle" in name:
            w = "Desert Eagle"
            c = "Pistol"

        elif "R8 Revolver" in name:
            w = "R8 Revolver"
            c = "Pistol"

        elif "Nova" in name:
            w = "Nova"
            c = "Shotgun"

        elif "XM1014" in name:
            w = "XM1014"
            c = "Shotgun"

        elif "MAG-7" in name:
            w = "MAG-7"
            c = "Shotgun"

        elif "Sawed-Off" in name:
            w = "Sawed-Off"
            c = "Shotgun"

        elif "MAG-10" in name:
            w = "MAG-10"
            c = "SMG"
        elif "MP9" in name:
            w = "MP9"
            c = "SMG"

        elif "UMP-45" in name:
            w = "UMP-45"
            c = "SMG"
        elif "MP7" in name:
            w = "MP7"
            c = "SMG"

        elif "PP-Bizon" in name:
            w = "PP-Bizon"
            c = "SMG"
        elif "P90" in name:
            w = "P90"
            c = "SMG"
        elif "MP5-SD" in name:
            w = "MP5-SD"
            c = "SMG"
        
        elif "Galil AR" in name:
            w = "Galil AR"
            c = "Rifle"

        elif "FAMAS" in name:
            w = "FAMAS"
            c = "Rifle"

        elif "AK-47" in name:
            w = "AK-47"
            c = "Rifle"
        elif "M4A4" in name:
            w = "M4A4"
            c = "Rifle"
        elif "M4A1-S" in name:
            w = "M4A1-S"
            c = "Rifle"
        elif "SG 553" in name:
            w = "SG 553"
            c = "Rifle"
        elif "AUG" in name:
            w = "AUG"
            c = "Rifle"

        elif "SSG 08" in name:
            w = "SSG 08"
            c = "Sniper"
        elif "AWP" in name:
            w = "AWP"
            c = "Sniper"
        elif "G3SG1" in name:
            w = "G3SG1"
            c = "Sniper"
        elif "SCAR-20" in name:
            w = "SCAR-20"
            c = "Sniper"
        elif "M249" in name:
            w = "M249"
            c = "Heavy"
        elif "Negev" in name:
            w = "Negev"
            c = "Heavy"
        
        elif "Knife" in name:
            w = "Knife"
            c = "Knife"
        elif "Gloves" in name:
            w = "Gloves"
            c = "Gloves"






        dic = {
            "name" : name, 
            "price" : temp_price[x],
            "img" : temp_img[x],
            "weapon" : w,
            "class" : c,

        }

        all_items.append(dic)

    with open("all_sorted_data.json", "w") as f:
        json.dump(all_items, f)

if __name__ == "__main__":
    main()