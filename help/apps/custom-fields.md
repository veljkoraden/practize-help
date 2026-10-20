---
layout: default
title: "Custom Fields"
permalink: /help/apps/custom-fields
canonical_url: https://practize.io/help/apps/custom-fields
corpus_id: en.custom-fields
source_sha256: 74b184a73eefb1b8d7a541dd2f7dcab6d020e103547d61316d34c652cabb16eb
---

# Custom Fields

## Plan a custom field

Custom Fields adds practice-defined information to supported client or workflow forms. Before creating one, decide why the information is needed, who may see it, how long it should be kept, and whether a standard Practize field already covers it.

## Create and place the field

Open **Settings → Apps → Custom Fields**. Activate the App and create the field using the type, label, choices, required setting, and placement options shown. Use a clear label and concise help text. Keep choice values stable when they are used for reporting.

Test the field with a non-production client. Confirm where it appears, whether required validation works, how it is displayed to employees, and whether it is included in exports or public forms as expected.

## Change or retire a field

Renaming or changing choices can alter how existing answers are interpreted. Export or review affected records before a material change. Disable a field only after deciding what should happen to existing values; hidden does not necessarily mean deleted.

If a field is missing, check the App, placement, active state, record type, employee permissions, and whether the current form was opened before the configuration changed.

## Sensitive data

A custom field can accidentally create a new store of health, identity, or financial data. Collect only what is necessary and approved. Never use it for passwords, card data, authentication secrets, or provider credentials. Do not paste field answers or client identities into an AI Assistant question.
