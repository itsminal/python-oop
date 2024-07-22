import requests


class IRCTC:

    def __init__(self):

        user_ip = input("""How'd you like to proceed?
        Enter
        1.To check live train status
        2.To check PNR
        3.To check train schedule""")

        if user_ip == "1":
            print("live train status")
        elif user_ip == "2":
            print("PNR")
        else:
            self.train_schedule()

    def train_schedule(self):
        train_no = input("Enter train no.")
        self.fetch_data(train_no)

    def fetch_data(self, train_no):
        data = requests.get(
            "https://indianrailapi.com/api/v2/TrainSchedule/apikey/013759ffad46ff28a29d6817156ef212/TrainNumber/{}".format(train_no))
        data = data.json()
        print(data['Route'])

        for i in data['Route']:
            print(i['StationName'],"|",i["ArrivalTime"],"|",i["DepartureTime"],"|",i["Distance"],"kms")


obj = IRCTC()
