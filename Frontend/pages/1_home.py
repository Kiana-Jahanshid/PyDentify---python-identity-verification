import streamlit as st

st.title("Welcome to eKYC Application👩🏻🧒🏻")
st.write("This is the user identity verification")

st.markdown(
'''

### Stages :
- Upload your ID-card
- Take a picture from yourself
- Record your voice 
- Hand gesture matching


## 🔻 Attention 🔻:
#### You have to allow microphone and camera acces during process. 

'''
)

st.write(" ")
st.markdown("""<style>.white-bold-text {color: #FAFAFA;font-family: 'Thaoma', monospace;font-size: 25px;font-weight: bold;
        text-decoration: none; display: flex;
        justify-content: center;align-items: center;
        text-align: center;border: 1px solid #262730; 
        border-radius: 6px;  padding: 10px;  
        background-color: #262735;width: 24%;  margin: 0 auto; }</style>""",
    unsafe_allow_html=True)

#st.page_link("pages/2_take_picture.py", label='Next Stage ⏭', use_container_width=True  )
#st.link_button("Next Stage ⏭", "take_picture")

st.markdown('<a href="upload_IDcard" target="_self" class="white-bold-text">Start</a>', unsafe_allow_html=True )



# streamlit run app.py

