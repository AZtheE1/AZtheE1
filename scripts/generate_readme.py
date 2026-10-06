import os
import requests

def get_language_badge(lang):
    if not lang:
        return ""
    lang_lower = lang.lower()
    if 'dart' in lang_lower:
        return '<img src="https://img.shields.io/badge/Dart-0175C2?logo=dart&logoColor=white" alt="Dart" />'
    elif 'typescript' in lang_lower:
        return '<img src="https://img.shields.io/badge/TypeScript-007ACC?logo=typescript&logoColor=white" alt="TypeScript" />'
    elif 'python' in lang_lower:
        return '<img src="https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white" alt="Python" />'
    elif 'javascript' in lang_lower:
        return '<img src="https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black" alt="JavaScript" />'
    elif 'html' in lang_lower:
        return '<img src="https://img.shields.io/badge/HTML-E34F26?logo=html5&logoColor=white" alt="HTML" />'
    elif 'java' in lang_lower and 'javascript' not in lang_lower:
        return '<img src="https://img.shields.io/badge/Java-ED8B00?logo=openjdk&logoColor=white" alt="Java" />'
    else:
        return f'`{lang}`'

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
        desc = repo.get('description')
        lang = repo.get('language')
        
        name_lower = name.lower()
        
        # Smart fallbacks for specific known projects if metadata is missing
        if not desc:
            if 'dart' in name_lower or 'salesman' in name_lower:
                desc = "AI-powered sales assistant and analytics platform."
            elif 'ev' in name_lower or 'voting' in name_lower:
                desc = "Secure electronic voting system with real-time tallying."
            elif 'sdp' in name_lower:
                desc = "Software development project showcasing core engineering skills."
            else:
                desc = "Autonomous agent or full-stack application."
                
        if not lang:
            if 'dart' in name_lower or 'flutter' in name_lower:
                lang = "Dart"
            else:
                lang = "TypeScript"
                
        lang_badge = get_language_badge(lang)
        markdown_output += f"| **[{name}]({html_url})** | {desc} | {lang_badge} |\n"
        
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
