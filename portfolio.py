import streamlit as st

# Set page title
st.set_page_config(page_title='My Personal Portfolio')

# Create header section
st.title('Personal Portfolio')
st.write('Welcome to my personal portfolio. This is a collection of my personal projects, skills, and experiences.')

# Create section for personal details and coding profile links
st.header('Personal Details and Coding Profile Links')
st.write('Here are my personal details and links to my coding profile:')

personal_details = {
    'Name': 'Rohan Godha',
    'Phone': '+91 8824024440',
    'Email': 'rohangodha.official@gmail.com',
    'LinkedIn': 'LinkedIn',
    'GitHub': 'GitHub',
    'LeetCode': 'LeetCode',
    'GeeksForGeeks': 'GeeksForGeeks'
}

# Display personal details in a table
for key, value in personal_details.items():
    st.write(f'**{key}:** {value}')

# Create section for about me
st.header('About Me')
st.write('I am an aspiring undergraduate professional with exceptional organizational and analytical skills. I thrive in dynamic environments and excel in Web, Graphics, Research, and Data Analysis. I am eager to collaborate with product leaders and provide meaningful insights to improve overall performance.')

# Create section for education
st.header('Education')
st.write('Here is my educational background:')

education = [
    {
        'degree': 'Bachelor of Computer Science and Engineering',
        'university': 'Chandigarh University Mohali, India',
        'duration': 'Aug. 2020 – May 2024',
        'details': 'CGPA: 8.64 (Sem I-IV)'
    },
    {
        'degree': 'XII',
        'university': 'Saint Xavier’s Sr.Sec School Jaipur, India',
        'duration': '2018-2020',
        'details': 'PCM: 81.2%'
    },
    {
        'degree': 'X',
        'university': 'Saint Xavier’s Sr.Sec School Jaipur, India',
        'duration': '2008-2018',
        'details': 'Percentage: 84.4%'
    }
]

# Display education in a table
for item in education:
    st.write(f"**{item['degree']}** from {item['university']} ({item['duration']})")
    st.write(item['details'])

# Create section for technical skills
st.header('Technical Skills')
st.write('Here are my technical skills:')

technical_skills = [
    'Languages: C, C++, Java, R, Python, HTML, CSS, ES6, JavaScript, MySQL, YAML',
    'Frameworks: Svelte.js, MongoDB, Firebase, WordPress, Tailwind, Bootstrap',
    'Tools: Linux, GitHub, GCP, AWS, VS Code, PyCharm, Netbeans, Tableau, MsOffice',
    'Libraries: Pandas, NumPy, Matplotlib, Streamlit',
    'UI/UX and Media Tools: Canva, Figma, AdobeXD, Audacity, Filmora, Kinemaster, Filmaker'
]

# Display skills in a bulleted list
for skill in technical_skills:
    st.write('- ' + skill)

# Create section for work experience
st.header('Work Experience')
st.write('Here is my work experience:')

work_experience = [
    {
        'position': 'Full Stack Web Developer',
        'company': 'Alhansat Technologies',
        'duration': 'Dec 2022 - Present',
        'details': 'Winter Internship'
    }
]
# Create section for community experience
st.header('Community Experience')
st.write('Here is my community experience:')

community_experience = [
    {
        'role': 'Founder University Chapter Lead',
        'organization': 'Hack2skill The Mountains',
        'duration': 'Aug 2022 – Dec 2022'
    },
    {
        'role': 'Founder Vice Chair',
        'organization': 'IEEE Computational Intelligence Society IEEE Chandigarh University Student Branch',
        'duration': 'Feb 2022 – June 2022'
    },
    {
        'role': 'Founder Treasurer',
        'organization': 'IEEE Robotics and Automation Society IEEE Chandigarh University Student Branch',
        'duration': 'Jan 2022 – Feb 2022'
    },
    {
        'role': 'Planning and Development Sub-Lead',
        'organization': 'Events CSE Chandigarh University',
        'duration': 'Jan 2022 – Aug 2022'
    },
    {
        'role': 'Promotion Manager and Coordinator',
        'organization': 'Tech Invent Chandigarh University',
        'duration': 'July 2021 – Sept 2021'
    }
]

# Display community experience in a table
for experience in community_experience:
    st.write(f"**{experience['role']}** at {experience['organization']} ({experience['duration']})")
    st.write("")

# Create section for research papers
st.header('Research Papers')
st.write('Here are some of my research papers:')

research_papers = [
    'Svelte.js: The Most Loved Framework Today',
    '6G: 6G Network Architecture, 6G Communication Essential Technologies, and 6G Use Cases and Applications',
    'IoT and Blockchain Integration for Secure Data Management',
    'The Transfer Learning Power in chatGPT: A Comprehensive Study',
    'UAVs - Pioneering the Future of Remote Sensing and Precision Agriculture',
    'From User Testing to Personalization - A Comprehensive Guide to Mobile App Design',
    'Augmented Reality(AR) and Mixed Reality (MR) - Applications in education, entertainment and industry',
    'An extensive comparative analysis of Chatbot technologies: ChatGPT, Google BARD, and Microsoft Bing',
    'Developing algorithms for efficient and scalable Machine Learning'
]

# Display research papers in a bulleted list
for paper in research_papers:
    st.write('- ' + paper)

# Create section for patents
st.header('Patents')
st.write('Here are some of my patents:')

patents = [
    'Automated Display Lid Closing System For Laptops (ID: 202211055162)',
    'Explosive Detection Device (ID: 202311014046)',
    'Smart User-Interactive System For Laptop (ID: 202211055159)'
]

# Display patents in a bulleted list
for patent in patents:
    st.write('- ' + patent)
