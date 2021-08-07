from bots.league_of_graphs_bot import LeagueOfGraphsBot
from multi_thread_bot import MultiThreadBot

MAX_THREADS = 5

if __name__ == "__main__":

    print("Collecting items to process...")
    items_to_process = []
    for champ in LeagueOfGraphsBot().get_all_champs():
        items_to_process.append({'name':champ})

    mb = MultiThreadBot(
        max_threads=MAX_THREADS, 
        bot=LeagueOfGraphsBot, 
        items_to_process=items_to_process)

    result = mb.run()

    print("Processed items: " + str(result))