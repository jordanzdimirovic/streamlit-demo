"""
    Module 2: Interactivity
    > Buttons
    > Sliders
    > Multi-selects
    > Checkbox
    > Combining interactivity
"""

# Import streamlit
import streamlit as st

# Write a title
st.title("User Interaction")

st.markdown("Streamlit provides *interactive widgets* that allow for control over your data apps in realtime:")

# Use a button to conditionally run things or show code
# >>>
if st.button("Click me"):
    st.write("Button WAS pressed")
else:
    st.write("Button WAS **NOT** pressed")

# Multiselects
# >>>
selected_items = st.multiselect("Select some value(s)", ["Option 1", "Option 2"])

st.markdown(f"You selected the following:")

for item in selected_items:
    st.markdown(f"- {item}")

st.markdown("---")

# Checkboxes
# >>>
if st.checkbox("Check this box to show content"):
    st.markdown("""
    ## Content
    You can use interactivity to show and hide content conditionally
    """)

    if st.checkbox("Show even more content"):
        st.markdown("""## More Content
        Here's some more content that can be shown conditionally
        """)

# Sliders
# >>>
number_value = st.slider("Pick a number", 0, 100)

# Range sliders
# >>>
# values = st.slider("Pick a range of numbers", 0, 100, (25, 75))
range_bottom, range_top = st.slider("Pick a range of numbers", 0, 100, (25, 75))

if range_bottom < number_value < range_top:
    st.write(f"# :white_check_mark: Number in range")

else:
    st.write(f"# :warning: ~~Number in range~~")
