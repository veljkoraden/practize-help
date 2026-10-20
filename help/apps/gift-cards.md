---
layout: default
title: "Gift Cards"
permalink: /help/apps/gift-cards
canonical_url: https://help.practize.io/help/apps/gift-cards
corpus_id: en.gift-cards
source_sha256: f9385d7f729b4262a6bf5706e459f7d9352284b6f8186562491ed6f8879c7ef8
---

# Gift Cards

## What Gift Cards do

Gift Cards let a practice sell or issue stored value that can be used in supported checkout flows. They differ from Vouchers, which grant a defined number of uses for selected services or events.

## Configure the App

Open **Settings → Apps → Gift Cards**. Activate the App and configure the client-facing text, availability, amounts or amount rules, validity, and payment options shown for the practice. Review VAT and accounting treatment with the practice's adviser before selling cards.

Preview the public Gift Card page. Complete a sandbox or approved test purchase and verify the amount, recipient details, delivery, payment status, and resulting balance. Never use a live card merely to test an unapproved integration.

## Redeem and reconcile

At checkout, apply an eligible Gift Card and verify the value used and remaining balance before completing the transaction. A card that is expired, exhausted, inactive, or unsupported for the selected flow should not be treated as payment.

If a purchase or redemption appears wrong, preserve the transaction record, verify the provider state, and use the supported correction or refund flow. Deleting a local record does not prove money was refunded.

## Protect Gift Card data

A Gift Card code can function like money. Do not place full codes, recipient contact data, balances tied to a named client, provider identifiers, or payment credentials in an AI Assistant question. The Assistant can explain usage but cannot reveal, redeem, or change Gift Cards.
