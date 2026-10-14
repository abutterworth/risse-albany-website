# RISSE website starter

A hello-world demonstration of an organization-owned, file-based website. It is separate from the current RISSE website and contains no archived site assets or private data.

## Live prototype

https://abutterworth.github.io/risse-albany-website/

## Edit in your browser

For a small wording change, edit `content/site.json` on GitHub and propose the change on a new branch. Open a pull request and wait for **Build and check** to pass. Review the wording before merging: merging into `main` publishes immediately.

An AI coding assistant can follow `AGENTS.md` and `patterns/page.md`. Copilot eligibility and usage billing are separate; this repository does not activate or buy AI subscriptions.

For a full preview, select **Code → Codespaces → Create codespace on main**. The container builds and checks the site automatically. In its terminal, run:

```sh
python3 -m http.server 8000 --directory dist
```

Open the forwarded port 8000 in the browser. Stop the preview and Codespace when finished; storage continues to count until a Codespace is deleted. Codespaces has account-dependent compute and storage allowances. You can edit and publish without Codespaces.

## Build without AI or Codespaces

Use Python 3.12 or newer. No pip or npm packages are required.

```sh
python3 scripts/build.py
python3 scripts/check.py
python3 -m http.server 8000 --directory dist
```

Open http://localhost:8000. The `dist/` folder contains the complete public website. Only that folder is deployed; source instructions and repository metadata are excluded from the hosting artifact.

## Files

- `content/site.json`: editable website copy.
- `templates/index.html`: page layout.
- `assets/style.css`: local styles; system fonts, no client JavaScript.
- `patterns/`: content and design examples.
- `AGENTS.md`: assistant editing and publication rules.
- `.devcontainer/`: repeatable browser development environment.
- `.github/workflows/pages.yml`: checks on pull requests and publishing on main.
- `.github/ISSUE_TEMPLATE/`: a simple update request form.

Pull requests run checks; a hosted pull-request preview is not included in this starter. Preview in Codespaces or locally before merging. Branch protection is not configured yet; repository administrators can make direct updates.

## Ownership, backups, and handoff

Keep the repository and domain under organization control when moving to production. Prefer a RISSE GitHub organization with two staff owners and separate individual accounts. Adam can retain collaborator access after transfer.

Repository transfer preserves history, but the GitHub Pages URL changes and old Pages URLs do not redirect automatically. Update this README's URL, check Pages settings, and review any domain/DNS configuration during transfer. No custom domain is configured here.

Keep an independent clone or download of the source, plus a built `dist/` backup. To move hosting, upload the contents of `dist/` to another static host. To restore editing, recover the source, install Python, build, and check using the commands above.

GitHub Pages and Actions have service limits. Domain renewal, external services, AI usage, and Codespaces may have separate costs. Donation and registration workflows remain outside this prototype.
