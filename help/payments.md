---
layout: default
title: "Recording and managing client payments"
permalink: /help/payments
canonical_url: https://help.practize.io/help/payments
corpus_id: en.payments
source_sha256: 19fa3a264f121c973b4297c70759dfb09ec020aa3deec51ea7917ad680b5dac6
---

# Recording and managing client payments

## Understand the payment type

Client payments are money a client pays the practice for an invoice, booking, event, course, voucher, membership, or service. They are separate from subscription billing, where the practice pays Practize for a plan or App.

The payment methods shown to a practice depend on its country, active Apps, provider setup, currency, permissions, and the type and status of the invoice or checkout. Use the payment action and status displayed for the signed-in practice. Do not assume that a provider is available because it appears in general product information.

## Record a payment manually

An authorized user can mark an eligible invoice as paid after independently confirming receipt of the money. The invoice overview may also offer a bulk action for eligible invoices.

Marking an invoice paid records its state in Practize. It does not move money through a bank, terminal, card network, or external provider. Removing or changing that local record does not prove that an external payment was reversed.

## Online and connected payments

When an active payment App offers a payment action, complete its setup before using it. A browser return or success-looking redirect alone is insufficient evidence that money was collected. Wait for Practize to display the provider-confirmed payment status and use the provider transaction for reconciliation when an exception occurs.

If a payment action is missing, check:

- whether the relevant payment App is active and fully configured;
- whether the invoice or checkout is eligible and still open;
- the practice's country and currency support;
- the signed-in user's payment and invoice permissions; and
- any rollout, merchant-account, or provider-status message on the App page.

## Refunds and corrections

Refund support depends on the original provider and payment type. Before confirming a refund, identify the original transaction, use the provider-supported refund or recovery flow, verify its final provider status, and then confirm that Practize shows the expected invoice and payment state.

Cancelling an invoice, deleting a local payment entry, or issuing a credit note does not automatically prove that the provider returned money. Some cases require manual accounting or provider support.

Never share full card or bank details, security codes, access tokens, API keys, webhook secrets, raw provider payloads, or client financial information in a help question.
