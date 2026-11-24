# Practize Help

Public, reviewed product-help pages exported from the practitioner corpus in `practize-v1`.

The generated `publication-manifest.json` binds each page to its reviewed source hash. Do not edit generated article bodies here; update and review the corpus source, then export again.

## Navigation

The shared layout renders accessible breadcrumbs above each page except the home page. App guides link through the existing Apps overview; other articles link directly through Help articles. Breadcrumbs wrap on small screens. The Pages build checks the rendered hierarchy, links and current-page marker for every published article before deployment (`python3 scripts/test_breadcrumbs.py _site`). Article bodies and publication hashes are unchanged by navigation updates.
