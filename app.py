import streamlit as st
import pandas as pd
from PIL import Image
import os

# Set page configuration
st.set_page_config(
    page_title="SaaS Revenue Intelligence & Predictive Customer Analytics",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for premium styling
st.markdown("""
<style>
    .main-title {
        font-size: 3rem;
        font-weight: 800;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 0.5rem;
    }
    .subtitle {
        font-size: 1.25rem;
        color: #4a5568;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f7fafc;
        border-radius: 12px;
        padding: 1.5rem;
        border-left: 5px solid #667eea;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        margin-bottom: 1rem;
    }
    .metric-value {
        font-size: 1.8rem;
        font-weight: 700;
        color: #1a202c;
    }
    .metric-label {
        font-size: 0.9rem;
        color: #718096;
        text-transform: uppercase;
        letter-spacing: 1px;
    }
</style>
""", unsafe_allow_html=True)

# App Sidebar
st.sidebar.image("https://img.icons8.com/color/96/data-configuration.png", width=80)
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to:", [
    "Dashboard Overview", 
    "Revenue Forecasting", 
    "Customer Churn Prediction", 
    "RFM Customer Segmentation", 
    "Cohort Retention Analysis",
])

# Loading RFM data
@st.cache_data
def load_rfm_data():
    csv_path = "rfm_segmentation.csv"
    if os.path.exists(csv_path):
        return pd.read_csv(csv_path)
    return None

rfm_df = load_rfm_data()

# Page 1: Dashboard Overview
if page == "Dashboard Overview":
    st.markdown("<h1 class='main-title'>SaaS Revenue Intelligence & Predictive Customer Analytics</h1>", unsafe_allow_html=True)
    st.markdown("<p class='subtitle'>An interactive showcase dashboard demonstrating analytical capabilities in time series forecasting, customer churn prediction, and behavioral segmentation.</p>", unsafe_allow_html=True)
    
    st.subheader("📌 Key Project Performance Indicators (KPIs)")
    
    # KPI Grid using Columns
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("""
        <div class='metric-card'>
            <div class='metric-label'>Annual Recurring Revenue (ARR)</div>
            <div class='metric-value'>$13.93M</div>
            <div style='color: #48bb78; font-size: 0.85rem; font-weight: 600;'>+13.26% Growth (6mo)</div>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div class='metric-card'>
            <div class='metric-label'>Overall Churn Rate</div>
            <div class='metric-value'>13.12%</div>
            <div style='color: #a0aec0; font-size: 0.85rem;'>5,000 Total Customers</div>
        </div>
        """, unsafe_allow_html=True)
        
    with col3:
        st.markdown("""
        <div class='metric-card'>
            <div class='metric-label'>Annual Revenue Churn Risk</div>
            <div class='metric-value'>$2.00M</div>
            <div style='color: #e53e3e; font-size: 0.85rem; font-weight: 600;'>652 accounts >50% probability</div>
        </div>
        """, unsafe_allow_html=True)
        
    with col4:
        st.markdown("""
        <div class='metric-card'>
            <div class='metric-label'>12mo Forecast Accuracy</div>
            <div class='metric-value'>99.27%</div>
            <div style='color: #48bb78; font-size: 0.85rem; font-weight: 600;'>0.73% MAPE Model Error</div>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("---")
    
    col_left, col_right = st.columns([3, 2])
    
    with col_left:
        st.subheader("🖼️ Executive Summary Dashboard")
        exec_img_path = os.path.join("financial_viz", "16_FINAL_EXECUTIVE_DASHBOARD.png")
        if os.path.exists(exec_img_path):
            st.image(exec_img_path, use_column_width=True, caption="Consolidated Executive View of SaaS Operations")
        else:
            st.warning("Visualizations not found. Make sure you extracted 'financial_viz.zip' into the 'financial_viz' folder.")
            
    with col_right:
        st.subheader("💡 Core Business Takeaways")
        st.markdown("""
        - **Proactive Retention Opportunity:** By identifying **652 at-risk customers**, customer success teams can target outreach to prevent **$2.0M in ARR loss**, representing a significant revenue-saving initiative.
        - **Highly Stable Operations:** A CLV-to-CAC ratio of **14.33x** indicates extremely strong unit economics, allowing room to scale marketing and acquisition channels aggressively.
        - **High-Fidelity Revenue Projections:** The ARIMA/Prophet ensemble models project next 12-month revenue of **$15.72M** with a historical validation error under **1%**, enabling precise financial modeling and operational planning.
        - **Strategic Customer Re-Engagement:** The RFM segment analysis identified 15% of the database as 'Slipping/At-Risk' VIP segments, which have high monetary values but haven't engaged recently.
        """)

# Page 2: Revenue Forecasting
elif page == "Revenue Forecasting":
    st.title("📈 Time Series Forecasting & Revenue Projections")
    st.markdown("We modeled subscription revenue over a 5-year historical period using ARIMA/SARIMA and Facebook Prophet models to forecast next-year revenue.")
    
    col1, col2 = st.columns([3, 2])
    
    with col1:
        img_path = os.path.join("financial_viz", "04_arima_forecast.png")
        if os.path.exists(img_path):
            st.image(img_path, use_column_width=True, caption="12-Month ARIMA Forecast with 95% Confidence Intervals")
            
    with col2:
        st.subheader("Forecasting Methodology & Results")
        st.markdown("""
        * **Seasonal Decomposition:** Extracted trend, yearly seasonality, and residuals. Strong seasonal spikes are observed in Q4, aligning with standard enterprise SaaS budget cycles.
        * **Stationarity Testing:** Ran Augmented Dickey-Fuller (ADF) test to confirm stationarity after first-differencing the monthly MRR series.
        * **Model Selection:**
            - **ARIMA (Autoregressive Integrated Moving Average):** Captured strong autoregressive features.
            - **Facebook Prophet:** Selected to account for holidays, seasonal fluctuations, and external business indicators.
        * **Accuracy Metrics:**
            - **Mean Absolute Percentage Error (MAPE):** **0.73%**
            - **Forecasted Next 12 Months:** **$15,718,813.24**
        """)
        
    st.subheader("🔍 ARIMA Parameters & Modeling Insights")
    st.code("""
# Fit ARIMA model
model = ARIMA(train_data, order=(p, d, q))
fitted_model = model.fit()

# Forecast next 12 periods
forecast = fitted_model.forecast(steps=12)
    """, language="python")

# Page 3: Customer Churn Prediction
elif page == "Customer Churn Prediction":
    st.title("🎯 Machine Learning for Churn Prediction")
    st.markdown("We designed a predictive classifier to identify customers likely to cancel their subscriptions within the next 30 days.")
    
    col1, col2 = st.columns([3, 2])
    
    with col1:
        tab1, tab2, tab3 = st.tabs(["Churn Distribution", "Feature Importance", "Risk Stratification"])
        
        with tab1:
            img1 = os.path.join("financial_viz", "07_churn_analysis.png")
            if os.path.exists(img1):
                st.image(img1, use_column_width=True)
        with tab2:
            img2 = os.path.join("financial_viz", "09_churn_feature_importance.png")
            if os.path.exists(img2):
                st.image(img2, use_column_width=True)
        with tab3:
            img3 = os.path.join("financial_viz", "10_risk_stratification.png")
            if os.path.exists(img3):
                st.image(img3, use_column_width=True)
                
    with col2:
        st.subheader("Model Evaluation & Key Factors")
        st.markdown("""
        * **Business Problem:** Churn costs subscription businesses billions annually. The objective was to flag churn early to trigger customer success campaigns.
        * **Engineered Features:** Usage frequency, Net Promoter Score (NPS), support ticket volume, plan type, and account age.
        * **Model Performance:** Random Forest and Gradient Boosting outperformed baseline Logistic Regression by capturing non-linear feature interactions.
        * **Key Predictors:**
            1. **Platform Usage Score:** Decreased usage is the strongest precursor to cancellation.
            2. **NPS Score:** Lower satisfaction scores strongly correlate with immediate churn.
            3. **Support Tickets:** A high volume of unresolved support requests increases churn risk.
        * **Impact:** Identified **652 high-risk customers** represent **$2.0M in potential annual recurring revenue loss**.
        """)
        
    st.subheader("🔍 Class-Balanced Random Forest Code")
    st.code("""
# Train model using balanced class weights to handle minor churn class (13.12%)
rf_model = RandomForestClassifier(n_estimators=100, class_weight='balanced', random_state=42)
rf_model.fit(X_train, y_train)

# Predict probabilities to segment risk groups
churn_probabilities = rf_model.predict_proba(X_test)[:, 1]
    """, language="python")

# Page 4: RFM Customer Segmentation
elif page == "RFM Customer Segmentation":
    st.title("👥 K-Means Clustering & RFM Segmentation")
    st.markdown("Customers were segmented into groups using Recency (days since last purchase), Frequency (total purchase count), and Monetary (total spend) values.")
    
    col1, col2 = st.columns([3, 2])
    
    with col1:
        img_rfm = os.path.join("financial_viz", "13_rfm_analysis.png")
        if os.path.exists(img_rfm):
            st.image(img_rfm, use_column_width=True, caption="RFM Distribution across Customer Segments")
            
    with col2:
        st.subheader("Segmentation & Unit Economics")
        st.markdown("""
        * **Clustering Approach:** Used K-Means Clustering on normalized RFM metrics. The optimal number of clusters was determined using the Elbow Method and Silhouette Coefficient.
        * **Segment Personas Identified:**
            - **Champions:** Highly active, frequent buyers, making up the bulk of monetary value.
            - **Loyal Customers:** Frequent buyers with steady usage.
            - **Need Attention:** High monetary customers whose login activity has dropped (Recency is growing).
            - **Lost:** Inactive customers with low engagement.
        * **Unit Economics Highlights:**
            - **Average Customer Lifetime Value (CLV):** **$7,166.83**
            - **CLV-to-CAC Ratio:** **14.33x** (assuming a $500 Customer Acquisition Cost)
            - **Average CAC Payback Period:** **5.0 months**
        """)
        
    if rfm_df is not None:
        st.markdown("---")
        st.subheader("🔍 Interactive RFM Data Table")
        
        # Segment filter
        all_segments = rfm_df["customer_segment"].unique()
        selected_segments = st.multiselect("Filter by Customer Segment:", all_segments, default=["Champions", "At Risk"])
        
        # Filter dataframe
        filtered_df = rfm_df[rfm_df["customer_segment"].isin(selected_segments)]
        
        st.write(f"Showing {len(filtered_df)} of {len(rfm_df)} customers:")
        st.dataframe(filtered_df[["customer_id", "customer_segment", "segment", "plan", "recency", "frequency", "monetary"]].head(100), height=300)

# Page 5: Cohort Retention Analysis
elif page == "Cohort Retention Analysis":
    st.title("📅 Cohort & Revenue Retention Curves")
    st.markdown("Cohort retention maps customer cohorts over their subscription lifecycle to identify product stickiness and revenue retention stability.")
    
    col1, col2 = st.columns([3, 2])
    
    with col1:
        tab1, tab2 = st.tabs(["Customer Cohort Retention", "Revenue Cohort Retention"])
        
        with tab1:
            img_cohort = os.path.join("financial_viz", "11_cohort_retention.png")
            if os.path.exists(img_cohort):
                st.image(img_cohort, use_column_width=True, caption="Monthly Cohort User Retention Heatmap")
        with tab2:
            img_rev_cohort = os.path.join("financial_viz", "12_revenue_cohorts.png")
            if os.path.exists(img_rev_cohort):
                st.image(img_rev_cohort, use_column_width=True, caption="Monthly Cohort Revenue Retention Heatmap")
                
    with col2:
        st.subheader("Cohort Analysis Key Insights")
        st.markdown("""
        * **Customer Lifetime:** Average customer lifetime duration is **26.9 months**.
        * **User Retention Heatmap:** Displays percentage of active customers month-by-month. It highlights customer churn trends, showing that the first 3 months have the steepest churn before flattening.
        * **Revenue Retention Heatmap:** Tracks monthly recurring revenue retention. It identifies expansion revenue trends (upsells, plans changes) offsetting churned accounts.
        * **Operational Recommendation:** Optimizing onboarding playbooks during the first 60 days can significantly increase retention rates of newer cohorts.
        """)

