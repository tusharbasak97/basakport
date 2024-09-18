import streamlit as st

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Certificates of Tushar Basak"
PAGE_ICON = ":trophy:"
LAYOUT="centered"
NAME = "Tushar Basak"
DESCRIPTION = "Embark on a secure digital journey with Tushar Basak, a Cybersecurity Analyst dedicated to safeguarding against cyber threats. Expert in vulnerability assessment, risk management, and resilient defense strategies."
EMAIL = "tushar.basak@yahoo.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/tusharbasak97/",
    "GitHub": "https://github.com/tusharbasak97",
    "Twitter": "https://twitter.com/tusharbasak97",
}
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)
st.title("My Certificates")



# Use Local CSS File
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("styles/general.css")

# --- Footer ---
ft = """
<style>
a:link , a:visited{
color: #BFBFBF;  /* theme's text color hex code at 75 percent brightness*/
background-color: transparent;
text-decoration: none;
}

a:hover,  a:active {
color: #0283C3; /* theme's primary color*/
background-color: transparent;
text-decoration: underline;
}

#page-container {
  position: relative;
  min-height: 10vh;
}

footer{
    visibility:hidden;
}

.footer {
position: relative;
left: 0;
top:230px;
bottom: 0;
width: 100%;
background-color: transparent;
color: #808080; /* theme's text color hex code at 50 percent brightness*/
text-align: center; /* you can replace 'left' with 'center' or 'right' if you want*/
}
</style>

<div id="page-container">

<div class="footer">
<p style='font-size: 0.875em;'>Made using <a style='display: inline; text-align: left;' href="https://streamlit.io/" target="_blank">Streamlit</a><br 'style= top:3px;'>
with <img src="https://em-content.zobj.net/source/skype/289/red-heart_2764-fe0f.png" alt="heart" height= "10"/> by <a style='display: inline; text-align: left;' href="https://www.linkedin.com/in/tusharbasak97/" target="_blank">Tushar Basak</a></p>
</div>

</div>
"""
st.write(ft, unsafe_allow_html=True)