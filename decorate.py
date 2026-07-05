import os

readme_path = r"C:\Users\ishan\Documents\Projects\Awesome-Few-Shot-Prompting\README.md"
with open(readme_path, "r", encoding="utf-8") as f:
    content = f.read()

# Add banner at the top
if "<div align=\"center\">" not in content[:200]:
    banner_html = "<div align=\"center\">\n  <img src=\"assets/banner.svg\" alt=\"Banner\" width=\"800\" />\n</div>\n\n"
    content = banner_html + content

# Add emojis to headers
replacements = {
    "## Few-Shot Prompting in AI: History, Progression, Variants, & Applications": "## 🧠 Few-Shot Prompting in AI: History, Progression, Variants, & Applications 🚀",
    "## 1. The Macro Chronological Evolution": "## ⏳ 1. The Macro Chronological Evolution",
    "## 2. Core Functional & Formatting Variants": "## 🛠️ 2. Core Functional & Formatting Variants",
    "## 3. The In-Context Activation & Attention Matrix": "## 🔮 3. The In-Context Activation & Attention Matrix",
    "## 4. Production Engineering Challenges & Mitigations": "## 🚧 4. Production Engineering Challenges & Mitigations",
    "## 5. Frontier Real-World AI Applications": "## 🌍 5. Frontier Real-World AI Applications",
    "## References": "## 📚 References",
}

for old, new in replacements.items():
    content = content.replace(old, new)

with open(readme_path, "w", encoding="utf-8") as f:
    f.write(content)
