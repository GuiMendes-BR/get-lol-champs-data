from pages.league_of_graphs import LeagueOfGraphs
from .base_bot import BaseBot
import queue


class LeagueOfGraphsBot(BaseBot):

    def __init__(self):
        self.page = LeagueOfGraphs()
    
    def run(self, args, out_queue:queue):
        name = self._clean_up_champ_name(args['name'])

        self.page.navigate_to_champ(name=name)

        # In the future we can implement more attributes for each champ
        data = {
                'champ_name': args['name'],
                'winrate': self.page.champ_winrate
            }

        self.page.close()

        out_queue.put(data)


    def get_all_champs(self):
        self.page.go()
        all_champs = self.page.get_all_champs()

        self.page.close()

        return all_champs

    def _clean_up_champ_name(self, name):

            # Most champs can have their name cleaned up by these rules
            name = str(name).lower()
            name = name.replace(" ", "")
            name = name.replace("'", "")
            name = name.replace(".", "")
            name = name.replace("&", "")

            # These champs need special rules 
            if name == "nunuwillump":
                name = "nunu"
            elif name == "wukong":
                name = "monkeyking"

            return name