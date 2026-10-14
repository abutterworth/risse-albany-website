# Working on the RISSE website

This is a hello-world prototype, not RISSE's production website.

## Content and patterns
- Read README.md and patterns/page.md before editing.
- Edit copy in content/site.json; use templates for layout and assets/style.css for styling.
- Never invent service details, schedules, costs, eligibility, staff roles, or impact statistics.
- Preserve the prototype notice until an authorized production launch.
- Use relative asset URLs so the site works under a GitHub Pages repository path.
- Use semantic HTML, one h1, keyboard-accessible links, visible focus, and image alt text.
- Keep the public site free of JavaScript frameworks and remote font dependencies unless explicitly requested.
- Never add credentials, inquiries, donor information, or other private records to this repository.
- Donations and registrations belong in existing external services; do not build a payment system.

## Verification
Run `python3 scripts/build.py` and `python3 scripts/check.py` after editing.
Preview with `python3 -m http.server 8000 --directory dist`.
Report what changed, verification results, and any limitations.

## Publication
Prepare changes on a branch and open a pull request unless the user explicitly requests a direct update.
Merging into main publishes immediately. Do not merge or publish without user authorization.
A pull request runs checks but does not publish a preview automatically.
GitHub Actions permissions and review controls enforce access; these instructions alone are not a security boundary.
