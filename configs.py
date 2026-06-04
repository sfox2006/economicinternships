"""
Newsletter configuration for the Economics Careers Australia bot.
"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class NewsletterConfig:
    name: str
    subject: str
    skill_dir: str
    filename_prefix: str
    section_field: str
    section_order: list[str]
    section_emojis: dict[str, str]
    spreadsheet_headers: list[str]
    spreadsheet_field_order: list[str]
    column_widths: dict[str, int]


ECONOMICS_CAREERS = NewsletterConfig(
    name="economics-careers",
    subject="Economics Careers Australia!",
    skill_dir="skills/economics-careers-australia",
    filename_prefix="economics-careers-australia",
    section_field="sector",
    section_order=[
        "Federal Government",
        "State Government",
        "Banks & Investment Banks",
        "Asset Managers & Super Funds",
        "Economics Consultancies",
        "Strategy & Big 4 Consulting",
        "Think Tanks & Policy Institutes",
        "Business Lobby Groups & Unions",
        "Nonprofits & NGOs",
        "International Organisations",
    ],
    section_emojis={
        "Federal Government": "\U0001f3db\ufe0f",
        "State Government": "\U0001f3db\ufe0f",
        "Banks & Investment Banks": "\U0001f3e6",
        "Asset Managers & Super Funds": "\U0001f4bc",
        "Economics Consultancies": "\U0001f4ca",
        "Strategy & Big 4 Consulting": "\U0001f9e0",
        "Think Tanks & Policy Institutes": "\U0001f52c",
        "Business Lobby Groups & Unions": "\U0001f4e3",
        "Nonprofits & NGOs": "\U0001f331",
        "International Organisations": "\U0001f310",
    },
    spreadsheet_headers=[
        "Sector",
        "Organisation",
        "Program name",
        "Type",
        "Deadline",
        "Location",
        "Duration",
        "Paid?",
        "Australian citizenship required?",
        "Year of study eligibility",
        "Notes",
        "Apply URL",
    ],
    spreadsheet_field_order=[
        "sector",
        "organisation",
        "program_name",
        "type",
        "deadline",
        "location",
        "duration",
        "paid",
        "citizenship",
        "year_of_study",
        "notes",
        "url",
    ],
    column_widths={
        "A": 22,
        "B": 28,
        "C": 38,
        "D": 18,
        "E": 22,
        "F": 16,
        "G": 22,
        "H": 24,
        "I": 18,
        "J": 24,
        "K": 40,
        "L": 48,
    },
)


ALL_NEWSLETTERS: dict[str, NewsletterConfig] = {
    ECONOMICS_CAREERS.name: ECONOMICS_CAREERS,
}
