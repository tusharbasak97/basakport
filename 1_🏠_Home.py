from pathlib import Path
import streamlit as st
# import streamlit_authenticator as stauth

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "resume.pdf"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Tushar Basak | Cybersecurity Analyst"
PAGE_ICON = ":shield:"
NAME = "Tushar Basak"
DESCRIPTION = "Embark on a secure digital journey with Tushar Basak, a Cybersecurity Analyst dedicated to safeguarding against cyber threats. Expert in vulnerability assessment, risk management, and resilient defense strategies."
EMAIL = "tushar.basak@yahoo.com"
SOCIAL_MEDIA = {
    "LinkedIn": "https://www.linkedin.com/in/tusharbasak97/",
    "GitHub": "https://github.com/tusharbasak97",
    "Twitter": "https://twitter.com/tusharbasak97",
}
PROJECTS = {
    "🛡️ Automated Threat Intelligence Platform": "https://github.com/tusharbasak97/threat-intel-platform",
    "🔍 Network Intrusion Detection System": "https://github.com/tusharbasak97/custom-ids",
    "📊 Security Compliance Checker Tool": "https://github.com/tusharbasak97/compliance-checker",
    "🎣 Phishing Email Detector": "https://github.com/tusharbasak97/phish-detector",
}

# --- SEO OPTIMIZATION ---
KEYWORDS = ["Tushar Basak", "Cybersecurity Analyst", "cyber threats", "vulnerability assessment", "risk management",
            "defense strategies", "cybersecurity insights", "cybersecurity solutions"]


st.set_page_config(page_title="Tushar Basak | Cybersecurity Analyst", page_icon=":shield:")

# --- LOAD CSS & PDF ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()

# --- PAGE LAYOUT ---
def centered_content():
    cont = st.container()
    cont.title(NAME)
    cont.write("+91 8299312126 ⋄ Delhi, India")
    # --- SOCIAL LINKS ---
    cols = cont.columns(len(SOCIAL_MEDIA))
    for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
        cols[index].write(f"[{platform}]({link})")
    cont.download_button(
            label=" 📄 Download Resume",
            data=PDFbyte,
            file_name=resume_file.name,
            mime="application/octet-stream",
        )
centered_content()
# --- ABOUT ME ---
st.write('\n')
st.subheader("OBJECTIVE", divider='rainbow')
st.markdown(
    """
    <p style='text-align: justify;'>
    Technically proficient, detail-oriented, and proactive Cybersecurity Analyst with a robust background in network security and threat detection. Experienced in vulnerability assessment, incident response, and security policy implementation. Skilled in using various security tools and technologies to protect organizational assets from cyber threats. Adept at analyzing complex security issues, implementing effective solutions, and collaborating with cross-functional teams to enhance overall security posture. Committed to staying current with emerging threats and security trends. Bilingual in English and Japanese, with strong communication skills and a keen ability to explain technical concepts to non-technical stakeholders.
    </p>
    """,
    unsafe_allow_html=True
)

# Expertise areas
st.write(
    """
    - **Network Security** | **Threat Detection & Response** | **Vulnerability Assessment** | **Incident Handling** | **Security Policy Implementation** | **Log Analysis** | **Penetration Testing**
    """
)

# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("Experience & Qualifications", divider='rainbow')
st.write(
    """
- ✔️ 1+ Years experience in cybersecurity and network defense
- ✔️ Strong hands-on experience with SIEM tools, IDS/IPS, and firewall management
- ✔️ Proficient in scripting languages such as Python for automation and analysis
- ✔️ Excellent problem-solving skills and ability to work under pressure
- ✔️ Certified Information Systems Security Professional (CISSP)
"""
)

# --- SKILLS ---
st.write('\n')
st.subheader("Technical Skills", divider='rainbow')
st.write(
    """
- 🛡️ Security Tools: Splunk, ELK Stack, Nessus, Wireshark, Metasploit
- 💻 Programming: Python, Bash scripting, PowerShell
- 🌐 Networking: TCP/IP, VPNs, Firewalls, Routers/Switches
- 🔐 Compliance: NIST, ISO 27001, HIPAA, PCI DSS
- 🖥️ Operating Systems: Windows, Linux, macOS
"""
)

# --- WORK HISTORY ---
st.write('\n')
st.subheader("Work History", divider='rainbow')

# --- JOB 1
st.write("🚧", "**Cybersecurity Analyst | Cywarden Global Services**")
st.write("09/2024 - Present")
st.write(
    """
- ► Led a team of 3 analysts in implementing a new SIEM solution, reducing incident response time by 40%
- ► Conducted regular vulnerability assessments and penetration tests, identifying and mitigating 50+ critical vulnerabilities
- ► Developed and maintained security policies and procedures, ensuring compliance with industry standards and regulations
"""
)

# --- JOB 2
st.write('\n')
st.write("🚧", "**Cybersecurity Trainee | Tata Strive**")
st.write("05/2024 - 09/2024")
st.write(
    """
- ► Assisted in ethical hacking and penetration testing projects, learning tools such as Metasploit, Nmap, and Wireshark.
- ► Supported the team in conducting regular vulnerability scans and preparing reports on security improvements.
- ► Gained experience in real-world incident response and disaster recovery planning.
- ► Monitored network traffic using IDS/IPS tools, detecting and responding to potential security incidents
- ► Performed log analysis and correlation, identifying patterns of suspicious activity and reducing false positives by 25%
- ► Assisted in the development of an incident response plan, improving the organization's ability to handle security breaches effectively.
"""
)

# --- JOB 3
st.write('\n')
st.write("🔒", "[**Intern Security Researcher | Voltsec.io - Cyber Security PtaaS**](https://www.voltsec-io.com/teamPortfolio/tushar-basak)")
st.write("03/2024 - 06/2024")
st.write(
    """
- ► Conducted daily security monitoring and analysis of various security tools and logs
- ► Participated in vulnerability scans and assisted in patch management processes
- ► Contributed to the creation of security awareness training materials for employees
"""
)

st.write('\n')
st.subheader("Projects & Accomplishments", divider='rainbow')
for project, link in PROJECTS.items():
    st.write(f"[{project}]({link})")


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
top:190px;
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