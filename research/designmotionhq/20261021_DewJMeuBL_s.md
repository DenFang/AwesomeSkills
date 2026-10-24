---
id: DewJMeuBL_s
reel_url: https://www.instagram.com/reel/DewJMeuBL_s/
pattern_page: none
date: 2026-10-21
duration_s: 54
type: ui
category: onboarding
topic: Mobile permission prompts: timing, pre-permission card, benefit copy, denied-state recovery, one request at a time
sources: frames, voice-over, caption
---

# Permission prompts: ask once, at the right moment

**Caption:** Your app gets one real shot at "Allow" (ends with a plug for the author's Claude Code plugin).
**Hook:** A habit app ("Streakly") fires the system "Would Like to Send You Notifications" dialog on first launch; the user taps Don't Allow and the permission is "denied forever".

## Main rule
Request a permission only right after the user starts the feature that needs it, show your own explanatory card first (stating the concrete benefit) and trigger the one-shot system dialog only after the user accepts it, ask for one permission at a time, and when permission is denied keep the feature visible but disabled with a direct link to the system Settings.

## Numbers and values
| Value | Applies to | Where shown |
|---|---|---|
| 5 | mistakes in the reel ("mistake 1/5" ... "5/5" progress dots) | throughout, on-screen |
| 1 | times iOS lets an app show the system notification dialog; after "Don't Allow" the app cannot ask again | 0:12-0:21 voice + "system prompt: used" |
| Android 11+: two No = no more prompts | Android re-prompt limit | 0:21 on-screen |
| 8:00 PM, every day | reminder the user just created (Drink water) | 0:07-0:12 on-screen |
| "Get a reminder at 8 pm" | benefit-led card title | 0:10-0:31 on-screen + voice ("a reminder at 8 every evening") |
| "Glass 6 of 8, keep the streak." | preview of the notification the user will receive | 0:24-0:25 on-screen |
| 1 tap to Settings | denied-state recovery path | 0:38-0:40 on-screen |
| 3 asks, 0 context / 3 denied | bad: three permission dialogs at launch | 0:41-0:47 on-screen |
| 1 ask, right after Scan | good: camera permission requested on tap | 0:45-0:47 on-screen |
| Vitalex 500 mg, 30 tablets | sample scanned medication box (demo content) | 0:46-0:47 on-screen |
No timing or size values are shown.

## Before / after
1. **Timing: ask right after the action (0:00-0:11).** Bad: the system notification dialog appears on the Welcome screen at first launch ("asked on first launch"); the user has no reason to allow, taps Don't Allow, and the permission is "denied forever". Good: the user goes Welcome -> New habit (Drink water, remind me at 8:00 PM, every day) -> Save reminder; on the Saved screen ("Reminder set for 8:00 PM") the app asks ("ask here"). Why: the request is understood and wanted at the moment the feature needs it; at launch it is context-free and gets refused.
2. **Your card before the dialog (0:12-0:21).** The app shows its own in-app card ("Get a reminder at 8 pm, Drink water, every evening", Not now / Turn on). Tapping "Not now" on the card leaves "system prompt: still available"; tapping "Don't Allow" on the system dialog marks it "used" (locked). Why: a "no" on your own card costs nothing and you can ask again later; a "no" on the system dialog is permanent on iOS (and after two denials on Android 11+).
3. **Say what they get (0:22-0:31).** Bad, "says nothing": "We'd like to send you notifications. Stay up to date." with Not now / Allow; the user dismisses it. Good, "says the gain": "Get a reminder at 8 pm. Drink water, every evening." plus a preview of the real notification ("Drink water, 8:00 PM, Glass 6 of 8, keep the streak."); Turn on leads to "Reminders on". Why: a concrete, personal benefit tied to what the user just set up gives a reason to accept; generic copy gives none.
4. **A way back to Settings (0:32-0:40).** Bad, "no way back": a Reminders screen that just says "Notifications are off. You won't get reminders." Good: the reminder row and its toggle stay visible but disabled, with "Notifications are off, Open Settings >" next to it; one tap opens the app's system notification settings ("1 tap to Settings") where "Allow Notifications" can be switched on. Why: after a system denial only the user can re-enable it in Settings; a direct link keeps the feature from being a dead end.
5. **One request, when it's needed (0:41-0:47).** Bad, "at launch": notifications, location and another permission requested back to back on the Welcome screen, all denied ("3 asks, 0 context", "3 denied"). Good, "on tap": on "Add medication", the camera prompt appears only after the user taps "Scan" ("Fill it in from the box"), with a purpose string "To scan your medication box."; scanning then fills the medication ("1 ask, right after Scan"). Why: each permission is tied to a visible user intent, so the purpose is self-evident.

## Do
- Trigger a permission request from the user action that needs it (save a reminder, tap Scan), never on launch.
- Show your own pre-permission card first; call the system API only after the user taps the card's positive button.
- Write the card as a concrete benefit with the user's own data ("a reminder at 8 pm"), optionally with a preview of what they will receive.
- Ask for one permission at a time.
- In the denied state, keep the feature visible but disabled and link straight to the app's Settings page.
- Write a specific purpose string for the system dialog (the reel's camera dialog: "To scan your medication box.").

## Don't
- Don't show any system permission dialog on first launch without context.
- Don't stack several permission requests in a row.
- Don't use vague copy like "Stay up to date" or "We'd like to send you notifications".
- Don't hide or remove a feature after a denial, and don't re-ask with the system dialog when the OS will not show it.

## Scene by scene
- 0:00 "Streakly, first launch: Permission prompt mistakes": the system notification dialog over the Welcome screen; finger taps Don't Allow; tags "asked on first launch" (struck) and "denied forever".
- 0:04 "Mistake 1, timing: Ask right after the action": three screens 1 Welcome ("ask here? no"), 2 New habit (Name: Drink water, Remind me at 8:00 PM, Repeat: Every day / Weekdays, Save reminder), 3 Saved (Today: Drink water 8:00 PM every day, "Reminder set for 8:00 PM", "ask here"), then the card "Get a reminder at 8 pm" with Not now / Turn on; "fix: ask after".
- 0:12 "Mistake 2, no pre-card: Your card before the dialog": "your card" phone vs "system dialog" phone; Not now on the card -> "system prompt: still available"; Don't Allow on the dialog -> lock icon, "system prompt: used"; "Android 11+: two No = no more prompts"; "fix: own card first".
- 0:22 "Mistake 3, vague copy: Say what they get": card labelled "says the gain"; notification preview drops in at the top; Turn on -> "Reminders on"; then a second card "We'd like to send you notifications. Stay up to date." labelled "says nothing", dismissed with Not now; "fix: say the gain".
- 0:32 "Mistake 4, dead end: A way back to Settings": before "Notifications are off, You won't get reminders." ("no way back") vs after: Drink water toggle greyed, "Notifications are off, Open Settings >"; tap opens system Settings > Streakly > Notifications, Allow Notifications switched on; "1 tap to Settings"; "fix: link to Settings".
- 0:41 "Mistake 5, all at once: One request, when it's needed": "at launch" stacked dialogs (notifications, location), "3 denied", "3 asks, 0 context" vs "on tap": Add medication, tap Scan, "Opening camera", camera dialog "To scan your medication box." -> Allow -> scanner reads "Vitalex 500, 30 tablets"; "1 ask, right after Scan"; "fix: one at a time".
- 0:48 Product plug: "UX Engine 2.3, Claude Code plugin: Five prompts, asked right. Screens first, then code."; terminal typing "add reminders with notifications" and a checklist (ask after the action / timing, pre-permission card / soft ask, say the gain / copy, denied state + Settings link / recovery, one prompt at a time / just in time); "Link in bio".

## Voice-over summary
- Asking for notifications on first launch fails: the user has no reason to allow anything yet.
- Ask right after the user sets their first reminder, when the feature needs it.
- Show your own card first because a no there costs nothing; on iPhone a no on the system dialog means the app can never ask again.
- The card states what the user gets, like a reminder at 8 every evening; a vague line about notifications gives no reason to tap Allow.
- If refused, the reminder toggle stays visible but disabled with a link to Settings, so the feature is never a dead end; the camera prompt waits until the user taps Scan, one request at a time.

## Notes for the skill
- Platform facts: on iOS the notification authorization dialog (`requestAuthorization`) is shown only once per install; later calls return the stored decision silently, so the recovery path is `UIApplication.openNotificationSettingsURLString` (iOS 16+) or `openSettingsURLString`. On Android 13+ notifications need the runtime `POST_NOTIFICATIONS` permission, and since Android 11 two denials of a runtime permission are treated as "don't ask again"; use `shouldShowRequestPermissionRationale` to decide when to show your own rationale, and `Settings.ACTION_APP_NOTIFICATION_SETTINGS` for recovery. On Android 12 and below notifications are granted by default, so the pre-card is not needed there.
- iOS also supports provisional authorization (quiet delivery without a prompt), an alternative for apps whose value is easier to show than explain.
- Model permission state explicitly: `notDetermined` (show pre-card on intent), `denied` (show disabled control + Settings link), `granted`; re-check the state when the app returns to foreground, since the user may have changed it in Settings.
- The "Not now" choice on the pre-card should be respected: do not re-show the card on every launch; wait for the next relevant intent.
- Do not design the pre-card to look like the system dialog or to trick users (for example a decoy "Allow" that must be tapped to continue); Apple's review guidelines and HIG reject misleading pre-permission screens. Always offer a real "Not now".
- A disabled toggle must still explain why it is disabled (the reel puts "Notifications are off" next to it) and the Settings link needs a clear accessible name; disabled controls are not focusable in some frameworks, so put the explanation on a focusable element.
- Web equivalent: call `Notification.requestPermission()` or `getUserMedia()` only from a user gesture tied to the feature; browsers increasingly auto-block or quiet prompts shown on page load.
- The final seconds are an advertisement for the author's plugin; nothing there is a design rule.
