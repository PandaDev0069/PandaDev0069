# Testing Instructions for Custom GitHub Streak Stats

## After PR Merge

Once this PR is merged to the main branch, follow these steps to test and verify the custom streak stats:

### 1. Automatic Workflow Trigger

The workflow will automatically run when the PR is merged to `main` because of this trigger:
```yaml
on:
  push:
    branches:
    - main
```

### 2. Manual Workflow Trigger (Recommended for immediate testing)

1. Go to your repository: https://github.com/PandaDev0069/PandaDev0069
2. Click on the **Actions** tab
3. In the left sidebar, select **Generate GitHub Streak Stats**
4. Click the **Run workflow** button (top right)
5. Select branch: `main`
6. Click **Run workflow**

### 3. Monitor the Workflow

1. Watch the workflow run in real-time
2. Check for any errors in the workflow logs
3. The workflow should complete in ~1-2 minutes

### 4. Verify the Output

After successful workflow completion:

1. Navigate to the `output` branch:
   - https://github.com/PandaDev0069/PandaDev0069/tree/output

2. Check for these files:
   - `github-streak-stats.svg`
   - `github-streak-stats-dark.svg`

3. View the raw SVG:
   - https://raw.githubusercontent.com/PandaDev0069/PandaDev0069/output/github-streak-stats-dark.svg

### 5. Verify README Display

1. Go to your main README: https://github.com/PandaDev0069/PandaDev0069
2. Scroll to the **GitHub Statistics** section
3. Verify the streak stats badge is displaying correctly
4. It should show:
   - Current Streak with 🔥
   - Total Contributions for the current year
   - Longest Streak with 🏆
   - Tokyo Night theme colors

### 6. Test Manual Updates

To test manual updates:
1. Make a commit to any repository
2. Wait a few minutes for GitHub to process
3. Manually trigger the workflow again
4. Verify the stats update with new data

### Expected Results

✅ Workflow completes successfully
✅ SVG files appear in `output` branch
✅ README displays the custom streak stats badge
✅ Stats show accurate GitHub contribution data
✅ Theme matches Tokyo Night colors
✅ Badge updates daily automatically

### Troubleshooting

If the workflow fails:

1. **Check workflow logs** for error messages
2. **Verify GITHUB_TOKEN** has proper permissions (should be automatic)
3. **Check Python syntax** with: `python3 -m py_compile generate_streak_stats.py`
4. **Verify API response** - GitHub API might be temporarily unavailable

If badge doesn't display:

1. **Check output branch exists** and has the SVG files
2. **Verify URL** in README.md matches: `https://raw.githubusercontent.com/PandaDev0069/PandaDev0069/output/github-streak-stats-dark.svg`
3. **Clear browser cache** to see updated badge
4. **Wait a few minutes** for GitHub CDN to update

### Customization

To customize the streak stats:

1. Edit `generate_streak_stats.py`
2. Modify colors in the `generate_svg()` function
3. Adjust SVG dimensions (currently 495x195)
4. Change update frequency in `.github/workflows/streak-stats.yml`
5. Commit and push changes
6. Manually trigger workflow to see updates

### Scheduled Updates

The workflow runs automatically every day at midnight UTC:
```yaml
schedule:
  - cron: "0 0 * * *"
```

No manual intervention needed after initial setup!

## Support

For issues or questions, refer to:
- `STREAK_STATS_README.md` - Detailed documentation
- `generate_streak_stats.py` - Code comments
- `.github/workflows/streak-stats.yml` - Workflow configuration
