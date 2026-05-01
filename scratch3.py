with open('index.html', 'r') as f:
    content = f.read()

# 1. Remove Data Interactive
data_interactive = """        <div class="article-grid" style="margin-bottom: 2rem;">
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
content = content.replace(data_interactive, "")

# 2. Convert Video Grid
old_video = """            <div class="project-item">
                <h3>Joyrager - Dooya? (Official Video)</h3>
                <p>I work on various creative projects for the band Joyrager, including helping produce their official music videos.</p>
                <p style="margin-bottom: 1.5rem; color: var(--text-color); opacity: 0.8;"><em>*Won a Student Production Award from the Heartland Region of The National Academy of Television Arts & Sciences.</em></p>
                <div class="video-container">
                    <iframe src="https://www.youtube.com/embed/EK8JRFMSdrM?si=33PJib4ZIu4U4jAg" title="YouTube video player" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
                </div>
            </div>

            <div class="project-item">
                <h3>Joyrager - Holiday Punk (Official Video)</h3>
                <p>Another official music video project I worked on for Joyrager.</p>
                <div class="video-container">
                    <iframe src="https://www.youtube.com/embed/7KyZUMys4xQ?si=yIp4lPKO3j6ASYHM" title="YouTube video player" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
                </div>
            </div>"""

new_video = """            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 1.5rem; margin-top: 2rem;" class="fade-in-section">
                <div class="project-item" style="margin-bottom: 0;">
                    <h3 style="font-size: 1.15rem; margin-top: 0;">Joyrager - Dooya?</h3>
                    <p style="font-size: 0.9rem; margin-bottom: 1rem; color: var(--text-color); opacity: 0.8;"><em>*Won a Student Production Award from the Heartland Region of The NATAS.</em></p>
                    <div class="video-container" style="margin-top: 0;">
                        <iframe src="https://www.youtube.com/embed/EK8JRFMSdrM?si=33PJib4ZIu4U4jAg" title="YouTube video player" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
                    </div>
                </div>

                <div class="project-item" style="margin-bottom: 0;">
                    <h3 style="font-size: 1.15rem; margin-top: 0;">Joyrager - Holiday Punk</h3>
                    <p style="font-size: 0.9rem; margin-bottom: 1rem; color: var(--text-color); opacity: 0.8;">Another official music video project I worked on for Joyrager.</p>
                    <div class="video-container" style="margin-top: 0;">
                        <iframe src="https://www.youtube.com/embed/7KyZUMys4xQ?si=yIp4lPKO3j6ASYHM" title="YouTube video player" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" allowfullscreen></iframe>
                    </div>
                </div>
            </div>"""
content = content.replace(old_video, new_video)

# 3. Update Contact Form
old_contact = """    <section id="contact" class="contact-section">
        <h2>Let's Connect</h2>
        <p>I'm always looking for new reporting opportunities and creative collaborations.</p>
        <a href="mailto:diepjustin@outlook.com" class="contact-btn">Email Me</a>
    </section>"""

new_contact = """    <section id="contact" class="contact-section">
        <h2>Let's Connect</h2>
        <p>I'm always looking for new reporting opportunities and creative collaborations. Drop me a line below.</p>
        
        <form action="https://api.web3forms.com/submit" method="POST" style="max-width: 500px; margin: 2rem auto; text-align: left; display: flex; flex-direction: column; gap: 1rem;" class="fade-in-section">
            <!-- Replace YOUR_ACCESS_KEY_HERE with your access key from Web3Forms.com -->
            <input type="hidden" name="access_key" value="YOUR_ACCESS_KEY_HERE">
            
            <input type="text" name="name" placeholder="Your Name" required style="padding: 0.8rem; border-radius: 4px; border: 1px solid var(--border-color); background-color: var(--photo-bg); color: var(--text-color); font-family: inherit;">
            
            <input type="email" name="email" placeholder="Your Email" required style="padding: 0.8rem; border-radius: 4px; border: 1px solid var(--border-color); background-color: var(--photo-bg); color: var(--text-color); font-family: inherit;">
            
            <textarea name="message" placeholder="Your Message" rows="5" required style="padding: 0.8rem; border-radius: 4px; border: 1px solid var(--border-color); background-color: var(--photo-bg); color: var(--text-color); font-family: inherit; resize: vertical;"></textarea>
            
            <button type="submit" class="contact-btn" style="border: none; cursor: pointer; width: 100%; margin-top: 0.5rem; font-family: inherit; font-size: 1rem;">Send Message</button>
        </form>
    </section>"""
content = content.replace(old_contact, new_contact)

with open('index.html', 'w') as f:
    f.write(content)

