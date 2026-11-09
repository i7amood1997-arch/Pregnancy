---
name: مسار الحمل
description: A calm Arabic pregnancy companion with one soft type family, a sage-tinted ground and the week's fruit standing in an arch.
colors:
  ground: "#F3F6F2"
  surface: "#FFFFFF"
  surface-quiet: "#E9EFE7"
  hairline: "#E3E8E1"
  hairline-strong: "#C6D0C3"
  arch-top: "#DCE7D8"
  leaf: "#3B6A4C"
  leaf-soft: "#E4EDE2"
  pomegranate: "#B0524B"
  ink: "#1D2A22"
  ink-2: "#3E4A42"
  ink-3: "#5C675F"
  night-ground: "#0F1411"
  night-surface: "#171D19"
  night-leaf: "#9DCAA8"
  night-ink: "#E6EDE6"
typography:
  display:
    fontFamily: "Alexandria, Noto Sans Arabic, sans-serif"
    fontSize: "2.65rem"
    fontWeight: 300
    lineHeight: 1.25
    letterSpacing: "-0.01em"
  title:
    fontFamily: "Alexandria, Noto Sans Arabic, sans-serif"
    fontSize: "2rem"
    fontWeight: 300
    lineHeight: 1.3
  body:
    fontFamily: "Alexandria, Noto Sans Arabic, sans-serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.7
  reading:
    fontFamily: "Alexandria, Noto Sans Arabic, sans-serif"
    fontSize: "1rem"
    fontWeight: 300
    lineHeight: 1.75
  label:
    fontFamily: "Alexandria, Noto Sans Arabic, sans-serif"
    fontSize: "0.78rem"
    fontWeight: 300
    lineHeight: 1.45
rounded:
  control: "14px"
  surface: "20px"
  home-card: "24px"
  pill: "999px"
  arch: "999px 999px 0 0"
spacing:
  xs: "4px"
  sm: "8px"
  md: "12px"
  lg: "16px"
  xl: "24px"
  2xl: "32px"
---

# Design System: مسار الحمل

## Overview

**North star: soft and quiet.** One type family, Alexandria, carries the whole app through weight alone: light 300 for the week headline and screen titles, 400 for text, 500 for titles of rows and the month line. The ground is a pale sage tint; content that belongs together sits on white surfaces with a soft, low shadow. The week's fruit stands in an arch that fades into the ground, with a small contact shadow under it.

## Layout rules (approved by the user)

- One job per screen. Home answers one question: where is she today.
- Details live one tap away (week panel, expanded appointment, folded history), never stacked on the screen.
- Each piece of information has one home; nothing is repeated across screens.
- Home, in order: date and Hijri date with the emergency icon, the fruit arch, «الأسبوع N», month and trimester, size, then one white card with the trimester bar, days left and due date, the next appointment (or the checkup due now) and the «هذا الأسبوع» row. It fits one phone screen.
- Week panel: header (arch thumbnail, week, month and trimester, dates), one size line, pregnancy age for the current week, three toggles (الجنين، أعراضكِ، نصائح) showing one list at a time, then checkups and milestones for that week.
- Weeks: one screen grouped by pregnancy month (one row of 4 or 5 weeks per month) under three trimester labels.
- Appointments: three toggles (القادمة، الملاحظات، السابقة) show one list; each row expands for notes, questions and actions. Calendar is an icon in the header.
- Tools: one tool at a time; history folded underneath.

## Colors

- **Leaf** `#3B6A4C` (dark `#9DCAA8`): the month line, active navigation, the add button, filled progress, icons in rows.
- **Pomegranate** `#B0524B` (dark `#E8908A`): only the "now" dot on the trimester bar and the current week cell.
- Neutrals: ground `#F3F6F2`, white surfaces, quiet fill `#E9EFE7` for tracks, past weeks and inactive toggles; hairlines `#E3E8E1`.
- The user rejected strong or per-week colour. Keep colour rare.

## Components

- **Arch:** full semicircle top, gradient from `arch-top` to the ground, no outline; the fruit at the bottom with a soft elliptical shadow.
- **Trimester bar:** three segments sized by days (91, 98, 91), 5px tall, 4px gaps; leaf fill; pomegranate dot with a white ring at today.
- **Home card / surfaces:** white, 24px (home card) or 20px radius, `0 12px 28px -18px` shadow.
- **Toggles:** a quiet track with the active option on white with a small shadow.
- **Week cells:** white arch-topped tiles (28px top radius); past weeks on the quiet fill; the current week outlined in leaf with a pomegranate dot.

## Do's and Don'ts

- Do keep every fruit at the same scale and keep the month next to the week everywhere.
- Do keep each screen to one job; move detail into a tap.
- Don't add colour floods, per-week colours, rings around the fruit or circles behind it.
- Don't stack sections that could be one tap away.
