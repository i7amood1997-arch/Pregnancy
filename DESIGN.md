---
name: مسار الحمل
description: A calm Arabic pregnancy companion where every week is a botanical plate in an arched frame.
colors:
  paper: "#FFFFFF"
  surface-mist: "#F6F8F5"
  surface-fern: "#EDF1EC"
  hairline: "#E3E8E2"
  hairline-strong: "#C2CEC0"
  sage-arch: "#A9BDA6"
  plate: "#FBFCFA"
  plate-current: "#F2F7F0"
  leaf: "#2F5D3A"
  leaf-deep: "#244A2E"
  leaf-soft: "#EAF1E8"
  pomegranate: "#9E3B3B"
  ink: "#1F2A21"
  graphite: "#4A4A47"
  graphite-soft: "#5E625D"
  night-paper: "#111512"
  night-surface: "#171D18"
  night-leaf: "#9CC9A3"
  night-ink: "#E5ECE4"
  night-pomegranate: "#E58C8C"
typography:
  display:
    fontFamily: "Amiri, Noto Naskh Arabic, serif"
    fontSize: "2.6rem"
    fontWeight: 700
    lineHeight: 1.35
    letterSpacing: "normal"
  heading:
    fontFamily: "Amiri, Noto Naskh Arabic, serif"
    fontSize: "1.4375rem"
    fontWeight: 700
    lineHeight: 1.3
  figure:
    fontFamily: "Amiri, Noto Naskh Arabic, serif"
    fontSize: "1.35rem"
    fontWeight: 700
    lineHeight: 1.55
  body:
    fontFamily: "Zain, Noto Sans Arabic, Segoe UI, Tahoma, sans-serif"
    fontSize: "1rem"
    fontWeight: 400
    lineHeight: 1.7
  label:
    fontFamily: "Zain, Noto Sans Arabic, Segoe UI, Tahoma, sans-serif"
    fontSize: "0.75rem"
    fontWeight: 700
    lineHeight: 1.5
rounded:
  control: "12px"
  section: "16px"
  pill: "999px"
  arch: "999px 999px 0 0"
spacing:
  xs: "4px"
  sm: "8px"
  md: "12px"
  lg: "16px"
  xl: "24px"
  2xl: "32px"
components:
  button-primary:
    backgroundColor: "{colors.leaf}"
    textColor: "{colors.paper}"
    rounded: "{rounded.pill}"
    height: "50px"
  button-primary-hover:
    backgroundColor: "{colors.leaf-deep}"
  button-ghost:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.leaf}"
    rounded: "{rounded.control}"
    height: "44px"
  plate:
    backgroundColor: "{colors.plate}"
    rounded: "{rounded.arch}"
  plate-current:
    backgroundColor: "{colors.plate-current}"
    rounded: "{rounded.arch}"
  week-cell:
    backgroundColor: "{colors.plate}"
    textColor: "{colors.graphite-soft}"
    rounded: "30px 30px 6px 6px"
    height: "86px"
  chip-accent:
    backgroundColor: "{colors.leaf-soft}"
    textColor: "{colors.leaf}"
    rounded: "{rounded.pill}"
---

# Design System: مسار الحمل

## Overview

**North star: the growth folio.** The app reads like a botanical folio that follows one fruit after another through 40 weeks. Every week is a plate: a fruit illustration standing in an arched frame, always at the same scale, so growth is something she can see in sequence rather than a number she has to interpret. The current week stands enlarged among its neighbours.

The world is calm and white. Colour is rare and meaningful: leaf green carries headings, the current plate and the one primary action; a single pomegranate dot marks "now"; everything else is ink, graphite and sage hairlines on paper white. Sections separate with hairlines, not filled cards. Arabic typography carries the personality: Amiri (classical naskh) for headings and figures, Zain for reading and labels.

Built for one pregnant woman checking her phone, often in the evening, so the dark theme is a full peer: deep green-black paper, light leaf for action, the same arches and hairlines.

## Colors

### Primary
- **Leaf** (`#2F5D3A`, dark `#9CC9A3`): headings, the week headline, the current plate outline, the primary button, active navigation. Never decoration.

### Secondary
- **Pomegranate** (`#9E3B3B`, dark `#E58C8C`): only the "now" marker: the current dot in the 40-dot strip and the «الآن» label in the current plate.

### Neutral
- **Paper** `#FFFFFF` ground; **Mist** `#F6F8F5` and **Fern** `#EDF1EC` for the rare quiet fills (past week cells, inputs); **Plate** `#FBFCFA` and **Plate current** `#F2F7F0` inside arches.
- **Sage arch** `#A9BDA6`: arch outlines and the plate baseline. **Hairline** `#E3E8E2` between sections and rows.
- **Ink** `#1F2A21`, **Graphite** `#4A4A47`, **Graphite soft** `#5E625D` for text (all at least 6:1 on paper).

### Named Rules
**The One Green Rule.** Leaf green appears on headings, the current plate and at most one filled button per screen.
**The Single Dot Rule.** Pomegranate marks only "now"; it is never used for alerts (alerts use the separate danger and warn tokens).

## Typography

**Display and headings:** Amiri 700. **Body and labels:** Zain 400/700. Base size is 17px (`html{font-size:106.25%}`) because Zain sets small.

### Hierarchy
- Week headline (home): Amiri 2.6rem, leaf, centred, with a 52px leaf rule under it.
- Section headings: Amiri 1.4375rem.
- Figures in the facts row (due date, days left): Amiri 1.35rem.
- Body: Zain 1rem, line height 1.7. Labels and captions: Zain 0.75rem bold.

### Named Rules
**The Naskh Headline Rule.** Headings and big figures are Amiri; never set running text or controls in it.

## Layout

Mobile-first single column; home is capped at 640px and centred on desktop, with a right-side rail (RTL inline-start) from 960px. The home first viewport is fixed in this order: top bar (name, Gregorian and Hijri date) → five arched plates on one sage baseline (previous two, current, next two; clamped at weeks 1 and 40) → week headline → month and trimester line → size line → 40-dot strip → pregnancy age → two facts split by a hairline → full-width primary button. Spacing follows the 4px scale; more space above a heading than below it.

## Elevation & Depth

Flat. The only shadow in the world is a soft drop shadow under fruit illustrations (`drop-shadow(0 6px 6px rgb(0 0 0 / .12))`). Sheets and dialogs use the shared overlay shadow.

## Shapes

- **Arch:** full semicircle top, flat bottom (`border-radius:999px 999px 0 0`) for home plates; 30px top radius with 6px bottom for week cells; the week panel plate uses 30px/4px.
- **Pill:** the primary button and small tags.
- **12px:** secondary controls and inputs. **16px:** the few framed sections.

## Components

### Buttons
Primary: leaf fill, white text, pill, 50px tall, full width on home. Ghost: paper with a sage border and leaf text, 12px radius. Press feedback scales to 0.97.

### Chips
Outline chips in hairline-strong; the accent chip is leaf-soft with leaf text.

### Cards / Containers
No filled cards. Panels, items, months and the week panel's size box are paper with a 1px hairline; lists separate rows with hairlines.

### Navigation
Bottom bar: paper with a top hairline, five text labels, the active one leaf and bold with a 22×2px leaf bar above it. Desktop rail: short labels, active row on leaf-soft.

### Plate strip (signature)
Five buttons, each an arch with the week number at the top and the fruit at the bottom; the current plate is about 1.7× wider, outlined 1.5px leaf, filled plate-current, labelled «الآن» in pomegranate. All plates open the week panel.

## Do's and Don'ts

### Do:
- Keep every fruit at the same scale inside its arch.
- Keep colour to leaf, the single pomegranate dot, and neutrals.
- Show the pregnancy month and trimester right under the week.

### Don't:
- Don't flood screens with colour or change the palette per week (tried and rejected by the user as loud).
- Don't bring back filled grey cards or a progress ring.
- Don't use cream or parchment grounds; the world is paper white.
