
CAREER_LIST = [
    "Software Developer",
    "Data Scientist",
    "Web Developer",
    "UX/UI Designer",
    "Digital Marketing Manager",
    "Product Manager",
    "Graphic Designer",
    "Content Writer",
    "Business Analyst",
    "Financial Analyst",
    "Registered Nurse",
    "Teacher",
    "Mechanical Engineer",
    "Civil Engineer",
    "Accountant",
    "Human Resources Manager",
    "Sales Manager",
    "Marketing Analyst",
    "Project Manager",
    "Data Analyst",
    "Cybersecurity Analyst",
    "Mobile App Developer",
    "DevOps Engineer",
    "Cloud Architect",
    "Database Administrator",
    "Network Engineer",
    "Social Media Manager",
    "Video Editor",
    "Interior Designer",
    "Research Scientist"
]

# Skills database
SKILLS_LIST = {
    'Technical': [
        'Programming', 'Data Analysis', 'Web Development', 'Mobile Development',
        'Database Management', 'Cloud Computing', 'Cybersecurity', 'DevOps',
        'Machine Learning', 'Network Administration', 'System Architecture'
    ],
    'Creative': [
        'Graphic Design', 'Video Editing', 'UI/UX Design', 'Content Writing',
        'Photography', 'Animation', '3D Modeling', 'Creative Writing'
    ],
    'Business': [
        'Project Management', 'Marketing', 'Sales', 'Financial Analysis',
        'Business Strategy', 'Leadership', 'Public Speaking', 'Negotiation'
    ],
    'Healthcare': [
        'Patient Care', 'Medical Knowledge', 'Healthcare Management',
        'Clinical Skills', 'Medical Research'
    ],
    'Engineering': [
        'CAD Design', 'Engineering Analysis', 'Quality Control',
        'Manufacturing', 'Technical Documentation'
    ]
}

# Career requirements with detailed information
CAREER_REQUIREMENTS = {
    "Software Developer": {
        "required_skills": ['Programming', 'Problem Solving', 'Data Structures', 'Git', 'Debugging'],
        "interests": ['Technology & Innovation', 'Problem Solving'],
        "education": ['Bachelor\'s Degree', 'Master\'s Degree'],
        "work_style": ['Remote', 'Hybrid', 'Office'],
        "description": "Design, develop, and maintain software applications and systems.",
        "salary_range": "$60,000 - $180,000",
        "job_growth": "+22% (Much faster than average)",
        "learning_resources": [
            {"name": "CS50 - Harvard", "url": "https://cs50.harvard.edu", "type": "Course"},
            {"name": "FreeCodeCamp", "url": "https://freecodecamp.org", "type": "Platform"},
            {"name": "The Odin Project", "url": "https://theodinproject.com", "type": "Curriculum"}
        ]
    },
    "Data Scientist": {
        "required_skills": ['Python', 'Statistics', 'Machine Learning', 'Data Visualization', 'SQL'],
        "interests": ['Technology & Innovation', 'Science & Research', 'Analytics'],
        "education": ['Bachelor\'s Degree', 'Master\'s Degree', 'PhD'],
        "work_style": ['Remote', 'Hybrid', 'Office'],
        "description": "Analyze complex data to help organizations make better decisions.",
        "salary_range": "$70,000 - $200,000",
        "job_growth": "+36% (Much faster than average)",
        "learning_resources": [
            {"name": "Kaggle Learn", "url": "https://kaggle.com/learn", "type": "Platform"},
            {"name": "DataCamp", "url": "https://datacamp.com", "type": "Course"},
        ]
    },
    "UX/UI Designer": {
        "required_skills": ['UI/UX Design', 'Prototyping', 'User Research', 'Figma', 'Adobe XD'],
        "interests": ['Arts & Design', 'Technology & Innovation', 'Psychology'],
        "education": ['Bachelor\'s Degree', 'Associate Degree', 'Bootcamp'],
        "work_style": ['Remote', 'Hybrid', 'Office'],
        "description": "Create intuitive and engaging user experiences for digital products.",
        "salary_range": "$55,000 - $140,000",
        "job_growth": "+16% (Much faster than average)",
        "learning_resources": [
            {"name": "Google UX Design Certificate", "url": "https://grow.google/uxdesign", "type": "Certificate"},
            {"name": "Interaction Design Foundation", "url": "https://interaction-design.org", "type": "Platform"},
        ]
    },
    "Web Developer": {
        "required_skills": ['HTML/CSS', 'JavaScript', 'React', 'Web Development', 'Git'],
        "interests": ['Technology & Innovation', 'Creative Problem Solving'],
        "education": ['Bachelor\'s Degree', 'Associate Degree', 'Bootcamp', 'Self-taught'],
        "work_style": ['Remote', 'Hybrid', 'Office'],
        "description": "Build and maintain websites and web applications.",
        "salary_range": "$50,000 - $130,000",
        "job_growth": "+23% (Much faster than average)",
        "learning_resources": [
            {"name": "MDN Web Docs", "url": "https://developer.mozilla.org", "type": "Documentation"},
            {"name": "Frontend Masters", "url": "https://frontendmasters.com", "type": "Platform"},
        ]
    },
    "Digital Marketing Manager": {
        "required_skills": ['Marketing', 'SEO', 'Social Media', 'Analytics', 'Content Strategy'],
        "interests": ['Business & Entrepreneurship', 'Communication', 'Creativity'],
        "education": ['Bachelor\'s Degree'],
        "work_style": ['Remote', 'Hybrid', 'Office'],
        "description": "Plan and execute digital marketing campaigns across various channels.",
        "salary_range": "$55,000 - $120,000",
        "job_growth": "+10% (Faster than average)",
        "learning_resources": [
            {"name": "Google Digital Marketing", "url": "https://grow.google", "type": "Certificate"},
            {"name": "HubSpot Academy", "url": "https://academy.hubspot.com", "type": "Platform"},
        ]
    },
    "Product Manager": {
        "required_skills": ['Product Strategy', 'Agile', 'User Research', 'Data Analysis', 'Communication'],
        "interests": ['Business & Entrepreneurship', 'Technology & Innovation', 'Problem Solving'],
        "education": ['Bachelor\'s Degree', 'Master\'s Degree', 'MBA'],
        "work_style": ['Hybrid', 'Office'],
        "description": "Guide product development from conception to launch.",
        "salary_range": "$70,000 - $180,000",
        "job_growth": "+14% (Faster than average)",
        "learning_resources": [
            {"name": "Product School", "url": "https://productschool.com", "type": "Platform"},
            {"name": "Inspired by Marty Cagan", "url": "#", "type": "Book"},
        ]
    },
    "Graphic Designer": {
        "required_skills": ['Graphic Design', 'Adobe Creative Suite', 'Typography', 'Color Theory'],
        "interests": ['Arts & Design', 'Creativity', 'Visual Communication'],
        "education": ['Bachelor\'s Degree', 'Associate Degree'],
        "work_style": ['Remote', 'Hybrid', 'Office', 'Freelance'],
        "description": "Create visual concepts to communicate ideas.",
        "salary_range": "$35,000 - $85,000",
        "job_growth": "+3% (As fast as average)",
        "learning_resources": [
            {"name": "Skillshare Design Courses", "url": "https://skillshare.com", "type": "Platform"},
            {"name": "Adobe Tutorials", "url": "https://helpx.adobe.com", "type": "Tutorial"},
        ]
    },
    "Data Analyst": {
        "required_skills": ['SQL', 'Excel', 'Data Visualization', 'Statistics', 'Python'],
        "interests": ['Analytics', 'Business & Entrepreneurship', 'Problem Solving'],
        "education": ['Bachelor\'s Degree', 'Associate Degree'],
        "work_style": ['Remote', 'Hybrid', 'Office'],
        "description": "Collect and analyze data to help organizations make decisions.",
        "salary_range": "$50,000 - $110,000",
        "job_growth": "+25% (Much faster than average)",
        "learning_resources": [
            {"name": "Mode Analytics", "url": "https://mode.com/sql-tutorial", "type": "Tutorial"},
            {"name": "Tableau Public", "url": "https://public.tableau.com", "type": "Platform"},
        ]
    },
    "Cybersecurity Analyst": {
        "required_skills": ['Network Security', 'Ethical Hacking', 'Risk Assessment', 'Cybersecurity'],
        "interests": ['Technology & Innovation', 'Problem Solving', 'Security'],
        "education": ['Bachelor\'s Degree', 'Professional Certification'],
        "work_style": ['Office', 'Hybrid'],
        "description": "Protect networks and systems from security breaches.",
        "salary_range": "$60,000 - $150,000",
        "job_growth": "+35% (Much faster than average)",
        "learning_resources": [
            {"name": "Cybrary", "url": "https://cybrary.it", "type": "Platform"},
            {"name": "TryHackMe", "url": "https://tryhackme.com", "type": "Practice"},
        ]
    },
    "Content Writer": {
        "required_skills": ['Content Writing', 'SEO', 'Research', 'Grammar', 'Storytelling'],
        "interests": ['Media & Communications', 'Creativity', 'Writing'],
        "education": ['Bachelor\'s Degree', 'Associate Degree'],
        "work_style": ['Remote', 'Freelance', 'Hybrid'],
        "description": "Create written content for websites, blogs, and marketing.",
        "salary_range": "$35,000 - $80,000",
        "job_growth": "+9% (As fast as average)",
        "learning_resources": [
            {"name": "Copyblogger", "url": "https://copyblogger.com", "type": "Blog"},
            {"name": "Content Marketing Institute", "url": "https://contentmarketinginstitute.com", "type": "Resource"},
        ]
    }
}

# Interest categories
INTERESTS_LIST = [
    'Technology & Innovation',
    'Science & Research',
    'Arts & Design',
    'Business & Entrepreneurship',
    'Healthcare & Medicine',
    'Education & Social Services',
    'Law & Public Policy',
    'Sports & Fitness',
    'Environment & Sustainability',
    'Media & Communications',
    'Engineering & Manufacturing',
    'Finance & Investment',
    'Analytics',
    'Problem Solving',
    'Creative Problem Solving'
]

# Education levels
EDUCATION_LEVELS = [
    'High School / GED',
    'Some College',
    'Associate Degree',
    'Bachelor\'s Degree',
    'Master\'s Degree',
    'Doctoral Degree / PhD',
    'Professional Certification',
    'Trade School / Vocational Training'
]

# Work styles
WORK_STYLES = [
    'Remote / Work from home',
    'Office / On-site',
    'Hybrid (mix of both)',
    'Field work / Travel',
    'Flexible / Freelance'
]