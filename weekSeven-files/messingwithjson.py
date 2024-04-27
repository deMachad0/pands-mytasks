#messing with json

import json

electric_bill = {
    'name' : "Andre",
    'amount' : 9999
}

with open("storeData.json", "wt") as f:
    json.dump(electric_bill, f) #this command writes the dictionary
    print(electric_bill)