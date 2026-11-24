---
layout: default
title: "Attendance"
permalink: /help/apps/attendance
canonical_url: https://help.practize.io/help/apps/attendance
corpus_id: en.attendance
source_sha256: c560143b135b96684dc52446238720772349ec8228e4363c6f0fe7c3a7e954a4
---

# Attendance

Attendance records that a client attended a booked session. Staff can check clients in manually or, where enabled, use a QR code or RFID card to identify them before confirming check-in. It is a supervised reception workflow, not a door-opening system.

## Before you start

The owner opens **Settings → Apps → Attendance**, activates the app where available, and enables **session check-in**. Attendance can be included automatically for configured gym and yoga practices; the settings page indicates when included access prevents deactivation. Other accounts may see an availability restriction. Staff need attendance permissions and access to the relevant client and calendar. Memberships is optional for existing reservations; membership-covered walk-ins require it.

## Check in an existing reservation

1. Open the client's profile and choose **Attendance**, or open the calendar session's **Participants** tab.
2. Select the reserved session or participant. The client profile lists sessions in the next 24 hours; use the calendar to inspect a particular session if it is missing here.
3. Review the reservation. Existing reservation coverage is reused, so check-in does not take another seat or spend another membership credit.
4. Select **Check in** and wait for the recorded result. Do not treat a loading indicator as confirmation.
5. If the result is uncertain, use **Retry request** for the same operation. Repeating a check-in does not create a second attendance record.

## Enroll and use a reception credential

1. Open the client's **Attendance** tab and its credentials card. These controls appear only when the feature and your credential-management permissions are available.
2. Issue a QR credential, or select RFID, focus the card-input field and scan the client's card. Set an expiry if appropriate and confirm enrollment. Verify you are on the correct client profile.
3. The selected reception reader must send the identifier as keyboard input. Keep focus in the scan field; input sent elsewhere cannot identify the client correctly.
4. For check-in, choose the relevant session and QR or RFID mode. Scan the credential and review the identified client and reservation.
5. Explicitly confirm check-in. Scanning identifies the person; it does not silently admit them.
6. Revoke a lost or compromised credential, then issue or enroll its replacement. Expired and revoked credentials cannot be used for check-in.

## Membership-covered walk-ins

Where enabled, select **Walk-in**, choose a client and session, and review membership coverage and seat availability. Select **Admit and check in** only after checking the preview. Availability is checked again on confirmation. A full session, exhausted allowance, ineligible membership or waiting-list priority can prevent admission. Use the waiting-list process first when required.

## History and corrections

The Attendance tab shows attendance history. Authorized staff can **Void attendance** with a reason and **Reinstate attendance** if it was voided incorrectly. Reload if another staff member changed the record. A correction changes attendance; it does not itself cancel a booking, refund a payment or return membership credits.

The Clients list shows **Last attendance** only while the Attendance app is active and the viewer has permission. It includes the date and Manual, QR or RFID method. Older records can show **Method not recorded**. A voided visit is excluded from the latest valid attendance; reinstating it restores its original check-in details.

## Troubleshooting and limits

- **No reservation:** check the session, client, calendar access and reservation state. Do not create an unrelated booking merely to bypass an error.
- **Outside the allowed window:** verify the session time and practice timezone.
- **Card not found or invalid:** check enrollment, expiry and revocation; re-scan into the correct field. Do not assign an existing card to someone else to force admission.
- **History only:** recording can be disabled while existing history is retained. Ask the owner to review Attendance settings.
- **Hardware:** the selected ACS ACR1281U-C2 reader and NTAG213 cards still require physical compatibility testing. Software tests do not certify reader/card operation.
- **Facility entry:** live occupancy, checkout, door locks and turnstiles are not provided by this session workflow. See [Facility occupancy](https://help.practize.io/help/apps/facility-occupancy).

## Related help

[Memberships](https://help.practize.io/help/apps/memberships) explains allowances. [Classes and events](https://help.practize.io/help/apps/events) explains reservations and capacity.
