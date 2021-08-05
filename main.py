from pages.league_of_graphs import LeagueOfGraphs

DRIVER_PATH = "driver\chromedriver.exe"

def run():

    print(LeagueOfGraphs().get_champ_data("ezreal"))

if __name__ == "__main__":
    run()