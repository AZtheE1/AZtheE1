import os
import requests
import base64

def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as f:
            return "data:image/png;base64," + base64.b64encode(f.read()).decode('utf-8')
    return ""

def generate_wordmark_svg():
    ascii_art = [
        "SS`         SS`   SSSSSSS+++`                  SSSSSSSSSSSSS`` SSSSSSSSSSSSS`  SS`       SS``   SSSSSSS``     SSSSSSSSSSSSS`` ",
        "SS`SS`   SSSSS`   SS`+++++++=SS`               ++++++++++++S`` ++++++SSS+++++``SS`       SS``   ++++++++``    SSS++++++++++++`",
        "SS`++`SS`=++SS`   SS`        SS`               ++++++++++++S``  ++++++S``++++= SS`       SS`` SS`+++++++=``   SS`++++++++++=S``",
        "SS`  ++`    SS`   SS`        SS`                       SS`++`         SS``     SSS+++++++S``  SS`      SS``   SS`          SS``",
        "SS`  =+=    SS`   SS`        SS`                       SS`++=         SS``     SSS+++++++S``  SSSSSSSSSSSSS`` SS`          SS``",
        "SS`         SS`   SS`        SS`                       SS`++`         SS``     SS`       SS`` SS`++++++++++`` SS`          S```",
        "SS`         SS`   SS`        SS`                       ++`            SS``     SS`       SS`` SS`        SS`` SS`          SS``",
        "SS`         SS`   SS`        SS`   SSSSS`              SS`++=         SS``     SS`       SS`` SS`        SS`` SS`          S++`",
        "SS`         SS`   SS`SSSSSSS`++`   SSSSS`              SS`SSSSSSSSS`` SSSSSSSS`SSSS``SS`       SS`` SS`        SS`` SS`SSSSSSS`++=",
        "++`         ++`   +++++++++++`     +++++`              +++++++++++++` ++++++++++++++`++`       +++` +++`       +++` +++++++++++`",
        "=+=         ++=   +++++++++++      +++++=                                                                                       "
    ]
    
    svg = """<svg width="900" height="250" viewBox="0 0 900 250" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="900" height="250" rx="8" fill="#0b0f10" stroke="#1f2937" stroke-width="1"/>
  
  <!-- macOS window controls -->
  <circle cx="20" cy="20" r="5" fill="#ef4444"/>
  <circle cx="40" cy="20" r="5" fill="#f59e0b"/>
  <circle cx="60" cy="20" r="5" fill="#22c55e"/>
  
  <text x="450" y="24" fill="#94a3b8" font-family="monospace" font-size="12" text-anchor="middle">azthee1@github: ~$ ./wordmark.sh --name</text>
  <text x="880" y="240" fill="#1f2937" font-family="monospace" font-size="10" text-anchor="end">gitskins.com</text>
  
  <!-- Moving Group -->
  <g clip-path="url(#reveal)">
    <clipPath id="reveal">
      <rect x="0" y="0" width="0" height="250">
        <!-- Typing reveal effect -->
        <animate attributeName="width" values="0;900;900" dur="4s" repeatCount="indefinite" />
      </rect>
    </clipPath>
"""
    y_start = 80
    for i, line in enumerate(ascii_art):
        svg += f'    <text x="50" y="{y_start + i*12}" fill="#e2e8f0" font-family="monospace" font-size="10" xml:space="preserve">{line}</text>\n'
        
    svg += """
    <!-- Slow hover/parallax movement -->
    <animateTransform attributeName="transform" type="translate" values="0,0; 10,0; -10,0; 0,0" dur="8s" repeatCount="indefinite" />
  </g>
  
  <!-- Glowing scanline sweeping up and down -->
  <line x1="0" y1="0" x2="900" y2="0" stroke="#34d399" stroke-width="2" opacity="0.3">
    <animate attributeName="y1" values="40;250;40" dur="4s" repeatCount="indefinite" />
    <animate attributeName="y2" values="40;250;40" dur="4s" repeatCount="indefinite" />
  </line>
</svg>"""
    return svg

def generate_hero_svg(avatar_b64, stats):
    repos = stats.get('public_repos', 12)
    followers = stats.get('followers', 7)
    
    return f"""<svg width="900" height="400" viewBox="0 0 900 400" fill="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
  <defs>
    <linearGradient id="glow" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#34d399" />
      <stop offset="100%" stop-color="#06b6d4" />
    </linearGradient>
    <filter id="blur">
      <feGaussianBlur stdDeviation="3" result="coloredBlur"/>
    </filter>
    <clipPath id="avatarClip"><circle cx="700" cy="150" r="90" /></clipPath>
  </defs>

  <rect width="900" height="400" rx="8" fill="#131c18" stroke="#1f2937" stroke-width="1"/>
  <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
    <path d="M 40 0 L 0 0 0 40 M 0 40 L 40 40" fill="none" stroke="#1f2937" stroke-width="0.5" opacity="0.3"/>
  </pattern>
  <rect width="900" height="400" fill="url(#grid)"/>

  <text x="50" y="70" fill="#94a3b8" font-family="monospace" font-size="12" letter-spacing="2">HELLO, WORLD, I'M</text>
  <text x="50" y="130" fill="#e2e8f0" font-family="Courier New, monospace" font-size="48" font-weight="900" letter-spacing="4">Md. Abu Zihad</text>
  <text x="50" y="180" fill="#e2e8f0" font-family="monospace" font-size="16" font-weight="bold">TypeScript / Java / Dart</text>
  <text x="50" y="210" fill="#94a3b8" font-family="monospace" font-size="12">Dhaka, Mirpur 12</text>
  
  <circle cx="700" cy="150" r="105" fill="none" stroke="url(#glow)" stroke-width="3" filter="url(#blur)">
    <animate attributeName="opacity" values="0.4;1;0.4" dur="2s" repeatCount="indefinite" />
    <animate attributeName="r" values="95;105;95" dur="2s" repeatCount="indefinite" />
  </circle>

  <circle cx="700" cy="150" r="130" fill="none" stroke="#34d399" stroke-width="1" stroke-dasharray="4 8" opacity="0.4">
    <animateTransform attributeName="transform" type="rotate" from="0 700 150" to="360 700 150" dur="20s" repeatCount="indefinite"/>
  </circle>

  <image x="610" y="60" width="180" height="180" preserveAspectRatio="xMidYMid slice" href="{avatar_b64}" clip-path="url(#avatarClip)" />
  
  <line x1="50" y1="280" x2="850" y2="280" stroke="#1f2937" stroke-width="1"/>
  
  <text x="50" y="320" fill="#94a3b8" font-family="monospace" font-size="10" letter-spacing="1">REPOSITORIES</text>
  <circle cx="140" cy="316" r="3" fill="#06b6d4">
    <animate attributeName="opacity" values="1;0.2;1" dur="1.5s" repeatCount="indefinite" />
  </circle>
  <text x="50" y="360" fill="#e2e8f0" font-family="sans-serif" font-size="28" font-weight="bold">{repos}</text>
  
  <text x="250" y="320" fill="#94a3b8" font-family="monospace" font-size="10" letter-spacing="1">STARS</text>
  <circle cx="295" cy="316" r="3" fill="#06b6d4">
    <animate attributeName="opacity" values="1;0.2;1" dur="1.2s" repeatCount="indefinite" />
  </circle>
  <text x="250" y="360" fill="#e2e8f0" font-family="sans-serif" font-size="28" font-weight="bold">2</text>
  
  <text x="450" y="320" fill="#94a3b8" font-family="monospace" font-size="10" letter-spacing="1">CONTRIBUTIONS</text>
  <circle cx="545" cy="316" r="3" fill="#06b6d4">
    <animate attributeName="opacity" values="1;0.2;1" dur="1.8s" repeatCount="indefinite" />
  </circle>
  <text x="450" y="360" fill="#e2e8f0" font-family="sans-serif" font-size="28" font-weight="bold">818</text>
  
  <text x="650" y="320" fill="#94a3b8" font-family="monospace" font-size="10" letter-spacing="1">FOLLOWERS</text>
  <circle cx="720" cy="316" r="3" fill="#06b6d4">
    <animate attributeName="opacity" values="1;0.2;1" dur="1.4s" repeatCount="indefinite" />
  </circle>
  <text x="650" y="360" fill="#e2e8f0" font-family="sans-serif" font-size="28" font-weight="bold">{followers}</text>
</svg>"""

def generate_identity_svg(stats):
    repos = stats.get('public_repos', 12)
    followers = stats.get('followers', 7)
    return f"""<svg width="900" height="200" viewBox="0 0 900 200" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="900" height="200" rx="8" fill="#131c18" stroke="#1f2937" stroke-width="1"/>
  <text x="40" y="50" fill="#e2e8f0" font-family="sans-serif" font-size="16">CSI @ BUP | ICPC'25 Regional Finalist | Full-Stack Developer</text>
  <text x="40" y="75" fill="#e2e8f0" font-family="sans-serif" font-size="16">exploring the intersection of AI-driven Cybersecurity and</text>
  <text x="40" y="100" fill="#e2e8f0" font-family="sans-serif" font-size="16">Advanced Algorithms.</text>
  
  <text x="40" y="150" fill="#e2e8f0" font-family="sans-serif" font-size="14" font-weight="bold">Focus:</text>
  <rect x="100" y="135" width="90" height="22" rx="4" fill="#0b0f10" stroke="#1f2937" stroke-width="1"/>
  <text x="145" y="150" fill="#e2e8f0" font-family="monospace" font-size="12" text-anchor="middle">TypeScript</text>
  
  <rect x="200" y="135" width="50" height="22" rx="4" fill="#0b0f10" stroke="#1f2937" stroke-width="1"/>
  <text x="225" y="150" fill="#e2e8f0" font-family="monospace" font-size="12" text-anchor="middle">Java</text>
  
  <rect x="260" y="135" width="50" height="22" rx="4" fill="#0b0f10" stroke="#1f2937" stroke-width="1"/>
  <text x="285" y="150" fill="#e2e8f0" font-family="monospace" font-size="12" text-anchor="middle">HTML</text>
  
  <text x="40" y="180" fill="#94a3b8" font-family="sans-serif" font-size="12">Thoughtful collaboration, ambitious protocols, and useful open source.</text>
  <line x1="600" y1="20" x2="600" y2="180" stroke="#1f2937" stroke-width="1"/>
  <rect x="630" y="35" width="90" height="22" rx="4" fill="#1f2937"/>
  <text x="675" y="50" fill="#e2e8f0" font-family="monospace" font-size="10" text-anchor="middle" letter-spacing="1">LIVE SIGNAL</text>
  
  <circle cx="730" cy="46" r="4" fill="#34d399">
    <animate attributeName="opacity" values="1;0.2;1" dur="1s" repeatCount="indefinite" />
  </circle>

  <text x="630" y="90" fill="#e2e8f0" font-family="sans-serif" font-size="14"><tspan font-weight="bold">{repos}</tspan> repos</text>
  <text x="630" y="115" fill="#e2e8f0" font-family="sans-serif" font-size="14"><tspan font-weight="bold">2</tspan> stars</text>
  <text x="630" y="140" fill="#e2e8f0" font-family="sans-serif" font-size="14"><tspan font-weight="bold">818</tspan> contributions</text>
  <text x="630" y="165" fill="#e2e8f0" font-family="sans-serif" font-size="14"><tspan font-weight="bold">{followers}</tspan> followers</text>
</svg>"""

def generate_ideas_svg():
    return """<svg width="900" height="250" viewBox="0 0 900 250" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="900" height="250" rx="8" fill="#131c18" stroke="#1f2937" stroke-width="1"/>
  <text x="40" y="40" fill="#94a3b8" font-family="monospace" font-size="10" letter-spacing="2">CURRENT FOCUS</text>
  <text x="40" y="75" fill="#e2e8f0" font-family="monospace" font-size="20" font-weight="bold">Ideas taking shape</text>
  <line x1="40" y1="100" x2="860" y2="100" stroke="#1f2937" stroke-width="1" stroke-dasharray="8 8"/>
  
  <text x="40" y="150" fill="#06b6d4" font-family="monospace" font-size="28" font-weight="bold">01</text>
  <line x1="40" y1="170" x2="200" y2="170" stroke="#1f2937" stroke-width="1"/>
  <text x="40" y="200" fill="#e2e8f0" font-family="monospace" font-size="14" font-weight="bold">TypeScript</text>
  <text x="40" y="220" fill="#94a3b8" font-family="sans-serif" font-size="12">Current focus</text>
  
  <text x="340" y="150" fill="#06b6d4" font-family="monospace" font-size="28" font-weight="bold">02</text>
  <line x1="340" y1="170" x2="500" y2="170" stroke="#1f2937" stroke-width="1"/>
  <text x="340" y="200" fill="#e2e8f0" font-family="monospace" font-size="14" font-weight="bold">Java</text>
  <text x="340" y="220" fill="#94a3b8" font-family="sans-serif" font-size="12">In the build queue</text>
  
  <text x="640" y="150" fill="#06b6d4" font-family="monospace" font-size="28" font-weight="bold">03</text>
  <line x1="640" y1="170" x2="800" y2="170" stroke="#1f2937" stroke-width="1"/>
  <text x="640" y="200" fill="#e2e8f0" font-family="monospace" font-size="14" font-weight="bold">HTML</text>
  <text x="640" y="220" fill="#94a3b8" font-family="sans-serif" font-size="12">In the build queue</text>
</svg>"""

def generate_tools_svg():
    return """<svg width="900" height="280" viewBox="0 0 900 280" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="900" height="280" rx="8" fill="#131c18" stroke="#1f2937" stroke-width="1"/>
  <text x="40" y="40" fill="#94a3b8" font-family="monospace" font-size="10" letter-spacing="2">TECHNOLOGY SPECTRUM</text>
  <text x="40" y="75" fill="#e2e8f0" font-family="monospace" font-size="20" font-weight="bold">The tools behind the work</text>
  <line x1="40" y1="100" x2="860" y2="100" stroke="#1f2937" stroke-width="1" stroke-dasharray="8 8"/>
  
  <rect x="40" y="120" width="24" height="24" rx="4" fill="#3178C6"/>
  <text x="52" y="137" fill="#fff" font-family="sans-serif" font-size="12" font-weight="bold" text-anchor="middle">TS</text>
  <text x="40" y="170" fill="#e2e8f0" font-family="monospace" font-size="14" font-weight="bold">TypeScript</text>
  <text x="40" y="190" fill="#94a3b8" font-family="sans-serif" font-size="10">25% of public code</text>
  <rect x="40" y="205" width="160" height="2" fill="#1f2937"/><rect x="40" y="205" width="40" height="2" fill="#3178C6">
    <animate attributeName="width" from="0" to="40" dur="1.5s" fill="freeze" />
  </rect>

  <rect x="250" y="120" width="24" height="24" rx="4" fill="#b07219" fill-opacity="0.2" stroke="#b07219" stroke-width="1"/>
  <text x="262" y="137" fill="#b07219" font-family="monospace" font-size="12" font-weight="bold" text-anchor="middle">J</text>
  <text x="250" y="170" fill="#e2e8f0" font-family="monospace" font-size="14" font-weight="bold">Java</text>
  <text x="250" y="190" fill="#94a3b8" font-family="sans-serif" font-size="10">24% of public code</text>
  <rect x="250" y="205" width="160" height="2" fill="#1f2937"/><rect x="250" y="205" width="38" height="2" fill="#b07219">
    <animate attributeName="width" from="0" to="38" dur="1.5s" fill="freeze" />
  </rect>

  <rect x="460" y="120" width="24" height="24" rx="4" fill="#00B4AB"/>
  <text x="472" y="137" fill="#fff" font-family="sans-serif" font-size="12" font-weight="bold" text-anchor="middle">D</text>
  <text x="460" y="170" fill="#e2e8f0" font-family="monospace" font-size="14" font-weight="bold">Dart</text>
  <text x="460" y="190" fill="#94a3b8" font-family="sans-serif" font-size="10">17% of public code</text>
  <rect x="460" y="205" width="160" height="2" fill="#1f2937"/><rect x="460" y="205" width="27" height="2" fill="#00B4AB">
    <animate attributeName="width" from="0" to="27" dur="1.5s" fill="freeze" />
  </rect>

  <rect x="670" y="120" width="24" height="24" rx="4" fill="#e34c26"/>
  <text x="682" y="137" fill="#fff" font-family="sans-serif" font-size="10" font-weight="bold" text-anchor="middle">5</text>
  <text x="670" y="170" fill="#e2e8f0" font-family="monospace" font-size="14" font-weight="bold">HTML</text>
  <text x="670" y="190" fill="#94a3b8" font-family="sans-serif" font-size="10">17% of public code</text>
  <rect x="670" y="205" width="160" height="2" fill="#1f2937"/><rect x="670" y="205" width="27" height="2" fill="#e34c26">
    <animate attributeName="width" from="0" to="27" dur="1.5s" fill="freeze" />
  </rect>
</svg>"""

def generate_projects_svg(repos):
    svg = """<svg width="900" height="350" viewBox="0 0 900 350" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="900" height="350" rx="8" fill="#131c18" stroke="#1f2937" stroke-width="1"/>
  <text x="40" y="40" fill="#94a3b8" font-family="monospace" font-size="10" letter-spacing="2">PROJECT CONSTELLATION</text>
  <text x="40" y="75" fill="#e2e8f0" font-family="monospace" font-size="20" font-weight="bold">A universe of work</text>
  <line x1="40" y1="100" x2="860" y2="100" stroke="#1f2937" stroke-width="1" stroke-dasharray="8 8"/>
  <path d="M 200 200 Q 350 250 500 200 T 750 150" fill="none" stroke="#1f2937" stroke-width="2" stroke-dasharray="4 4"/>
  <path d="M 500 200 Q 600 300 700 250" fill="none" stroke="#1f2937" stroke-width="2" stroke-dasharray="4 4"/>
"""
    positions = [(200, 200), (500, 200), (750, 150), (700, 250)]
    for i, repo in enumerate(repos[:4]):
        cx, cy = positions[i]
        name = repo['name']
        desc = repo.get('language') or 'Java'
        stars = repo.get('stargazers_count', 0)
        svg += f"""
  <circle cx="{cx}" cy="{cy}" r="50" fill="none" stroke="#f59e0b" stroke-width="1" stroke-dasharray="2 4" opacity="0.3">
    <animateTransform attributeName="transform" type="rotate" from="0 {cx} {cy}" to="360 {cx} {cy}" dur="{10 + i*2}s" repeatCount="indefinite"/>
    <animate attributeName="opacity" values="0.1;0.6;0.1" dur="2s" repeatCount="indefinite" />
  </circle>
  <circle cx="{cx}" cy="{cy}" r="35" fill="#131c18" stroke="#f59e0b" stroke-width="1" opacity="0.5"/>
  <circle cx="{cx}" cy="{cy}" r="15" fill="#f59e0b" fill-opacity="0.1" stroke="#f59e0b" stroke-width="1"/>
  <text x="{cx}" y="{cy+4}" fill="#f59e0b" font-family="monospace" font-size="10" text-anchor="middle">J</text>
  <text x="{cx}" y="{cy+70}" fill="#e2e8f0" font-family="monospace" font-size="14" font-weight="bold" text-anchor="middle">{name}</text>
  <text x="{cx}" y="{cy+90}" fill="#94a3b8" font-family="sans-serif" font-size="10" text-anchor="middle">{desc} • {stars} stars</text>
"""
    svg += "</svg>"
    return svg

def generate_energy_svg():
    return """<svg width="900" height="220" viewBox="0 0 900 220" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="900" height="220" rx="8" fill="#131c18" stroke="#1f2937" stroke-width="1"/>
  <text x="40" y="40" fill="#94a3b8" font-family="monospace" font-size="10" letter-spacing="2">CONTRIBUTION MATRIX</text>
  <text x="40" y="75" fill="#e2e8f0" font-family="monospace" font-size="20" font-weight="bold">Every day leaves a trace</text>
  <line x1="40" y1="100" x2="860" y2="100" stroke="#1f2937" stroke-width="1" stroke-dasharray="8 8"/>
  <g fill="#34d399">
    <circle cx="100" cy="150" r="2" opacity="0.2"/><circle cx="120" cy="150" r="3" opacity="0.5"/>
    <circle cx="140" cy="150" r="4" opacity="0.8"/>
    <circle cx="160" cy="140" r="5" opacity="1.0" filter="drop-shadow(0 0 4px #34d399)">
        <animate attributeName="opacity" values="0.5;1;0.5" dur="1.5s" repeatCount="indefinite" />
    </circle>
    <circle cx="180" cy="160" r="3" opacity="0.6"/><circle cx="200" cy="150" r="2" opacity="0.3"/>
    <circle cx="300" cy="170" r="2" opacity="0.4"/><circle cx="320" cy="160" r="4" opacity="0.7"/>
    <circle cx="340" cy="130" r="5" opacity="1.0"/>
    <circle cx="360" cy="140" r="3" opacity="0.5">
        <animate attributeName="opacity" values="0.2;0.8;0.2" dur="2s" repeatCount="indefinite" />
    </circle>
    <circle cx="500" cy="160" r="4" opacity="0.8"/><circle cx="520" cy="150" r="3" opacity="0.6"/>
    <circle cx="540" cy="150" r="2" opacity="0.4"/>
    <circle cx="700" cy="150" r="5" opacity="1.0" filter="drop-shadow(0 0 4px #34d399)">
        <animate attributeName="opacity" values="0.5;1;0.5" dur="1.2s" repeatCount="indefinite" />
    </circle>
    <circle cx="720" cy="140" r="4" opacity="0.8"/><circle cx="740" cy="160" r="3" opacity="0.5"/>
    <circle cx="760" cy="170" r="2" opacity="0.2"/>
  </g>
  <text x="450" y="200" fill="#94a3b8" font-family="sans-serif" font-size="12" text-anchor="middle">1 day current streak · 90 active days</text>
</svg>"""

def get_repo_score(repo):
    score = repo.get('stargazers_count', 0) * 10
    score += repo.get('forks_count', 0) * 5
    topics = [t.lower() for t in repo.get('topics', [])]
    name_lower = repo.get('name', '').lower()
    for kw in ['ai', 'fullstack', 'full-stack', 'nextjs', 'python', 'pytorch', 'machine-learning', 'react', 'fastapi', 'llm', 'langchain']:
        if kw in topics or kw in name_lower:
            score += 100
            
    # Guarantee specific core repositories from the execution plan appear first
    if 'e-voting' in name_lower or 'salesman-ai' in name_lower or 'sslcommerz' in name_lower:
        score += 1000
        
    return score

def main():
    username = os.getenv("GITHUB_REPOSITORY_OWNER") or "AZtheE1"
    headers = {"Authorization": f"Bearer {os.getenv('GITHUB_TOKEN')}"} if os.getenv('GITHUB_TOKEN') else {}
    
    # 1. Fetch User Stats
    user_response = requests.get(f"https://api.github.com/users/{username}", headers=headers)
    user_stats = user_response.json() if user_response.status_code == 200 else {}
    
    # 2. Fetch Repos
    repos_response = requests.get(f"https://api.github.com/users/{username}/repos?sort=updated&per_page=100", headers=headers)
    valid_repos = [r for r in repos_response.json() if not r.get('fork') and not r.get('private')] if repos_response.status_code == 200 else []
    sorted_repos = sorted(valid_repos, key=get_repo_score, reverse=True)
    
    # 3. Generate SVGs
    os.makedirs('assets', exist_ok=True)
    avatar_b64 = get_base64_image('assets/avatar-dithered.png')
    
    with open('assets/wordmark-card.svg', 'w', encoding='utf-8') as f: f.write(generate_wordmark_svg())
    with open('assets/hero-card.svg', 'w', encoding='utf-8') as f: f.write(generate_hero_svg(avatar_b64, user_stats))
    with open('assets/identity-card.svg', 'w', encoding='utf-8') as f: f.write(generate_identity_svg(user_stats))
    with open('assets/ideas-card.svg', 'w', encoding='utf-8') as f: f.write(generate_ideas_svg())
    with open('assets/tools-card.svg', 'w', encoding='utf-8') as f: f.write(generate_tools_svg())
    with open('assets/projects-card.svg', 'w', encoding='utf-8') as f: f.write(generate_projects_svg(sorted_repos))
    with open('assets/energy-card.svg', 'w', encoding='utf-8') as f: f.write(generate_energy_svg())
        
    # 4. Inject into Template
    with open("templates/README.md.tpl", "r", encoding="utf-8") as f:
        template = f.read()
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(template)

if __name__ == "__main__":
    main()
