import os , requests, json, openai
from dotenv import load_dotenv


load_dotenv()

openai.api_key = os.getenv("OPENAI_API")
RapidAPI_Key = os.getenv("RAPIDAPI_KEY")
RapidAPI_Host = os.getenv("RAPIDAPI_HOST")
url = os.getenv("URL_FOR_API")


def creatWorkouts(goal):
    prompt = (f'List some target workout areas I can focus on according to this fitness goal of mine {goal}')
    message =  [{"role": "user", "content": f"{prompt}"}]
    try:
        response =openai.ChatCompletion.create(model="gpt-4",
                                messages=[
                                        {"role": "user", "content": prompt}])
    except:
        pass
    areas = response["choices"][0]["message"]["content"]
    recommendations = matchWorkouts(areas)



def matchWorkouts(areas):
    #url =  "https://exercisedb.p.rapidapi.com/target/"
    # orig_url = url
    querystring = {"limit":"10"}

   
    for area in areas:
        excersises = {}
        new_url = (f"https://exercisedb.p.rapidapi.com/exercises/target/{area}")
        headers = {"X-RapidAPI-Key": RapidAPI_Key, "X-RapidAPI-Host": RapidAPI_Host}
        response = requests.get(new_url, headers=headers, params=querystring)

        recommendations = response.json()
        for excersise in recommendations:
            # excersises[(part['name'])] = {excersise}
            # # print(excersises[(part['name'])])
            name = excersise['name']
            excersises[name] = excersise
            

        


        



if __name__ == '__main__':
    target_areas = ('abs','biceps')
    matchWorkouts(target_areas)

    



