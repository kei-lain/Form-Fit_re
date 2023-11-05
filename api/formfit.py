import os , requests, json, openai
import asyncio , aiohttp
from dotenv import load_dotenv


load_dotenv()

openai.api_key = os.getenv("OPENAI_API")
RapidAPI_Key = os.getenv("RAPIDAPI_KEY")
RapidAPI_Host = os.getenv("RAPIDAPI_HOST")
url = os.getenv("URL_FOR_API")


def creatWorkouts(goal):
    recommendations = []
    limited = ("abductors,abs,adductors,biceps,calves,cardiovascular system,delts,forearms,glutes,hamstrings,lats,levator scapulae,pectorals,quads,serratus anterior,spine,traps,triceps,upper back")
    prompt = (f'what areas should this person focus on to archieve the following goal: {goal}? only answer using these terms of this {limited}. no extra words')
    message =  [{"role": "user", "content": f"{prompt}"}]
    try:
        response =openai.ChatCompletion.create(model="gpt-4",
                                messages=[
                                        {"role": "user", "content": prompt}])
    except:
        pass
    areas = response["choices"][0]["message"]["content"]

    
    print(areas)
    for area in areas.split(", "):
        area.strip()
        area = str(area)
        print(area)
        

        recommendation =  matchWorkouts(area)
        recommendations.append(recommendation)

    return recommendations
    print('done')




def matchWorkouts(area):
    #url =  "https://exercisedb.p.rapidapi.com/target/"
    # orig_url = url
    querystring = {"limit":"10"}

   
    # for area in areas:
    excersises = {}
    if area.__contains__("  "):
        area.replace("  ", "%20")
        print(area)
    elif area.__contains__("."):
        area.split(".")
        print(area)
    area = area.lower()
    new_url = (f"https://exercisedb.p.rapidapi.com/exercises/target/{area}")
    headers = {"X-RapidAPI-Key": RapidAPI_Key, "X-RapidAPI-Host": RapidAPI_Host}
    response = requests.get(new_url, headers=headers, params=querystring)

    compList = response.json()
    print(compList)
    for excersise in compList:
        print(excersise)
        # excersises[(part['name'])] = {excersise}
        # # print(excersises[(part['name'])])
        name = excersise['name']
        excersises[name] = excersise
        print((f"{name}----{excersise}"))
        print(f"{name} is added to the collection of excersises")
        print("-------------------------------")
    return(excersises)
        


        



if __name__ == '__main__':
  
    goal = "I want to tone my arms"
    creatWorkouts(goal)
    



    



