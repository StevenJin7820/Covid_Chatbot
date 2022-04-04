from chatterbot.logic import LogicAdapter

class MyLogicAdapter(LogicAdapter):
    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        words = ['how', 'many', 'cases', 'state']
        if all(x in statement.text.split() for x in words):
            return True
        else:
            return False

    def process(self, input_statement, additional_response_selection_parameters):
        from chatterbot.conversations import Statement
        import requests
        
        url = "https://fastah-ip.p.rapidapi.com/whereis/v1/json/auto"

        headers = {
            "X-RapidAPI-Host": "fastah-ip.p.rapidapi.com",
            "X-RapidAPI-Key": "SIGN-UP-FOR-KEY"
        }

        response = requests.request("GET", url, headers=headers)
        if response.status_code == 200:
            location = response.locationData.cityName
            temp = location.split(',')
            state = temp[1]
            state = state[1:]
            url = "/v2/states/"+state+".json"
            response2 = requests.request("GET", url)
            if response2.status_code == 200:
                data = response.json
                confidence = 1
                print(data)
            else:
                confidence = 0
                statement = "Sorry I could not find this data."
        else:
            statement = "Sorry I could not find this data."

        # For this example, we will just return the input as output
        selected_statement = input_statement
        selected_statement.confidence = confidence

        return selected_statement