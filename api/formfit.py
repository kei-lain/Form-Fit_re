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

    
    
    for area in areas.split(", "):
        area.strip()
        area = str(area)
        
        

        recommendation =  matchWorkouts(area)
        recommendations.append(recommendation)

    return recommendations
    print('done')




def matchWorkouts(area):
    querystring = {"limit":"10"}
    excersises = {}
    if area.__contains__("  "):
        area = area.replace("  ", "%20")
       
    elif area.__contains__("."):
        area = area.replace(".","")
        
    else:
        pass
    area = area.lower()
    print(area)


    new_url = (f'https://exercisedb.p.rapidapi.com/exercises/target/{area}')
   
    headers = {"X-RapidAPI-Key": RapidAPI_Key, "X-RapidAPI-Host": RapidAPI_Host}
    response = requests.get(new_url, headers=headers, params=querystring)

    compList = response.json()
    
    for excersise in compList:
       
        name = excersise['name']
        excersises[name] = excersise
       
    return(excersises)

def createPlan(workouts, workout_days):
    print(f"You wanna workout {workout_days} a week? making a plan now!")
    prompt = (f"This user wants to workout {workout_days} a week. Split up the following workouts so that it can be for {workout_days} days: {workouts}.")
    message =  [{"role": "user", "content": f"{prompt}"}]
    try:
        response = openai.ChatCompletion.create(model="gpt-4",
                                messages=[
                                        {"role": "user", "content": prompt}])
    except:
        pass
    plans = response["choices"][0]["message"]["content"]
    # return(seperatePlans(plans))
    for section in plans.split('\n'):
        for part in section:
            part.strip()
            



    
# def seperatePlans(plans):
#     plan_dict = {}
#     plan_day = ''
#     workoutName = ''
#     wks = []
#     # for section in plans.split('\n'):
        
    #     section.strip()
    #     print(section)
    #     if "Day" in section:
    #         plan_day = section
    #     elif "Workout" in section:
    #         section.replace("Workout: ","")
    #         workoutName = section
    #         workoutName = ''.join([i for i in workoutName if not i.isdigit()]) 
    #     wks.append(workoutName)
    #     plan_dict[plan_day]=wks
    # return(plan_dict)





    

    



