import streamlit as st

# Set page title
st.set_page_config(page_title='My Personal Portfolio')

# Create header section
st.title('Personal Portfolio')
st.write('Welcome to my personal portfolio. This is a collection of my personal projects, skills, and experiences.')

# Create section for personal details and coding profile links
st.header('Personal Details and Coding Profile Links')
st.write('Welcome to my profile! Here you will find my personal details and links to my coding portfolio:')

personal_details = {
    'Name': 'Rohan Godha',
    'Phone': '+91 8824024440',
    'Email': 'rohangodha.official@gmail.com',
    'LinkedIn': 'https://www.linkedin.com/in/rohan-godha-1257411b3/',
    'GitHub': 'https://github.com/RohanGodha',
    'LeetCode': 'https://leetcode.com/RohanGodha/',
    'GeeksForGeeks': 'https://auth.geeksforgeeks.org/user/yoyorodha/?utm_source=geeksforgeeks&utm_medium=my_profile&utm_campaign=auth_user'
}

# Display personal details in a table
for key, value in personal_details.items():
    st.write(f'**{key}:** {value}')

# Create section for about me
st.header('About Me')
st.write('I am an ambitious undergraduate professional with strong organizational and analytical skills. I excel in web development, graphics design, research, and data analysis. I thrive in dynamic environments and am eager to collaborate with product leaders to deliver valuable insights for enhancing overall performance.')

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
    'Frameworks: Svelte.js, Node.js, Streamlit, MongoDB, Firebase, WordPress, Tailwind, Bootstrap',
    'Tools: Linux, GitHub, GCP, AWS, VS Code, PyCharm, Netbeans, Tableau, MsOffice',
    'Libraries: Pandas, NumPy, Matplotlib',
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
        'duration': 'Dec 2022 – Present',
        'description': 'UI-UX-Figma, Svelte.js, Node.js and Firebase. Created and deployed Fincalsy, Resume Builder, and Image Editor.'
    },
    {
        'position': 'Graphic Designing Intern',
        'company': 'Hack The Mountains',
        'duration': 'Feb 2022 – Present',
        'description': 'Been the Organizer at their various events. Developing Graphics and Media for the International Level Events by the Company.'
    }
]

# Display work experience in a table
for job in work_experience:
    st.write(f"**{job['position']}** at {job['company']} ({job['duration']})")
    st.write(job['description'])

# Create section for certifications
st.header('Certifications')
st.write('Here are my certifications:')

certifications = [
    'Postman API Fundamental Student Expert: Postman',
    'Blockchain Training: Internshala',
    'Data Analytics Specialization: Google, Coursera',
    'The Fundamentals of Digital Marketing: Google',
    '30 Days of Google Cloud: Developer Students Club, Google',
    'Hacktoberfest 2020, 2021, 2022: Github, Digital Ocean, Open source'
    'Girl Script Summer Of Code'
]

# Display certifications in a bulleted list
for certification in certifications:
    st.write('- ' + certification)

# Create section for projects
st.header('Projects')
st.write('Here are some of my projects:')

projects = [
    {
        'name': 'Mandala',
        'description': 'Women Safety Platform',
        'technologies': 'Internet of Things, React, Node.js, Express, MongoDB',
        'duration': 'May 2022 – Present'
    },
    {
        'name': 'CVD Prediction in Humans',
        'description': 'Research on Cardiovascular Diseases',
        'technologies': 'Python, Machine Learning',
        'duration': 'April 2022'
    },
    {
        'name': 'Gesture-IT',
        'description': 'HandGesture Control Library using OpenCV',
        'technologies': 'Python, OpenCV, Machine Learning',
        'duration': '2022'
    },
    {
        'name': 'YouThoob',
        'description': 'Clone of YouTube',
        'technologies': 'HTML, CSS, JavaScript',
        'duration': 'July 2021'
    },
    {
        'name': 'Investigatory Project ICICI Bank',
        'description': 'GUI Portal for banking operations',
        'technologies': 'Java, Netbeans, MySQL',
        'duration': '2020'
    }
]

# Display projects in a table
for project in projects:
    st.write(f"**{project['name']}**")
    st.write(f"- Description: {project['description']}")
    st.write(f"- Technologies: {project['technologies']}")
    st.write(f"- Duration: {project['duration']}")
    st.write("")

# Create section for awards
st.header('Awards')
st.write('Here are some of my awards:')

awards = [
    'Finalist: Forti Hackathon',
    '2nd Runner Ups: Ideathon 2022 Hackathon',
    'Top 30 International: Technothon 2022 Hackathon, GCET'
]

# Display awards in a bulleted list
for award in awards:
    st.write('- ' + award)

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
