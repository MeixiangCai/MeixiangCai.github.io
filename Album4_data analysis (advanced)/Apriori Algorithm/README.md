# Apriori Algorithm for Article Recommendation

## Objective
Analyze user browsing data with the Apriori algorithm to discover association rules between headline and secondary articles in a WeChat public account. The goal is to identify how article arrangement may influence the reading volume of secondary articles.

## Process
1. Convert browsing records into a transaction dataset.  
2. Apply the **Apriori algorithm** with minimum support = 0.1 and minimum confidence = 0.6.  
3. Extract association rules and calculate support, confidence, and lift.  
4. Identify rules that promote (lift > 1) or restrict (lift < 1) secondary article views.  
5. Visualize results with bar charts showing strong positive and negative associations.  

- **Data Source**: Provided in the project folder  