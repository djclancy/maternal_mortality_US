import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report
from xgboost import XGBRegressor
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error

# Step 1: Load the data
## load the data here
data = pd.read_excel("R:/Fei.Li/Python/Erdos/merged_data_scaled_totals.xlsx")

data.sample(5)


# Step 2: Prepare the data
# Define the target variable and features
target = 'Maternal_Mortality_Rate'
features = data.columns.difference(['State', 'Year', target])

# Prepare the data for training
X = data[features]
y = data[target]

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Initialize the XGBoost model
xgb_model = XGBRegressor(objective='reg:squarederror', n_estimators=100, learning_rate=0.1, max_depth=3)

# Train the model
xgb_model.fit(X_train, y_train)

# Predict on the test set
y_pred = xgb_model.predict(X_test)

# Calculate the mean squared error
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

import matplotlib.pyplot as plt
import xgboost as xgb

# Create a figure with a larger size
plt.figure(figsize=(16, 10))  # Increased size for better readability

# Plot feature importance
ax = xgb.plot_importance(xgb_model, importance_type='weight', max_num_features=15)  # Show top 15 features for clarity

# Rotate x-axis labels for better readability
ax.set_yticklabels(ax.get_yticklabels(), fontsize=12)
ax.set_xlabel('F Score', fontsize=14)
ax.set_ylabel('Features', fontsize=14)
ax.set_title('Feature Importance', fontsize=16)

plt.tight_layout()  # Adjust layout to make room for rotated labels
plt.show()

##### Random Forest Approach ########

# Initialize the Random Forest model
rf_model = RandomForestRegressor(n_estimators=100, random_state=42)

# Train the model
rf_model.fit(X_train, y_train)

# Predict on the test set
y_pred = rf_model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse}")

# Plot feature importance
importances = rf_model.feature_importances_
indices = importances.argsort()[::-1]
feature_names = [features[i] for i in indices]

plt.figure(figsize=(20, 24))  # Increased size for better readability
sns.barplot(x=importances[indices], y=feature_names, orient='h')
plt.title("Feature Importance from Random Forest")
plt.xlabel("Importance", fontsize=16)
plt.ylabel("Feature", fontsize=16)
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)  # Adjust font size for y-ticks for readability
plt.grid(axis='x', linestyle='--', alpha=0.7)
plt.tight_layout()
plt.show()