# README

This is a simple mutli-thread bot implementation, it was created only for study purposes so feel free to use however you like. 

I tried to write it in a way that should be easy to add new functionalities by creating a new bot in the "bots" folder and passing its class as an argument to a MultiThreadBot object. Example below:

```python
from multi_thread_bot import MultiThreadBot
from bots.league_of_graphs_bot import LeagueOfGraphsBot # You would have to create a new bot object

mb = MultiThreadBot(
        max_threads=10, 
        bot=LeagueOfGraphsBot, # You need to pass the new bot object here
        items_to_process=[{"name": "Aatrox"}, {"name": "Zilean"}])

result = mb.run()

```


## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](https://choosealicense.com/licenses/mit/)
