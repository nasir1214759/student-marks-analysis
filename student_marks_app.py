# 📦 Zaroori libraries import
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 🧾 Page settings
st.set_page_config(page_title="Student Marks Analysis", layout="centered")
st.title("📊 Student Marks Analysis")

# 📁 CSV file upload karne ka option
uploaded_file = st.file_uploader("📁 Upload your CSV file", type=['csv'])

# ✅ Agar file upload hui ho
if uploaded_file is not None:
    # 📊 CSV data read karna
    df = pd.read_csv(uploaded_file)
    st.success("✅ File uploaded successfully!")

    # 👁️ Data preview dikhana
    st.subheader("🔍 Data Preview")
    st.dataframe(df)

    # 🧠 Subjects identify karna (Name ke ilawa sab subjects)
    if 'Name' in df.columns:
        subjects = df.columns.drop('Name')
    else:
        subjects = df.columns

    # ➕ Total & Average marks calculate karna
    df['Total'] = df[subjects].sum(axis=1)
    df['Average'] = df[subjects].mean(axis=1)

    # 📈 Total & Average display
    st.subheader("📈 Total & Average")
    st.dataframe(df[['Name', 'Total', 'Average']] if 'Name' in df.columns else df[['Total', 'Average']])

    # 🏆 Top scorers show karna
    st.subheader("🏆 Top Scorers")
    st.table(df.sort_values(by="Total", ascending=False).head(3))

    # ✅ Pass/Fail logic
    st.subheader("✅ Pass/Fail Status")
    pass_mark = st.number_input("Enter pass mark for each subject", value=40)

    # 🎯 Pass ya Fail decide karna har student ke liye
    df['Status'] = df[subjects].apply(lambda x: 'Pass' if all(x >= pass_mark) else 'Fail', axis=1)

    # 📋 Status table display
    st.dataframe(df[['Name', 'Status']] if 'Name' in df.columns else df[['Status']])

    # 📊 Pass/Fail ka chart
    st.bar_chart(df['Status'].value_counts())

    # 📚 Subject-wise average marks
    st.subheader("📊 Subject Averages")
    st.bar_chart(df[subjects].mean())

    # 🔥 Heatmap dikhana for subject correlation
    st.subheader("📉 Correlation Heatmap")
    fig, ax = plt.subplots()
    sns.heatmap(df[subjects].corr(), annot=True, cmap="coolwarm", ax=ax)
    st.pyplot(fig)

# ⚠️ Agar file upload nahi hui to yeh message show hoga
else:
    st.info("📥 Please upload a CSV file to begin.")
