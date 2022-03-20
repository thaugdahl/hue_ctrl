from light import Light
import requests
import json

class Group():
    name = ""
    lights = []
    state = {}
    id = 0

    action_url = ""

    def get_name(self):
        return self.name

    def get_state(self):
        return self.state

    def get_light_by_id(self, id):
        pass

    def set_brightness(self, brightness):
        global api_url

        pct = brightness = min(max(brightness, 0), 100)
        brightness = int(254 * (brightness / 100))

        json_body = "{\"bri\":" + str(brightness) + "}"

        response = requests.put(self.action_url, json_body).json()

        if len(response) == 0:
            return

        if "success" in response[0].keys():
            self.brightness = brightness
            print(f"Brightness was set to {pct}%")



    def __str__(self):
        return f"Group({self.id}: {self.get_name()})"
