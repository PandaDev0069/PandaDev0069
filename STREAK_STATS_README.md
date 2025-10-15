# Custom GitHub Streak Stats Generator

This is a custom implementation of GitHub streak statistics that generates an SVG badge showing:
- **Current Streak**: Number of consecutive days with contributions
- **Total Contributions**: Contributions in the current year
- **Longest Streak**: The longest streak of consecutive days with contributions

## Why Custom?

The external streak stats services (like github-readme-streak-stats.herokuapp.com) can be unreliable due to:
- Server downtime
- Rate limiting
- Dependency on third-party services
- Privacy concerns

This custom solution:
- ✅ Runs directly in your GitHub repository using GitHub Actions
- ✅ Uses official GitHub GraphQL API for accurate data
- ✅ Generates SVG locally without external dependencies
- ✅ Updates automatically daily via scheduled workflow
- ✅ Matches the Tokyo Night theme consistently
- ✅ Full control and customization

## How It Works

1. **GitHub Action Workflow** (`.github/workflows/streak-stats.yml`):
   - Runs daily at midnight UTC
   - Can be manually triggered
   - Triggers on push to main branch

2. **Python Script** (`generate_streak_stats.py`):
   - Fetches contribution data from GitHub GraphQL API
   - Calculates streaks and statistics
   - Generates Tokyo Night themed SVG
   - Saves to `dist/` directory

3. **Output Branch**:
   - SVG files are pushed to the `output` branch
   - Accessible via raw GitHub URLs
   - Used in README.md

## Configuration

The generator can be customized by editing `generate_streak_stats.py`:
- Colors (Tokyo Night theme by default)
- SVG dimensions
- Statistics displayed
- Update frequency (in workflow file)

## Manual Trigger

To manually update the stats:
1. Go to **Actions** tab
2. Select **Generate GitHub Streak Stats** workflow
3. Click **Run workflow**

## Files

- `generate_streak_stats.py` - Main Python script
- `.github/workflows/streak-stats.yml` - GitHub Actions workflow
- Output: `https://raw.githubusercontent.com/PandaDev0069/PandaDev0069/output/github-streak-stats-dark.svg`

## Requirements

- GitHub repository with Actions enabled
- `GITHUB_TOKEN` (automatically provided by GitHub Actions)
- Python 3.x with `requests` library
