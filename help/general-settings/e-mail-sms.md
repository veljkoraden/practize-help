---
layout: default
title: "Configuring email and SMS message templates"
permalink: /help/general-settings/e-mail-sms
canonical_url: https://help.practize.io/help/general-settings/e-mail-sms
corpus_id: en.messages
source_sha256: 940a1fd35574adbd2ec786b6fa226ef85cce96ad46d047745cc677930f670589
---

# Configuring email and SMS messages

## Configure a message template

1. Open **Settings** and select **E-mail and SMS**.
2. Find the message category you want to change. Common categories include appointment confirmation, reminder, update, cancellation, invoice, and Online Booking messages.
3. Enable the email or SMS channel when the page offers a switch for it.
4. Select **Edit** for the template.
5. Update the email subject and body or the SMS text.
6. Use only placeholders offered by the editor. Placeholders insert values such as a client name, appointment time, practice name, or invoice link when the message is generated. Some specialized templates require a link placeholder; validation identifies it when it is missing.
7. Save the template, then save the settings page if it has a separate save action.

Some pages separate messages sent to clients from notifications sent to the practice. Check the heading and recipient description before enabling a template.

Saving or enabling a template does not send a message. A message is generated only when its product event occurs and the recipient and account meet the requirements. A sent state also does not by itself prove carrier or inbox delivery.

## Conditional templates and controls

Templates for Events, Secure Messages, surveys, Online Courses, Online Meetings, cleanup, or other features appear only when the related App is active. Employee-specific templates or overrides appear only when they are configured and your role can edit them.

The **E-mail and SMS** page requires message-edit permission. If the page or an edit control is missing, ask the practice owner to check your permission and whether the related App is active.

SMS sender name and sender phone number are managed under **Settings → Your profile** when those controls are available. SMS length and supported characters are limited; use the counter and validation shown by the editor. The price or included allowance shown in your account is authoritative.

## If a message is not generated or received

- Confirm that the correct template and channel are enabled.
- Confirm that the relevant App or appointment notification option is active.
- Check that the recipient has a valid email address or phone number.
- Correct validation errors, including any required link placeholder or text-length error shown by the editor.
- Check the message history or status shown in Practize before treating the issue as delivery failure.
- Ask an administrator to verify messaging permissions and account configuration.

The assistant cannot inspect a real message, recipient, delivery status, or provider response. Do not paste client names, contact details, appointment information, invoice content, health information, or message bodies into a product-help question.
