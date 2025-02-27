# Create a new Document for the research task
doc = Document()

# Title for the Research Task
doc.add_heading('Independent Research Task: Understanding IT Legislation', 0)

# Objective
doc.add_heading('Objective:', level=1)
doc.add_paragraph(
    "To research and understand the importance, key provisions, and impact of various IT-related legislations."
)

# Materials Needed
doc.add_heading('Materials Needed:', level=1)
doc.add_paragraph(
    "- Access to the internet for research.\n"
    "- Writing materials for taking notes.\n"
    "- Presentation software for creating a summary of their findings (optional)."
)

# Instructions
doc.add_heading('Instructions:', level=1)

# Introduction
doc.add_heading('1. Introduction (10 minutes):', level=2)
doc.add_paragraph(
    "Begin by reading the task sheet provided by the teacher, which outlines the goals and expectations "
    "for the research. Form into pairs or groups of three and divide the legislation topics among group "
    "members to ensure coverage of all areas."
)

# Research Phase
doc.add_heading('2. Research Phase (60 minutes):', level=2)
doc.add_paragraph(
    "Each student or subgroup will focus on one piece of legislation, conducting detailed research to answer "
    "the following questions:"
)
doc.add_paragraph(
    "- What is the purpose of the legislation?\n"
    "- What are the key provisions or rules within the legislation?\n"
    "- How does this legislation impact individuals and businesses?\n"
    "- Find a real-world case where this legislation was applied. What happened, and what was the outcome?\n"
    "- How does this legislation affect the IT industry specifically?\n"
    "- Are there any recent updates or amendments to the legislation?"
)
doc.add_paragraph(
    "Legislations to Research:\n"
    "- Computer Misuse Act\n"
    "- Data Protection Act (and any updates like GDPR if applicable)\n"
    "- Consumer Rights Act\n"
    "- Health and Safety (Display Screen Equipment) Regulations\n"
    "- Equality Act (with a focus on IT accessibility provisions)"
)

# Analysis and Synthesis
doc.add_heading('3. Analysis and Synthesis (20 minutes):', level=2)
doc.add_paragraph(
    "After completing their research, students should analyze their findings and synthesize the information into "
    "key points. Prepare a brief presentation or report that summarizes the legislation, its impact, and case studies."
)

# Preparation for Presentation
doc.add_heading('4. Preparation for Presentation (10 minutes):', level=2)
doc.add_paragraph(
    "Use this time to prepare a short presentation. This could be a slide deck, a written report, or any other "
    "creative means to convey the information. Make sure to practice presenting the key points clearly and concisely."
)

# Deliverables
doc.add_heading('Deliverables:', level=1)
doc.add_paragraph(
    "- A set of notes or a summary document of the findings for each piece of legislation.\n"
    "- A prepared presentation or report that can be shared with the class upon the teacher's return."
)

# Assessment Criteria
doc.add_heading('Assessment Criteria:', level=1)
doc.add_paragraph(
    "- The depth and accuracy of the research conducted.\n"
    "- Clarity and organization of the presented information.\n"
    "- Understanding of the legislation's implications and real-world applications."
)

# Note to Students
doc.add_heading('Note to Students:', level=1)
doc.add_paragraph(
    "- The teacher will review the research and presentations upon return, so be sure to cover the topics comprehensively.\n"
    "- Cite any sources you use for your research to avoid plagiarism.\n"
    "- This task is designed to be collaborative; however, each student is responsible for their own part of the research."
)

# Save the document
file_path = '/Users/cjackson/Documents/1. Teacher Work/23:24 Prendergast/Year 12/BTEC IT/Research_Task_Y12.docx'
doc.save(file_path)
