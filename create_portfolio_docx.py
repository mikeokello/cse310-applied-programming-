from pathlib import Path
from zipfile import ZipFile
from xml.sax.saxutils import escape

out_path = Path("c:/Users/user/OneDrive/Desktop/cse310-applied prog/hello-world/W01-Hello-World-Portfolio.docx")
paragraphs = [
    "CSE 310: Applied Programming",
    "Week 01 Software Portfolio Document",
    "",
    "Student Information",
    "Name: [Your Full Name]",
    "Course: CSE 310 - Applied Programming",
    "Assignment: W01 Hello World Module",
    "Date Submitted: September 1, 2026",
    "",
    "1. GitHub Repository",
    "I created a public GitHub repository for this project.",
    "",
    "GitHub Repository Link:",
    "https://github.com/your-username/hello-world",
    "",
    "Checklist:",
    "- [x] Public GitHub repository created",
    "- [x] Project folder contains the code files",
    "- [x] README.md is included at the root of the repository",
    "- [x] Code is visible and accessible to the public",
    "",
    "2. README File",
    "The README.md file was completed and placed in the root folder of the project.",
    "",
    "README Link:",
    "https://github.com/your-username/hello-world/blob/main/README.md",
    "",
    "Checklist:",
    "- [x] README.md is present at the root of the project",
    "- [x] The README includes a description of the software",
    "- [x] The README includes how to run the program",
    "- [x] The README includes the project output",
    "- [x] The README includes the language and environment used",
    "- [x] The README includes the video link and author information",
    "",
    "3. Video Demonstration",
    "I created a public video that includes my face, a demonstration of the program running, and a walkthrough of the code.",
    "",
    "Video Link:",
    "https://www.youtube.com/watch?v=your-video-id",
    "",
    "Checklist:",
    "- [x] My face is visible in the video",
    "- [x] The software is demonstrated running",
    "- [x] The code is explained and walked through",
    "- [x] The video is public or unlisted and accessible",
    "- [x] The video link is included in the README and submission document",
    "",
    "4. Project Summary",
    "This project is a simple JavaScript Hello World application created in Visual Studio Code using Node.js. The program prints \"Hello World\" to the console and demonstrates the basic workflow for creating, running, and sharing software in CSE 310.",
    "",
    "5. Program Description",
    "The Hello World program is the classic beginner software project used to confirm that the development environment is working correctly. It demonstrates how to write code, run a script, and verify output using the terminal.",
    "",
    "6. Code Walkthrough",
    "The program uses the following command in the JavaScript file:",
    "console.log(\"Hello World\");",
    "This statement writes the text \"Hello World\" to the console when the program runs.",
    "",
    "7. Time Spent",
    "I spent approximately 1 hour completing this assignment, including setup, coding, documentation, and video preparation.",
    "",
    "Hours Reported: 1",
    "",
    "8. Final Checklist",
    "- [x] I created a public GitHub repository",
    "- [x] My project folder contains the code and README.md",
    "- [x] I completed the README.md template correctly",
    "- [x] I created a public video with my face, demo, and code walkthrough",
    "- [x] I included the video link in the submission document",
    "- [x] I reported my time accurately",
    "- [x] I am ready to submit this assignment",
    "",
    "9. Submission Statement",
    "I confirm that this assignment was completed honestly and that all required components for the W01 Hello World module have been included.",
]

body_xml = "".join(
    f"<w:p><w:r><w:t>{escape(p)}</w:t></w:r></w:p>" if p else "<w:p/>"
    for p in paragraphs
)

document_xml = f'''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<w:document xmlns:w="http://schemas.openxmlformats.org/wordprocessingml/2006/main">
  <w:body>
    {body_xml}
    <w:sectPr>
      <w:pgSz w:w="12240" w:h="15840"/>
      <w:pgMar w:top="1440" w:right="1440" w:bottom="1440" w:left="1440" w:header="720" w:footer="720" w:gutter="0"/>
    </w:sectPr>
  </w:body>
</w:document>
'''

content_types = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Types xmlns="http://schemas.openxmlformats.org/package/2006/content-types">
  <Default Extension="rels" ContentType="application/vnd.openxmlformats-package.relationships+xml"/>
  <Default Extension="xml" ContentType="application/xml"/>
  <Override PartName="/word/document.xml" ContentType="application/vnd.openxmlformats-officedocument.wordprocessingml.document.main+xml"/>
  <Override PartName="/docProps/core.xml" ContentType="application/vnd.openxmlformats-package.core-properties+xml"/>
  <Override PartName="/docProps/app.xml" ContentType="application/vnd.openxmlformats-officedocument.extended-properties+xml"/>
</Types>
'''

rels = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Relationships xmlns="http://schemas.openxmlformats.org/package/2006/relationships">
  <Relationship Id="rId1" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/officeDocument" Target="word/document.xml"/>
  <Relationship Id="rId2" Type="http://schemas.openxmlformats.org/package/2006/relationships/metadata/core-properties" Target="docProps/core.xml"/>
  <Relationship Id="rId3" Type="http://schemas.openxmlformats.org/officeDocument/2006/relationships/extended-properties" Target="docProps/app.xml"/>
</Relationships>
'''

core = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<cp:coreProperties xmlns:cp="http://schemas.openxmlformats.org/package/2006/metadata/core-properties" xmlns:dc="http://purl.org/dc/elements/1.1/" xmlns:dcterms="http://purl.org/dc/terms/" xmlns:dcmitype="http://purl.org/dc/dcmitype/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance">
  <dc:title>CSE310 W01 Hello World Portfolio</dc:title>
  <dc:creator>Student</dc:creator>
  <cp:lastModifiedBy>Student</cp:lastModifiedBy>
  <dcterms:created xsi:type="dcterms:W3CDTF">2026-09-01T00:00:00Z</dcterms:created>
  <dcterms:modified xsi:type="dcterms:W3CDTF">2026-09-01T00:00:00Z</dcterms:modified>
</cp:coreProperties>
'''

app = '''<?xml version="1.0" encoding="UTF-8" standalone="yes"?>
<Properties xmlns="http://schemas.openxmlformats.org/officeDocument/2006/extended-properties" xmlns:vt="http://schemas.openxmlformats.org/officeDocument/2006/docPropsVTypes">
  <Application>Microsoft Office Word</Application>
</Properties>
'''

out_path.parent.mkdir(parents=True, exist_ok=True)
with ZipFile(out_path, "w") as zf:
    zf.writestr("[Content_Types].xml", content_types)
    zf.writestr("_rels/.rels", rels)
    zf.writestr("docProps/core.xml", core)
    zf.writestr("docProps/app.xml", app)
    zf.writestr("word/document.xml", document_xml)

print(f"Created: {out_path}")
