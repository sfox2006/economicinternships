# Spreadsheet Schema — Economics Careers Australia

Every "Economics Careers Australia" newsletter is accompanied by an Excel spreadsheet (`.xlsx`) listing every currently-open program. Subscribers can filter by sector, type, deadline, location, etc.

## File naming

`economics-careers-australia-YYYY-MM-DD.xlsx` (use the send date).

## Columns

| # | Column name | Type | Allowed values / notes |
|---|---|---|---|
| 1 | Sector | Fixed list | Federal Government / State Government / Banks & Investment Banks / Asset Managers & Super Funds / Economics Consultancies / Strategy & Big 4 Consulting / Think Tanks & Policy Institutes / Business Lobby Groups & Unions / Nonprofits & NGOs / International Organisations / Other |
| 2 | Organisation | Text | Full name (e.g. "Reserve Bank of Australia") |
| 3 | Program name | Text | Specific program (e.g. "2027 Graduate Program — Economist Stream") |
| 4 | Type | Fixed list | Graduate Program / Cadetship / Summer Vacation / Internship / Industry Placement / Scholarship / Other |
| 5 | Deadline | Text | Specific date `DD Mon YYYY`, or one of: "Rolling", "Apply early", "Annual cycle — check live page", "Applications open". Never invent a deadline. |
| 6 | Location | Text | "Sydney", "Melbourne", "Canberra", "Multiple locations", etc. |
| 7 | Duration | Text | e.g. "12 months", "10-12 weeks", "Semester-long", "2 years rotational" |
| 8 | Paid? | Text | "Yes — ~$95,000" / "Yes — APS3-5" / "Yes — hourly" / "Stipend only" / "Unpaid" |
| 9 | Australian citizenship required? | Fixed list | Yes / No / Some restrictions |
| 10 | Year of study eligibility | Text | "Penultimate year", "Final year + recent graduates", "Honours/postgrad required", "Any year", etc. |
| 11 | Notes | Text (optional) | Other key caveats — security clearance, specific majors required, exam/aptitude tests, etc. |
| 12 | Apply URL | URL | Direct link to the application page |

## Rules

- **Only currently-open programs** are listed.
- **One row per program** — Treasury Graduate Program and Treasury Summer Vacation are separate rows.
- **Sort order**: Sector (in the order listed above), then Type (Graduate Programs first), then deadline (sooner first).
- **Header row**: Bold, freeze top row, enable Excel auto-filter so users can sort/filter.

## Implementation

Use the xlsx skill at `/mnt/skills/public/xlsx/SKILL.md` to generate the file.

## Example rows

```
Sector              | Organisation               | Program name                          | Type              | Deadline       | Location | Duration | Paid?              | Citizen? | Year of study           | Notes                              | Apply URL
Federal Government  | Reserve Bank of Australia  | 2027 Graduate Program - Economist     | Graduate Program  | 14 Mar 2026    | Sydney   | 12 months | Yes — ~$95,000     | Yes      | Final year + Honours    | Two streams: Economist, Analyst    | https://www.rba.gov.au/careers/graduate.html
Big 4 Bank          | Commonwealth Bank          | 2026 Summer Internship                | Summer Vacation   | Rolling        | Multiple | 10-12 wks | Yes — competitive  | No       | Penultimate year        | Several streams; finance focus     | https://www.commbank.com.au/careers/students.html
Economics Consulting| Frontier Economics         | 2027 Graduate Program                 | Graduate Program  | 31 Aug 2026    | Sydney   | Full-time | Yes — competitive  | No       | Final year + Honours    | Quant skills valued                | https://www.frontier-economics.com.au/careers
```
