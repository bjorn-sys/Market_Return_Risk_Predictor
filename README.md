 # Project Overview
**AfriMarket** (a fictional eCommerce platform similar to Jumia) is facing major operational challenges—ranging from fake reviews and product complaints to seller non-fulfillment and high product return rates. This project is designed to detect risky sellers, flag fraudulent behavior, and recommend policy actions to improve customer experience and platform trust.
---
# 📂 Dataset Summary
Source: jumia_jitters_dataset.csv
Rows: 1000
Columns: 16
Core Fields:

Order ID, Seller ID, Product Category

Delivery & Dispatch Dates

Customer Rating, Review Text, Sentiment Score

Return Flag, Complaint Code, Delivery Method
---
# 🧹 Data Cleaning & Preparation
Handled missing values (dropna)

Parsed date fields to datetime

Fixed inconsistent categories (e.g., "Lag" → "Lagos")

Rounded Sentiment Score to 2 decimals

Flagged duplicate reviews and review text anomalies
---
# 🛠 Feature Engineering
Delivery Delay: Delivery Date - Dispatch Date

Return Rate / Complaint Rate / Avg Delivery Delay per seller

Suspicious Review Detection using repetitive cross-product/seller reviews

Seller Risk Score = 40% Return Rate + 30% Complaint Rate + 30% Normalized Delay
---
# 📊 Key Insights & Analysis
# ✅ Top Sellers by Reliability
Sellers like S039 and S041 had 0% return rate — potentially excellent or suspicious.

Most Reliable Sellers (lowest avg delay): S039, S034, S040
---
# ❌ Least Reliable Sellers
S010, S019, S025 had delivery delays over 5 days and high risk scores.

🔥 Sellers with Highest Risk Scores
Seller	Risk Score	Return Rate	Complaint Rate	Avg Delay
S025	0.34	11.7%	11.7%	5 days
S019	0.32	5.6%	5.6%	5.5 days
S036	0.31	14.3%	7.1%	4.6 days
---
# 🚩 Fraudulent Review Detection
All reviews were highly duplicated and repeated across multiple sellers/categories — indicating possible fake review campaigns.
---
# 🧪 Hypothesis Testing
ANOVA Test on Delivery Method vs Customer Rating:

P-value = 0.53 — No significant difference. Delivery method does not influence customer satisfaction statistically.
---
# 🧠 Machine Learning: Return Prediction
Target: Predict if a product will be returned (Return Flag)
Model Used: Random Forest Classifier
Steps:

Ordinal encoding for categorical data

Handled class imbalance using:

Random OverSampler

Random UnderSampler

Hyperparameter tuning (n_estimators=200, max_depth=30, etc.)

Best Model Performance (Over-Sampled Data):

Accuracy: 91%

Recall: 83% (Important for minimizing undetected returns)

ROC AUC: 0.95

✅ Emphasis on Recall ensures we correctly identify risky/return-prone transactions.
---
# 📈 Business Recommendations
**1. 🚫 Seller Enforcement & Marketplace Hygiene**
Immediate Suspension or Review of top high-risk sellers (e.g., S025, S019, S036).

Quarterly Risk Audits based on dynamic Seller Risk Score (delay, complaints, returns).

Require Performance Improvement Plans (PIPs) for underperforming sellers before relisting.

**2. ⚖️ Product Category Regulations**
High Complaint Categories (e.g., Electronics, Health, Toys) should undergo:

Mandatory product quality inspections

Third-party certification for high-risk items (e.g., health-related products)

Prioritize sellers with verified sourcing and fulfillment

**3. 🔍 Fake Review Detection System**
Deploy a review moderation engine using:

NLP-based duplicate detection

Sentiment analysis + keyword filtering

Cross-product/seller review anomaly flagging

Reward customers who report suspicious reviews

**4. ⏱️ Fulfillment Reliability Policy**
Set maximum delivery delay thresholds by category (e.g., 3 days for electronics).

Penalize sellers for:

Exceeding delay thresholds

Frequent returns/complaints due to delivery

Introduce Fulfillment Performance Score to boost seller visibility

**5. 📦 Return Risk Prevention System**
Integrate the ML Return Prediction Model into the backend to:

Flag likely-return orders in real-time

Trigger alerts for manual quality check or delivery reassignment

Offer optional return protection packages to customers

**6. 🧪 Monitoring & A/B Testing**
Continuously test:

Impact of delivery method on customer satisfaction

Effects of suspending risky sellers on return/complaint trends

Use dashboards to monitor seller trends, sentiment shifts, and complaint hot zones

**7. 🤝 Customer Trust Programs**
Highlight "Top Trusted Sellers" with badges (based on low risk scores & timely delivery)

Offer extended warranties and fast refunds for risky categories

Educate customers on how to identify trusted sellers and genuine reviews

**⚠️ Product Regulation Needed**
Category	Complaint Count
Electronics	6
Health	3
Toys	3

**These categories attract excessive customer complaints and require:**

Supplier audits

Warranty checks

Enhanced QC standards

**🤖 Implement NLP Filters**
Flag repetitive reviews

Detect review duplication across categories/sellers

🛠 Model Deployment
The model is exported as a .pkl file for integration into a fraud detection or return prevention system.
---
# 📎 Technologies Used
Python, Pandas, Numpy

Matplotlib, Seaborn

Scikit-learn, XGBoost, Imbalanced-learn

Statistical Testing (ANOVA)

Data Cleaning & Engineering
---
# DEPLOYMENT
 Network URL: http://172.19.183.243:8501

Machine Learning with Sampling Strategies
