
# Movies Recommendation System

This is a movie recommendation system that uses three different filtering methods to provide personalized recommendations to users. The three filtering methods used are popularity-based filtering, content-based filtering, and collaborative filtering.


## Popularity Based Recommendation system

Created a web page for popularity based recommendation system. the system will recommend top 5 similar movies based on genres.
          
 `Demo`


eeeeeeeeeeeeeeeeeeeee
## Context

Over  the  past  two  decades,  there  has  been  a  monumental  shift  in  how  people  access  and consume video content. With the universal access to broadband internet, numerous platforms like YouTube, Netflix, and HBO Go emerged and steadily grew to prominence.

Although not a household name in itself, OTT is the exact technology that made the streaming revolution possible.

OTT stands for “Over The Top” which refers to any video streaming service delivering content to  the  users  over  the  internet,  however,there  are  subscription  charges  associated  with  the usage of such platforms such as PrimeVideo, Netflix, HotStart, Zee5, SonyLiv,etc.

But choosing your next movie to watch can still be a daunting task, even if you have access to all the platforms
## Data Description

The  data  consists  of  105339  ratings  applied  over  10329  movies.  The  average  rating  and minimum and maximum rating are 0.5 and 5 respectively. There are 668 users who have given their ratings for 149532 movies.

There are two data files which are provided:

Movies.csv

- movieId:IDassignedtoamovie
- title:Titleofamovie
- genres:pipe-separatedlistofmoviegenres.

Ratings.csv
- userId:IDassignedtoauser
- movieId:IDassignedtoamovie
- rating:ratingbyausertoamovie
- Timestamp:timeatwhichtheratingwasprovided
## Filtering Methods
- `Popularity Based Recommendation System`

Popularity-based filtering is a type of recommendation algorithm that suggests items that are popular among all users. In the context of a movie recommendation system, this would involve recommending movies that have been highly rated and viewed by a large number of users. This approach is simple to implement and can be effective for new users who haven't yet provided much data on their preferences.

Created a popularity-based recommender system at a genre level. The user will input a genre for a movie for which it will recommend top 5 movies which are most popular within that genre ordered by ratings in descending order where each movie has at least 100 reviews.


eeeeeeeeeeeeeeeeee


- `Content Based Recommendation System`

Content-based filtering is a type of recommendation algorithm that suggests items similar to the ones that a user has liked in the past. In the context of a movie recommendation system, this would involve recommending movies that have similar genres, actors, directors, and other attributes to movies that the user has already enjoyed. This approach requires detailed information about the movies in order to generate recommendations.

Created a content-based recommender system that recommends top 5 movies based on similar movie.

eeeeeeeeeeeeeeeeeeeeeeeeee

- `Collaborative Based recommendation system`

Collaborative filtering is a type of recommendation algorithm that suggests items based on the preferences of similar users. In the context of a movie recommendation system, this would involve analyzing the ratings and preferences of multiple users to identify those who have similar tastes, and then recommending movies that have been highly rated by those similar users. This approach is based on the assumption that users who have similar tastes in movies will also enjoy similar movies.

Created a collaborative based recommender system which recommends top 5 movies based on similar users for a target user.

eeeeeeeeeeeeeeeeeeeeeeeeeeee
## File Structure
- gitignore file
- app.py file
- genres.pkl
- movie_recommendation.ipynb (notebook)
- movies_dict_pop.pkl
- procfile
- requirements.txt file
- setup.sh
## Running the Project

To run the project, open a terminal and navigate to the project directory. 

Run the following command:


```bash
  streamlit run app.py
```


## Conclusion

the movie recommendation system project provides a simple implementation of a recommendation system using collaborative filtering. It recommends movies to users based on their past ratings and preferences. The project uses the MovieLens 100k dataset and the scikit-learn library for the implementation. With further improvements, this project can be extended to build more advanced recommendation systems and can be used in various applications such as e-commerce, social media, and more.
## 🔗 Links
[![portfolio](https://img.shields.io/badge/my_portfolio-000?style=for-the-badge&logo=ko-fi&logoColor=white)](https://github.com/malikjanattar)
[![linkedin](https://img.shields.io/badge/linkedin-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/malikjan-attar-69a7a317b)
