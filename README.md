# Walmart-Store-Sales-Prediction
Sales Prediction Model
Project Overview
The Sales Prediction Model project aims to predict weekly sales for various stores using machine learning. This project includes a comprehensive EDA (Exploratory Data Analysis), model training and testing, and deployment of a Streamlit app that provides sales predictions based on user inputs. The analysis and modeling were conducted in Python using key libraries like Pandas, Seaborn, and Scikit-Learn.

EDA
Univariate Analysis
Univariate analysis was performed on individual features to understand their distribution and detect any outliers or anomalies. Boxplots, histograms, and KDE plots were used to visualize the characteristics of each numerical feature such as Unemployment, Temperature, Fuel_Price, and Weekly_Sales. The Fuel_Price column revealed some significant patterns that helped in understanding how fuel costs might affect consumer spending and weekly sales. Outliers were identified and managed to enhance model stability.

Bivariate Analysis
In the bivariate analysis, correlations between pairs of features were examined to understand their relationships. A correlation heatmap was created to visualize these relationships, revealing strong and weak correlations with Weekly_Sales. Relationships between Fuel_Price and sales were explored through scatter plots, showing that variations in fuel prices had an impact on weekly sales patterns. Features like Year, Month, and Date were also analyzed to understand how time-based factors correlated with sales.

Time Series Analysis
In the time-based analysis, attention was paid to the Year, Month, Date, and Season columns to capture both seasonal and yearly trends. The data was segmented by year to examine annual sales patterns, showing that 2011 had the highest sales figures, which aligned with the year having the most data entries. Monthly patterns highlighted consistent peaks in certain months, suggesting seasonality in sales.

The Season variable was further analyzed to capture its effect on sales, revealing that specific seasons correlated with higher sales volumes. For instance, certain holiday seasons resulted in noticeable increases in weekly sales. By breaking down trends based on these seasonal patterns, a clearer understanding of the impact of Season on sales was established, providing valuable insights for the model.

Model Selection and Training
To predict Weekly_Sales, three models were tested:

Linear Regression: This model provided a strong baseline and was ultimately selected due to its high accuracy and simplicity. After tuning, it achieved an accuracy of 96.84%.
Support Vector Regressor (SVR): Using various kernel options and parameter tuning, the SVR model achieved an accuracy of 8.68%, making it less effective for this dataset.
K-Nearest Neighbors (KNN) Regressor: Although it offered non-linear capabilities, after tuning with grid search, the KNN model reached an accuracy of 70.78%, performing better than SVR but still lower than Linear Regression.
The models were evaluated using Root Mean Squared Error (RMSE) and R-squared (R²) scores. Despite the performance of SVR and KNN models, Linear Regression achieved the highest accuracy, making it the final model selection for deployment.

Streamlit Application
A Streamlit application was developed to provide an interactive interface where users can input specific values for features such as Store, Holidays, Fuel_Price, Temperature, CPI, Unemployment, Week, Month_Name, and Season. The app uses the pre-trained Linear Regression model to output a predicted Weekly_Sales value based on these inputs, making it a practical tool for users to forecast sales.

Conclusion
This project combines thorough EDA with machine learning modeling and an interactive application. With insights from univariate, bivariate, and time-based analyses, including seasonal trends, the Linear Regression model accurately predicts weekly sales, and the Streamlit app enables easy, real-time predictions. Future improvements could involve adding more granular seasonal and store-specific features and experimenting with advanced models to further optimize prediction accuracy.





