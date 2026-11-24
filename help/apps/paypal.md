---
layout: default
title: "PayPal"
permalink: /help/apps/paypal
canonical_url: https://help.practize.io/help/apps/paypal
corpus_id: en.app-paypal
source_sha256: 40df41bbc323a1f54eb286c823c3a275978b815162c6e09515662146eb6eef55
---

# PayPal

The Apps page currently offers controlled sandbox merchant setup. A verified connection does not by itself enable customer payments.

## Availability and permissions

Open **Settings → Apps** and find **PayPal**. The card's availability, price, connection state and available actions apply to your account. A help article does not activate an app. Ask the owner to review missing access; staff permissions and app availability are separate. Do not use another person's login to bypass a restriction.

## Set up

1. As the owner with app-management permission, open **Merchant setup**.
2. Read the sandbox notice and connection consent, then use **Connect or reconnect with PayPal** for the intended test merchant.
3. Return to Practize and select **Check connection**. Review the connection state and last-checked time.
4. Resolve an incomplete, disconnected or error state using this same setup page. Do not substitute live merchant data for a sandbox configuration.

## Everyday use

Use the displayed connection state to verify onboarding. The current card can say merchant setup verified while payments remain unavailable. Only use a customer-payment workflow if that environment explicitly enables it.

## Troubleshooting

For checking or pending setup, refresh the connection status. For an unverified connection, restart setup from the page. Do not infer a payment from a connected account or from a provider window closing.

## Limits and changes

Disconnecting disables the Practize connection and retains existing records. Revoking provider permissions also requires the PayPal account settings. [PayPal documentation](https://developer.paypal.com/api/rest) distinguishes provider setup from transaction operations; it does not override the sandbox-only availability message.

## Related help

Return to [App help](https://help.practize.io/help/) to find related setup guides. Before changing a connected workflow, finish pending work and verify its status in the relevant booking, invoice or client record.
