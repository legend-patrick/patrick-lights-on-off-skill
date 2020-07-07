from mycroft import MycroftSkill, intent_file_handler


class PatrickLightsOnOff(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('off.on.lights.patrick.intent')
    def handle_off_on_lights_patrick(self, message):
        self.speak_dialog('off.on.lights.patrick')


def create_skill():
    return PatrickLightsOnOff()

