import streamlit as st
import pickle as pk
import pandas as pd

# Title of the app
st.title('Netflix Review Analysis')

# Load the model
filename = 'Netflix_review.pickle'
with open(filename, 'rb') as file:
    lr_model = pk.load(file)

# Input prompt for the user
st.write("Input below: Review given by the customer")
comment = st.text_input("Comment")

# When the user clicks the submit button
if st.button('Submit'):
    # Ensure that the comment is not empty
    if comment:
        df = pd.DataFrame({'cleaned': [comment]})
        # Predict the sentiment
        output = lr_model.predict(df['cleaned'])
        # Display the result
        if output[0] == '5':
            st.write("Positive Review")
        else:
            st.write("Negative Review")
    else:
        st.write("Please enter a review.")
