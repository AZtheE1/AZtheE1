import os
import requests

def get_repo_score(repo):
    """Score repositories to highlight AI and Full-Stack projects."""
    score = repo.get('stargazers_count', 0) * 10
    score += repo.get('forks_count', 0) * 5
    
    topics = [t.lower() for t in repo.get('topics', [])]
    name_lower = repo.get('name', '').lower()
    desc_lower = str(repo.get('description') or '').lower()
    
    target_keywords = ['ai', 'fullstack', 'full-stack', 'nextjs', 'python', 'pytorch', 'machine-learning', 'react', 'fastapi', 'llm', 'langchain', 'dart', 'flutter', 'java']
    
    for kw in target_keywords:
        if kw in topics or kw in name_lower or kw in desc_lower:
            score += 100
            
    return score

def fetch_top_repositories():
    username = os.getenv("GITHUB_REPOSITORY_OWNER") or "AZtheE1"
        
    url = f"https://api.github.com/users/{username}/repos?sort=updated&per_page=100"
    headers = {"Authorization": f"Bearer {os.getenv('GITHUB_TOKEN')}"} if os.getenv('GITHUB_TOKEN') else {}
    
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return "<!-- API Error: Failed to fetch repos -->"
    
    repos = response.json()
    valid_repos = [r for r in repos if not r.get('fork') and not r.get('private')]
    sorted_repos = sorted(valid_repos, key=get_repo_score, reverse=True)
    
    # Format into markdown timeline cards
    markdown_output = "| Project | Description | Metrics |\n| :--- | :--- | :--- |\n"
    for repo in sorted_repos[:4]:  # Top 4 projects
        name = repo['name']
        html_url = repo['html_url']
        desc = repo.get('description') or "Engineered full-stack or AI system."
        stars = repo.get('stargazers_count', 0)
        forks = repo.get('forks_count', 0)
        markdown_output += f"| **[{name}]({html_url})** | {desc} | ⭐ {stars} • 🍴 {forks} |\n"
        
    return markdown_output

def main():
    template_path = "templates/README.md.tpl"
    if not os.path.exists(template_path):
        return
        
    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()
        
    final_readme = template.replace("{{latest_projects}}", fetch_top_repositories())
    
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(final_readme)

if __name__ == "__main__":
    main()
