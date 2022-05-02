
import streamlit as st
import streamlit.components.v1 as components

  


st.title("Maryland Forestry Team 2 Dashboard")
st.sidebar.markdown("## Lessons Learned")
if not st.sidebar.checkbox("Hide",True,key="24"):
  st.subheader("Lessons Learned")
  components.html(
      """
      <h2 style="color:green;" > Re-education </h2>
      <p> It’s in the best interest for TGCC to increase the public’s understanding of the positive impacts 
      of forestry management practices because it can lead to a boost in public perception of the industry, 
      ultimately tipping the consumer desire from fast/cheap/easy production to sustainable and locally sourced, 
      leading to increase in ESG participation due to increased demand for certified products
      </p>
      """
  )
  components.html(
      """
      <h2 style="color:green;" > Positive Marketing </h2>
      <p> The terms “clear cutting”, “final harvest” and “dirty chips” need to be marketed towards an audience 
      that is not aware of their definitions. For instance, “regenerative cut” and “unrefined chips” would allow 
      the general public to understand that they aren’t bad for the environment. Tt is still important to note that on the regulatory side, 
      clear definitions have still proven beneficial
      </p> 

      """
  )
  components.html(
      """
      <h2 style="color:green;" > Highlighting Social Aspects </h2>
      <p> Foresters and manufacturers believe that they are doing beneficial social work currently, 
      and want that work to be highlighted by metric reporting; They want their 
      ESG report to highlight the work they’ve been doing

      </p> 

      """
  )
  components.html(
      """
      <h2 style="color:green;" >Speculation on necessity of ESG </h2>
      <p> Most foresters/manufacturers don’t see any necessity for ESG reporting because they 
      don’t reap any direct benefits under their current production services; most people 
      are speculative on the growth opportunities ESG provides


      </p> 

      """
  )
  
st.sidebar.markdown("## Interactive Mind Map")
if not st.sidebar.checkbox("Hide",True,key="34"):
  components.html(
        """
        <iframe width="768" height="432" src="https://miro.com/app/live-embed/uXjVO4s3HQE=/?moveToViewport=-18668,-6881,8718,4830" frameBorder="0" scrolling="no" allowFullScreen></iframe>
        """,
        height = 10000,width = 3000
    )



st.sidebar.markdown("## Stakeholder Wise Analysis")
page = st.sidebar.selectbox(
      "Select Stakeholder",
        ["Foresters","Scientists","Consumer Manufacturers","Regulators","Commercial Manufacturers"]
    )

if not st.sidebar.checkbox("Hide", True):
  if page == "Foresters":
    st.subheader("Foresters")
    img = "https://github.com/vishalvindyala/ICF/blob/main/ESG%20STAKEHOLDER%20PERSPECTIVES.jpg?raw=true"
    img = st.image(img,width=1000,caption="Foresters Mind Map")
    st.subheader("Insights")
    components.html(
        """
        <ul>
        <li>Education : Would like the public to be educated on the benefits of forestry management to increase production of forestry products
        Creating job opportunities by utilizing local lumber at all levels of its value while educating the public the value of sustainable harvesting</li>
        <li>Definitions : Redefine phrases that have been historically miscommunicated between different stakeholders, as well as the public.
        Such as Dirty Chips -> Non-stripped Chips,Clear cutting -> regenerative cutting</li>
        <li>Public perception of Forestry Management is bad; affects production of products.Because Maryland already has a lot of environmental regulation; 
        ESG shouldn't require any new requirements for land </li>
        <li>Most foresters see no benefit of ESG b/c they aren't servicing  consumers at the end of supply chain where ESG sees it's most marketability</li>
        <li>Benefits of ESG participation should > Costs ≈ 10% of total costs for supply chain reform</li>
        <li>Increase the desirability of products to secondary manufacturers, given that majority of market doesn't service direct consumers</li>
        <li>ESG regulated regulations should mesh in with the existing regulations and it should be an opt-in based program</li> 
        </ul>
        """,
        height = 10000
    )

  elif page == "Regulators":
    st.subheader("Regulators mind map")
    img = "https://github.com/vishalvindyala/ICF/blob/main/ESG%20STAKEHOLDER%20PERSPECTIVES%20(1).jpg?raw=true"
    img = st.image(img,width=1000,caption="Regulators Mind Map")
    st.subheader("Insights")
    components.html(
        """
        <ul>
        <li>The public has a skewed idea of what regulations are voluntary and what is required in terms of regulation</li>
        <li>No market, no management; regulators understand the importance of a stable market allowing the sustainability of forests</li>
        <li>Use natural resources that are more environmental friendly that benefits the environment,Generates profit while promoting environmental health,
        Find new natural resources for generating more profits</li>
        <li>Consequences should be applied to organizations in response to issues caused by them,Industry needs to understand that they're not getting regulated 
        out of existance, they're just becoming more sustainable in the long term</li>
        <li>Reeducate stakeholders and public by providing common definitions and providing positive social perception to ease tensions within forestry industry.</li>
        </ul>
        """,
        height = 1000
    )
  elif page == "Scientists":
    st.subheader("Scientists mind map")
    img = "https://github.com/vishalvindyala/ICF/blob/main/ESG%20STAKEHOLDER%20PERSPECTIVES%20(3).jpg?raw=true"
    img = st.image(img,width=1000,caption="Scientists Mind Map")
    st.subheader("Insights")
    components.html(
        """
        <ul> 
        <li>Forestry operations must be viewed as a positive for the environment and as sustainable</li>
        <li>If effective a good opportunity to educate other states or countries</li>
        <li>Companies who do not meet the standards should have repercussions,
        Need to be sure not to penalize companies for products and actions that are sustainable and are just perceived incorrectly</li>
        </ul>
        """,
        height = 1000
    )


  elif page == "Commercial Manufacturers":
    st.subheader("Commercial Manufacturers mind map")
    img = "https://github.com/vishalvindyala/ICF/blob/main/ESG%20STAKEHOLDER%20PERSPECTIVES%20(2).jpg?raw=true"
    img = st.image(img,width=1000,caption="Commercial Manufacturers Mind Map")
    st.subheader("Insights")
    components.html(
        """
        <ul>
        <li> Could use ESG metrics as standard for sourcing materials,Opportunity to create sourcing hierarchy, where priority is given to sources with highest ESG scores; 
        would boost secondary manufacturers' ESG scores as well</li>
        <li> Wide variety of perspectives on how sustainable practices need to be. 
        Some view forestry as a culture where tradition needs to be upheld, whereas some see the need to adapt with new standards</li>
        <li>Marketing appeal of sustainable/locally sourced n/a to commercial manufacturing process currently,
         as most manufacturers don't service other sectors where ESG certification would help,
         If local manufacturing allows for prioritization for government projects, ESG participation would increase</li>
        <li>There should be standards to address bad actors,Bad actors should see immediate drops in ESG score,Against additional regulations; 
         ESG certification should comply with existing certifications</li>
         </ul>
         
        """,
        height = 1000
    )
  else:
    st.subheader("Consumer Manufacturers mind map")
    img = "https://github.com/vishalvindyala/ICF/blob/main/ESG%20STAKEHOLDER%20PERSPECTIVES%20(4).jpg?raw=true"
    img = st.image(img,width=1000,caption="Consumer Manufacturers Mind Map")
    st.subheader("Insights")
    components.html(
        """
        <ul>
        <li>Would be open to social good campaign to boost sales, not willing to put in a lot of time/$ due to opportunity costs</li>
        <li>Reducing transport costs can come alongside sourcing more wood locally; production requirements aren't met locally though,
        Currently easier to source production materials both domestically and internationally, at the cost of environment</li>
        <li>The market for fast/cheap/easy products is a lot larger than the market for sustainable/locally produced -> public demand 
        for sustainable needs to be greater There is demand for sustainable production in higher-end markets; 
        the average consumer still isn't paying the sustainability premium</li>
        <li>Against additional regulations; ESG certification should comply with existing certifications</li>
        </ul>
        """,
        height = 1000
    )
  
st.sidebar.markdown("## Similarities & Differences")

page3 = st.sidebar.selectbox(
      "Select Stakeholder",
        ["Foresters","Scientists","Regulators"],key="40"
    )
page4 = st.sidebar.selectbox(
      "Select Stakeholder 2",
        ["Regulators","Scientists","Foresters"],key="23"
    )
if not st.sidebar.checkbox("Hide", True,key="2"):
  if page3=="Foresters" and page4=="Scientists":
    st.text(page4)
    st.subheader("Foresters & Scientists")
    img = "https://github.com/vishalvindyala/ICF/blob/main/venn%201.PNG?raw=true"
    st.image(img)
    st.subheader("Insights")
    components.html(
        """
        <h3>Foresters</h3>
        <ul>
        <li>Should be opt-in</li>
        <li>Problem with terminology that negatively perceive cutting</li>
        <li>ESG should have an emphasis on monetary social impacts</li>
        </ul>
        <h3> Similarities </h3>
        <ul>
        <li>there should be an emphasis on education and knowledge within the industry</li>
        <li>government should improve current regulations</li>
        <h3>Science Sector</h3>
        <ul>
        <li>ESG metrics are essential for analysis and should be required</li>
        <li>no problematic terminology noted</li>
        <li>maryland is ecologically diverse and is a major concern of ESG metrics</li>
        </ul>
        """,
        height =1000
    )

  elif page3 == "Scientists" and page4 == "Regulators" :
    st.subheader("Science & Regulators")
    img = "https://github.com/vishalvindyala/ICF/blob/main/venn2.PNG?raw=true"
    st.image(img)
    st.subheader("Insights")
    components.html(
        """
        <h3>Regulators</h3>
        <ul>
        <li>ESG metrics can bring forestry into a positive light.</li>
        <li>clear cutting, dirty chips, final harvest all problem terms that are known</li>
        <li>Corporate Responsibility should be used to hold groups accountable and enforce standards.</li>
        <li>Profit is a concern.</li>
        </ul>
        <h3> Similarities </h3>
        <ul>
        <li>Emphasis on education and knowledge of ESG</li>
        <h3>Science Sector</h3>
        <ul>
        <li>ESG metrics are essential for analysis and should be required</li>
        <li>no problematic terminology noted</li>
        <li>maryland is ecologically diverse and is a major concern of ESG metrics</li>
        </ul>
        """,
        height =1000
    )
  else:
    st.subheader("Regulators & Foresters")
    img = "https://github.com/vishalvindyala/ICF/blob/main/venn3.PNG?raw=true"
    st.image(img)
    st.subheader("Insights")
    components.html(
        """
        <h3>Regulators</h3>
        <ul>
        <li>ESG metrics can bring forestry into a positive light.</li>
        <li>clear cutting, dirty chips, final harvest all problem terms that are known</li>
        <li>Corporate Responsibility should be used to hold groups accountable and enforce standards.</li>
        <li>Profit is a concern.</li>
        </ul>
        <h3> Similarities </h3>
        <ul>
        <li>knowledge of public and stakeholders will be invaluable</li>
        <li>problems with definitions that negatively perceive forestry</li>
        <li>profit is a main concern</li>

        <h3>Foresters</h3>
        <ul>
        <li>Should be opt-in</li>
        <li>Problem with terminology that negatively perceive cutting</li>
        <li>ESG should have an emphasis on monetary social impacts</li>
        </ul>
        """,
        height =1000
    )

   
  