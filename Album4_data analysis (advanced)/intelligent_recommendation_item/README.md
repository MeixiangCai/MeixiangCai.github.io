# Intelligent Movie Recommendation System (Item-Based Collaborative Filtering)

## Objective
Build an item-based collaborative filtering recommendation system to suggest movies that the target user is most likely to be interested in.

## Process
1. Merge the movie list with the ratings list.  
2. Construct a **user–movie pivot table**.  
3. Calculate the **Pearson correlation coefficient** between every pair of movies.  
4. Identify movies similar to those liked by the target user.  

- **Data Source**: Provided in the project folder  