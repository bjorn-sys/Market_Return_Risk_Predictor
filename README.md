🛒 AfriMarket Seller Risk & Return Prediction Project
📌 Project Overview
AfriMarket (a fictional Jumia-style e-commerce platform) is experiencing surging traffic but a drop in customer satisfaction due to issues like fake reviews, late deliveries, high return rates, and unreliable sellers. This project performs a comprehensive risk analysis and return prediction, helping AfriMarket improve operational reliability and customer trust.

🧠 Objectives
Clean and preprocess seller and order data.

Identify high-risk sellers based on delivery, complaints, and return patterns.

Detect fraudulent review behaviors.

Predict return likelihood using a classification model.

Generate actionable insights and visualizations to guide policy.

🗂️ Dataset Description
📁 jumia_jitters_dataset.csv
The dataset contains 1,000 orders with the following key columns:

Order ID, Seller ID, Product Category

Order/Dispatch/Delivery Date

Customer Rating, Review Text, Complaint Code

Return Flag (Yes/No), Delivery Method, Region

Price, Quantity, Sentiment Score

⚙️ Key Tasks Performed
✅ 1. Data Cleaning & Engineering
Removed missing and duplicate entries.

Standardized inconsistent category entries (e.g., "Fashon" → "Fashion").

Converted date fields to datetime.

Engineered:

Delivery Delay = Delivery Date - Dispatch Date

Suspicious Reviews based on duplicates and reused patterns.

📊 2. Exploratory Data Analysis (EDA)
Seller Risk Scoring: Combined return rate, complaint rate, and delivery delay to calculate a composite risk score.

Seller Ratings: Seller S050 has the highest average customer rating (4.16).

Return & Complaint Rates:

Seller S039 has the highest return rate (15%).

Seller S040 leads in complaint rate (12.5%).

Regional Delivery Delays: Volta and South West regions have the highest average delivery delays.

Product Complaints: Electronics and Health categories had the most complaints.

📉 Visuals Used:

Bar plots (Return/Complaint rates, Seller ratings)

Heatmaps (Complaints by product and region)

Delivery reliability comparisons

Risk score ranking charts

🕵️ 3. Fraud Detection
Flagged potentially fraudulent reviews:

Reused identical reviews across products/sellers.

Sellers with perfect 5-star ratings and high return rates were flagged (none found in this case).

🤖 4. Return Prediction Modeling
🧪 Model Used:
Random Forest Classifier

Tested with:

Original data

Over-sampled data (RandomOverSampler)

Under-sampled data (RandomUnderSampler)

🔍 Model Evaluation:
Tuned hyperparameters (n_estimators=200, max_depth=30, etc.)

ROC AUC: 0.95

Recall: 0.83 (High — captures most returns)

Precision: 0.26 (Trade-off for higher recall)

F1 Score: 0.40

Cross-Validation Accuracy: ~98% average across 5 folds

🚨 Risk Insights & Business Recommendations
🧑‍💼 Sellers to Investigate or Suspend
Based on highest risk scores:

S010, S019, S025, S006, S007

🛑 Products to Regulate or Blacklist
Electronics, Health, Toys (highest complaints)

⚙️ Strategies to Reduce Delivery Delays:
Warehouse Rebalancing — Reduce load from Lagos hub.

Seller SLAs — Penalize breach of max delivery times.

Regional Optimization — Add capacity to high-traffic zones.

Real-Time Order Routing — Use the model to avoid risky sellers.

💾 Deployment
The final model was saved using pickle:

python
Copy
Edit
import pickle
pickle.dump(model, open('jumia.pkl', 'wb'))
Can be integrated into a Streamlit or Flask API for real-time return prediction and seller flagging.

📈 Tools & Technologies
Python, Pandas, NumPy

Matplotlib, Seaborn

Scikit-learn, RandomForest, Imbalanced-learn

Statistical Testing (ANOVA)

Jupyter Notebook

📬 Contact
Author: Emmanuel Bjorn
📧 [emmanuelekuonye948@gmail.com.com]
💼 [LinkedIn Profile](https://www.linkedin.com/in/ekuonye-chinonso-emmanuel-bb2041208/)

