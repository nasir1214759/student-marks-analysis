import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# 🧾 Page Configuration
st.set_page_config(page_title="📊 Student Marks Analysis", layout="centered")
st.title("📊 Student Marks Analysis")

# 📤 CSV Upload
uploaded_file = st.file_uploader("📁 Upload your CSV file", type=['csv'])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.success("✅ File uploaded successfully!")

    st.subheader("🔍 Data Preview")
    st.dataframe(df)

    if 'Name' in df.columns:
        subjects = df.columns.drop('Name')
    else:
        subjects = df.columns

    df['Total'] = df[subjects].sum(axis=1)
    df['Average'] = df[subjects].mean(axis=1)

    st.subheader("📈 Total & Average")
    st.dataframe(df[['Name', 'Total', 'Average']] if 'Name' in df.columns else df[['Total', 'Average']])

    st.subheader("🏅 Top Scorers")
    st.table(df.sort_values(by='Total', ascending=False).head(3))

    st.subheader("✅ Pass/Fail Status")
    pass_mark = st.number_input("📌 Enter pass mark per subject", value=40)

    df['Status'] = df[subjects].apply(lambda x: 'Pass' if all(x >= pass_mark) else 'Fail', axis=1)
    st.dataframe(df[['Name', 'Status']] if 'Name' in df.columns else df[['Status']])

    st.bar_chart(df['Status'].value_counts())

    st.subheader("📊 Subject Averages")
    st.bar_chart(df[subjects].mean())

    st.subheader("📉 Correlation Heatmap")
    fig, ax = plt.subplots()
    sns.heatmap(df[subjects].corr(), annot=True, cmap='coolwarm', ax=ax)
    st.pyplot(fig)

else:
    st.info("📥 Please upload a CSV file to begin.")
