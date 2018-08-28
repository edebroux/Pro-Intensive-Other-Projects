
# coding: utf-8

# # Project: Board Slides for FoodWheel
# 
# FoodWheel is a startup delivery service that takes away the struggle of deciding where to eat! FoodWheel picks you an amazing local restaurant and lets you order through the app. Senior leadership is getting ready for a big board meeting, and as the resident Data Analyst, you have been enlisted to help decipher data and create a presentation to answer several key questions:
# 
# What cuisines does FoodWheel offer? Which areas should the company search for more restaurants to partner with?
# How has the average order amount changed over time? What does this say about the trajectory of the company?
# How much has each customer on FoodWheel spent over the past six months? What can this tell us about the average FoodWheel customer?
# 
# Over this project, you will analyze several DataFrames and create several visualizations to help answer these questions.

# We're going to use `pandas` and `matplotlib` for this project.  Import both libraries, under their normal names (`pd` and `plt`).

# In[15]:


import matplotlib.pyplot as plt
import pandas as pd


# ## Task 1: What cuisines does FoodWheel offer?
# The board wants to make sure that FoodWheel offers a wide variety of restaurants.  Having many different options makes customers more likely to come back.  Let's create pie chart showing the different types of cuisines available on FoodWheel.

# Start by loading `restaurants.csv` into a DataFrame called `restaurants`.

# In[16]:


restaurants = pd.read_csv("restaurants.csv")


# Inspect `restaurants` using `head`

# In[17]:


restaurants.head(10)


# How many different types of cuisine does FoodWheel offer?
# (hint: use `.nunique`)

# In[18]:


print(restaurants.cuisine.nunique())
# There are 7 different types of cuisine delivered by foodwheel


# Let's count the number of restautants of each `cuisine`.  Use `groupby` and `count`.  Save your results to `cuisine_counts`.

# In[19]:


cuisine_counts = restaurants.groupby('cuisine').id.count().reset_index()
print(cuisine_counts)


# Let's use this information to create a pie chart.  Make sure that your pie chart includes:
# - Labels for each cuisine (i.e, "American", "Chinese", etc.)
# - Percent labels using `autopct`
# - A title
# - Use `plt.axis` to make the pie chart a perfect circle
# - `plt.show()` to display your chart

# In[20]:


plt.pie(cuisine_counts['id'], labels = ['American', 'Chinese', 'Italian', 'Japanese', 'Korean', 'Pizza', 'Vegetarian'], 
        autopct = '%0.1f%%')
ax = plt.subplot
plt.axis('equal')
plt.title('FoodWheel Delivery Cuisine Types')
plt.show()


# ## Task 2: Orders over time
# FoodWheel is a relatively new start up.  They launched in April, and have grown more popular since them.  Management suspects that the average order size has increased over time.
# 
# Start by loading the data from `orders.csv` into the DataFrame `orders`.

# In[21]:


orders = pd.read_csv('orders.csv')


# Examine the first few rows of `orders` using `head`.

# In[22]:


orders.head(10)


# Create a new column in `order` called `month` that contains the month that the order was placed.
# 
# Hint: The function `split` will split a string on a character.  For instance, if `mydate` is the string `9-26-2017`, then `mydate.split('-')` would return the list `['9', '26', '2017']`.  `mydate.split('-')[0]` would return `'9'`.

# In[23]:


orders['month'] = orders.date.str.split('-').str.get(0)
print(orders['month'])


# Group `orders` by `month` and get the average order amount in each `month`.  Save your answer to `avg_order`.

# In[24]:


avg_order = orders.groupby('month').price.mean().reset_index()
print(avg_order)


# It looks like the average order is increasing each month.  Great!  We're eventually going to make a bar chart with this information.  It would be nice if our bar chart had error bars.  Calculate the standard deviation for each month using `std`.  Save this to `std_order`.

# In[25]:


std_order = orders.groupby('month').price.std().reset_index()
print(std_order)


# Create a bar chart to share this data.
# - The height of each bar should come from `avg_order`
# - Use the standard deviations in `std_order` as the `yerr`
# - The error capsize should be 5
# - Make sure that you label each bar with the name of the month (i.e., 4 = April).
# - Also be sure to label the y-axis
# - Give your plot a descriptive title

# In[26]:


month = [4, 5, 6, 7, 8, 9]
avg_order = avg_order.price
std_order = std_order.price
ax = plt.subplot(1, 1, 1)
plt.bar(month, avg_order, yerr = std_order, capsize = 5)
ax.set_xticks(month)
ax.set_xticklabels(['April', 'May', 'June', 'July', 'August', 'September'])
plt.xlabel('Month')
plt.ylabel('Average Order')
plt.title('Average Order Amount By Month')
plt.show()


# ## Task 3: Customer types
# There is a range of amounts that customers spend at FoodWheel.  We'd like to create a histogram of the amount spent by each customer over the past six months.
# 
# Start by grouping `orders` by `customer_id` and calculating the total amount spent by each customer.  Save your results to `customer_amount`.

# In[27]:


customer_amount = orders.groupby('customer_id').price.sum().reset_index()
print(customer_amount)


# Create a histogram of this data.
# - The range should be from 0 to 200
# - The number of bins should be 40
# - Label the x-axis `Total Spent`
# - Label the y-axis `Number of Customers`
# - Add a title

# In[28]:


customer_id = customer_amount.customer_id
price = customer_amount.price
plt.hist(price, bins = 40, range = (0, 200))
plt.xlabel('Total Spent')
plt.ylabel('Number of Customers')
plt.title('Number of Customers by Size of Orders')
plt.show()

