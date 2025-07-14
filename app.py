import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pickle
from sklearn.preprocessing import OrdinalEncoder

# Set Streamlit page config
st.set_page_config(page_title="AfriMarket Seller Risk Dashboard", layout="wide")

# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv("jumia_jitters_dataset.csv")
    df.dropna(inplace=True)
    df['Delivery Date'] = pd.to_datetime(df['Delivery Date'])
    df['Dispatch Date'] = pd.to_datetime(df['Dispatch Date'])
    df['Delivery Delay'] = (df['Delivery Date'] - df['Dispatch Date']).dt.days
    df['Return Flag'] = df['Return Flag'].replace({'No': 0, 'Yes': 1})
    return df

df = load_data()

# Load Trained Model
model = pickle.load(open("jumia.pkl", "rb"))

# Sidebar
st.sidebar.title("📦 Seller Risk Dashboard")
menu = st.sidebar.radio("Choose Section", ["📊 Overview", "📉 Seller Risk Analysis", "🤖 Predict Return", "📌 Recommendations"])

# Overview Section
if menu == "📊 Overview":
    st.title("📊 AfriMarket Seller Performance Overview")
    st.markdown("This dashboard helps monitor sellers, detect risky behavior, and improve marketplace health.")

    st.subheader("🗃 Dataset Preview")
    st.dataframe(df.head())

    st.subheader("🔍 Missing Data Summary")
    st.write(df.isna().sum())

    st.subheader("📈 Delivery Delay Distribution")
    fig, ax = plt.subplots()
    sns.histplot(df['Delivery Delay'], bins=15, kde=True, ax=ax)
    st.pyplot(fig)

# Seller Risk Section
elif menu == "📉 Seller Risk Analysis":
    st.title("📉 Seller Risk Scorecard")

    return_rate = df.groupby('Seller ID')['Return Flag'].mean()
    complaint_rate = df.groupby('Seller ID')['Complaint Code'].apply(lambda x: (x != 'No Complaint').mean())
    avg_delay = df.groupby('Seller ID')['Delivery Delay'].mean()
    max_delay = avg_delay.max()

    # Risk Score
    seller_metrics = pd.DataFrame({
        'Return Rate': return_rate,
        'Complaint Rate': complaint_rate,
        'Avg Delay': avg_delay,
        'Normalized Delay': avg_delay / max_delay
    })

    seller_metrics['Risk Score'] = (
        0.4 * seller_metrics['Return Rate'] +
        0.3 * seller_metrics['Complaint Rate'] +
        0.3 * seller_metrics['Normalized Delay']
    )

    top_risk = seller_metrics.sort_values(by='Risk Score', ascending=False).head(10).reset_index()

    st.subheader("🚨 Top 10 Risky Sellers")
    st.dataframe(top_risk)

    fig, ax = plt.subplots(figsize=(10, 4))
    sns.barplot(data=top_risk, x='Seller ID', y='Risk Score', ax=ax, palette='Reds_r')
    ax.set_title("Top 10 Risky Sellers")
    st.pyplot(fig)

# Prediction Section
elif menu == "🤖 Predict Return":
    st.title("🤖 Return Risk Prediction")
    st.markdown("Fill in order details to predict whether the item is likely to be returned.")

    with st.form("prediction_form"):
        seller_id = st.selectbox("Seller ID", sorted(df['Seller ID'].unique()))
        category = st.selectbox("Product Category", sorted(df['Product Category'].unique()))
        price = st.number_input("Price", min_value=10.0, max_value=1000.0)
        quantity = st.slider("Quantity", 1, 10, 1)
        warehouse = st.selectbox("Warehouse Zone", sorted(df['Warehouse Zone'].unique()))
        rating = st.slider("Customer Rating", 1.0, 5.0, 3.0, step=0.5)
        sentiment = st.slider("Sentiment Score", -1.0, 1.0, 0.0, step=0.1)
        delivery_method = st.selectbox("Delivery Method", sorted(df['Delivery Method'].unique()))
        region = st.selectbox("Customer Region", sorted(df['Customer Region'].unique()))
        delay = st.slider("Delivery Delay (days)", 0, 10, 3)

        submitted = st.form_submit_button("Predict")

    if submitted:
        encoder = OrdinalEncoder(handle_unknown='use_encoded_value', unknown_value=-1)
        cat_cols = ['Seller ID', 'Product Category', 'Warehouse Zone', 'Delivery Method', 'Customer Region']
        df_temp = df[cat_cols].drop_duplicates()
        encoder.fit(df_temp)

        input_data = pd.DataFrame({
            'Seller ID': [seller_id],
            'Product Category': [category],
            'Price': [price],
            'Quantity': [quantity],
            'Warehouse Zone': [warehouse],
            'Customer Rating': [rating],
            'Sentiment Score': [sentiment],
            'Delivery Method': [delivery_method],
            'Customer Region': [region],
            'Delivery Delay': [delay]
        })

        input_data[cat_cols] = encoder.transform(input_data[cat_cols])
        prediction = model.predict(input_data)[0]
        proba = model.predict_proba(input_data)[0][1]

        st.success(f"🔁 Return Probability: **{proba:.2%}**")
        if prediction == 1:
            st.error("⚠️ Likely to be Returned")
        else:
            st.success("✅ Unlikely to be Returned")

# Recommendations
elif menu == "📌 Recommendations":
    st.title("📌 Business Recommendations")

    st.markdown("""
### 1. 🚫 Seller Enforcement
- Suspend top risky sellers or trigger audits.
- Enforce minimum performance thresholds.

### 2. 📦 Product Regulations
- Target top complaint categories (Electronics, Health, Toys).
- Require certification or reviews for high-risk categories.

### 3. 🔍 Review Fraud Detection
- Flag duplicate reviews and cross-seller patterns.
- Launch a verified review program.

### 4. ⏱ Fulfillment Improvements
- Incentivize fast delivery sellers.
- Penalize delays and missed SLAs.

### 5. 🔁 Return Risk System
- Use model prediction to flag suspicious orders before shipping.

### 6. 🧪 Monitoring & A/B Testing
- Evaluate delivery method, rating trends, and seller impact using analytics.

### 7. 🧑‍🤝‍🧑 Customer Trust
- Add “Trusted Seller” badges.
- Fast refunds, warranty policies for high-risk categories.
""")

# Footer
st.markdown("---")
st.markdown("Developed by **AfriMarket Data Intelligence Team** | Powered by Streamlit & scikit-learn")
