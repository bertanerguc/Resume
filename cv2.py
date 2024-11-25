import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime

# Sayfa yapılandırması
st.set_page_config(page_title="Interactive CV - Bertan Erguc", layout="wide")

# Sidebar Menü
st.sidebar.title("Navigation")
menu = st.sidebar.radio(
    "Select Section",
    ["Home", "Personal Info", "Education", "Technical Skills", "Work Experience", "Projects", "Trainings", "Interests"]
)

# Home Sayfası
if menu == "Home":
    st.title("Welcome to My Interactive CV!")
    st.write("Navigate through the sidebar to explore different sections of my CV.")
    st.image("profile.jpg", caption="Bertan Erguc", use_column_width=True)

# Personal Info Sayfası
elif menu == "Personal Info":
    st.title("Personal Information")
    st.write("""
    - **Name:** Bertan Erguc  
    - **Phone:** 786.830.1976  
    - **Email:** bertanerguc@gmail.com  
    - **Address:** 1750 NE 115TH ST APT#509, Miami, 33181
    """)

# Education Sayfası
elif menu == "Education":
    st.title("Education")
    st.subheader("Bachelor of Crop Science in Agricultural Engineering")
    st.write("**University:** Adnan Menderes University")
    st.write("**Year:** 2005 - 2009")
    st.write("""
    - Due to my outstanding academic performance, I was awarded the opportunity to complete an internship at Humboldt University in Berlin.
    - Notably, I was the first Turkish student accepted in the field of agriculture from Turkey to this prestigious institution.
    """)
    st.subheader("MBA, Accounting and Finance")
    st.write("**University:** University of Economics")
    st.write("**Year:** 2012 - 2014")
    st.write("""
    - While working at İnci Holding, I pursued an MBA in Accounting and Finance at the University of Economics to further specialize in the field of finance and deepen my expertise.
    """)

# Technical Skills Sayfası
elif menu == "Technical Skills":
    st.title("Technical Skills")

    st.subheader("Programming and Tools")
    st.write("""
    - PyCharm, Virtual Environments, Dependency Management, Git
    - PySpark, MS SQL, Docker, Google Cloud
    - Network Administration, Agile & Scrum
    """)

    st.subheader("Analytics and Forecasting")
    st.write("""
    - Measurement Problems (Dynamic Pricing, AB Testing, Sorting)
    - Demand Forecasting (Time Series)
    - CRM Analytics (KPI, Cohort, CLTV, Segmentation)
    - BG-NBD: Expected Sales Forecasting
    - Gamma-Gamma: Expected Average Profit
    - RFM Analysis
    - Churn Analysis
    """)

    st.subheader("Machine Learning and AI")
    st.write("""
    - Recommendation Systems (ARL, Collaborative Filtering, Matrix Factorization)
    - Advanced Feature Engineering
    - Script-Level Machine Learning
    - NLP (Text Mining, Review Modeling, Word Embeddings)
    - Home Credit Default Risk Prediction
    """)

    st.subheader("Automation and Deployment")
    st.write("""
    - House Price Prediction Model
    - Automation of Machine Learning Pipelines
    - Model Deployment with Flask, Makefile
    """)

    # Radar Chart - Teknik Becerilerin Görselleştirilmesi
    skill_levels = {
        "Python": 80,
        "SQL": 75,
        "PowerBI": 70,
        "Git": 75,
        "Docker": 60,
        "PySpark": 65,
        "Google Cloud": 40,
        "Agile & Scrum": 60
    }

    radar_fig = go.Figure()
    radar_fig.add_trace(go.Scatterpolar(
        r=list(skill_levels.values()),
        theta=list(skill_levels.keys()),
        fill='toself',
        name='Skill Levels'
    ))

    radar_fig.update_layout(
        polar=dict(radialaxis=dict(visible=True, range=[ 0, 100 ])),
        title="Technical Skill Levels"
    )

    st.plotly_chart(radar_fig, use_container_width=True)


# Work Experience Sayfası
elif menu == "Work Experience":
    st.title("Work Experience")

    # İş Deneyimi Detayları
    work_experience = [
        {
            "Position": "Food and Beverage Supervisor",
            "Company": "Fisher Island Club",
            "Start": "2024-08",
            "End": "Present",
            "Highlights": [
                "Managing exclusive dining and beach club operations",
                "Team training and development",
                "Crafting seasonal menus with executive chef",
                "Building relationships with high-profile clientele"
            ]
        },
        {
            "Position": "General Manager",
            "Company": "Eat Greek",
            "Start": "2015-03",
            "End": "2021-03",
            "Highlights": [
                "Oversaw daily operations for multiple locations across Miami",
                "Streamlined supply chain processes, reducing costs by 15%",
                "Implemented customer feedback systems, improving satisfaction scores",
                "Hired and trained a team of 50+ employees"
            ]
        },
        {
            "Position": "Data Science Apprentice",
            "Company": "Qubit Science",
            "Start": "2023-12",
            "End": "2024-07",
            "Highlights": [
                "Cleaned and analyzed large datasets using Python and SQL",
                "Prepared datasets for machine learning models",
                "Created visualizations with PowerBI and Tableau",
                "Represented company at Bitcoin Energy Summit"
            ]
        },
        {
            "Position": "General Manager",
            "Company": "Spitfire Mediterranean Grill",
            "Start": "2021-04",
            "End": "2023-09",
            "Highlights": [
                "Oversaw daily restaurant operations",
                "Maintained HACCP compliance",
                "Managed recruitment and staff training programs",
                "Increased profitability through cost control and efficiency improvements"
            ]
        },
        {
            "Position": "Assistant Finance Manager",
            "Company": "Inci Holding",
            "Start": "2011-12",
            "End": "2014-03",
            "Highlights": [
                "Managed financial operations, including accounting and budgeting",
                "Led a finance team and implemented internal controls",
                "Collaborated with senior management on strategic financial planning",
                "Prepared financial risk assessments and stakeholder reports"
            ]
        }
    ]

    # Her İş Pozisyonunu Listeleme
    for job in work_experience:
        st.subheader(f"{job['Position']} at {job['Company']}")
        st.write(f"**Duration:** {job['Start']} - {job['End']}")
        st.write("**Key Highlights:**")
        for highlight in job["Highlights"]:
            st.write(f"- {highlight}")

    # Zaman Çizelgesi Verisi
    timeline_data = [
        {
            "Position": job["Position"],
            "Company": job["Company"],
            "Start": datetime.strptime(job["Start"], "%Y-%m"),
            "End": datetime.now() if job["End"] == "Present" else datetime.strptime(job["End"], "%Y-%m")
        }
        for job in work_experience
    ]

    # DataFrame ile Görselleştirme
    timeline_df = pd.DataFrame(timeline_data)

    fig = px.timeline(
        timeline_df,
        x_start="Start",
        x_end="End",
        y="Position",
        color="Company",
        title="Professional Experience Timeline"
    )

    fig.update_layout(
        xaxis_title="Timeline",
        yaxis_title="Position",
        hoverlabel=dict(font_size=12, font_family="Arial"),
        title_font_size=22,
        template="plotly_dark",  # Daha koyu ve etkileyici tema
        showlegend=True,
    )

    # Zaman Çizelgesi Görseli
    st.plotly_chart(fig, use_container_width=True)



# Projects Sayfası
elif menu == "Projects":
    st.title("Projects and Achievements")

    # Projeler Verisi
    projects = [
        {
            "Title": "Mimar Olsaydım",
            "Description": """
            Developed a unique design project showcasing innovative and sustainable architectural solutions.
            - Conceptualized and implemented design principles to merge functionality with aesthetics.
            - Collaborated with cross-disciplinary teams to bring creative ideas to life.
            - Received widespread recognition for originality and practical approach.
            """
        },
        {
            "Title": "Bitcoin Energy Summit",
            "Description": """
            Represented Qubit Science and reported sustainable energy insights to senior management.
            - Analyzed blockchain energy consumption data.
            - Proposed actionable strategies for reducing environmental impact.
            """
        },
        {
            "Title": "Data Science Bootcamp",
            "Description": """
            Completed advanced topics including Time Series Analysis, NLP, and Deployment.
            - Built a recommendation system using collaborative filtering.
            - Deployed a machine learning model for credit risk prediction.
            """
        }
    ]

    # Her Projeyi Listeleme
    for proj in projects:
        st.subheader(proj["Title"])
        st.write(proj["Description"])


# Trainings Sayfası
elif menu == "Trainings":
    st.title("Trainings and Certifications")

    # Eğitimler ve Sertifikalar
    trainings = [
        "Data Science Bootcamp - Miuul (Jun 2024 - Nov 2024)",
        "UX/UI Design Certification - Coursera",
        "Time Management and Persuasion Techniques",
        "Advanced Machine Learning with Python",
        "Docker and Kubernetes Fundamentals",
        "Google Cloud Data Engineering",
        "NLP Specialization ",
        "Python for Data Analysis"
    ]

    # Eğitimleri Listeleme
    for training in trainings:
        st.write(f"- {training}")


# Interests Sayfası
elif menu == "Interests":
    st.title("Interests")

    # İlgi Alanları ve Uygun Emojiler
    interests = [
        "🏊 Swimming",
        "🤿 Diving",
        "🛶 Sea Kayaking",
        "🚴 Cycling",
        "🏂 Snowboarding",
        "🥊 Kickboxing",
        "📚 Reading",
        "🎮 Gaming",
        "🎵 Listening to Music",
        "🍳 Cooking"
    ]

    # İlgi Alanlarını Listeleme
    for interest in interests:
        st.write(f"- {interest}")

# Footer
st.sidebar.markdown("---")
st.sidebar.write("Created by Bertan Erguc")
