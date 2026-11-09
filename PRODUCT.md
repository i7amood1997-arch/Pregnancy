# Product

<!-- impeccable:product-schema 1 -->

## Platform

web (mobile-first; also installed to the phone home screen from GitHub Pages)

## Stack

Single self-contained HTML file (inline CSS/JS, no framework), published as a claude.ai artifact and as `index.html` on GitHub Pages. `tools/build_index.py` builds `index.html` from `pregnancy-tracker.html`. Data lives in the browser's localStorage only.

## Users

One specific pregnant woman, for personal use (not a public product). Arabic speaker in the Gulf, reading Modern Standard Arabic, addressed in the feminine. She checks the app on her phone, often briefly and often in the evening, to see where she is in the pregnancy and what is coming next.

## Product Purpose

A calm, private companion for the 40 weeks: pregnancy age, due date (Gregorian and Hijri), the current week and month, the baby's size as a fruit, development and common symptoms per week, appointments with questions for the doctor, a few practical tools (kick counter, contraction timer, weight, daily log), checklists, warning signs and backup. Success means she opens it, understands her week at a glance, and closes it feeling calmer, not busier.

## Positioning

Arabic-first and RTL by construction (not a translation), with Hijri dates beside Gregorian ones, Arabic grammar done properly, and one consistent set of fruit illustrations for every week.

## Constraints

- 100% Arabic UI, `dir="rtl"`, Western digits 0-9, Gregorian month names, Hijri via Umm al-Qura.
- Medical content stays general; no medication or dosing advice; the doctor and ultrasound are the reference.
- Dates and calculations are fixed and verified (Naegele, UTC-only math); visual work must not change them.
- Works from 360px to desktop, light and dark, keyboard accessible, WCAG AA contrast.

## Brand commitments (confirmed by the user)

- Calm and simple above all; the interface should feel restful, never busy.
- Keep the fruit illustrations (weeks 3-40).
- Rejected: full-screen strong colour that changes every week (felt loud, not calm).
- Rejected earlier: the generic look of the current build (white, teal, grey rounded cards, IBM Plex), which reads as "made by an AI".
- The app name is «مسار الحمل».
