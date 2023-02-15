"""
    Module 1: Hello World!
    > Rendering markdown
        > Titles
        > Subtitles
        > Text + Formatting
    > Displaying dataframes
"""

# Import streamlit
import streamlit as st
import pandas as pd

# Write a title
# st.title("Hello World!")

# Write some markdown
st.markdown(
"""
# Hello World!
## This is some example markdown

Here is some markdown with ~~inline~~ *special* **formatting**.

"""
)

# Or, just use st.write(...)
st.write(    
    # Some content
    "Streamlit allows for writing many types of object, such as the `pandas.dataframe` below:",

    pd.read_csv("hello-world/customers.csv")
)
