from pymongo import MongoClient

client = MongoClient("localhost", 27017)
db = client["Assignment_1"]
athletes = db["Olympic_Athletes"]


medal_winning_summer_olympics_athletes = athletes.find(
    {
    "edition": {"$regex": "Summer"}, 
    "medal": {"$exists": True, "$ne": None}
    }
)

with open("athletes.txt", "w", encoding="utf-8") as output_file:
    for athlete in medal_winning_summer_olympics_athletes:
        athlete_id = int(athlete["athlete_id"])
        country = athlete["country_noc"]
        event = athlete["event"]
        year = int(athlete["edition"].split(" ")[0])
        medal = athlete["medal"]
        if (year >= 1980) and (year <= 2020):
            output_file.write(f"{athlete_id}, {country}, {year}, {event}, {medal}\n")

print("Task_1.1 complete.")