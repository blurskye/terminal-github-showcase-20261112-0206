# Terminal workflow

This is a synthetic public playground; every issue and pull request is demo data.

Install the upstream tools:

```sh
gh extension install dlvhdr/gh-dash
gh extension install dlvhdr/gh-enhance
# Install dlvhdr/diffnav and dandavison/delta from their official releases.
gh dash --config .gh-dash.yml
```

The preset uses a Tokyo Night-inspired palette, compact tables, a 52% right preview, and repository-scoped PR/issue sections. It is a curated preference, not an objectively best theme.

- `e`: expand description
- `[` / `]`: activity, commits, checks and changed-file tabs
- `d`: diffnav + delta
- `T`: ENHANCE for the selected PR checks
- `Ctrl+e`: ENHANCE repository runs
- `s`: switch PRs / issues
- `P`: move preview between right and bottom

GitHub workflow publishing requires a gh login with the workflow scope. The prepared demo workflows use read-only contents permissions and short job timeouts.
