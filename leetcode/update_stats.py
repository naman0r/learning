#!/usr/bin/env python3
"""
Automatically count LeetCode problems and update README.md with stats
"""

import os
import re
from pathlib import Path

def count_problems():
    """Count problems by difficulty level"""
    problems_dir = Path("problems")
    
    if not problems_dir.exists():
        print("Error: problems/ directory not found")
        return None
    
    # Count different difficulty levels
    easy_count = len(list(problems_dir.glob("*_easy.py")))
    medium_count = len(list(problems_dir.glob("*_medium.py"))) + len(list(problems_dir.glob("*_med.py")))
    hard_count = len(list(problems_dir.glob("*_hard.py")))
    
    # Count total Python files
    total_py_files = len(list(problems_dir.glob("*.py")))
    
    return {
        'easy': easy_count,
        'medium': medium_count,
        'hard': hard_count,
        'total': total_py_files
    }

def update_readme(stats):
    """Update README.md with current statistics"""
    readme_path = Path("README.md")
    
    if not readme_path.exists():
        print("Error: README.md not found")
        return False
    
    # Read current README content
    with open(readme_path, 'r') as f:
        content = f.read()
    
    # Create stats section
    stats_section = f"""
## 📊 Problem Statistics

- **Total Problems Solved**: {stats['total']}
- **Easy**: {stats['easy']} problems
- **Medium**: {stats['medium']} problems  
- **Hard**: {stats['hard']} problems

*Last updated: {__import__('datetime').datetime.now().strftime('%Y-%m-%d %H:%M:%S')}*

---
"""
    
    # Check if stats section already exists
    stats_pattern = r'## 📊 Problem Statistics.*?---\n'
    
    if re.search(stats_pattern, content, re.DOTALL):
        # Replace existing stats section
        new_content = re.sub(stats_pattern, stats_section, content, flags=re.DOTALL)
    else:
        # Add stats section after the title
        lines = content.split('\n')
        # Find the first line (title) and insert stats after it
        if lines and lines[0].startswith('##'):
            lines.insert(1, stats_section)
            new_content = '\n'.join(lines)
        else:
            # If no title found, add at the beginning
            new_content = stats_section + '\n' + content
    
    # Write updated content back
    with open(readme_path, 'w') as f:
        f.write(new_content)
    
    return True

def main():
    """Main function to run the stats update"""
    print("🔍 Counting LeetCode problems...")
    
    stats = count_problems()
    if stats is None:
        return
    
    print(f"📊 Found {stats['total']} total problems:")
    print(f"   Easy: {stats['easy']}")
    print(f"   Medium: {stats['medium']}")
    print(f"   Hard: {stats['hard']}")
    
    print("\n📝 Updating README.md...")
    
    if update_readme(stats):
        print("✅ README.md updated successfully!")
    else:
        print("❌ Failed to update README.md")

if __name__ == "__main__":
    main() 