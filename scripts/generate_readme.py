import os
import requests

def fetch_top_repositories():
    username = os.getenv("GITHUB_REPOSITORY_OWNER")
    url = f"https://api.github.com/users/{username}/repos?sort=updated&per_page=100"
    headers = {"Authorization": f"Bearer {os.getenv('GITHUB_TOKEN')}"} if os.getenv('GITHUB_TOKEN') else {}
    
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return "<!-- Failed to fetch repos -->"
    
    repos = response.json()
    # Filter out forks and sort by stars/activity
    valid_repos = [r for r in repos if not r.get('fork') and not r.get('private')]
    sorted_repos = sorted(valid_repos, key=lambda x: (x.get('stargazers_count', 0), x.get('forks_count', 0)), reverse=True)
    
    markdown_output = "| Project | Description | Tech / Language |\n| :--- | :--- | :--- |\n"
    for repo in sorted_repos[:5]:  # Select top 5 repositories automatically
        name = repo['name']
        html_url = repo['html_url']
        desc = repo.get('description') or "No description provided."
        lang = repo.get('language') or "Python/TS"
        markdown_output += f"| **[{name}]({html_url})** | {desc} | `{lang}` |\n"
        
    return markdown_output

def main():
    # Make sure we use absolute paths or path relative to the repo root since the action runs at the repo root.
    with open("templates/README.md.tpl", "r", encoding="utf-8") as f:
        template = f.read()
        
    projects_markdown = fetch_top_repositories()
    final_readme = template.replace("{{latest_projects}}", projects_markdown)
    
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(final_readme)

if __name__ == "__main__":
    main()
