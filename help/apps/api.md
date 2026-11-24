---
layout: default
title: "API access"
permalink: /help/apps/api
canonical_url: https://help.practize.io/help/apps/api
corpus_id: en.app-api
source_sha256: 211f80321c577d20d1fd0fc590048ef18b664d4f6a5d675ff3c850a225068850
---

# API access

Allow an authorized integration to communicate with the supported Practize API.

## Availability and permissions

Open **Settings → Apps** and find **API access**. The card's availability, price, connection state and available actions apply to your account. A help article does not activate an app. Ask the owner to review missing access; staff permissions and app availability are separate. Do not use another person's login to bypass a restriction.

## Set up

1. Activate API access only when you have an integration purpose and an authorized technical maintainer.
2. Follow the app setup for the supported personal access token or OAuth connection. Enter any credentials only in the intended secure connection flow.
3. Review the payment-type settings and other mapping options exposed by setup, then use the current API documentation linked by the product for exact endpoints.
4. Test a minimal read operation in the intended account before enabling writes or automated jobs.

## Everyday use

Keep a record of which system uses each connection and review access when a maintainer leaves. Validate the result of API writes in the underlying Practize records.

## Troubleshooting

An unauthorized response can mean an expired or invalid credential, insufficient permissions or unavailable endpoint. Ask the integration maintainer to inspect the response without copying secrets into support chat.

## Limits and changes

API access is not unrestricted access to other practices. This guide does not define endpoint contracts or promise unsupported automation. Never publish tokens in client-side scripts, screenshots or public repositories.

## Related help

Return to [App help](https://help.practize.io/help/) to find related setup guides. Before changing a connected workflow, finish pending work and verify its status in the relevant booking, invoice or client record.
