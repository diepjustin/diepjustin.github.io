import re

with open('index.html', 'r') as f:
    content = f.read()

# 1. Update resume link
content = content.replace('Diep%20Justin%20Resume%20April%202026.pdf', 'justin-diep-resume.pdf')

# 2. Remove Leo XIV article
leo_article = """            <div class="article-card">
                <a href="https://journalstar.com/life-entertainment/local/faith-values/article_150c4da3-aa45-43af-81c2-d069619046a9.html" target="_blank">
                    <img src="https://bloximages.chicago2.vip.townnews.com/journalstar.com/content/tncms/assets/v3/editorial/1/50/150c4da3-aa45-43af-81c2-d069619046a9/681d1766be8b9.preview.jpg?crop=1763%2C926%2C0%2C124&amp;resize=1200%2C630&amp;order=crop%2Cresize" alt="Article image">
                </a>
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.2rem;"><span class="tag" style="margin-bottom: 0;">Lincoln Journal Star</span><span style="font-size: 0.8rem; color: var(--text-color); opacity: 0.6;">May 8, 2025</span></div>
                <h3><a href="https://journalstar.com/life-entertainment/local/faith-values/article_150c4da3-aa45-43af-81c2-d069619046a9.html" target="_blank">Nebraskans react to election of Leo XIV, 1st American pope</a></h3>
            </div>"""
content = content.replace(leo_article, "")

# 3. Remove Christmas shopping article
xmas_article = """            <div class="article-card">
                <a href="https://journalstar.com/news/local/article_13ff1f98-af58-11ef-86fd-3bb64b0de42d.html" target="_blank">
                    <img src="https://bloximages.chicago2.vip.townnews.com/journalstar.com/content/tncms/assets/v3/editorial/1/3f/13ff1f98-af58-11ef-86fd-3bb64b0de42d/674b7e2399e9b.preview.jpg?crop=1782%2C936%2C0%2C113&amp;resize=1200%2C630&amp;order=crop%2Cresize" alt="Article image">
                </a>
                <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.2rem;"><span class="tag" style="margin-bottom: 0;">Lincoln Journal Star</span><span style="font-size: 0.8rem; color: var(--text-color); opacity: 0.6;">Nov. 30, 2024</span></div>
                <h3><a href="https://journalstar.com/news/local/article_13ff1f98-af58-11ef-86fd-3bb64b0de42d.html" target="_blank">Lincoln businesses, shoppers feel pressure with short season</a></h3>
            </div>"""
content = content.replace(xmas_article, "")

# 4. Clean up blank lines left behind (optional but good)
content = re.sub(r'\n\s*\n\s*\n', '\n\n', content)

# 5. Extract awards from bio
content = content.replace(" I've been named Rookie of the Semester (fall 2023) and Greatest Contributor in both spring and fall 2025 by The Daily Nebraskan newsroom.", "")
content = content.replace("where I collaborated on comprehensive coverage of an ICE raid at an Omaha meatpacking plant and was ranked among the top-viewed authors across Lee Enterprises' 77 daily newspapers;", "where I collaborated on comprehensive coverage of an ICE raid at an Omaha meatpacking plant;")
content = content.replace(", where I was named the 2023 Nebraska High School Journalist of the Year", "")

# 6. Insert new Awards section
awards_section = """
    <section id="awards" style="margin-top: 4rem;">
        <h2>Awards & Recognition</h2>
        <ul style="list-style-type: none; padding-left: 0; line-height: 1.8; color: var(--text-color); font-size: 1.05rem;">
            <li style="margin-bottom: 0.5rem;">🏆 <strong>Top-Viewed Author</strong> — Ranked among the top-viewed authors across Lee Enterprises' 77 daily newspapers (June 2025)</li>
            <li style="margin-bottom: 0.5rem;">🏆 <strong>Student Production Award</strong> — Heartland Region of the National Academy of Television Arts & Sciences (NATAS)</li>
            <li style="margin-bottom: 0.5rem;">🏆 <strong>Nebraska High School Journalist of the Year</strong> — 2023</li>
            <li style="margin-bottom: 0.5rem;">🏆 <strong>Greatest Contributor (Spring & Fall 2025)</strong> — The Daily Nebraskan</li>
            <li style="margin-bottom: 0.5rem;">🏆 <strong>Rookie of the Semester (Fall 2023)</strong> — The Daily Nebraskan</li>
        </ul>
    </section>
"""

# Insert before <section id="writing">
content = content.replace('    <section id="writing">', awards_section + '\n    <section id="writing">')

with open('index.html', 'w') as f:
    f.write(content)

print("Done")
