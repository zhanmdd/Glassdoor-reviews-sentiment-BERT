# Glassdoor Reviews Sentiment Analysis: Overview

* Scraped slightly over 10,000 reveiws on 20 IT companies of 1,000-10,000 company sizes from Glassdoor using python and selenium.
* Integrated 20 datasets on each company into a single dataset.
* Cleaned, organized data and engineered 3 classes using Pandas library.
* Conducted multiclass sentiment classification on Glassdoor reviews using pre-trained BERT base cased model to predict sentiment classes of the reviews.

## Code and Resources Used

**Python Version:** 3.7

**Packages:** pandas, numpy, sklearn, matplotlib, seaborn, selenium, transformers, torch

**Glassdoor Reviews Scraper Github:** https://github.com/MatthewChatham/glassdoor-review-scraper

**"Getting Things Done With Pytorch" Github:** https://github.com/curiousily/Getting-Things-Done-with-Pytorch

## Selecting Category and Companies to Scrape
In order to save time, I have decided to limit number of reviews to 10,000 (500 reviews per company).

In order to maximize efficiency of when training a model, I had two ways:
* Provide **a lot of data (reviews)** to train on.
* Select a specific category of companies which would contain specific field related terms.


Criteria:
* Category: Information Technology (IT)
* Number of Companies: 20
* Reviews Per Company: 500

## Scraper
The scraper is designed to scrape reviews and corresponding data per individually per company.

I odified the scraper (referenced above) from its original version due to changes in architechture of Glassdoor.com.

Removed scrapers of some features and added two extra scrapers.

Ended up with 20 datasets with roughly 500 rows each and the following features.

    'date',
    'employee_title',
    'location',
    'employee_status',
    'review_title',
    'main_text',
    'pros',
    'cons',
    'rating_overall'

## Organizing and Cleaning Data
* Integrated 20 datasets into 1 single dataset with one extra feature 'company name' identifying a corresponding company of the review.
* Continued the rest cleaning process with explanations to [Glassdoor Reviews cleaning.ipynb](https://colab.research.google.com/drive/1x4m1X-cqk4xjp4GxnxGov_zlnhWhlr9s).

Here is the list of changes, I have done:
1. Converted **'date'** column into datetime type for EDA
2. Parsed **'location'** column into **'city'** and **'state'** columns for EDA
3. Combined **'review_title',	'main_text',	'pros',	'cons'** into a single **'reviews'** column for a model
4. Removed '★★★★★' in **'rating_overall'** and convert it to float for EDA and a model
5. Included 'sentiment' column
6. Improved the order of the columns
7. Exported the "cleaned" dataset

## EDA
Conducted EDA in a separate [Glassdoor Reviews EDA.ipynb](https://colab.research.google.com/drive/1mStdG-0Vb1srldmJhR7HmUnx41yWyESY#scrollTo=1eYZ5TL_kePb).
I provide 3 generalized viisualizations. For detailed EDA you can refer to the [notebook](https://colab.research.google.com/drive/1mStdG-0Vb1srldmJhR7HmUnx41yWyESY#scrollTo=1eYZ5TL_kePb).


![image](https://user-images.githubusercontent.com/53638836/90074729-c74e6e80-dd36-11ea-9ec4-0f87fb86f745.png)

## Preprocessing, Building Model, Conducting Classification
The rest of my project is in
[Glassdoor Reviews Preprocessing and Sentiment Analysis .ipynb](https://colab.research.google.com/drive/1QYjiJJg46pYcGohEz2wbnlfiAyAugY1e#scrollTo=Slmcx-FbbcDL).

### Preprocessing 
Steps:
1. Tokenize
2. Format specifically for BERT model

BERT Model Requierements:
1. **Add special tokens** to specify separations and specify the task of classification (example of the special tokens: 'SEP', 'CLS', 'PAD', 'UNK')
2. **Truncate and pad sentences** to a one common length
3. **Create an attention mask** to specify a pad token (0-not referring to any word) and an actual token (1-referring to a word)

### Building a Model and Experimenting
* Uploaded BERT Base Cased (*Casing is important in reviews since it conveys a stronger sentiment*)
* Defined classifier function
* Split the data into train, test, validation sets
* Trained, validated, tested the model
* Experimented with tuning: *sequence lenghts, batch sizes, epochs*

## Results
The model performed well at classifying reviews with positive and negative sentiments. However, it had it was not trained well enough to classify correctly review with a neutral sentiment.
|             | precision | recall | f1-score | support |
|-------------|-----------|--------|----------|-------- |
| negative    |    0.81   |  0.79  |   0.80   |   223   |
| neutral     |    0.43   |  0.49  |   0.46   |   140   |
| positive    |    0.88   |  0.85  |   0.87   |   397   |
|             |           |        |          |         | 
| accuracy    |           |        |   0.77   |   760   | 
| macro avg   |    0.71   |  0.71  |   0.71   |   760   |
| weighted avg|    0.78   |  0.77  |   0.77   |   760   |

![image](https://user-images.githubusercontent.com/53638836/90077283-bb65ab00-dd3c-11ea-8288-66d36853a3e0.png)

Interestingly, the accuracy at correctly classifying the review was directly proporional to the number of reviews with a corresnponding sentiment.

Overall, the model didn't have enough data to train on to classify reviews with neutral sentiment.
|                                   | negative | neutral | positive |
|-----------------------------------|----------|---------|----------|
| Fraction of Correctly Classified  |0.303602  |0.118353 |0.578045  |
| Fraction of Reviews in the Dataset|0.278052  |0.183426 |0.538522  |
