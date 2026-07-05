import os

readme_path = r"C:\Users\ishan\Documents\Projects\Awesome-Few-Shot-Prompting\README.md"
with open(readme_path, "r", encoding="utf-8") as f:
    content = f.read()

badges_left = '<a href="https://github.com/ishandutta2007/Awesome-Awesome-Awesome"><img src="https://img.shields.io/badge/Awesome-%E2%9C%94-blueviolet?style=flat-square&logo=github" alt="Awesome"/></a><a href="https://discord.gg/jc4xtF58Ve"><img src="https://img.shields.io/badge/Discord-5865F2?style=for-the-badge&logo=discord&logoColor=white" alt="Discord" /></a>'

seo_text = """
<div align="center">
  <p><strong>SEO Keywords:</strong> <em>Few-Shot Prompting, In-Context Learning, LLM, VLM, Prompt Engineering, Zero-Shot, Chain-of-Thought, CoT, Generative AI, Artificial Intelligence</em></p>
</div>
"""

# Insert badges and SEO after the banner or at the top if banner not found
if "</div>\n\n" in content[:300]:
    content = content.replace("</div>\n\n", "</div>\n\n<div align=\"center\">\n  " + badges_left + "\n</div>\n" + seo_text + "\n", 1)
else:
    content = "<div align=\"center\">\n  " + badges_left + "\n</div>\n" + seo_text + "\n" + content

with open(readme_path, "w", encoding="utf-8") as f:
    f.write(content)
