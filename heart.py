import pandas as pd
import seaborn as sns
from sklearn.model_selection import train_test_split
sns.set()

columns = ['age', 'sex', 'chest pain type', 'resting blood pressure',
	 'serum cholestoral in mg/dl', 'fasting blood sugar > 120 mg/dl',
	 'resting electrocardiographic results', 'maximum heart rate achieved',
	 'exercize induced angina', 'oldpeak = ST depression induced by exercize relative to rest',
	 'the slope of the peak exercize ST segment',
	 'number of major vessels colored by flourosopy', 'thal', 'absence or presence']

heart = pd.read_csv("heart.csv")

features = [x for x in heart.columns if x != "absence(1) or presence(2)"]

target = "absence(1) or presence(2)"

absence = heart["absence(1) or presence(2)"] == 1
presence = heart["absence(1) or presence(2)"] == 2

#print(heart.describe())
#print(heart.info())

x_train, x_test, y_train, y_test = train_test_split(heart, features, test_size=0.2, random_state=42)
print(x_train.shape())
