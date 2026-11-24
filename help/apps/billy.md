---
layout: default
title: "Billy"
permalink: /help/apps/billy
canonical_url: https://help.practize.io/help/apps/billy
corpus_id: en.app-billy
source_sha256: 6eea261992673a14bc906ccefd9d4d5b6cbc72c9620571f1c0ca547b28daeb91
---

# Billy

Connect supported invoice and accounting workflows to Billy. Account and country eligibility apply; a coming-soon card is not an active integration.

## Availability and permissions

Open **Settings → Apps** and find **Billy**. The card's availability, price, connection state and available actions apply to your account. A help article does not activate an app. Ask the owner to review missing access; staff permissions and app availability are separate. Do not use another person's login to bypass a restriction.

## Set up

1. Check the Apps card first. If it says unavailable or coming soon, stop setup and use your existing accounting process until activation is offered.
2. When available, complete the connection shown by Practize. Review the API-key connection, VAT and non-VAT sales-tax rules, payment terms and payment-account mappings. Review the option that permits personal identification numbers on invoices.
3. Review client and offering mappings where setup requests them. Avoid creating duplicate contacts for people already present in the accounting system.
4. Check an authorized invoice through the normal workflow and compare the customer, lines, tax, totals and resulting accounting record. Do not create a real invoice solely as an undocumented test.

## Everyday use

Practize invoice-related operations invoke the integration when its connection and relevant workflow conditions are satisfied. Check the corresponding Billy record after invoicing, payment or credit-note work; do not assume every provider change is synchronized back into Practize.

## Troubleshooting

If synchronization fails, inspect the displayed invoice error, connection state and required account/client mappings. For a partial result, search for the existing provider invoice before retrying. Avoid manually recreating it until you know whether the original exists.

## Limits and changes

Disconnection and deactivation can expose invoice-handling options: read them before confirming, especially any delete option. Disconnecting is not a refund or deletion of every provider record. Ask your accountant to approve accounting mappings. [Official Billy documentation](https://www.billy.dk/api/) is a provider reference, not a guarantee that all its API features are implemented in Practize.

## Related help

Return to [App help](https://help.practize.io/help/) to find related setup guides. Before changing a connected workflow, finish pending work and verify its status in the relevant booking, invoice or client record.
