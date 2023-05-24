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
