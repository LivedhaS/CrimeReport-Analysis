# CrimeReport-Analysis
This project utilizes Django to create a web-based crime reporting platform, enabling users to 
submit diverse data elements. Leveraging machine learning algorithms such as Random Forest for 
crime prediction and K-Means for resource allocation, the system analyses historical data. 
Preprocessing techniques and feature engineering ensure data quality, while interactive 
visualizations (Matplotlib and Seaborn) aid in understanding trends. The outcome is an efficient, 
scalable system providing law enforcement with actionable insights for evidence-based decision
making. 
 
Utilizing readily available data in form of .csv files, this system promotes error-free, reliable, and 
efficient crime analysis. Our project emphasizes societal well-being by empowering law 
enforcement with predictive insights and optimizes resource allocation for more effective crime 
prevention. 
 
The anticipated outcome is a versatile and scalable system that empowers law enforcement agencies 
with valuable insights derived from historical crime data. This platform not only streamlines the 
crime reporting process but also contributes to more efficient resource allocation and proactive 
crime prevention strategies. The emphasis on data analysis and visualization tools aims to foster 
evidence-based decision-making for a safer community.

# Work Flow
1. User Registration and Authentication: Use Django's built-in authentication system to set up user registration, login, and password reset functionality. Create user roles, such as regular users and administrators, and manage permissions accordingly. Admins might have the ability to review reported crimes and manage user accounts.

2. Data Input and Visualisation: Create a user-friendly form for inputting crime data, including fields for location, type, date, and description.Use Django models to store this data in your database. Implement data analysis and visualisation using EDA and libraries like Matplotlib, Seaborn to display crime trends and statistics to users.

3. Crime Trend Analysis: Develop algorithms for time-series analysis to identify trends and patterns in historical crime data. Create visualisations like line charts, heatmaps, or bar graphs to represent these trends. Users can see how crime rates change over time and identify seasonal or long-term patterns. Design database models that align with the structure of the imported data.

4. Crime Hotspot Identification: Use clustering algorithms (here, K-Means) to identify crime hotspots based on historical data. Overlay hotspot data on a map to provide users with a visual representation of high-crime areas.

5. Crime Prediction: Implement machine learning models (here, regression) to predict future crime rates based on historical data and user-defined criteria (e.g., time of day, location). Display predicted results to users, along with metrics indicating the model's accuracy or confidence in the predictions.

 ![image](https://github.com/user-attachments/assets/9ee6191b-d161-46c1-aec7-b60ea985af23)

 # Algorithms 
 1. Random Forest:
In this project, a Random Forest classifier is instantiated and trained on the training set, consisting 
of various crime-related features. The trained model is used to predict crime categories on the test 
set. Model performance is evaluated using metrics such as accuracy, a confusion matrix, and a 
classification report, providing insights into the model's predictive capabilities.

2. K Means Clustering:
In this project, K-means clustering is utilized for pattern identification. Data 
preprocessing involves handling missing values, label-encoding, and standardizing 
features. The Elbow method guides the selection of an optimal cluster count, and K
means clustering is then applied for grouping similar data points. Principal 
Component Analysis (PCA) aids in 2D visualization of clusters. The project further 
explores crime type distribution within each cluster, categorized by severity levels. 
Overall, K-means clustering facilitates insight into spatial crime patterns and the 
composition of crime types within distinct clusters.

# Front End 
![image](https://github.com/user-attachments/assets/1d0ea5f2-7dfc-48f7-a457-6b352493cb39)

![image](https://github.com/user-attachments/assets/505ed77d-9602-4609-8d27-58cda977497f)

![image](https://github.com/user-attachments/assets/091d5b9d-9b7b-4d3d-9361-103ab2b85bbb)

![image](https://github.com/user-attachments/assets/c8c202bc-c1ac-4717-a8eb-dc01f70ec849)

![image](https://github.com/user-attachments/assets/38009dad-8971-4335-882c-34585d2cb699)

![image](https://github.com/user-attachments/assets/c81a1681-7d4e-4ce1-9715-18e98b813f67)

![image](https://github.com/user-attachments/assets/fb0e7c93-3278-4456-8447-0630ee757409)

 
In conclusion, the Crime Report Analysis System is a pivotal advancement in leveraging 
technology for public safety. Through Django's robust framework, the system offers an intuitive 
platform for detailed and insightful crime prediction analysis. Real-time updates and community 
engagement features foster a proactive approach to public safety, enhancing overall awareness.




