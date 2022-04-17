import pickle
import numpy as np
import pandas as pd
import streamlit as st
import datetime

st.title("ABC Inc.")
st.write("Flight Charges Prediction ")
st.image("data//images.jpeg")

data = pd.read_csv('data//train.csv')
RFR = pickle.load(open('RFR.pkl', 'rb'))

nav = st.sidebar.radio('Navigation', ['Home', 'Prediction'])
if nav == 'Home':
    st.subheader('Flight Charges Prediction')
    if st.checkbox('Show Data'):
        st.dataframe(data)

if nav == 'Prediction':
    st.subheader('Please give the following information:')

    Airline = st.selectbox('Select Airline',
                           ("Jet Airways", "IndiGo", "Air India", "Multiple carriers", "SpiceJet",
                            "Vistara", "Air Asia", "GoAir", "Multiple carriers Premium economy",
                            "Trujet"))

    if Airline == "Jet Airways":
        Airline = 1
    elif Airline == "IndiGo":
        Airline = 2
    elif Airline == "Air India":
        Airline = 3
    elif Airline == "Multiple carriers":
        Airline = 4
    elif Airline == "SpiceJet":
        Airline = 5
    elif Airline == "Vistara":
        Airline = 6
    elif Airline == "Air Asia":
        Airline = 7
    elif Airline == "GoAir":
        Airline = 8
    elif Airline == "Multiple carriers Premium economy":
        Airline = 9
    elif Airline == "Trujet":
        Airline = 10

    Source = st.selectbox("Select the Source", ('Banglore', "Chennai", "Delhi", "Kolkata", "Mumbai"))

    if Source == "Banglore":
        Source = 1
    elif Source == "Chennai":
        Source = 2
    elif Source == "Delhi":
        Source = 3
    elif Source == "Kolkata":
        Source = 4
    elif Source == "Mumbai":
        Source = 5

    Destination = st.selectbox("Select the Destination", ("Cochin", "Banglore", "Delhi", "Hyderabad", "Kolkata"))

    if Destination == "Banglore":
        Destination = 1
    elif Destination == "Cochin":
        Destination = 2
    elif Destination == "Delhi":
        Destination = 3
    elif Destination == "Hyderabad":
        Destination = 4
    elif Destination == "Kolkata":
        Destination = 5

    Total_Stops = st.selectbox("Select no of stops or no stops for point to point travel without layover",
                               ('non-stop', '2 stops', '1 stop', '3 stops', '4 stops'))

    if Total_Stops == "non-stop":
        Total_Stops = 1
    elif Total_Stops == "1 stop":
        Total_Stops = 2
    elif Total_Stops == "2 stops":
        Total_Stops = 3
    elif Total_Stops == "3 stops":
        Total_Stops = 4
    elif Total_Stops == "4 stops":
        Total_Stops = 5

    st.subheader("Select Departure")
    m = pd.to_datetime("today").month
    d = pd.to_datetime("today").day
    y = pd.to_datetime("today").year

    journey = st.date_input("Date of Journey", datetime.date(y, m, d))

    journey_month = journey.month
    journey_day = journey.day

    Dep_Time_hour = st.selectbox("Hour", list(range(1, 25)))
    Dep_Time_min = st.selectbox("Minute", list(range(0, 61)))

    st.subheader("Departure Time :")

    A = "2022" + "/" + str(journey_month) + "/" + str(journey_month) + " " + str(Dep_Time_hour) + ":" + str(
        Dep_Time_min)
    A = pd.to_datetime([A])

    st.subheader("Select Arrival")
    Arrival = st.date_input("Date of Arrival", datetime.date(y, m, d + 1))
    journey_month = Arrival.month
    journey_day = Arrival.day

    Arrival_Time_hour = st.selectbox("Hour.", list(range(1, 25)), 2)
    Arrival_Time_min = st.selectbox("Minute.", list(range(0, 61)))

    st.subheader("Arrival Time :")
    x1 = "2020" + "/" + str(journey_month) + "/" + str(journey_day) + " " + str(Arrival_Time_hour) + ":" + str(
        Arrival_Time_min)
    op1 = pd.to_datetime([x1])

    st.subheader("Duration")
    st.write(Arrival_Time_hour - Dep_Time_hour, ":", Arrival_Time_min - Dep_Time_min, "Hrs")
    dur_hour = Arrival_Time_hour - Dep_Time_hour
    dur_min = Arrival_Time_min - Dep_Time_min

    x = np.array([Airline, Source, Destination, Total_Stops, journey_day, journey_month, Dep_Time_hour, Dep_Time_min,
                  Arrival_Time_hour, Arrival_Time_min, dur_hour, dur_min])
    x = x.reshape(1, 12)

    if st.button("Predict"):
        st.title(f'The Flight charges are ' + str(round(int(RFR.predict(x)[0]))) + '₹')




