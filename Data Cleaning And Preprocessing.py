import pandas as pd
dataset= pd.read_csv("Netflix Movies and TV Shows.csv")


print(dataset.head(3)) #Saw the general format of the data, with the columns of the 1st 3 rows.
print(dataset.shape)   #Got the idea of rows and columns.- (8807, 12)

print(dataset.isnull().sum().sum()) #Got the total null values present in the dataset.
print((dataset.isnull().sum().sum()) / (dataset.shape[0] * dataset.shape[1]) * 100) #Percentage of Total Null values.
print((dataset.isnull().sum() / dataset.shape[0]) * 100) #percentage of missing data column wise

#Filling missing values with mode of the column for object type columns
for i in dataset.select_dtypes(include="object").columns:
    dataset[i].fillna(dataset[i].mode()[0], inplace=True)

#Filling missing values with mean of the column for numeric type columns
dataset = dataset.fillna(dataset.mean(numeric_only=True))

#Verifying whether all null values are filled now
print(dataset.isnull().sum().sum())


#2)Remove duplicate rows using.drop_duplicates()
dataset.drop_duplicates(inplace=True)

#3)Standardize text values like gender, country names, etc.< br >
for i in dataset.columns:
    if i == "show_id" or i == "rating":
        dataset[i] = dataset[i].str.upper().str.strip()
    elif i == "type" or i == "title" or i == "description":
        dataset[i] = dataset[i].str.capitalize().str.strip()
    elif i == "director" or i == "duration" or i == "cast" or i == "listed_in" or i == "country":
        dataset[i] = dataset[i].str.title().str.strip()

dataset["country"].replace({"United States": "USA", "US": "USA", "U.S.A:": "USA"})

#4)Convert date formats to a consistent type(e.g., dd - mm - yyyy)
dataset['date_added'] = pd.to_datetime(dataset['date_added'])
dataset['date_added'] = dataset['date_added'].dt.strftime('%d-%m-%Y')
dataset['date_added'] = pd.to_datetime(dataset['date_added'])

#5)Rename column headers to be clean and uniform(e.g.,lowercase, no spaces).
dataset.columns = dataset.columns.str.strip().str.title()

#Verifying if the dataset has been cleaned as required now
print(dataset.head(100))



