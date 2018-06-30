Project Proposal

Chinese Party Congress

Weihua Li

1. what is the subject of the project?

For the final project, I'd like to look into the Chinese Party Congress. It's the legislative branch of the Chinese government, currently consisting of 204 official members and 172 alternate members. 

All of these people are members of the Chinese Communist Party (hence it's the "Party" Congress). Every five years, they meet and decide who China's next leader will be. Five years ago, they appointed Xi Jinping as China's president. This year, they amended the constitution and removed term limits for the president -- so Xi, who was set to retire in 2023, now can be president for life.

2. what is your main research question?

Chinese politics is a patron-client system, meaning that because there is no such thing as "free election," all political leaders are essentially appointed by party elders. So which leader they served and who they know is more important than anything else.

Since Xi came into power, he has launched an aggressive anti-corruption campaign that put many of China's top leaders in prison. Some critics argue that Xi's agenda goes beyond anti-corruption -- he was using it as a tool to get rid of his political enemies.

Now the 19th Party Congress, elected by CCP this March, is the first Party Congress formed while Xi's power is in full swing. I am interested in, among many other things, who these delegates were before they were appointed to the Party Congress. How many of them have served in the same department? Same province? Which political fraction they each belong to.


3. what is/are your data source(s)? please provide links

"Chinese Political Leader Database" -- compiled by People.cn, which is the propaganda branch of CCP:

http://cpc.people.com.cn/GB/64162/394696/index.html (Links to an external site.)Links to an external site.

List of names for Party Congress official and alternate members -- published by XInhua News Agency, another propaganda branch of CCP:

http://www.xinhuanet.com/politics/19cpcnc/2017-10/24/c_1121848878.htm (Links to an external site.)Links to an external site.

http://www.xinhuanet.com/politics/19cpcnc/2017-10/24/c_1121848883.htm (Links to an external site.)Links to an external site.

4. how will you transform the data into your own data set: scraping, regex, etc?

Good question! I plan on using selenium to scrap the leadership database, which includes leaders ranging from Tthe Prime Minister to deputy mayors. The amazing part is that besides information like age, gender, when they joined the party, People.cn website also documents every political official's entire work history -- which province they worked in on a given year, which position they held, under which department, etc.

Though none of that information is nicely organized in a chart. Instead, for every official, there's a whole block of information, separated only by <br>s, so I'll use regex to sort through them.

Oh also, did I mention the website is in Chinese ...? I found a python library that can convert Chinese characters into Pinyin. For example, my name is 卫华 in Chinese Character, but it's Weihua in Pinyin. I also need to do a lot of translation work, unless I'm able to find an equally good website in English.


4. how can this data set be geocoded?

There are a few ways. For example, I can geocode each delegate by their place of birth, and see which province has most delegates in the central government (it's not like the U.S., where each state elects a set number of congressman/woman and senators. 

But what interests me the most is building an interactive map where, when we select a given year, the map will tell us where each delegate was during that year.

Moreover, I really want to build a map that shows the history of each delegate, i.e. how they move from provinces to provinces and if there's a pattern. Though I'm sure if that's possible.

5. on the map, what level of study would be displayed: Country, State, City, neighborhood?

At lease provincial, maybe city.


6. what information would be displayed when you click on/rollover a country (city, etc)?

Which delegates were working in that province during that year and what are their positions.
