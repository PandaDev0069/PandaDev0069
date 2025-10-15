#!/usr/bin/env python3
"""
Custom GitHub Streak Stats Generator
Generates an SVG image showing GitHub contribution streak statistics
"""

import os
import sys
from datetime import datetime, timedelta
import requests
import json

GITHUB_TOKEN = os.environ.get('GITHUB_TOKEN')
GITHUB_USERNAME = os.environ.get('GITHUB_USERNAME', 'PandaDev0069')

def get_contribution_data():
    """Fetch contribution data from GitHub GraphQL API"""
    headers = {
        'Authorization': f'Bearer {GITHUB_TOKEN}',
        'Content-Type': 'application/json',
    }
    
    # Get the current year and last year for comprehensive data
    current_year = datetime.now().year
    last_year = current_year - 1
    
    query = """
    query($username: String!, $from: DateTime!, $to: DateTime!) {
      user(login: $username) {
        contributionsCollection(from: $from, to: $to) {
          contributionCalendar {
            totalContributions
            weeks {
              contributionDays {
                contributionCount
                date
              }
            }
          }
        }
      }
    }
    """
    
    # Fetch contributions for the last year
    from_date = f"{last_year}-01-01T00:00:00Z"
    to_date = f"{current_year}-12-31T23:59:59Z"
    
    variables = {
        'username': GITHUB_USERNAME,
        'from': from_date,
        'to': to_date
    }
    
    response = requests.post(
        'https://api.github.com/graphql',
        json={'query': query, 'variables': variables},
        headers=headers
    )
    
    if response.status_code != 200:
        print(f"Error fetching data: {response.status_code}")
        print(response.text)
        sys.exit(1)
    
    data = response.json()
    return data['data']['user']['contributionsCollection']['contributionCalendar']

def calculate_streaks(contribution_calendar):
    """Calculate current streak, longest streak, and total contributions"""
    weeks = contribution_calendar['weeks']
    total_contributions = contribution_calendar['totalContributions']
    
    # Flatten all contribution days
    all_days = []
    for week in weeks:
        all_days.extend(week['contributionDays'])
    
    # Sort by date to ensure chronological order
    all_days.sort(key=lambda x: x['date'])
    
    # Calculate current streak (working backwards from today or most recent contribution)
    current_streak = 0
    today = datetime.now().date()
    
    # Find the most recent day in the data
    most_recent_date = None
    for day in reversed(all_days):
        day_date = datetime.strptime(day['date'], '%Y-%m-%d').date()
        if day_date <= today:
            most_recent_date = day_date
            break
    
    if most_recent_date:
        # Check if today or yesterday had contributions (streak is still active)
        check_date = today
        streak_active = False
        
        # Allow for today and yesterday to maintain streak
        for i in range(2):
            target_date = today - timedelta(days=i)
            for day in reversed(all_days):
                day_date = datetime.strptime(day['date'], '%Y-%m-%d').date()
                if day_date == target_date and day['contributionCount'] > 0:
                    streak_active = True
                    check_date = target_date
                    break
            if streak_active:
                break
        
        if streak_active:
            # Count backwards from the streak start
            for day in reversed(all_days):
                day_date = datetime.strptime(day['date'], '%Y-%m-%d').date()
                if day_date > check_date:
                    continue
                if day_date < check_date - timedelta(days=current_streak):
                    break
                if day['contributionCount'] > 0:
                    current_streak += 1
                else:
                    break
    
    # Calculate longest streak
    longest_streak = 0
    temp_streak = 0
    
    for day in all_days:
        if day['contributionCount'] > 0:
            temp_streak += 1
            longest_streak = max(longest_streak, temp_streak)
        else:
            temp_streak = 0
    
    # Get contributions for current year
    current_year = datetime.now().year
    current_year_contributions = sum(
        day['contributionCount'] 
        for day in all_days 
        if day['date'].startswith(str(current_year))
    )
    
    return {
        'current_streak': current_streak,
        'longest_streak': longest_streak,
        'total_contributions': total_contributions,
        'current_year_contributions': current_year_contributions
    }

def generate_svg(stats):
    """Generate SVG visualization of streak stats"""
    
    # Tokyo Night theme colors
    bg_color = "#1a1b26"
    border_color = "#414868"
    text_color = "#a9b1d6"
    accent_color = "#7aa2f7"
    highlight_color = "#bb9af7"
    fire_emoji = "🔥"
    
    svg = f'''<svg width="495" height="195" xmlns="http://www.w3.org/2000/svg">
  <defs>
    <style>
      .stat-text {{ fill: {text_color}; font-family: 'Segoe UI', Ubuntu, sans-serif; font-size: 14px; }}
      .stat-value {{ fill: {accent_color}; font-family: 'Segoe UI', Ubuntu, sans-serif; font-size: 28px; font-weight: bold; }}
      .stat-label {{ fill: {text_color}; font-family: 'Segoe UI', Ubuntu, sans-serif; font-size: 12px; opacity: 0.8; }}
      .title {{ fill: {highlight_color}; font-family: 'Segoe UI', Ubuntu, sans-serif; font-size: 18px; font-weight: bold; }}
    </style>
  </defs>
  
  <!-- Background -->
  <rect width="495" height="195" rx="4.5" fill="{bg_color}"/>
  
  <!-- Title -->
  <text x="247.5" y="30" class="title" text-anchor="middle">GitHub Streak Stats</text>
  
  <!-- Current Streak -->
  <g transform="translate(40, 70)">
    <text x="0" y="0" class="stat-value">{stats['current_streak']}</text>
    <text x="0" y="20" class="stat-label">Current Streak</text>
    <text x="0" y="35" class="stat-text">{fire_emoji} days</text>
  </g>
  
  <!-- Total Contributions -->
  <g transform="translate(185, 70)">
    <text x="0" y="0" class="stat-value">{stats['current_year_contributions']}</text>
    <text x="0" y="20" class="stat-label">Total Contributions</text>
    <text x="0" y="35" class="stat-text">in {datetime.now().year}</text>
  </g>
  
  <!-- Longest Streak -->
  <g transform="translate(370, 70)">
    <text x="0" y="0" class="stat-value">{stats['longest_streak']}</text>
    <text x="0" y="20" class="stat-label">Longest Streak</text>
    <text x="0" y="35" class="stat-text">🏆 days</text>
  </g>
  
  <!-- Footer -->
  <text x="247.5" y="175" class="stat-label" text-anchor="middle">Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M UTC')}</text>
</svg>'''
    
    return svg

def main():
    if not GITHUB_TOKEN:
        print("Error: GITHUB_TOKEN environment variable is required")
        sys.exit(1)
    
    print(f"Fetching contribution data for {GITHUB_USERNAME}...")
    contribution_calendar = get_contribution_data()
    
    print("Calculating streak statistics...")
    stats = calculate_streaks(contribution_calendar)
    
    print(f"Current Streak: {stats['current_streak']} days")
    print(f"Longest Streak: {stats['longest_streak']} days")
    print(f"Total Contributions ({datetime.now().year}): {stats['current_year_contributions']}")
    
    print("Generating SVG...")
    svg_content = generate_svg(stats)
    
    # Ensure output directory exists
    os.makedirs('dist', exist_ok=True)
    
    # Save SVG files
    output_files = [
        'dist/github-streak-stats.svg',
        'dist/github-streak-stats-dark.svg'
    ]
    
    for output_file in output_files:
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(svg_content)
        print(f"Saved: {output_file}")
    
    print("Done!")

if __name__ == '__main__':
    main()
