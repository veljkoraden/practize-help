---
layout: default
title: "Dinero"
permalink: /help/apps/dinero
canonical_url: https://help.practize.io/help/apps/dinero
corpus_id: en.app-dinero
source_sha256: b327236563799d7c5010b0c643bb264fb2d5bbc9f583005ae39ad9a30febd0ee
---

# Dinero

Connect supported invoice and accounting workflows to Dinero. Account and country eligibility apply; a coming-soon card is not an active integration.

## Availability and permissions

Open **Settings → Apps** and find **Dinero**. The card's availability, price, connection state and available actions apply to your account. A help article does not activate an app. Ask the owner to review missing access; staff permissions and app availability are separate. Do not use another person's login to bypass a restriction.

## Set up

1. Check the Apps card first. If it says unavailable or coming soon, stop setup and use your existing accounting process until activation is offered.
2. When available, complete the connection shown by Practize. Review the API-key connection, VAT and non-VAT accounts, payment terms and days, payment-type account mappings and the EasyPay fee-posting option. Review whether personal identification numbers may be included.
3. Review client and offering mappings where setup requests them. Avoid creating duplicate contacts for people already present in the accounting system.
4. Check an authorized invoice through the normal workflow and compare the customer, lines, tax, totals and resulting accounting record. Do not create a real invoice solely as an undocumented test.

## Everyday use

Practize invoice-related operations invoke the integration when its connection and relevant workflow conditions are satisfied. Check the corresponding Dinero record after invoicing, payment or credit-note work; do not assume every provider change is synchronized back into Practize.

## Troubleshooting

If synchronization fails, inspect the displayed invoice error, connection state and required account/client mappings. For a partial result, search for the existing provider invoice before retrying. Avoid manually recreating it until you know whether the original exists.

## Limits and changes

Disconnection and deactivation can expose invoice-handling options: read them before confirming, especially any delete option. Disconnecting is not a refund or deletion of every provider record. Ask your accountant to approve accounting mappings. [Official Dinero documentation](https://developer.dinero.dk/) is a provider reference, not a guarantee that all its API features are implemented in Practize.

## Related help

Return to [App help](https://help.practize.io/help/) to find related setup guides. Before changing a connected workflow, finish pending work and verify its status in the relevant booking, invoice or client record.
