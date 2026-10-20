---
layout: default
title: "Payment rates (installments)"
permalink: /help/apps/payment-rates
canonical_url: https://practize.io/help/apps/payment-rates
corpus_id: en.payment-rates
source_sha256: 4d8ef9ee6705b6a4bfff9f0721f2d16f287fe62d1e5421cb0d08406c21a17cba
---

# Payment rates (installments)

## What Payment Rates does

Payment Rates lets an eligible purchase be divided into multiple scheduled portions when the supported checkout and payment configuration allow it. Here, “rates” means installments; it does not mean card-processing fees or exchange rates.

## Configure installments

Open **Settings → Apps → Payment Rates** and activate the App. Configure the installment options shown for the practice, then enable them only for eligible services, vouchers, or other supported products. Review the total, number of installments, timing, currency, VAT, and provider requirements.

Preview the client checkout. Verify that the full price, each installment, and payment schedule are clear before confirmation. Use only an approved sandbox or test method for provider testing.

## Monitor and correct

After a test purchase, confirm the local schedule and provider-confirmed payment status. A browser redirect or local pending row does not prove collection. If an installment fails, use the displayed recovery flow and provider record; do not create duplicate charges while the first attempt is unresolved.

Changing the App configuration should not be assumed to rewrite an existing payment agreement. Refunds and cancellations depend on the original transaction and provider workflow.

## Security and troubleshooting

If installments are missing, check App activation, product eligibility, price minimums, currency, payment provider readiness, and employee permissions. Never paste card data, provider customer or charge identifiers, webhook payloads, API keys, or a named client's schedule into an AI Assistant question.
