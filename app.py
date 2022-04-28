
import streamlit as st
import streamlit.components.v1 as components

  


st.title("ICF (Title to be decided)")
st.sidebar.markdown("### Definitions")
page4 = st.sidebar.selectbox(
    "Select Definition",
    ["A","B","C"]
)

st.sidebar.markdown("### Stakeholder Wise Analysis")
page = st.sidebar.selectbox(
      "Select Stakeholder",
        ["Foresters","Conservationists","Scientists","Sawmill Producers","Regulators","Commercial Manufacturers","Forestry Associations"]
    )


if not st.sidebar.checkbox("Hide", True):
  if page == "Foresters":
    st.subheader("Foresters")
    img = "https://github.com/vishalvindyala/ICF/blob/main/Mind%20Map%20(2).jpg?raw=true"
    img = st.image(img,width = 1000,caption = "Foresters Mind Map")
    st.subheader("Environmanetal")
    st.text("Text Here")
    st.subheader("Social")
    st.text("Text Here")
    st.subheader("Governmental")
    st.text("Text Here")

  elif page == "Conservationists":
    st.subheader("Conservationists mind map")
    img = "https://github.com/vishalvindyala/ICF/blob/main/Mind%20Map%20(3).jpg?raw=true"
    img = st.image(img,width=1000,caption="Conservationists Mind Map")
  elif page == "Scientists":
    st.subheader("Scientists mind map")
    img = "https://github.com/vishalvindyala/ICF/blob/main/Mind%20Map%20(4).jpg?raw=true"
    img = st.image(img,width=1000,caption="Scientists Mind Map")
  elif page == "Sawmill Producers":
    st.subheader("Sawmill Poducers mind map")
    img = "https://github.com/vishalvindyala/ICF/blob/main/Mind%20Map%20(5).jpg?raw=true"
    img = st.image(img,width=1000,caption="Sawmill Producers Mind Map")
  elif page == "Regulators":
    st.subheader("Regulators mind map")
    img = "https://github.com/vishalvindyala/ICF/blob/main/Mind%20Map%20(6).jpg?raw=true"
    img = st.image(img,width=1000,caption="Regulators Mind Map")
  elif page == "Commercial Manufacturers":
    st.subheader("Commercial Manufacturers mind map")
    img = "https://github.com/vishalvindyala/ICF/blob/main/Mind%20Map%20(7).jpg?raw=true"
    img = st.image(img,width=1000,caption="Commercial Manufacturers Mind Map")
  else:
    st.subheader("Forestry Associations mind map")
    img = "https://github.com/vishalvindyala/ICF/blob/main/Mind%20Map%20(8).jpg?raw=true"
    img = st.image(img,width=1000,caption="Commercial Manufacturers Mind Map")
  
st.sidebar.markdown("### Similarities & Differences")


page2 = st.sidebar.selectbox(
      "Select Stakeholder",
        ["Foresters","Next"]
    )
page3 = st.sidebar.selectbox(
    "Select Stakeholder",
    ["Forestry Associations","Next"]
)
typ = st.sidebar.selectbox(
    "Type",
    ["Similarities"]
)
if not st.sidebar.checkbox("Hide", True,key="2"):
  if page2 == "Foresters" and typ == "Similarities" and page3 == "Forestry Associations":
    st.subheader("Foresters & Forestry Associations")
    img = "https://github.com/vishalvindyala/ICF/blob/main/sweets%20Diagram.png?raw=true"
    st.image(img)
    img2 = "https://github.com/vishalvindyala/ICF/blob/main/My%20First%20Board.jpg?raw=true"
    st.image(img2)
    st.subheader("Catergory")
    st.text("Further explanation here")
   
  
