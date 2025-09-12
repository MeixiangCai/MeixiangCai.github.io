# Sentiment Analysis on Product Reviews

## Objective
Extract keywords from product reviews and automatically determine their sentiment polarity (positive or negative) to assist purchase decisions.

## Process
1. Read the file and perform data normalization.  
2. Apply **jieba** for word segmentation to generate tokenized strings.  
3. Construct a **Bag-of-Words model**.  
4. Extract text features and labels, then prepare training data.  
5. Build a classifier using the extracted data.  
6. Train the classifier, evaluate predictions on the test set, and calculate accuracy.  
7. Input a custom review to test whether the model correctly predicts sentiment polarity.  

- **Data Source**: Provided in the project folder  