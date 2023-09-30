https://www.youtube.com/watch?v=ElUPypOHLmE&t=200s
# MobilePhonePrice
get estimated price of your specifications

# MobilePhonePrice
get estimated price of your specifications
# About:
This project is a machine learning model, to estimate the price of a phone with your given specifications.
# Data:
The data was picked up from kaggle. The description of features is very straight forward, like Brand,Model, Storage, RAM, Screen Size, Camera (Megapixels), Battery and price.
# Project Story:
1-Data was collected. Price is predictned.
2- Data cleaning: in raw form data had different kind of entries. it took data cleaning skills to bring it in a uniform format.
3- Dimensionality Reduction: feature "Model" was overly spread , Considering it comparatively less important it is droped from data set to save computational power. Also in feature Brand some entries with v less repitation are droped to avoid higher mean square error.
4-Model Fitting: Three different models were tested. and finally RandomForestRegressor is chosen to find predictions.model is chose on higher score.
# Challenges:
The whole process of data cleaning was a challenge.
# Coclusion:
i was hoping to have a good Score with linear regression model. but it didn't went in my way, same for Ridge regression. The reason is might be each brand has a different market segment, different demand supply behaviour, customer preception and quality. So customer behave is diverse for same specifications but different barnd.
In my opinion more data should be collected. and Model should be fitted for each brand seprately. to get more precise results.

