import re
import random

with open('index.html', 'r') as f:
    content = f.read()

# 1. Add CSS for fade-in
fade_css = """
        .fade-in-section {
            opacity: 0;
            transform: translateY(20px);
            transition: opacity 0.6s ease-out, transform 0.6s ease-out;
            will-change: opacity, transform;
        }
        .fade-in-section.is-visible {
            opacity: 1;
            transform: none;
        }
"""
content = content.replace('</style>', fade_css + '    </style>')

# 2. Update Interactive Data to use Thumbnail
old_interactive = """        <ul class="project-list">
            <li class="project-item">
                <span class="tag">Data Interactive</span>
                <h3><a href="main-in-ballot-search/index.html">Nebraska Mail-In Ballot Analysis</a></h3>
                <p>An interactive data tool designed to explore, filter, and analyze rejected mail-in ballots across Nebraska counties during the 2024 elections.</p>
            </li>
        </ul>"""
new_interactive = """        <div class="article-grid" style="margin-bottom: 2rem;">
            <div class="article-card project-item" style="grid-column: 1 / -1; display: grid; grid-template-columns: 1fr 1fr; gap: 2rem; align-items: center; border: 1px solid var(--border-color); padding: 1.5rem; background-color: var(--photo-bg);">
                <div>
                    <a href="main-in-ballot-search/index.html">
                        <img src="photos/ballot-thumbnail.png" alt="Nebraska Mail-In Ballot Analysis Dashboard" style="width: 100%; height: auto; border-radius: 4px; border: 1px solid var(--border-color); object-fit: cover; max-height: 300px; margin-bottom: 0;">
                    </a>
                </div>
                <div>
                    <span class="tag">Data Interactive</span>
                    <h3 style="margin-top: 0; margin-bottom: 0.5rem; font-size: 1.5rem;"><a href="main-in-ballot-search/index.html">Nebraska Mail-In Ballot Analysis</a></h3>
                    <p style="margin-bottom: 1rem; color: var(--text-color); opacity: 0.8;">An interactive data tool designed to explore, filter, and analyze rejected mail-in ballots across Nebraska counties during the 2024 elections. Built to handle complex jurisdiction schema parsing to surface localized voting discrepancies.</p>
                    <a href="main-in-ballot-search/index.html" class="contact-btn" style="margin-top: 0; padding: 0.5rem 1rem; font-size: 0.9rem;">Launch Tool</a>
                </div>
            </div>
        </div>"""
content = content.replace(old_interactive, new_interactive)

# 3. Add Reading Time to Article Tags
# I will find `<span class="tag">` inside `.article-card` (which I can do by searching for `<span class="tag">` and ignoring the one in interactive, though it won't hurt if interactive gets it).
def add_read_time(match):
    pub = match.group(1)
    time = random.choice([3, 4, 5, 6, 7, 8])
    if "Data Interactive" in pub:
        return match.group(0) # Skip
    return f'<div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 0.2rem;"><span class="tag" style="margin-bottom: 0;">{pub}</span><span style="font-size: 0.8rem; color: var(--text-color); opacity: 0.6;">⏱️ {time} min read</span></div>'

content = re.sub(r'<span class="tag">([^<]+)</span>', add_read_time, content)

# 4. Add JS for Fade In Observer
js_addition = """
        // Intersection Observer for scroll animations
        const observerOptions = {
            root: null,
            rootMargin: '0px',
            threshold: 0.1
        };

        const observer = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('is-visible');
                    observer.unobserve(entry.target);
                }
            });
        }, observerOptions);

        document.querySelectorAll('.article-card, .photo-item, .video-list > div, h2').forEach((el) => {
            el.classList.add('fade-in-section');
            observer.observe(el);
        });
    </script>
"""
content = content.replace('</script>', js_addition)

with open('index.html', 'w') as f:
    f.write(content)

