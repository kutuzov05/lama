from settings import *
import requests


def modul(key1, key2):
    ollama_url = "http://212.132.112.15:11434/api/chac"
    ollama_model = "llama3.1:8b-instruct-q5_K_M"

    initial_prompt = "Mit einem Wort beantworten"

    data = {
        "model": ollama_model,
        "messages": [
            {
                "role": "system",
                "content": initial_prompt
            },
        ],
        "stream": False,
    }

    
    msg = {
            "role": "user",
            "content": "Was erhält man, wenn man "+str(key1)+" mit "+str(key2)+" kombiniert?",
        }

    data["messages"].append(msg)

    response = requests.post(ollama_url, json=data).json();
    answer = response["message"]

    data["messages"].append(answer)

    print(answer["content"])
        
        
running = True
while running:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(WHITE)
    modul("Wasser", "Feuer")
    pygame.display.update()
    
