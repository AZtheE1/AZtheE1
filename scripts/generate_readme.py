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
    elif 'c++' in lang_lower:
        return '<img src="https://img.shields.io/badge/C++-00599C?logo=cplusplus&logoColor=white" alt="C++" />'
    elif 'c#' in lang_lower:
        return '<img src="https://img.shields.io/badge/C%23-239120?logo=csharp&logoColor=white" alt="C#" />'
    else:
        return f'`{lang}`'

def get_repo_score(repo):
    """Calculate a score for sorting repositories based on stars, forks, and relevant AI/Full-Stack keywords."""
    score = repo.get('stargazers_count', 0) * 10
    score += repo.get('forks_count', 0) * 5
    
    topics = [t.lower() for t in repo.get('topics', [])]
    name_lower = repo.get('name', '').lower()
    desc_lower = str(repo.get('description') or '').lower()
    
    # Priority keywords
    target_keywords = ['ai', 'fullstack', 'full-stack', 'nextjs', 'python', 'pytorch', 'machine-learning', 'react', 'fastapi', 'llm', 'langchain', 'dart', 'flutter']
    
    for kw in target_keywords:
        if kw in topics or kw in name_lower or kw in desc_lower:
            score += 100
            
    return score

def fetch_top_repositories():
    username = os.getenv("GITHUB_REPOSITORY_OWNER")
    if not username:
        return "<!-- GITHUB_REPOSITORY_OWNER environment variable is missing -->"
        
    url = f"https://api.github.com/users/{username}/repos?sort=updated&per_page=100"
    headers = {"Authorization": f"Bearer {os.getenv('GITHUB_TOKEN')}"} if os.getenv('GITHUB_TOKEN') else {}
    
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        return "<!-- Failed to fetch repos from GitHub API -->"
    
    repos = response.json()
    # Filter out forks and private repositories
    valid_repos = [r for r in repos if not r.get('fork') and not r.get('private')]
    
    # Sort by custom AI & Fullstack score
    sorted_repos = sorted(valid_repos, key=get_repo_score, reverse=True)
    
    markdown_output = "| Project | Description | Tech / Language |\n| :--- | :--- | :--- |\n"
    
    for repo in sorted_repos[:5]:  # Select top 5 optimized repositories
        name = repo['name']
        html_url = repo['html_url']
        desc = repo.get('description')
        lang = repo.get('language')
        
        name_lower = name.lower()
        
        # Robust fallbacks for missing descriptions
        if not desc or desc.strip() == "":
            if 'dart' in name_lower or 'salesman' in name_lower:
                desc = "AI-powered sales assistant and analytics platform."
            elif 'ev' in name_lower or 'voting' in name_lower:
                desc = "Secure electronic voting system with real-time tallying."
            elif 'sdp' in name_lower:
                desc = "Software development project showcasing core engineering skills."
            else:
                desc = "Autonomous agent or scalable full-stack application."
                
        # Robust fallbacks for missing languages
        if not lang or lang.strip() == "":
            if 'dart' in name_lower or 'flutter' in name_lower:
                lang = "Dart"
            elif 'react' in name_lower or 'next' in name_lower:
                lang = "TypeScript"
            else:
                lang = "Python/TypeScript"
                
        lang_badge = get_language_badge(lang)
        markdown_output += f"| **[{name}]({html_url})** | {desc} | {lang_badge} |\n"
        
    return markdown_output

def main():
    template_path = "templates/README.md.tpl"
    if not os.path.exists(template_path):
        print(f"Error: Template not found at {template_path}")
        return
        
    with open(template_path, "r", encoding="utf-8") as f:
        template = f.read()
        
    projects_markdown = fetch_top_repositories()
    final_readme = template.replace("{{latest_projects}}", projects_markdown)
    
    with open("README.md", "w", encoding="utf-8") as f:
        f.write(final_readme)

if __name__ == "__main__":
    main()
