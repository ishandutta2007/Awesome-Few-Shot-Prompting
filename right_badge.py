import os

readme_path = r"C:\Users\ishan\Documents\Projects\Awesome-Few-Shot-Prompting\README.md"
with open(readme_path, "r", encoding="utf-8") as f:
    content = f.read()

badge_right = '<a href="https://github.com/ishandutta2007"><img alt="GitHub followers" src="https://img.shields.io/github/followers/ishandutta2007?label=Follow" /></a>'

# Find the end of the discord badge and insert the new badge right after it
old_discord = 'alt="Discord" /></a>'
new_discord_with_right = old_discord + '\n  ' + badge_right

content = content.replace(old_discord, new_discord_with_right)

with open(readme_path, "w", encoding="utf-8") as f:
    f.write(content)
