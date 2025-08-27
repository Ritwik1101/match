How It Works

Name & Address → Uses fuzzy matching (token_set_ratio from RapidFuzz).

Ignores word order & duplicates.

Example: "raju bala" vs "bala raju" → 100%.

DOB → Converts all formats to YYYY-MM-DD.

Example: "2000-12-1", "12-1-2000", "12/1/2000" → 100% match.

Age → Direct integer comparison.
