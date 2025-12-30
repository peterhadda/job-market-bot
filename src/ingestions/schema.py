"""
Schema & normalization configuration for job postings data.

This file defines all mappings and rules required to transform raw job-market
datasets into a clean, standardized format used across the project.

It contains:
- Column name normalization rules
- Columns to retain after cleaning
- Categorical value mappings for employment, experience, and education levels

The goal is to enforce a single data schema so downstream components
(feature extraction, NLP, modeling, reporting) can rely on consistent inputs.
"""



COLUMN_MAPPING = {
    "company_pro_description": "description",
    "required_exp": "experience_level",
    "required_edu": "education_level",
    "telecommuting": "remote"
}

KEEP_COLUMNS = [
    "job_id",
    "title",
    "location",
    "description",
    "salary_range",
    "employment_type",
    "experience_level",
    "education_level",
    "remote",
    "industry",
    "function"
]

EMPLOYMENT_MAP = {
    "Full-time": "full_time",
    "Part-time": "part_time",
    "Internship": "internship"
}

EXPERIENCE_MAP = {
    "Entry level": "entry",
    "Mid-Senior level": "mid",
    "Senior level": "senior"
}

EDUCATION_MAP = {
    "High School": "high_school",
    "Bachelor's Degree": "bachelor",
    "Master's Degree": "master",
    "PhD": "phd"
}
