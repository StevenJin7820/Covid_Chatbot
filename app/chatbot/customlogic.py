from chatterbot.logic import LogicAdapter

class MyLogicAdapter(LogicAdapter):
    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        words = ['coronavirus', 'US']
        if all(x in statement.text.split() for x in words):
            return True
        else:
            return False

    def process(self, input_statement, additional_response_selection_parameters):
        from chatterbot.conversation import Statement
        import requests
        
        url = "https://api.covidtracking.com/v2/us/daily/2021-01-02/simple.json"

        response = requests.request("GET", url)
        if response.status_code == 200:
            data = response.json()
            confidence = 1
            totalCases = str(data['data']['cases']['total'])
            totalHospital = str(data['data']['outcomes']['hospitalized']['currently'])
            totalDeath = str(data['data']['outcomes']['death']['total'])
            statement = "Total Cases: "+totalCases+"\n"
            +"Total Hospitalized: "+totalHospital+"\n"
            +"Total Deaths: "+totalDeath
            confidence = 1
        elif response.status_code == 404:
            statement = "Could not find data sorry."
            confidence = 0
        else:
            statement = "Could not find data sorry."
            confidence = 0

        # For this example, we will just return the input as output
        selected_statement = Statement(text=statement)
        selected_statement.confidence = confidence

        return selected_statement