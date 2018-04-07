# PubgApiWrapper
## Description:
Custom wrapper for the PUBG API using python. Because the data is returned in a huge block of JSON as defined in [PUBG's API documentation](https://documentation.playbattlegrounds.com/en/introduction.html), I converted the JSON data into different objects that can retreieve the data needed.

Using the API Wrapper, I will create a crawler which will go through various player profiles (unfortunately I am limited to 10 api requests per minute), and save the player data into a database. Using the data I will track some trends in PUBG for games over time and make some pretty graphics/images/graphs from the data.

## Current Takebacks:
- Use a Web API and API keys to access endpoints and parse JSON data that is returned.
- Reading and understand [API documentation](https://documentation.playbattlegrounds.com/en/introduction.html)

## Future Takebacks:
- Create of a 'crawler' add future candidates to a queue
- Use of database Models to more easily update database entries
- Creation of infographics/graphs/etc. from large amounts of data over time
