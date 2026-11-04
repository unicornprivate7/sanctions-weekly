# Sanctions weekly

Weekly open dataset of **new entries on official sanctions lists**, aggregated by country and list. Counts only, no names.

**Run a free test on all your contacts now and find out if there are any compliance issues.**
[Start the free test](https://intel.unicornprivate.com/login?next=%2Fdashboard%23blind&src=github)

## What it contains

- `data/latest.json`: the most recent 7 days (today included).
- `data/YYYY-WW.json`: one snapshot per ISO week, added every Monday by a GitHub Actions workflow.

Fields: `period` (from, to), `totalNewEntries`, `days` (new entries per day), `byCountry` (country code to list to count),
`byList` (list to count), `lists` (list names and source URLs when available), `generatedAt`.

## Source

Daily comparison of the official sanctions lists monitored by Unicorn Intelligence (lists that are newly added to the engine
are not counted as new entries). Only aggregated counts are published.

- API (free, JSON, CORS open, cached 1 hour): https://intel.unicornprivate.com/api/public/sanctions-weekly
- Documentation: https://intel.unicornprivate.com/docs#public-sanctions-weekly
- Daily view: https://intel.unicornprivate.com/sanctions/today/

## License

Data: [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/). Attribution: Unicorn Intelligence (https://intel.unicornprivate.com).
Information only: the data may contain errors and must be verified; decisions and legal obligations remain with the user.

## About

Unicorn Intelligence by Unicorn Private LLC: automatic daily compliance on all your customers and suppliers.
New accounts also get $50 of credit as a gift.
