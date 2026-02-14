# Notification Settings Prototype Walkthrough

Use this narrative whenever a task references the clickable prototype for Lab C.

## Screen 1 · Channel Selection (00:00–00:45)
- Toggle list for Email, SMS, Push; default states: Email ON, SMS OFF, Push OFF.
- Switching SMS ON triggers inline warning: "Cost applies to international numbers" after 1.5 s.

## Screen 2 · Quiet Hours (00:45–01:20)
- Time range slider initially set 22:00–06:00.
- Adjusting handles updates preview text beneath slider.
- Error toast appears if start time >= end time, but toast floats at top-left.

## Screen 3 · Preview + Save (01:20–02:10)
- Live preview card shows sample notification copy with channel badges.
- Save button remains disabled until at least one channel enabled and quiet hours defined.
- Successful save displays modal confirmation plus inline status badge next to toggles.
