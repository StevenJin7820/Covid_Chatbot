from chatterbot.logic import LogicAdapter

class MyLogicAdapter(LogicAdapter):
    def __init__(self, chatbot, **kwargs):
        super().__init__(chatbot, **kwargs)

    def can_process(self, statement):
        words = ['coronavirus', 'state']
        if all(x in statement.text.split() for x in words):
            return True
        else:
            return False

    def process(self, input_statement, additional_response_selection_parameters):
        from chatterbot.conversation import Statement
        import requests
        words = input_statement.text.split()
        url = "https://corona.lmao.ninja/v2/states"

        response = requests.request("GET", url)
        if response.status_code == 200:
            data = response.json()
            statement = "-1"
            for state in data:
                val = state['state'].split()
                if (set(val).issubset(set(words))):
                    cases = str(state['active'])
                    deaths = str(state['deaths'])
                    newCases = str(state['todayCases'])
                    recovered = str(state['recovered'])
                    statement = "In "+state['state']+" there are, \n"+"Current Cases: "+cases+"\n"+"Deaths: "+deaths+'\n'+"New Cases: "+newCases+'\n'+"Recovered: "+recovered
                    break
            if statement == "-1":
                statement = "Could not find state data sorry"
            confidence = 1
        elif response.status_code == 404:
            statement = "Could not find data sorry."
            confidence = 0
        else:
            statement = "Could not find data sorry."
            confidence = 0

        selected_statement = Statement(text=statement)
        selected_statement.confidence = confidence

        return selected_statement