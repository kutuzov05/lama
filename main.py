from settings import *
import requests


def modul(key1, key2):
    ollama_url = "http://212.132.112.15:11434/api/chat"
    ollama_model = "llama3.1:8b-instruct-q5_K_M"

    initial_prompt = "Antworte mit exakt einem Wort ohne Satzzeichen"

    data = {
        "model": ollama_model,
        "messages": [
            {
                "role": "system",
                "content": initial_prompt
            },
        ],
                "stream": False,
                "options": {
                    "seed": 1,
                    "top_k": 0,
                    "top_p": 0,
                    "temperature": 0,
                }
    }

    
    msg = {
            "role": "user",
            "content": "Was erhält man, wenn man "+str(key1)+" mit "+str(key2)+" kombiniert?"
        }

    data["messages"].append(msg)

    response = requests.post(ollama_url, json=data).json();
    answer = response["message"]

    data["messages"].append(answer)

    print(answer["content"])


def show_boxes():
    font = pygame.font.Font(None, int(height*0.025))
    words.sort()
    for nums in range(len(words)):
        pygame.draw.rect(screen, BLACK, (width*0.8, height*0.05+height*0.1*nums, width*0.15, height*0.05), int(height*0.005))
        text = font.render(str(words[nums]), True, BLACK)
        text_render = text.get_rect()
        text_render.center = (width*0.875, height*0.075+height*0.1*nums)
        screen.blit(text, text_render)
    pygame.draw.rect(screen, BLUE, (0, 0, width*0.375, height))
    pygame.draw.rect(screen, RED, (width*0.375, 0, width*0.375, height))
    pygame.draw.rect(screen, BLACK, (width*0.75, 0, width*0.01, height))
    if slot_l is not None:
        pygame.draw.rect(screen, BLACK, (width*0.375/2-width*0.15/2, height*0.5-height*0.05/2, width*0.15, height*0.05), int(height*0.005))
        text = font.render(str(slot_l), True, BLACK)
        text_render = text.get_rect()
        text_render.center = (width*0.375/2, height*0.5)
        screen.blit(text, text_render)
    if slot_r is not None:
        pygame.draw.rect(screen, BLACK, (width*0.375/2-width*0.15/2+width*0.375, height*0.5-height*0.05/2, width*0.15, height*0.05), int(height*0.005))
        text = font.render(str(slot_r), True, BLACK)
        text_render = text.get_rect()
        text_render.center = (width*0.375/2+width*0.375, height*0.5)
        screen.blit(text, text_render)

        
running = True
while running:
    clock.tick(FPS)
    mouse_x, mouse_y = pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill(WHITE)
    show_boxes()
    # modul("Wasser", "Feuer")
    pygame.display.update()
    
