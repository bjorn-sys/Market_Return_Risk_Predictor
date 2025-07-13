# Market_Return_Risk_Predictor

🛒 AfriMarket Seller Risk & Fraud Detection Project
📌 Project Overview
AfriMarket (a fictional Jumia-style platform) is experiencing record-breaking traffic, but customer satisfaction is falling due to rising complaints, fake reviews, late deliveries, and unreliable sellers.

This data intelligence project is designed to:

Clean and preprocess transactional data

Engineer features for risk profiling

Detect seller fraud using NLP and statistical techniques

Build and evaluate classification models for return prediction

Recommend business actions such as seller suspension and product regulation

📁 Dataset Summary
Rows: 1000

Columns: 16

Source: Simulated transactional dataset including order dates, reviews, complaints, delivery info, etc.

✅ Tasks and Solutions
📌 Task 1: Data Cleaning & Feature Engineering
Removed missing values and duplicates

Converted date columns to datetime

Created Delivery Delay column

Engineered key seller-level metrics:

Average Rating

Return Rate

Complaint Rate

Duplicate Review Flag

NLP-based detection of fraudulent reviews via repetitive text patterns

📈 Visual Insights:
Top Sellers by Rating: Seller S050 leads with 4.15 avg rating

Return Rate Leaders: Seller S039 has the highest at 15.3%

Complaint Trends: Health & Electronics are most flagged

Fraud Reviews: Identified reviews reused across products/sellers

⚠️ Risk Score Calculation
Weighted risk score based on:

Return Rate (40%)

Complaint Rate (30%)

Normalized Avg Delay (30%)

📊 Top Risky Sellers:

plaintext
Copy
Edit
Seller ID    Risk Score
S025         0.337
S019         0.322
S036         0.311
📌 Task 2: Seller Fulfillment Reliability
Computed average delivery delays

Identified top 5 most and least reliable sellers

plaintext
Copy
Edit
Most Reliable Sellers: S039, S004, S034, S040, S018
Least Reliable Sellers: S010, S006, S007, S019, S003
Region Delay Analysis: Volta region has the longest average delays

📌 Task 3: Return Prediction Modeling
💡 Preprocessing
Encoded categorical columns with OrdinalEncoder

Resampled imbalanced data with:

RandomOverSampler (Up to 1370 samples)

RandomUnderSampler (Down to 32 samples)

🧠 Models Used
RandomForestClassifier (base and tuned)

Hyperparameter tuning:

n_estimators=200, max_depth=30, min_samples_leaf=9, min_samples_split=9

✅ Model Performance (Best: Oversampled + Threshold 0.3)
Metric	Score
Accuracy	0.92
ROC AUC	0.95
Precision	0.30
Recall	1.00
F1 Score	0.46

Why Recall? Catching all true returns is more critical than minimizing false alarms.

📌 Task 4: Final Business Recommendations
🔎 Sellers to Suspend or Audit
Based on top 5 Risk Scores:

plaintext
Copy
Edit
Seller ID  Risk Score  Avg Delay
S010       0.300       5.88 days
S019       0.299       5.55 days
S025       0.290       5.00 days
🚫 Products to Regulate or Blacklist
Based on volume of complaints:

plaintext
Copy
Edit
Electronics
Health
Toys
📦 Model Deployment
Final model saved as jumia.pkl for integration into applications or Streamlit dashboards.

python
Copy
Edit
import pickle
pickle.dump(model, open('jumia.pkl', 'wb'))
📊 Statistical Test: Delivery Method vs Customer Rating
Used ANOVA to test impact of delivery method on customer rating

Result: No statistically significant effect (p = 0.536)

💡 Key Insights
High return rates often correlate with delayed deliveries and increased complaints.

Duplicate and cross-seller reviews are strong indicators of fraudulent behavior.

Certain regions (e.g., Volta) experience chronic delivery delays.

Recall is the preferred evaluation metric due to the business need to capture all high-risk returns.

🔗 Technologies Used
Python (Pandas, Numpy, Scikit-learn, XGBoost, Seaborn, Matplotlib)

Imbalanced-learn (RandomOverSampler, RandomUnderSampler)

NLP techniques for fraud review detection

Statistical testing (ANOVA)

Model persistence (Pickle)

🧠 Author
Emmanuel Bjorn
Data Intelligence Officer | eCommerce Analyst | Fraud Detection Specialist

