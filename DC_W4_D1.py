first_name = input("Edit your first name : ");
last_name = input("Edit your last name : ");

pro_experience = input("Edit your latest professional experience : ");
programming_skills = input("Edit your latest programming skills : ");
software_skills = input("Edit your latest software skills : ");
education = input("Edit your degree : ");

str_HTML = """
<!DOCTYPE html>
<html>
<head>
  <title></title>
</head>
<body>

  <br>
  <h1>Resume</h1>
  <h2>"""+ first_name + last_name + """</h2>
  <hr />
  <br>
  <p><strong>Professional Experience</strong></p>
  <ul>
    <li>""" + pro_experience + """</li>
    <li></li>
    <li></li>
    <li></li>
  </ul>
  <p><strong>Programming Skills</strong></p>
  <ul>
    <li>""" + programming_skills + """</li>
  </ul>
  <p><strong>Software</strong></p>
  <ul>
    <li>""" + software_skills + """</li>
  </ul>
  <p><strong>Education</strong></p>
  <ul>

      <li>Developers Institute : Coding Bootcamp FullStack Development in Python</li>
      <li>""" + education + """</li>
      <li></li> 
      <li></li>
      <li></li>
 </ul>
  <p><strong>Extracurriculars</strong></p>
  <ul>
    <li>Readings</li>
    <li>Python, R in Data Science</li>
    <li>Soccer</li>
  </ul>
</div>
<hr />
"""

Html_file= open("/home/davzaf/Documents/Dev_Institute_Python_Course/Python/Week 4/DC_W4_D1.html","w")
Html_file.write(str_HTML)
Html_file.close()