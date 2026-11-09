---
version: 1
slug: "pregnancy-tracker-html"
primary_target: "pregnancy-tracker.html"
related_targets: []
---

## Scope and mode
Whole app (home first), Operate mode: a calm daily check-in for one pregnant woman on her phone, often in the evening.

## Direction
Growth folio (chosen by the user over the assigned mashrabiya direction). Each week is a botanical plate in an arched frame at one shared scale; the current week sits enlarged among its neighbours so growth reads as a sequence. Approved comp: `.impeccable/mocks/comp1.png`.

## Comp design system (record for everything the comp does not show)
- Ground: pure white; dark mode deep green-black. Colour only in leaf green (headings, primary button, current outline), sage hairlines, one muted pomegranate dot for "now". No filled grey cards; sections separate with hairlines.
- Corner language: arches (tall rounded top, small bottom radius) for plates and week cells; 14px for the primary button; pills only for small tags.
- Line weights: 1px sage hairlines; 1.5px leaf for the current plate.
- Type ramp: Amiri for headings and the week number (700), Zain for body and labels.
- Elevation: none, except a soft shadow under fruit illustrations.

## Inventory (element, medium)
| Element | Medium |
|---|---|
| Top bar: app name right, date + Hijri left | HTML text |
| Five arched plates on one baseline, current enlarged, labels under | HTML/CSS arches + existing fruit WebP assets |
| Centered Amiri headline, short leaf rule, green subtitle (month, trimester), size line | HTML text |
| 40-dot stage strip, current dot in pomegranate | HTML/CSS |
| Two-column facts split by hairlines (due date + Hijri, remaining) | HTML |
| Full-width leaf primary button "تفاصيل الأسبوع" | HTML button |
| Bottom nav, five text labels, leaf indicator on the active one | HTML |
| Below the fold: upcoming rows, this-week rows (development, symptoms, tip), warning-signs link | HTML with hairlines |

## Unresolved
None.
