import os
import requests
import base64

def get_base64_image(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as f:
            return "data:image/png;base64," + base64.b64encode(f.read()).decode('utf-8')
    return ""

def generate_hero_svg(avatar_b64):
    return f"""<svg width="850" height="280" viewBox="0 0 850 280" fill="none" xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink">
  <rect width="850" height="280" rx="12" fill="#0b0f10" stroke="#1f2937" stroke-width="2"/>
  <text x="40" y="60" fill="#e2e8f0" font-family="monospace" font-size="32" font-weight="bold">Md. Abu Zihad</text>
  <text x="40" y="100" fill="#34d399" font-family="monospace" font-size="18">TypeScript / Java / Dart</text>
  <text x="40" y="130" fill="#94a3b8" font-family="monospace" font-size="14">Dhaka, Mirpur 12</text>
  <line x1="40" y1="160" x2="550" y2="160" stroke="#1f2937" stroke-width="2"/>
  <text x="40" y="200" fill="#e2e8f0" font-family="sans-serif" font-size="16" font-weight="bold">CSI @ BUP | ICPC'25 Regional Finalist</text>
  <text x="40" y="230" fill="#94a3b8" font-family="sans-serif" font-size="14">Full-Stack Developer exploring the intersection of AI-driven</text>
  <text x="40" y="250" fill="#94a3b8" font-family="sans-serif" font-size="14">Cybersecurity and Advanced Algorithms.</text>
  
  <rect x="620" y="40" width="180" height="180" rx="10" fill="#131c18" stroke="#34d399" stroke-width="2"/>
  <image x="620" y="40" width="180" height="180" preserveAspectRatio="xMidYMid slice" href="{avatar_b64}" clip-path="url(#clipAvatar)" />
  <text x="710" y="245" fill="#34d399" font-family="monospace" font-size="12" text-anchor="middle">Neural-Matrix Portrait</text>
  
  <defs>
    <clipPath id="clipAvatar">
      <rect x="620" y="40" width="180" height="180" rx="10" />
    </clipPath>
  </defs>
</svg>"""

def generate_identity_svg(stats):
    repos = stats.get('public_repos', 12)
    followers = stats.get('followers', 7)
    return f"""<svg width="850" height="180" viewBox="0 0 850 180" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="850" height="180" rx="12" fill="#131c18" stroke="#1f2937" stroke-width="2"/>
  <rect x="580" y="0" width="270" height="180" fill="#0b0f10" rx="12"/>
  <line x1="580" y1="0" x2="580" y2="180" stroke="#34d399" stroke-width="4"/>
  
  <text x="40" y="45" fill="#e2e8f0" font-family="sans-serif" font-size="16" font-weight="bold">CSI @ BUP | ICPC'25 Regional Finalist</text>
  <text x="40" y="70" fill="#94a3b8" font-family="sans-serif" font-size="14">Full-Stack Developer exploring the intersection of AI-driven</text>
  <text x="40" y="90" fill="#94a3b8" font-family="sans-serif" font-size="14">Cybersecurity and Advanced Algorithms.</text>
  
  <text x="40" y="130" fill="#e2e8f0" font-family="monospace" font-size="14" font-weight="bold">Focus:</text>
  <rect x="100" y="115" width="100" height="24" rx="4" fill="#0b0f10"/>
  <text x="150" y="132" fill="#34d399" font-family="monospace" font-size="12" text-anchor="middle">TypeScript</text>
  <rect x="210" y="115" width="60" height="24" rx="4" fill="#0b0f10"/>
  <text x="240" y="132" fill="#34d399" font-family="monospace" font-size="12" text-anchor="middle">Java</text>
  <rect x="280" y="115" width="60" height="24" rx="4" fill="#0b0f10"/>
  <text x="310" y="132" fill="#34d399" font-family="monospace" font-size="12" text-anchor="middle">HTML</text>
  
  <rect x="610" y="30" width="100" height="24" rx="4" fill="#131c18" stroke="#34d399" stroke-width="1"/>
  <text x="660" y="47" fill="#34d399" font-family="monospace" font-size="12" text-anchor="middle" font-weight="bold">LIVE SIGNAL</text>
  <text x="610" y="85" fill="#e2e8f0" font-family="monospace" font-size="14">📂 {repos} repositories</text>
  <text x="610" y="115" fill="#e2e8f0" font-family="monospace" font-size="14">👥 Open Source Contributor</text>
  <text x="610" y="145" fill="#e2e8f0" font-family="monospace" font-size="14">👤 {followers} followers</text>
</svg>"""

def generate_projects_svg(repos):
    svg = """<svg width="850" height="300" viewBox="0 0 850 300" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="850" height="300" rx="12" fill="#0b0f10" stroke="#1f2937" stroke-width="2"/>
  <text x="40" y="50" fill="#94a3b8" font-family="monospace" font-size="12" letter-spacing="2">PROJECT CONSTELLATION</text>
  <text x="40" y="90" fill="#e2e8f0" font-family="monospace" font-size="24" font-weight="bold">A universe of work</text>
  <line x1="40" y1="120" x2="810" y2="120" stroke="#1f2937" stroke-width="2" stroke-dasharray="8 8"/>
"""
    colors = ["#34d399", "#06b6d4", "#f59e0b"]
    for i, repo in enumerate(repos[:3]):
        x_offset = 150 + (i * 270)
        name = repo['name']
        if len(name) > 20: name = name[:17] + "..."
        desc = repo.get('language') or 'Full-Stack'
        stars = repo.get('stargazers_count', 0)
        
        svg += f"""
  <circle cx="{x_offset}" cy="180" r="40" fill="#131c18" stroke="{colors[i]}" stroke-width="2"/>
  <circle cx="{x_offset}" cy="180" r="50" fill="none" stroke="{colors[i]}" stroke-width="1" stroke-dasharray="4 4" opacity="0.5"/>
  <text x="{x_offset}" y="186" fill="{colors[i]}" font-family="monospace" font-size="20" font-weight="bold" text-anchor="middle">{name[:1].upper()}</text>
  <text x="{x_offset}" y="255" fill="#e2e8f0" font-family="monospace" font-size="16" font-weight="bold" text-anchor="middle">{name}</text>
  <text x="{x_offset}" y="275" fill="#94a3b8" font-family="monospace" font-size="12" text-anchor="middle">{desc} • {stars} stars</text>
"""
    svg += "</svg>"
    return svg

def get_repo_score(repo):
    score = repo.get('stargazers_count', 0) * 10
    score += repo.get('forks_count', 0) * 5
    topics = [t.lower() for t in repo.get('topics', [])]
    name_lower = repo.get('name', '').lower()
    for kw in ['ai', 'fullstack', 'full-stack', 'nextjs', 'python', 'pytorch', 'machine-learning', 'react', 'fastapi', 'llm', 'langchain']:
        if kw in topics or kw in name_lower:
            score += 100
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
    
    with open('assets/hero-card.svg', 'w', encoding='utf-8') as f:
        f.write(generate_hero_svg(avatar_b64))
        
    with open('assets/identity-card.svg', 'w', encoding='utf-8') as f:
        f.write(generate_identity_svg(user_stats))
        
    with open('assets/projects-card.svg', 'w', encoding='utf-8') as f:
        f.write(generate_projects_svg(sorted_repos))
        
    # 4. Inject into Template
    with open("templates/README.md.tpl", "r", encoding="utf-8") as f:
        template = f.read()
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(template) # No more text replacements needed, SVGs are linked!

if __name__ == "__main__":
    main()
