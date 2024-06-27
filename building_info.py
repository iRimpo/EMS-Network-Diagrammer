building_images = {
    "02": "images/buildings/2.png",
    "04": "images/buildings/4.png",
    "05": "images/buildings/5.png",
    "06": "images/buildings/6.png",
    "07": "images/buildings/7.png",
    "10A": "images/buildings/10A.png",
    "14": "images/buildings/14.png",
    "15": "images/buildings/15.png",
    "16": "images/buildings/16.png",
    "17": "images/buildings/17.png",
    "23": "images/buildings/23.png",
    "25": "images/buildings/25.png",
    "25A": "images/buildings/25A.png",
    "26": "images/buildings/26.png",
    "27": "images/buildings/27.png",
    "30": "images/buildings/30.png",
    "31": "images/buildings/31.png",
    "32": "images/buildings/32.png",
    "33": "images/buildings/33.png",
    "34": "images/buildings/34.png",
    "35": "images/buildings/35.png",
    "36": "images/buildings/36.png",
    "37": "images/buildings/37.png",
    "40": "images/buildings/40.png",
    "41": "images/buildings/41.png",
    "43": "images/buildings/43.png",
    "44": "images/buildings/44.png",
    "45": "images/buildings/45.png",
    "46": "images/buildings/46.png",
    "46A": "images/buildings/46A.png",
    "47": "images/buildings/47.png",
    "48": "images/buildings/48.png",
    "48A": "images/buildings/48A.png",
    "50": "images/buildings/50.png",
    "50A": "images/buildings/50A.png",
    "50B": "images/buildings/50B.png",
    "50C": "images/buildings/50C.png",
    "50E": "images/buildings/50E.png",
    "50F": "images/buildings/50F.png",
    "52": "images/buildings/52.png",
    "53": "images/buildings/53.png",
    "54": "images/buildings/54.png",
    "55": "images/buildings/55.png",
    "55A": "images/buildings/55A.png",
    "56": "images/buildings/56.png",
    "56A": "images/buildings/56A.png",
    "58": "images/buildings/58.png",
    "58A": "images/buildings/58A.png",
    "59": "images/buildings/59.png",
    "60": "images/buildings/60.png",
    "61": "images/buildings/61.png",
    "62": "images/buildings/62.png",
    "63": "images/buildings/63.png",
    "64": "images/buildings/64.png",
    "65": "images/buildings/65.png",
    "65A": "images/buildings/65A.png",
    "65B": "images/buildings/65B.png",
    "66": "images/buildings/66.png",
    "67": "images/buildings/67.png",
    "67A": "images/buildings/67A.png",
    "69": "images/buildings/69.png",
    "70": "images/buildings/70.png",
    "70A": "images/buildings/70A.png",
    "71": "images/buildings/71.png",
    "71A": "images/buildings/71A.png",
    "71B": "images/buildings/71B.png",
    "72": "images/buildings/72.png",
    "72A": "images/buildings/72A.png",
    "72B": "images/buildings/72B.png",
    "72C": "images/buildings/72C.png",
    "73": "images/buildings/73.png",
    "74": "images/buildings/74.png",
    "75": "images/buildings/75.png",
    "75A": "images/buildings/75A.png",
    "75B": "images/buildings/75B.png",
    "76": "images/buildings/76.png",
    "77": "images/buildings/77.png",
    "77A": "images/buildings/77A.png",
    "78": "images/buildings/78.png",
    "79": "images/buildings/79.png",
    "80": "images/buildings/80.png",
    "80A": "images/buildings/80A.png",
    "81": "images/buildings/81.png",
    "82": "images/buildings/82.png",
    "83": "images/buildings/83.png",
    "84": "images/buildings/84.png",
    "85": "images/buildings/85.png",
    "85B": "images/buildings/85B.png",
    "88": "images/buildings/88.png",
    "90": "images/buildings/90.png",
    "91": "images/buildings/91.png"
}

def add_building_images(building_number):
    return building_images.get(str(building_number), "images/buildings/default.png")