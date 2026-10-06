import os
import requests

def fetch_top_repositories():
    username = os.getenv("GITHUB_REPOSITORY_OWNER")
    if not username:
        return "<!-- Missing owner -->"
        
    url = f"https://api.github.com/users/{username}/repos?sort=updated&per_page=100"
    headers = {"Authorization": f"Bearer {os.getenv('GITHUB_TOKEN')}"} if os.getenv('GITHUB_TOKEN') else {}
    
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return "<!-- API Error -->"
    
    repos = response.json()
    valid_repos = [r for r in repos if not r.get('fork') and not r.get('private')]
    sorted_repos = sorted(valid_repos, key=lambda x: x.get('stargazers_count', 0), reverse=True)
    
    markdown_output = "| Project | Description | Metrics |\n| :--- | :--- | :--- |\n"
    for repo in sorted_repos[:4]:  # Top 4 timeline cards
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
