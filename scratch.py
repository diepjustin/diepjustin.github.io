import re

with open('index.html', 'r') as f:
    content = f.read()

# 1. Update CSS variables
css_vars = """
        :root {
            --bg-color: #fff;
            --text-color: #333;
            --heading-color: #111;
            --link-color: #0366d6;
            --border-color: #eee;
            --nav-bg: rgba(255, 255, 255, 0.95);
            --photo-bg: #f5f5f5;
            --btn-bg: #111;
            --btn-text: #fff;
        }
        .dark-mode {
            --bg-color: #121212;
            --text-color: #e0e0e0;
            --heading-color: #fff;
            --link-color: #58a6ff;
            --border-color: #333;
            --nav-bg: rgba(18, 18, 18, 0.95);
            --photo-bg: #1e1e1e;
            --btn-bg: #eee;
            --btn-text: #111;
        }
"""
content = re.sub(r'(<style>\s*)', r'\1' + css_vars, content)

# 2. Replace hardcoded colors with variables
content = re.sub(r'color:\s*#333;', 'color: var(--text-color);', content)
content = re.sub(r'background-color:\s*#fff;', 'background-color: var(--bg-color);', content)
content = re.sub(r'color:\s*#111;', 'color: var(--heading-color);', content)
content = re.sub(r'color:\s*#0366d6;', 'color: var(--link-color);', content)
content = re.sub(r'border-bottom:\s*1px solid #eee;', 'border-bottom: 1px solid var(--border-color);', content)
content = re.sub(r'background-color:\s*rgba\(255, 255, 255, 0.95\);', 'background-color: var(--nav-bg);', content)
content = re.sub(r'color:\s*#555;', 'color: var(--text-color); opacity: 0.8;', content)
content = re.sub(r'color:\s*#000;', 'color: var(--heading-color);', content)
content = re.sub(r'border:\s*1px solid #ccc;', 'border: 1px solid var(--border-color);', content)
content = re.sub(r'background-color:\s*#f9f9f9;', 'background-color: var(--photo-bg);', content)
content = re.sub(r'border:\s*1px solid #ddd;', 'border: 1px solid var(--border-color);', content)
content = re.sub(r'border:\s*1px solid #eee;', 'border: 1px solid var(--border-color);', content)
content = re.sub(r'color:\s*#777;', 'color: var(--text-color); opacity: 0.6;', content)
content = re.sub(r'background-color:\s*#f5f5f5;', 'background-color: var(--photo-bg);', content)
content = re.sub(r'border-top:\s*1px solid #eee;', 'border-top: 1px solid var(--border-color);', content)
content = re.sub(r'color:\s*#444;', 'color: var(--heading-color);', content)

# 3. Add Lightbox & Animations CSS
animations_css = """
        .article-card {
            display: flex;
            flex-direction: column;
            transition: transform 0.2s ease, box-shadow 0.2s ease;
            border-radius: 4px;
            padding-bottom: 1rem;
        }
        .article-card:hover {
            transform: translateY(-4px);
        }
        figure.photo-item img {
            width: 100%;
            height: auto;
            border-radius: 4px;
            border: 1px solid var(--border-color);
            object-fit: cover;
            margin-bottom: 0.5rem;
            background-color: var(--photo-bg);
            transition: transform 0.2s ease, box-shadow 0.2s ease;
            cursor: pointer;
        }
        figure.photo-item img:hover {
            transform: scale(1.02);
            box-shadow: 0 8px 16px rgba(0,0,0,0.2);
        }

        /* Lightbox */
        .lightbox {
            display: none;
            position: fixed;
            z-index: 2000;
            left: 0;
            top: 0;
            width: 100%;
            height: 100%;
            background-color: rgba(0, 0, 0, 0.9);
            backdrop-filter: blur(5px);
            -webkit-backdrop-filter: blur(5px);
        }
        .lightbox-content {
            margin: auto;
            display: block;
            max-width: 90%;
            max-height: 80vh;
            margin-top: 5vh;
            border-radius: 4px;
        }
        #lightbox-caption {
            margin: auto;
            display: block;
            width: 80%;
            max-width: 800px;
            text-align: center;
            color: #ccc;
            padding: 15px 0;
            height: 10vh;
        }
        .lightbox-close {
            position: absolute;
            top: 20px;
            right: 35px;
            color: #f1f1f1;
            font-size: 40px;
            font-weight: bold;
            cursor: pointer;
        }

        .skill-tag {
            background-color: var(--bg-color);
            border: 1px solid var(--border-color);
            padding: 0.3rem 0.8rem;
            border-radius: 20px;
            font-size: 0.85rem;
            color: var(--text-color);
            font-weight: 500;
            display: inline-block;
        }
"""
content = re.sub(r'(\.article-card\s*\{\s*display:\s*flex;\s*flex-direction:\s*column;\s*\})', '', content)
content = re.sub(r'(figure\.photo-item\s*img\s*\{[^}]*\})', '', content)
content = content.replace('</style>', animations_css + '\n    </style>')

# Nav Dark Mode Toggle Button
nav_replacement = """    <nav style="display: flex; align-items: center;">
        <a href="#writing">Writing</a>
        <a href="#photography">Photography</a>
        <a href="#video">Video</a>
        <a href="#about">About</a>
        <button id="theme-toggle" aria-label="Toggle Dark Mode" style="background: none; border: none; cursor: pointer; font-size: 1.2rem; margin-left: auto;">🌙</button>
    </nav>"""
content = re.sub(r'<nav>.*?</nav>', nav_replacement, content, flags=re.DOTALL)

# Add Skills section at the end of About Me
skills_html = """        <div class="skills-banner" style="margin-top: 2rem; padding: 1.5rem; background-color: var(--photo-bg); border-radius: 8px; border: 1px solid var(--border-color);">
            <h3 style="margin-top: 0; margin-bottom: 1rem; font-size: 1.2rem; color: var(--heading-color);">Skills & Tools</h3>
            <div style="display: flex; flex-wrap: wrap; gap: 0.5rem;">
                <span class="skill-tag">Data Analysis (Python, Excel)</span>
                <span class="skill-tag">Video Editing (Premiere Pro)</span>
                <span class="skill-tag">Photo Editing (Lightroom, Photoshop)</span>
                <span class="skill-tag">DSLR Photography</span>
                <span class="skill-tag">AP Style</span>
                <span class="skill-tag">CMS (TownNews, WordPress)</span>
                <span class="skill-tag">FOIA/Public Records Requests</span>
            </div>
        </div>
    </section>"""
content = content.replace('</section>\n\n    <section id="writing">', skills_html + '\n\n    <section id="writing">')

# Add Lightbox HTML and JS at the bottom
lightbox_js = """
    <div id="lightbox" class="lightbox">
        <span class="lightbox-close">&times;</span>
        <img class="lightbox-content" id="lightbox-img">
        <div id="lightbox-caption"></div>
    </div>

    <script>
        // Dark Mode Toggle
        const themeToggle = document.getElementById('theme-toggle');
        const body = document.body;
        
        const currentTheme = localStorage.getItem('theme');
        if (currentTheme === 'dark') {
            body.classList.add('dark-mode');
            themeToggle.textContent = '☀️';
        }

        themeToggle.addEventListener('click', () => {
            body.classList.toggle('dark-mode');
            if (body.classList.contains('dark-mode')) {
                localStorage.setItem('theme', 'dark');
                themeToggle.textContent = '☀️';
            } else {
                localStorage.setItem('theme', 'light');
                themeToggle.textContent = '🌙';
            }
        });

        // Lightbox
        const lightbox = document.getElementById('lightbox');
        const lightboxImg = document.getElementById('lightbox-img');
        const lightboxCaption = document.getElementById('lightbox-caption');
        const closeBtn = document.getElementsByClassName('lightbox-close')[0];

        document.querySelectorAll('figure.photo-item img').forEach(img => {
            img.addEventListener('click', function() {
                lightbox.style.display = 'block';
                lightboxImg.src = this.src;
                lightboxCaption.innerHTML = this.nextElementSibling.innerHTML;
            });
        });

        closeBtn.onclick = function() {
            lightbox.style.display = 'none';
        }
        
        lightbox.onclick = function(e) {
            if (e.target !== lightboxImg) {
                lightbox.style.display = 'none';
            }
        }
    </script>
</body>"""
content = content.replace('</body>', lightbox_js)

# Save
with open('index.html', 'w') as f:
    f.write(content)

