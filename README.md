# Project_4 - Web Scraping 

# Context 
We want to make people read more. That is why our webscraping project is about data on books.
First, we used the dataset of GoodReads, the world's largest site for readers and book recommendations:https://www.kaggle.com/datasets/bahramjannesarr/goodreads-book-datasets-10m 
The prices and the format of the books were missing, that is why we webscrapped Amazon to get more valuable information.
We decided to just work on the books with more than 500 votes to avoid the books with 1 vote and 5 stars, so non-representative. 

# Deliverables 
1) Insights with:
- Books publish from 1950 - 2022 (histogram)
- Book’s rating distribution (data webscraped vs data without webscraping) (boxplots)
- Book’s Rating vs Nb of Votes (scatterplot)
- Book’s format (hardcover / paperback) price distribution (boxplots) 

2) A streamlit with :
- the top / flop books (based on more than 500 votes and on the best rating)
- the books per price (for all people with different budget can be able to buy a book)

3) Statistical analysis 
- 1st analysis : an independant test for the price before 2008 and after 2008. Result: We didn't reject the null hypothesis.
- 2nd analysis : an independant test regarding the price of the books with good and bad rating. Result: We didn't reject the null hypothesis.

# GitHub folders - Description 
TO WRITE 


# Pre-processing 

# Cleaning explanation
Cleaning of Kaggle_2_goodreads by steps:
1) Dropna from ISBN
2) Str.split to remove strings from column 'RatingDistTotal', 'RatingDist1', 'RatingDist2', 'RatingDist3', 'RatingDist4', 'RatingDist5'
3) Drop columns 'PublishDay', 'PublishMonth', 'Language', 'RatingDistTotal'
4) Drop rows from 'Authors'=="Anonymous" or "Unknown"

Then we create a new dataset with this first clean called "Clean_data.csv".
The second cleaning took place, and were made the follow steps in this last file:
1) Dropna from 'PagesNumber'
2) Drop columns 'Unnamed: 0.1', 'Unnamed: 0', 'Id', 'pagesNumber'
 
# Web Scraping explanation 
TO WRITE 
We webscrapped 4651 books from Amazon and 


# Navigate colab files
TO WRITE 
