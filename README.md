# Data-Cleaning-and-Preprocessing
This repository contains all the data and technical knowledge related to data cleaning and preprocessing basics using Pandas library of Python programming language. The raw dataset contains missing, inconsistent, irregular data which is cleaned before using the same for analysis purpose or Machine Learning algorithm development purposes.
<br>Dataset used- Netflix Movies and TV Shows<br>
<br>Tools used- Python language (Pandas)<br>
<br>Outcome- Cleaned and Pre Processed data from Raw Dataset<br>
<br>Data Cleaning Steps<br>
<br>Identify and handle missing values using .isnull() in Python or filters in Excel<br>
<br>Discovering the insights related to the data-<br>
<br>dataset.head(3)- Saw the general format of the data, with the columns of the 1st 3 rows.
dataset.shape- (8807, 12)- Got the idea of rows and columns.
dataset.isnull().sum().sum()- 4307- Got the total null values present in the dataset.

(dataset.isnull().sum().sum())/(dataset.shape[0]*dataset.shape[1])*100- 4.075- Percentage of Total Null values.<br>

<br>(dataset.isnull().sum()/dataset.shape[0])*100  - percentage of missing data col wise<br>
<br>show_id          0.000000<br>
<br>type             0.000000<br>
<br>title            0.000000<br>
<br>director        29.908028<br>
<br>cast             9.367549<br>
<br>country          9.435676<br>
<br>date_added       0.113546<br>
<br>release_year     0.000000<br>
<br>rating           0.045418<br>
<br>duration         0.034064<br>
<br>listed_in        0.000000<br>
<br>description      0.000000<br>
<br>Insight gained- The dataset has considerable amount of null values present in the dataset. Therefore, we need to fill those values instead of dropping them altogether which has the risk of missing key insights.<br>


<br>Techniques used to fill the missing data-<br>
<br>1) If the dataset column is numeric, then filled the missing cell with the mean of that column.<br>
<br>2) If the dataset column is of object type, then filled the missing cell with the mode of that column.<br>
<br>dataset.info()- Got the information on the column types present-

<br>0   show_id       8807 non-null   object<br>
<br>1   type          8807 non-null   object<br>
<br>2   title         8807 non-null   object<br>
<br>3   director      6173 non-null   object<br>
<br>4   cast          7982 non-null   object<br>
<br>5   country       7976 non-null   object<br>
<br>6   date_added    8797 non-null   object<br>
<br>7   release_year  8807 non-null   int64 <br>
<br>8   rating        8803 non-null   object<br>
<br>9   duration      8804 non-null   object<br>
<br>10  listed_in     8807 non-null   object<br>
<br>11  description   8807 non-null   object<br>

<br>Columns having null values- director, cast, country, date_added, rating, duration<br>

<br>Filling the null values by the mode of that particular column, for the object type columns.<br>
<br>for i in dataset.select_dtypes(include="object").columns:
	dataset[i].fillna(dataset[i].mode()[0], inplace=True)<br>
 
 <br>Filling the null values by the mean of that particular column, for the numeric type columns<br>
 <br>dataset = dataset.fillna(dataset.mean(numeric_only=True))<br>

 <br>Verified again using  dataset.isnull().sum().sum() to find there is no NaN values now in the entire dataset.<br>
 
  
 <br>2) Remove duplicate rows using .drop_duplicates() or Excel’s “Remove Duplicates”.<br>
 
 <br>dataset.drop_duplicates(inplace=True)- It drops all the duplicate rows, if any and replaces the operated data with the original data with inplace=True function<br>
 
 <br>3) Standardize text values like gender, country names, etc.<br>
 <br>for i in dataset.columns:
	<br>if i=="show_id" or i=="rating":<br>
		<br>dataset[i]=dataset[i].str.upper().str.strip()<br>
	<br>elif i=="type" or i=="title" or i=="description":<br>
		<br>dataset[i]=dataset[i].str.capitalize().str.strip()<br>
	<br>elif i=="director" or i=="duration" or i=="cast" or i=="listed_in" or i=="country":<br>
		<br>dataset[i]=dataset[i].str.title().str.strip()<br>

dataset["country"].replace({"United States": "USA", "US": "USA", "U.S.A:":"USA"})<br>

<br>4) Convert date formats to a consistent type (e.g., dd-mm-yyyy).<br>

<br>dataset['date_added'] = pd.to_datetime(dataset['date_added'])<br>
<br>dataset['date_added'] = dataset['date_added'].dt.strftime('%d-%m-%Y')<br>
<br>dataset['date_added'] = pd.to_datetime(dataset['date_added'])<br>

<br>5) Rename column headers to be clean and uniform (e.g., lowercase, no spaces).<br>
<br>dataset.columns = dataset.columns.str.strip().str.title() - Strip removed trailing and leading zeros and title converts the column names to title case.<br>

<br>6) Check and fix data types (e.g., age should be int, date as datetime)<br>
<br>- All columns have the correct data types mentioned as was required.<br>

<br>Regards,<br>
<br>Shrish Kumar Srivastava<br>

