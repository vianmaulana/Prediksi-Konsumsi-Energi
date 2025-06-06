import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

url = "https://raw.githubusercontent.com/vianmaulana/Prediksi-Konsumsi-Energi/main/data_application_energy.csv"
df = pd.read_csv(url)

print(df.info())
print(df.describe())

df.drop(columns=['date', 'rv1', 'rv2'], inplace=True)
print(df.isnull().sum())

X = df.drop(columns=['Appliances'])
y = df['Appliances']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = DecisionTreeRegressor(random_state=42)
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("Mean Absolute Error (MAE):", mae)
print("Root Mean Squared Error (RMSE):", rmse)
print("R-squared (R2 Score):", r2)

importances = pd.Series(model.feature_importances_, index=X.columns)
plt.figure(figsize=(12, 6))
importances.sort_values(ascending=False).plot(kind='bar', color='skyblue')
plt.title('Feature Importance dalam Prediksi Konsumsi Energi')
plt.ylabel('Pentingnya Fitur')
plt.tight_layout()
plt.show()
