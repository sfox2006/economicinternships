# Economics Careers Australia Bot

A monthly automation that drafts Sam's "Economics Careers Australia!" student newsletter, saves it as a Gmail draft, and emails Sam to review. Nothing is ever sent automatically.

## What it does

On the 1st of every month, or whenever Sam triggers it manually, a GitHub Actions job runs `agent.py`. The script:

1. Reads the skill files in `skills/economics-careers-australia/`.
2. Searches Sam's Gmail for the most recent prior Economics Careers newsletter.
3. Checks listed employer application pages for currently-open internships and graduate programs.
4. Builds the email body and a filterable `.xlsx` spreadsheet.
5. Saves the email as a Gmail draft with the spreadsheet attached.
6. Sends Sam a notification email with the draft link.

Sam opens the draft, reviews or edits it, and sends it manually.

## What it does not do

- Send the newsletter directly.
- Add or remove employers from the canonical list.
- Guess deadlines when the live page is unclear.
- Sync newsletter sign-ups from Google Forms.

## One-time setup

### 1. Anthropic API key

Create an API key at https://console.anthropic.com.

### 2. Google Cloud project for Gmail

1. Go to https://console.cloud.google.com and create or select a project.
2. Enable the Gmail API.
3. Configure the OAuth consent screen as External and add yourself as a Test User.
4. Create an OAuth client ID of type Desktop application.
5. Download the OAuth client JSON.

### 3. Get a Gmail refresh token

Run this locally:

```bash
git clone https://github.com/sfox2006/economicinternships.git
cd economicinternships
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt

# Save the downloaded OAuth JSON as credentials.json in this folder.
python gmail_auth.py
```

The helper prints the client ID, client secret, and refresh token.

### 4. Add GitHub Actions secrets

In the GitHub repo, go to Settings -> Secrets and variables -> Actions -> New repository secret. Add:

| Name | Value |
|---|---|
| `ANTHROPIC_API_KEY` | Your Anthropic API key |
| `GMAIL_CLIENT_ID` | From the OAuth helper |
| `GMAIL_CLIENT_SECRET` | From the OAuth helper |
| `GMAIL_REFRESH_TOKEN` | From the OAuth helper |
| `SAM_EMAIL` | The Gmail address where drafts should be created |

### 5. Run it

The workflow runs monthly. You can also trigger it manually from Actions -> Monthly Economics Careers Newsletter Draft -> Run workflow.

## Running locally

```bash
cp .env.example .env
# Fill in the secrets in .env, then export them for your shell.
python agent.py --newsletter economics-careers
```

Drafts appear in Gmail Drafts. Generated spreadsheets are written to `output/`.

## Updating the newsletter docs

Edit files in `skills/economics-careers-australia/references/`:

- `organisations.md`: employer and program source list.
- `template.md`: email structure and wording.
- `spreadsheet-schema.md`: spreadsheet columns and allowed values.
- `known-traps.md`: employer-specific verification notes.

If spreadsheet columns change, also update the `ECONOMICS_CAREERS` config in `configs.py`.

## File map

```text
.
|-- README.md
|-- requirements.txt
|-- agent.py
|-- configs.py
|-- gmail_auth.py
|-- .env.example
|-- .gitignore
|-- .github/
|   `-- workflows/
|       `-- monthly-newsletter.yml
`-- skills/
    `-- economics-careers-australia/
        |-- SKILL.md
        `-- references/
            |-- organisations.md
            |-- template.md
            |-- spreadsheet-schema.md
            `-- known-traps.md
```
