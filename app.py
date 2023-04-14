import streamlit as st
import pandas as pd
import numpy as np

st.set_page_config(
    page_title="Gregorius Ferry", 
    page_icon=":rocket:",
    layout="centered"
)

def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style", unsafe_allow_html=True)
local_css("style/style.css")

with st.container():
    st.title(":rocket:")
    st.subheader("Hi, I am Ferry! :wave:")
    st.title("A Tech Enthusiast from Indonesia")
    st.write("As a seasoned professional with experience in finance, education, and technology, I am dedicated to leveraging data, product, technology, and business to create outstanding work results. I welcome all inquiries and opportunities for collaboration, and look forward to hearing from you.")
    left_column, mid_column, right_colum = st.columns(3)
    with left_column:
        st.metric(label="Years of Experience", value="4 years", delta="since 2019", delta_color="off")
    with mid_column:
        st.metric(label="Projects Done", value="5 projects", delta="2 projects, YoY", delta_color="off")
    with right_colum:
        st.metric(label="Satisfied Clients", value="5 clients", delta="2 clients, YoY", delta_color="off")
    
with st.container():
    st.divider()
    st.header("Projects")
    left_column, mid_column, right_column = st.columns(3)
    with left_column:
        st.image('https://source.unsplash.com/480x240?architecture black and white')
        st.write("<strong style='font-size:22px'>Project Zeus</strong><br/> <strong>2020</strong> <br /><small style='color: #9c9d9f'>Use statistical analysis to uncover patterns and insights in customer behavior data, enabling better targeting and personalization of marketing campaigns.</small>", unsafe_allow_html=True)
    with mid_column:
        st.image('https://source.unsplash.com/480x240?mountain black and white')
        st.write("<strong style='font-size:22px'>Project Athena</strong><br/> <strong>2021</strong> <br /><small style='color: #9c9d9f'>Build a model using historical stock data to predict future prices, allowing investors to make more informed trading decisions.</small>", unsafe_allow_html=True)
    with right_column:
        st.image('https://source.unsplash.com/480x240?gadget black and white')
        st.write("<strong style='font-size:22px'>Project Hades</strong><br/> <strong>2022</strong> <br /><small style='color: #9c9d9f'>Design and develop a user-friendly mobile application that allows users to set fitness goals, track progress, and receive personalized recommendations.</small>", unsafe_allow_html=True)
    st.write("###")
    left_column, mid_column, right_column = st.columns(3)
    with left_column:
        st.image('https://source.unsplash.com/480x240?forest black and white')
        st.write("<strong style='font-size:22px'>Project Hermes</strong><br/> <strong>2023</strong> <br /><small style='color: #9c9d9f'>Develop algorithms to detect and flag transactions that deviate from typical patterns, reducing the risk of financial losses due to fraudulent activity.</small>", unsafe_allow_html=True)
    with mid_column:
        st.image('https://source.unsplash.com/480x240?sea black and white')
        st.write("<strong style='font-size:22px'>Project Poseidon</strong><br/> <strong>2023</strong> <br /><small style='color: #9c9d9f'>Build a web platform that allows property owners to list their vacation rentals, and users to search and book rentals, while providing features for managing bookings and payments.</small>", unsafe_allow_html=True)
    with right_column:
        st.empty()

with st.container():
    st.divider()
    st.header("Backgrounds")
    left_column, right_column = st.columns(2)
    with left_column:
        st.subheader("Experiences")
        a, b = st.columns([0.07, 0.93])
        a.write(":technologist:")
        b.write("<strong>Freelance <br />Self employed</strong> <br /><small style='color: #808495'>Oct 2019 - now</small>", unsafe_allow_html=True)
        a, b = st.columns([0.07, 0.93])
        a.write(":studio_microphone:")
        b.write("<strong>Data Analyst <br />Inspigo, Technology and Information</strong> <br /><small style='color: #808495'>Dec 2021 - Jun 2023</small>", unsafe_allow_html=True)
        a, b = st.columns([0.07, 0.93])
        a.write(":bank:")
        b.write("<strong>Business Analyst <br />DBS Bank, Financial Service</strong> <br /><small style='color: #808495'>Jan 2020 - Dec 2021</small>", unsafe_allow_html=True)
    with right_column:
        st.subheader("Educations")
        a, b = st.columns([0.07, 0.93])
        a.write(":computer:")
        b.write("<strong>Full Stack Web Developmment <br />Binar Academy</strong> <br /><small style='color: #808495'>Mar 2022 - Sep 2022</small> <br /><small style='color: #808495'>Best student awardee :star:</small>", unsafe_allow_html=True)
        a, b = st.columns([0.07, 0.93])
        a.write(":construction_worker:")
        b.write("<strong>Engineering <br />Bandung Institute of Technology</strong> <br /><small style='color: #808495'>Aug 2015 - Oct 2019</small>", unsafe_allow_html=True)

with st.container():
    st.divider()
    st.header("Core Abilities")
    
    st.subheader("Programming Language")
    st.write("<small>SQL, Python, Javascript, R</small>", unsafe_allow_html=True)
    
    a, b = st.columns(2)
    with a:
      st.subheader("Tools")
      
      x, y = st.columns([0.03, 0.97])
      x.write(":computer:", unsafe_allow_html=True)
      y.write("<strong>Data and Programming</strong> <br /><small>Google Colab, Jupyter Lab/Notebook, RStudio, VSCode, Redash, BigQuery, Redshift, SAS Enterprise Guide, Git, Postman, Wordpress, Webflow</small>", unsafe_allow_html=True)

      x, y = st.columns([0.03, 0.97])
      x.write(":bar_chart:", unsafe_allow_html=True)
      y.write("<strong>Data Visualization</strong> <br /><small>Google Data Studio/Looker Studio, Tableau, Power BI</small>", unsafe_allow_html=True)

      x, y = st.columns([0.03, 0.97])
      x.write(":chart:", unsafe_allow_html=True)
      y.write("<strong>Product Analytics, MMP, and Apps Management</strong> <br /><small>Google Analytics, MoEngage, AppsFlyer, Branch.io, Google Play Console, App Store Connect, Firebase</small>", unsafe_allow_html=True)

      x, y = st.columns([0.03, 0.97])
      x.write(":pencil:", unsafe_allow_html=True)
      y.write("<strong>Prototyping and Whiteboarding</strong> <br /><small>Figma, FigJam, Miro</small>", unsafe_allow_html=True)

      x, y = st.columns([0.03, 0.97])
      x.write(":building_construction:", unsafe_allow_html=True)
      y.write("<strong>Project Management</strong> <br /><small>Notion, Asana, ClickUp, Trello</small>", unsafe_allow_html=True)

      x, y = st.columns([0.03, 0.97])
      x.write(":artist:", unsafe_allow_html=True)
      y.write("<strong>Design</strong> <br /><small>Adobe Photoshop, Adobe Illustrator, Canva</small>", unsafe_allow_html=True)

      x, y = st.columns([0.03, 0.97])
      x.write(":office:", unsafe_allow_html=True)
      y.write("<strong>Office suite</strong> <br /><small>Microsoft Word, Excel, Powerpoint, Google Docs, Sheets, Slides</small>", unsafe_allow_html=True)

    with b:
      st.subheader("Skills")
      
      x, y = st.columns([0.03, 0.97])
      x.write(":bar_chart:", unsafe_allow_html=True)
      y.write("<strong>Data</strong> <br /><small>data analysis, data visualization, data modeling, data management, statistics, statistical analysis, A/B testing, root cause analysis</small>", unsafe_allow_html=True)

      x, y = st.columns([0.03, 0.97])
      x.write(":computer:", unsafe_allow_html=True)
      y.write("<strong>Programming</strong> <br /><small>front end development, back end development, full stack web development, python apps development, javascript apps development, Wordpress website development, Webflow website development</small>", unsafe_allow_html=True)

      x, y = st.columns([0.03, 0.97])
      x.write(":artist:", unsafe_allow_html=True)
      y.write("<strong>Design</strong> <br /><small>prototyping, low fidelity design, high fidelity design, interaction design, UI/UX research, copywriting, asset design, vector art design</small>", unsafe_allow_html=True)

      x, y = st.columns([0.03, 0.97])
      x.write(":rocket:", unsafe_allow_html=True)
      y.write("<strong>Product</strong> <br /><small> user testing, agile project management, product discovery, product roadmapping, product requirement documents, quantitative research, qualitative research</small>", unsafe_allow_html=True)

with st.container():
    st.divider()
    st.header("Get in touch with me!")
    contact_form = """
    <form action="https://formsubmit.co/grgsferry@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="Your name" required>
        <input type="email" name="Your email" required>
        <textarea name="message" placeholder="Your message here" requrired></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns([0.65, 0.35])
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()