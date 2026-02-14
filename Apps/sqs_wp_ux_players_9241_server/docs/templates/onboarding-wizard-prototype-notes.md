# Onboarding Wizard Prototype Notes

Use this description as the prototype reference when testing accessibility.

- **Step tabs**: Horizontal tabs with numerical labels. Focus order currently jumps from tab 1 to footer link before hitting tab 2.
- **Form fields**: Email invitation list uses pill-style tokens; error text appears under the field but lacks aria-live.
- **Coach marks**: Appear on first load with close button hidden until focus. Color contrast between tooltip text (#9CA6B5) and background (#F9FBFF) is 2.1:1.
- **Permission modal**: Primary CTA "Apply roles" sits before explanatory text in DOM order.
- **Summary screen**: Success banner only changes background color; icon slot empty.
