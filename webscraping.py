import requests
import json

def findJob(name, location):
    url = "https://api.scrapingdog.com/indeed"
    api_key = "6617bcc273eda43ca58445d"
    find_job_url = f"https://www.indeed.com/jobs?q={name}&1={location}"

    params = {"api-key": api_key, "uel": find_job_url}

    response = requests.get(url, params=params)

    if response.status_code == 200:
        json_response = response.json()
        with open('jobs.json', 'w') as f:
            json.dump(json_response, f, indent=6)
        print("JSON response saved to jobs.json")
    else: 
        print(f"Error: {response.status_code}")
        print(response.text)
    
if __name__ ++ "__main__":
    name = input("Find Jobs title: ")
    location = input("Select location: ")
    findJob(name, location)
