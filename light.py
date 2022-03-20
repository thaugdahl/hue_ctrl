from config import api_url
import requests
import json

class Light():
    name = ""
    id = 0
    brightness = 0
    is_on = False

    ct_range = []
    color_tone = 0

    state_url = ""

    def get_name(self):
        return self.name

    def get_id(self):
        return self.id

    def construct_from_id(id):
        global api_url

        print(id)
        request_url = api_url + "lights/" + str(id)

        response = requests.get(request_url).json()

        new_instance = Light()
        new_instance.id = int(id)
        new_instance.name = response['name']
        new_instance.brightness = int(response['state']['bri'])
        new_instance.is_on = response['state']['on'] == True
        new_instance.state_url = request_url + "/state"

        if "ct" in response['state'].keys():
            new_instance.ct_range.append(response['capabilities']['control']['ct']['min'])
            new_instance.ct_range.append(response['capabilities']['control']['ct']['max'])
            new_instance.color_tone = response['state']['ct']

        return new_instance

    def off(self):
        global api_url

        response = requests.put(self.state_url, "{\"on\": false}").json()


        if "success" in response[0].keys():
            is_on = False

    def on(self):
        global api_url

        response = requests.put(self.state_url, "{\"on\": true}").json()

        if "success" in response[0].keys():
            is_on = True

    def set_brightness(self, brightness):
        global api_url


        pct = brightness = min(max(brightness, 0), 100)
        brightness = int(254 * (brightness / 100))

        json_body = "{\"bri\":" + str(brightness) + "}"
        response = requests.put(self.state_url, json_body).json()

        if len(response) == 0:
            return

        if "success" in response[0].keys():
            self.brightness = brightness
            print(f"Brightness was set to {pct}%")

    def set_color_tone(self, ct):
        global api_url

        pct = ct = min(max(ct, 0), 100)
        print(pct)
        ct = int(self.ct_range[0] + (pct/100)*(self.ct_range[1]-self.ct_range[0]))

        print(self.ct_range)

        print(ct)

        json_body = "{\"ct\": " + str(ct) + "}"
        response = requests.put(self.state_url, json_body).json()

        if len(response) == 0:
            return

        if "success" in response[0].keys():
            self.ct = ct
            print(f"Color tone was set to {ct}")

    def set_xy_color(self, x, y):
        global api_url

        # Normalize color vector
        norm = (x**2 + y**2)**(1/2)

        x /= norm
        y /= norm

        json_body = "{\"xy\": [" + str(x) + ", " + str(y) + "]}"
        response = requests.put(self.state_url, json_body).json()

        if len(response) == 0:
            return

        print(response)

        if "success" in response[0].keys():
            print(f"Color was set to {x}, {y}")

    def set_hue(self, hue):
        global api_url

        pct = hue = min(max(hue, 0), 100)
        print(pct)
        hue = int((hue / 100) * 65534)


        json_body = "{\"hue\": " + str(hue) + "}"
        response = requests.put(self.state_url, json_body).json()

        if len(response) == 0:
            return

        if "success" in response[0].keys():
            print(f"Hue was set to {hue}")





    def __str__(self):
        return f"Light(id: {self.id}, name: {self.name})"

