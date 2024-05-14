import requests

api_key = "<enter your api key>"


url = "https://api.openai.com/v1/chat/completions"
headers = {
    "Content-Type": "application/json",
    "Authorization": 'Bearer {}'.format(api_key)
}


def main():
    messages = [{"role": "system", "content": "you are an ai assistant to receive orders for 'Mom's Bakery'. Its a bakery shop in Lucknow. Following are the available cakes: Vanilla, Chocolate, Pineapple. Available toppers are 'Happy Birthday', 'Happy Anniversary','Bride to be'.We have two choices: Egg and Eggless cakes. We can make the cake in round, square, heart and doll shape. Cake is available in half kg, one kg and two kgs."},
                {"role": "assistant", "content": "How may I help you today?"}]
    while True:
        user_input: str = input('You: ')
        messages.append({"role": "user", "content": user_input})
        response = requests.post(url, headers=headers, json={
            "model": "gpt-3.5-turbo",
            "messages": messages,
            "temperature": 0.7
        })
        if response.status_code != 200:
            print("Error:", response.text)
        else:
            # print(response.json())
            choices = response.json()["choices"][0]
            text = choices["message"]["content"]
            print("Bot: {}".format(text))
            messages.append({"role": "assistant", "content": text})
            


if __name__ == '__main__':
    main()


