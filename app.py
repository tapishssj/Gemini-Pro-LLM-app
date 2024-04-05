from dotenv import load_dotenv

##loading all the environment variables

import streamlit as st 
import os 
import sqlite3

import google.generativeai as genai


##configure API key

genai.configure(api_key=os.getenv("GOOGLE_API_KEY")) 

##function to load Gemini and provide sql query
def get_gemini_response(question,prompt):
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt[0],question])
    return response.text

def read_sql_query(sql,db):

    connection = sqlite3.connect(db)
    cursor = connection.cursor()
    cursor.execute(sql)
    rows = cursor.fetchall()
    connection.commit()
    connection.close()
    for row in rows:
        print(row)
    return rows




prompt=[
    """
    You are an expert in converting English questions to SQL query!
    The SQL database has the name EMPLOYEE and has the following columns - NAME, DEPARTMENT, 
    SALARY \n\nFor example,\nExample 1 - How many entries of records are present?, 
    the SQL command will be something like this SELECT COUNT(*) FROM STUDENT ;
    \nExample 2 - Tell me all the employees in IT department?, 
    the SQL command will be something like this SELECT * FROM EMPLOYEE
    WHERE DEPARTMENT="IT"; 
    also the sql code should not have ``` in beginning or end and sql word in output

    """

]


## Streamlit App

st.set_page_config(page_title="I can Retrieve Any SQL query")
st.header("Text2SQL App to Retrieve SQL Data")
st.subheader('(Gemini Pro LLM based APP)')

question=st.text_input("Input: ",key="input")

submit=st.button("Ask the question")

if submit:
    response=get_gemini_response(question,prompt)
    print(response)
    data=read_sql_query(response,"employee.db")
    st.subheader("The Response is")
    for row in data:
        print(row)
        st.header(row)











