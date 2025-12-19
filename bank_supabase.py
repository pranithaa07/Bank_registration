import streamlit as st
import pandas as pd
from supabase import create_client

#Supabase Configuration
SUPABASE_URL = "https://wmaagzjdgdsonirrltqr.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6IndtYWFnempkZ2Rzb25pcnJsdHFyIiwicm9sZSI6ImFub24iLCJpYXQiOjE3NjYwNDE4NzcsImV4cCI6MjA4MTYxNzg3N30.dcTc0OM58YOH5oGUE7hq_t7TgGs3xEoYGi9MdzMJB3s"

supabase=create_client(SUPABASE_URL, SUPABASE_KEY)

#Streamlit UI
st.title(" HDFC BANK (Supabase)")
#
menu=["REGISTER", "VIEW"]
choice=st.sidebar.selectbox ("Menu", menu)

#REGISTER
if choice=="REGISTER":
    name=st.text_input("Enter name")
    age=st.number_input("AGE", min_value=18)
    account=int(st.number_input("ACCOUNT NUMBER"))
    bal=st.number_input("BALANCE", min_value=500)
    if st.button("Save"):
        supabase.table("users1").insert({
            "name": name,
            "age": age,
            "account": account,
            "balance":bal}).execute()
        st.success ("user added successfully")

#View Students
if choice == "VIEW":
    st.subheader("view users")
    data=supabase.table("users1").select("*").execute()
    df=pd.DataFrame(data.data)
    st.dataframe(df)
