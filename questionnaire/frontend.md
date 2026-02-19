---
id: ui-design-consistency
category: frontend
---
# UI Design Consistency (Centralized Design System)

**What is it?** A centralized approach to design: shared component library, design tokens, or at least a single CSS/theme file so that changing a button or colour updates the whole app consistently. The opposite is custom CSS per element—e.g. having to change the same thing in 400 places.

**Why is it important?** Inconsistent UI confuses users and makes every design change expensive and error-prone. Vibecoded UIs often have duplicated, inconsistent styles.

**How badly can things break?** Inconsistent look and feel, accessibility and layout bugs, and any design change requiring hundreds of edits. Custom class on every element with no shared system is an immediate 1/10.

---

Is there centralized design (component library, shared CSS/theme, or design config) so that design changes apply consistently across the app?

- 1: Custom CSS/classes per element; change one button = change in hundreds of places; no shared system
- 10: Centralized design system, shared components or theme; consistent changes app-wide
