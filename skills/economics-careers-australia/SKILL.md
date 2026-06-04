---
name: economics-careers-australia
description: Drafts Sam Fox's "Economics Careers Australia" newsletter — a roundup of currently-open internships, graduate jobs, cadetships, vacationer/vacation programs, industry placements, and scholarships for economics students and graduates in Australia, covering the private sector (banks, asset managers, economics consultancies, strategy firms), public sector (federal and state Treasury, RBA, ABS, Productivity Commission, regulators), think tanks, universities, research institutes, nonprofits, and international organisations based in Australia. Each newsletter includes a filterable spreadsheet attachment. Trigger whenever Sam asks to draft, build, update, or refresh an "Economics Careers" newsletter, asks for current economics internships, graduate jobs, cadetships, or vacation programs in Australia, asks "what econ grad programs are open right now", or asks to add specific economics employers to a draft. Politically neutral; covers the full sector spectrum without ideological framing. Use this skill any time Sam mentions the phrase "Economics Careers" or references the regular economics-students-focused roundup.
---

# Economics Careers Australia Newsletter

A skill for drafting Sam Fox's recurring "Economics Careers Australia" newsletter. The newsletter goes to students studying or interested in economics and lists currently-open Australian internships, graduate jobs, cadetships, vacationer/vacation programs, industry placements, and scholarships across the full sector spectrum — politically neutral, not aligned to any ideological position.

## Critical principles (do not skip)

1. **Verify everything is genuinely open before listing it.** Application windows for economics grad programs, cadetships, vacation programs, and internships are tight and predictable per organisation — but they also shift cycles and pages. Verify each listing on the live page or careers portal before including.
2. **Direct URL fetching beats general search.** Most major employers (Treasury, RBA, Macquarie, Big 4 banks) post on their careers portals with dated rounds. Go to the careers page, not Google.
3. **Distinguish role types clearly.** Internships/vacationer programs, cadetships, graduate jobs, industry placements, and scholarships have different applicant pools, timelines, and durations. The spreadsheet has a Type column for this — never list a graduate role under "Internship".
4. **Be specific about discipline.** Economics is broad — some roles want quantitative modelling, some want policy writing, some want financial markets analysis. Where the live page specifies, capture that in the description.
5. **When uncertain, be honest.** Use "Apply early", "Rolling", "Annual cycle — check live page", or "Applications open" rather than guessing. Never invent a deadline.
6. **Drop anything you cannot verify as open** by the planned send date.
7. **Upcoming programs are separate.** If an opportunity is likely to open in the next 3 months, include it only in the `COMING UP SOON` watchlist, not in the currently-open sections or spreadsheet.
8. **Closed programs are not included** — neither in the currently-open email body nor in the spreadsheet.
9. **Politically neutral framing.** This is not the More Opportunities! newsletter. Don't import its ideological framing. Describe each employer factually — Treasury is "Australia's central economic policy department", Grattan is "Australia's leading domestic policy think tank", not "centrist" or "non-partisan" labels that could read as editorialising.

## Workflow

### Step 1: Find what's been covered before

Use the Gmail search tool with: `subject:"Economics Careers"` to find prior threads. Pull recent context with `messageFormat: FULL_CONTENT` to see what was featured. Programs from any previous newsletter can and should be re-featured for however many newsletters are needed if deadlines are still ahead, applications are still open, or the opportunity remains useful to readers. Do not suppress a program merely because it appeared in an earlier newsletter.

### Step 2: Build the candidate list

Read `references/organisations.md` for the full list of target organisations grouped by sector. The list covers:

- **Public sector — federal**: core economics agencies and regulators such as Treasury, RBA, Productivity Commission, ABS, ACCC, APRA, ASIC, ATO, Finance, DFAT, and related economic policy departments. This is not every Australian Government agency.
- **Public sector — state**: NSW, VIC, QLD, WA, SA, TAS, ACT, NT Treasuries
- **Private sector — banks**: CBA, ANZ, NAB, Westpac, Macquarie, plus investment banks
- **Private sector — asset managers**: Future Fund, BlackRock, Magellan, etc.
- **Economics consultancies**: Frontier Economics, Deloitte Access Economics, NERA, ACIL Allen, etc.
- **Strategy and Big 4 consulting**: McKinsey, Bain, BCG, Deloitte, PwC, EY, KPMG
- **Think tanks**: Grattan, CEDA, Lowy, CIS, IPA, Mitchell, Australia Institute, Per Capita
- **Universities and research institutes**: economics schools, business schools, public policy schools, research centres, RA roles, tutoring, internships, cadetships, and graduate programs
- **Nonprofits**: World Vision, Oxfam, CARE, ACOSS
- **International orgs in Australia**: OECD, World Bank, ADB

Search live employer pages for all economics-relevant early-career entry points, including keywords such as `internship`, `intern`, `graduate program`, `graduate job`, `graduate economist`, `cadetship`, `cadet`, `vacation program`, `vacationer`, `summer vacation`, `industry placement`, and `scholarship`.

For opportunities that are not yet open but are likely to open in the next 3 months, capture them in `upcoming_programs` with:
- Organisation
- Program name
- Sector
- Expected window (e.g. "Expected June-July 2026", "Applications usually open in July")
- A short note explaining why students should watch it
- URL

Do not put upcoming programs in the spreadsheet.

For each candidate program or role, capture:
- Organisation
- Program name (Graduate Program, Cadetship, Summer Internship, Vacationer Program, Industry Placement, etc.)
- Type (Internship / Graduate Program / Graduate Job / Cadetship / Vacationer Program / Industry Placement / Scholarship / Other)
- Application status — only "open" entries make it into the newsletter and spreadsheet
- Specific deadline if visible on the live page (otherwise: rolling, apply early, etc.)
- Duration
- Paid? (Yes — amount/grade; No — rare for econ roles)
- Sector (Federal Government / State Government / Banks & Investment Banks / Asset Managers & Super Funds / Economics Consultancies / Strategy & Big 4 Consulting / Think Tanks & Policy Institutes / Universities & Research Institutes / Nonprofits & NGOs / International Organisations)
- Location (Canberra / Sydney / Melbourne / Multiple / etc.)
- Eligibility quirks (Australian citizenship required? Final-year only? Honours required?)
- A short description paragraph (3–5 sentences)
- Apply URL

### Step 3: Verify everything

Cross-check each program. Read `references/known-traps.md` before finalising — it lists employer-specific verification gotchas (Treasury's two streams, RBA's economist vs cadetship, Macquarie's penultimate vs final year, etc.).

### Step 4: Draft the newsletter email

Read `references/template.md`. Subject is `Economics Careers Australia!`. Sections in this order:

1. 🏛️ Federal Government & Regulators
2. 🏛️ State Government
3. 🏦 Banks & Investment Banks
4. 💼 Asset Managers
5. 📊 Economics Consultancies
6. 🧠 Strategy & Big 4 Consulting
7. 🔬 Think Tanks
8. 🎓 Universities & Research Institutes
9. 🌱 Nonprofits
10. 🌐 International Organisations

After the currently-open sections, include `🗓️ COMING UP SOON` if there are useful upcoming programs expected in the next 3 months. Keep it short and clearly labelled as a watchlist.

Skip any section with no currently-open programs.

### Step 5: Generate the spreadsheet

Read `references/spreadsheet-schema.md` for the column structure. Save as `economics-careers-australia-YYYY-MM-DD.xlsx` in `/mnt/user-data/outputs/`.

### Step 6: Output

Use `message_compose_v1` with `kind: email` and the subject. Use `present_files` for the spreadsheet. Give Sam a summary of what was kept, dropped, and added.

## Tone & style

- Direct and factual — economics students respond to specifics (deadlines, pay, role type, role focus) more than colour.
- Each program gets 3–5 sentences. Don't pad.
- Use specific deadlines where verified; honest hedges where not.
- Section header format: `🏛️ FEDERAL GOVERNMENT & REGULATORS` (emoji, space, all caps).
- Program header format: `Organisation — Program Name | Deadline or Status`
- URLs go on their own line, no markdown link syntax.
- Sign off as "Best, Sam" — Gmail auto-appends signature.
- **Politically neutral.** Describe employers by what they do, not where they sit ideologically.

## File map

- `references/organisations.md` — list of target organisations grouped by sector
- `references/template.md` — email template with intro, opt-out, signup link, sign-off
- `references/spreadsheet-schema.md` — column structure for the xlsx attachment
- `references/known-traps.md` — employer-specific verification gotchas
