#!/usr/bin/env python
# coding: utf-8

# ## Analyzing Airbnb Data with geoplotlib

# In this last activity for geoplotlib, we will use airbnb listing data to determine the most expensive and best rated regions of accomodations in the New York area.   
# We will write a custom layer with which we can switch between the price and the review score of each accomodation.   
# 
# In the end, we will be able to see the hostpots for the most expensive and best rated accomodations across New York.   
# In theory, we should see a price increase the closer we get to the center of Manhatten. It will be very interesting to see if the ratings for the given accomodations also increase the closer we get to the center of Manhatten.

# #### Loading the dataset

# In[1]:


# importing the necessary dependencies
import numpy as np
import pandas as pd
import geoplotlib


# **Note:**    
# If your system is a little bit slower, just use `./data/airbnb_new_york_smaller.csv` which has fewer datapoints. The activity stays the same, we just cut down on the number of datapoints.

# In[2]:


# loading the Dataset
dataset = pd.read_csv('./data/airbnb_new_york.csv')
# dataset = pd.read_csv('./data/airbnb_new_york_smaller.csv')


# **Note:**   
# If we import our dataset without defining the `dtypes` specifically - like we did in the chapter about geoplotlib - we will get a warning telling out the it has a mixed datatype.   
# We can get rid of this warning by explicitly defining the type of the values in this column by using the `dtype` parameter.   
# We will ignore this since we are only using a small subset of the data in this dataset.   
# Normally you want to define the `dtypes` of each column of the used dataset to avoid errors later on.

# In[3]:


# print the first 5 rows of the dataset
dataset.head()


# ---

# ### Data handling 

# Before we start plotting our data, we want to *wrangle* our data to fit our needs.   
# As with all the previous geoplitlib exercises and activites, we have to map the `latitude` and `longitude` columns to `lat` and `lon`.
# 
# Considering the fact, that there might be some missing data points in the `review_scores_rating` and `price` columns, we want to fill them in with data of the same datatype.   
# > This is where you would want to apply some data augmentation in real projects.
# 
# The last step of our pre-processing is to create a sub-section view of our dataset that is much easier to handle and will be used for plotting.

# #### Mapping `Latitude` and `Longitude` to `lat` and `lon`

# Again, our dataset has a `latitiude` and a `longitude` column.   
# As we've already discussed in the lesson about geoplotlib, we need them as `lat` and `lon`.

# In[4]:


# mapping Latitude to lat and Longitude to lon
dataset['lat'] = dataset['latitude']
dataset['lon'] = dataset['longitude']


# **Note:**   
# Geoplotlibs methods expect dataset columns `lat` and `lon` for plotting. This means your dataframe has to be tranfsormed to resemble this structure.   

# #### Mapping `price` to `dollar_price` as int type

# When creating a color map that changes color based on the price of an accommodation, we need a value that can easily be compared and checked whether it's smaller or bigger than any other listing.   
# Therefore we will create a new column called `dollar_price` that will hold the value of the `price` column as a float.

# In[5]:


# convert string of type $<numbers> to <nubmers> of type float
def convert_to_float(x):
    try:
        value=str.replace(x[1:], ',', '')
        return float(value)
    except:
        return 0.0


# In[6]:


# create new dollar_price column with the price as a number
# and replace the NaN values by 0 in the ratings column
dataset['price'] = dataset['price'].fillna('$0.0')
dataset['review_scores_rating'] = dataset['review_scores_rating'].fillna(0.0)

dataset['dollar_price'] = dataset['price'].apply(lambda x: convert_to_float(x))


# #### Reducing the amount of columns

# This dataset has 96 columns. When working with such a huge dataset it makes sense to think about what data we really need and create a subsection of our dataset that only holds the data we need.   
# Before we can do that , we'll take a look at all the columns available and an example for that column. This will help us decide what information is suitable.

# In[7]:


# print the col name and the first entry per column
for col in dataset.columns:
    print('{}\t{}'.format(col, dataset[col][0]))


# For now, we want to **only use the fields that help us build the described visualization**.   
# 
# Those fields are:
# - **id**
# - **latitude (as lat)**
# - **longitude (as lon)**
# - **price (in $)**
# - **review_scores_rating**

# In[8]:


# create a subsection of the dataset with the above mentioned columns
columns=['id', 'lat', 'lon', 'dollar_price', 'review_scores_rating']
sub_data=dataset[columns]


# In[9]:


# print the first 5 rows of the dataset
sub_data.head()


# **We are now left with only 5 of the 96 columns.**

# ---

# #### Understanding the spatial features of our dataset

# Even though we know that our data holds airbnb listings for New York city, at the moment we have no feeling about the amount, distribution, and character of our dataset.   
# The simplest way to get a first glance at the data is to plot every listing with a simple dot map.

# In[10]:


# import DataAccessObject and create a data object as an instance of that class
from geoplotlib.utils import DataAccessObject
data = DataAccessObject(sub_data)


# In[43]:


# plotting the whole dataset with dots
geoplotlib.dot(data)
geoplotlib.show()


# This gives us a better understanding about the distribution and character of our data.

# ---

# ### Writing the custom layer to map the price and rating to a color

# The last step is to write the custom layer. Here we want to define a `ValueLayer` that extends the `BaseLayer` of geoplotlib.   
# For the mentioned interactive feature we need an additional import. `pyglet` provides us with the option to act on key presses.
# 
# Given the data, we want to plot each point on the map with a color that is defined by the currently selected attribute, either price or rating.   
# To avoid non-descriptive output, we need to also adjust the scale of our color map. Ratings are between 0 and 100, whereas prices can be much higer. Using a linear (`lin`) scale for the ratings and a logarithmic ('log') scale for the price will give us much better insights into our data.
# The view (bounding box) of our visualization will be set to New York and a text information with the currently selected attribute will be displayed in the upper right corner.

# <img src="./data/colorscale.png" width=500/>   
# > The jet color map displays low values as cooler tones and higher values as hotter. 

# In order to assign each point a different color, we simply paint each point separately. This is definitely not the most efficient solution, but it wills suite for now.
# We will need the following instance variables:   
# - self.data that holds the dataset
# - self.display that holds the currently selected attribute name
# - self.painter holds an instance of the BatchPainter class
# - self.view holds the BoundingBox
# - self.cmap holds a color map with the `jet` color schmema, alpha of 255 and 100 levels
# 
# Inside the `invalidate` method that holds the logic of projection the data to points on the map, we have to switch between the `lin` and `log` scales, depending on the attribute that is currently selected.   
# The color is then determined by "placing" the value between 0/1 and the maximum (`max_val`) value which also has to be taken from the dataset based on what attribute currently is display.

# In[20]:


# custom layer creation
import pyglet
import geoplotlib
from geoplotlib.layers import BaseLayer
from geoplotlib.core import BatchPainter
from geoplotlib.colors import ColorMap
from geoplotlib.utils import BoundingBox

class ValueLayer(BaseLayer):

    def __init__(self, dataset, bbox=BoundingBox.WORLD):
        # initialize instance variables
        self.data = dataset
        self.display = 'dollar_price'
        self.painter = BatchPainter()
        self.view = bbox
        self.cmap = ColorMap('jet', alpha=255, levels=100)
        
    def invalidate(self, proj):
        # paint every point with a color that represents the currently selected attributes value
        self.painter = BatchPainter()
        max_val = max(self.data[self.display])
        scale = 'log' if self.display == 'dollar_price' else 'lin'
        
        for index, id in enumerate(self.data['id']):
            # log scale can't start at 0, must be 1
            min_val = max(self.data[self.display][index], 1)
            
            color = self.cmap.to_color(min_val, max_val, scale)
            self.painter.set_color(color)
            lat, lon = self.data['lon'][index], self.data['lat'][index]
            x, y = proj.lonlat_to_screen(lat, lon)
            self.painter.points(x, y, 5)
        
    def draw(self, proj, mouse_x, mouse_y, ui_manager):
        # display the ui manager info
        ui_manager.info('Use left and right to switch between the displaying of price and ratings. Currently displaying: {}'.format(self.display))
        self.painter.batch_draw()
        
    def on_key_release(self, key, modifiers):
        # check if left or right keys are pressed to switch to other attribute
        if key == pyglet.window.key.LEFT or key == pyglet.window.key.RIGHT:
            self.display = 'dollar_price' if self.display != 'dollar_price' else 'review_scores_rating'
            return True
        return False
        
    # bounding box that gets used when layer is created
    def bbox(self):
        return self.view


# Since our dataset only contains data from New York, we want to set the view to New York in the beginning.   
# Therefore we need an instance of the `BoundingBox` class with the given parameters.
# 
# In addition to a custom `BoundingBox`, we will use the `darkmatter` tile provider we have looked at in lesson 5.

# In[21]:


# bounding box for our view on New York
from geoplotlib.utils import BoundingBox

ny_bbox = BoundingBox(north=40.897994, west=-73.999040, south=40.595581, east=-73.95040)


# In[22]:


# displaying our custom layer using add_layer
geoplotlib.tiles_provider('darkmatter')
geoplotlib.add_layer(ValueLayer(data, bbox=ny_bbox))
geoplotlib.show()


# In[ ]:




