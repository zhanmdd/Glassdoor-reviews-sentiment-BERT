import pandas as pd
import os

directory = '/Users/AZM/Desktop/Projectss/glassdoor-reviews-sentiment-BERT/Raw and Clean Datatsets/Datasets'
df_list = []

#creating a new column 'company_name' with a corresponding company name in each dataset individually
for file in os.listdir(directory):
    #reading csv file in the datasets folder
    df = pd.read_csv(directory + '/' + file)
    
    #creating a column 'company_name' with a corresponding company in the dataset 
    company_name = file.replace('.csv', '')
    df['company_name'] = company_name
    
    #saving the updated dataset
    df.to_csv(r'/Users/AZM/Desktop/Projectss/glassdoor-reviews-sentiment-BERT/Raw and Clean Datatsets/Datasets' + file, index = False)

    #creating a list of csv files we have in our datasets folder
    df_list.append(file)

#Now each of our datasets have a column_name column with a corresponding company name in it

#Combining all 20 datasets into single one dataset
data = pd.concat([pd.read_csv(directory +'/'+ f) for f in df_list], ignore_index = True)

#savigng the dataset into single one dataset
data.to_csv(r'/Users/AZM/Desktop/Projectss/glassdoor-reviews-sentiment-BERT/Raw and Clean Datatsets/data.csv', index = False)

