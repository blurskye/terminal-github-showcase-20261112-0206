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
- `s`: cycle PRs → issues → notifications → PRs (gh-dash v4.26.2)
- `P`: move preview between right and bottom

The demo contains real passing and deliberately failing GitHub Actions runs. Workflows use read-only contents permissions and three-minute timeouts. Publishing workflow files requires an authorized SSH identity or HTTPS credentials with the `workflow` scope.


## Recorded setup

- gh-dash **v4.26.2**; diffnav **v0.13.1**; Delta **0.20.1**; ENHANCE **v0.8.1**.
- Kitty at 190 columns × 44 rows, JetBrains Mono Nerd Font.
- Terminal background `#1a1b26`, foreground `#c0caf5`; ENHANCE's Dracula theme.
- Unified diffs keep both added files and modifications readable.

From this clone, configure Delta locally (not globally):

```sh
git config --local delta.syntax-theme Dracula
git config --local delta.dark true
```

`Ctrl+c` returns from ENHANCE to gh-dash; `q` returns from diffnav.
Use a Nerd Font for the status icons. PR #18 intentionally fails its retry-limit test; the failed preview run intentionally reports HTTP 503. No real deployment is attempted.

Observed upstream quirk: ENHANCE v0.8.1 retains some previous step rows when switching runs in the repository view. The preview failure log shown in the recording belongs to the selected preview run; its actual workflow has four steps.
