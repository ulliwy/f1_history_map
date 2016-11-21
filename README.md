# FORMULA 1 Grand Prix History Results
## Summary:
This graph describes the whole 66 years of Formula 1 Championship history since 1950. Watch how championship was spread over the world over the years, see each race results on the map.
Each year is represented by several Grand Prix that took place on selected year. Also, specific Grand Prix results can be found on this graph.
Main data was parsed from http://www.f1-data.com using Python script. Coordinates, teams colors were added manually by me.

### Folder content:
- /parser - Python code to parse f1-data website.
- /img - contains logo image
- /progress - images of design improving
- f1.csv - main data set
- world_countries.json - data for map drawing

## Design:
1. The initial design was pretty simple: color countries by Grand Prix winners on the map. Show results for each year. See _"progress/1.jpg"_ for the first scratch. Firstly the map with colored countries was added with teams colors legend.
2. Only countries coloring wasn't very representative. I've added the exact circuits where Grand Prix took place. See _"progress/2.png"_. Here the first feedback was collected (see first feedback below).
3. List of Grand Prix results was added for each race: position number, pilot name and finish time. I also changed the design of Grand Prix circles on the map and buttons design. I have changed text font and added map zoom. See "progress/3.png".
4. GP results list still looked messy, so I have changed <div> structure to a table. See "progress/4.png". Here the second feedback was collected.
5. During this improvement the page layout was redesigned: the map is shown on 100% of the page, map legend and pilot list are placed on the left and right sides. See "progress/5.jpg" and "progress/6.png".

### Final design description: 
The main map is placed in the middle. Countries are colored by team colors. The colors legend is placed on the left with teams names. The map can be zoomed and moved via mouse.
On the right, there is a list of Grand Prix results for the specific race. List is showed by clicking on circuit circle or country.
There are years buttons under the map, clicking each button shows results of selected year.
Moving mouse on the countries shows country name. Moving mouse on Gran Prix circle shows circuit name.

## Feedback:
##### Konstantin, JavaScript Developer:
1. What do you notice in the visualization? What relationships do you notice?
   - Countries are colored by teams colors. Each year there are only 2-3 winners in Grand Prix. Earlier there were more winners.
2. What questions do you have about the data?
   - Good to know names of Grand Prix and each race results.
3. Suggest any improvements?
   - Add headers. 
   - CSS style must be significantly improved.
   - Add zoom, especially to see Europe part, there are a lot of races.
   - Add each Grand Prix result.

##### Paul, Compiler Developer, big fan of Formula 1:
1. What is this visualization about? What did you notice?
    - It shows championship results for each year. Nice visualization, shows the dominance of specific teams, Mercedes team won most of the GPs last years. I see Ferrari triumph in 2000-2004 when Schumacher joined the team.
2. What is the main takeaway of this visualization?
   - It is possible to see the whole story of Formula 1 GPs. The main takeaway to see races winners for each year.
3. Any improvements or unclear moments?
   - When loading visualization the page is blank. It would be nice to have a message about it. 
   - Colors on the map are dull.
   - It would be good to see the order of GPs.

##### Dmitriy, Software Developer:
1. What is this visualization about? What did you notice?
   - This is Formula 1 results per year. Each year there are different races in different countries. Winner team is shown via color. Dots on the map - races in the specific country. There are race results on the right.
2. Is there something you don’t understand in the graphic?
   - Sometimes there are several races in a country. Probably several races?
3. Any improvements, suggestions?
   - Improve design, make it more beautiful. Table on the right is clumsy.

##### Kate, Designer:
1. What is this visualization about? What did you notice?
   - Formula 1 results.
2. What relationships do you notice?
   - The graph shows races results in specific countries.
3. Design comments?
   - Make races circles different color, because they look like Red Bull team.

## Resources
- http://www.f1-data.com
- https://www.udacity.com/course/data-visualization-and-d3js--ud507
- https://github.com/d3/d3/wiki/3.0
- http://bl.ocks.org/mbostock/3680999
- http://vanseodesign.com/css/
- http://www.w3schools.com/



