# Interaction patterns

Choose by the person's task and target platform, not visual resemblance. The tests
below are this skill's practical adaptations of the linked guidance.

## Navigation versus actions

| Need | Starting choice | Avoid |
|---|---|---|
| Switch among top-level destinations | Tab bar appropriate to the platform | A Create or Delete command masquerading as a destination |
| Navigate a deeper collection/hierarchy | Sidebar and detail navigation where suitable | A permanent phone-style sidebar on every device |
| Act on the current content | Toolbar or contextual control | Crowding the toolbar with every possible command |
| Reveal secondary commands | Menu with meaningful groups | Hiding the sole path to the main task in an obscure gesture |
| Find content | Search with a clear scope and placement | Undifferentiated empty, loading, and no-result states |

**Tabs:** Keep destinations stable and meaningfully labeled. An empty section should
explain itself rather than disappear. Balance frequency of access against crowding;
do not invent a universal five-tab rule. Current iPad guidance starts with tabs and
allows a sidebar presentation for more complex navigation. Source:
[Tab bars](https://developer.apple.com/design/human-interface-guidelines/tab-bars).

**Sidebars:** Keep groups comprehensible and hierarchy shallow; support hiding or
customization where useful. Do not assume the same presentation fits compact space.
Source: [Sidebars](https://developer.apple.com/design/human-interface-guidelines/sidebars).

**Toolbars and menus:** Group related commands, preserve standard navigation controls,
and prioritize frequent actions. Mac toolbar commands should also be available through
the menu bar. Name commands by their result; use standard unavailable-state and submenu
behavior rather than custom conventions. Sources:
[Toolbars](https://developer.apple.com/design/human-interface-guidelines/toolbars),
[Menus](https://developer.apple.com/design/human-interface-guidelines/menus).

**Search:** Explain the searchable content, offer useful suggestions and filtering,
and update promptly when feasible. Decide whether search filters the current view or
is a destination for discovery. Placement varies by platform and available space;
read the current guidance rather than freezing it at the top of every screen. Source:
[Search fields](https://developer.apple.com/design/human-interface-guidelines/search-fields).

## Buttons, sheets, and interruptions

**Buttons:** Make the action understandable, using text when an icon is ambiguous.
Distinguish the likely action with an appropriate style, not arbitrary size inflation.
Custom buttons need press feedback and full interaction semantics. Do not give an
ordinary destructive button the primary role. Check the specific alert conventions
when designing confirmation dialogs. Source:
[Buttons](https://developer.apple.com/design/human-interface-guidelines/buttons).

**Sheets:** Use for a bounded task tied to the current context. Give people a clear
way to complete or leave it; handle unsaved changes when dismissed by either a button
or gesture. Prefer one sheet from the main interface instead of a stack of sheets.
Choose detents and grabbers only where the content and platform support them. Source:
[Sheets](https://developer.apple.com/design/human-interface-guidelines/sheets).

**Modality:** Use interruption intentionally. Persistent navigation and supplementary
work often belong in nonmodal views; a sufficiently complex, focused editing task may
warrant a full-screen presentation. Preserve a clear way back and the suspended context.
Source: [Modality](https://developer.apple.com/design/human-interface-guidelines/modality).

**Alerts:** Reserve for consequential, actionable information. Routine success and
ordinary undoable actions rarely need an alert. State the situation clearly and use
specific action labels. On iOS/iPadOS, choices following an intentional action may fit
an action sheet instead. Do not generalize one platform's button order to all targets.
Source: [Alerts](https://developer.apple.com/design/human-interface-guidelines/alerts).

**Recovery:** Where appropriate, support standard undo/redo, describe what will change,
and make the result visible. For actions that cannot be reversed, make consequences
clear and provide a safe cancellation path. Source:
[Undo and redo](https://developer.apple.com/design/human-interface-guidelines/undo-and-redo).

## Forms and language

Request only needed information. Prefer sensible defaults, existing authorized data,
or choices over avoidable typing. Keep field purposes understandable after placeholders
disappear. Match keyboards and formatters to the data, support paste/autofill where
appropriate, and make focus traversal predictable. Validate at useful moments without
discarding input or trapping people in a correction loop.

Use consistent, plain, action-oriented language. Explain errors near the affected
control with a recovery step, not blame or a vague failure code. Match input vocabulary
to the device: tap, click, select, or another appropriate term. An empty state should
explain what belongs there and how to proceed, not just display an illustration.

Sources: [Entering data](https://developer.apple.com/design/human-interface-guidelines/entering-data),
[Text fields](https://developer.apple.com/design/human-interface-guidelines/text-fields),
[Writing](https://developer.apple.com/design/human-interface-guidelines/writing).

## First use, accounts, and permissions

**Onboarding:** Lead toward useful activity. Teach in context, postpone optional setup,
and let people skip a nonessential tutorial and find it later. A necessary prerequisite
should be brief and clearly tied to the experience. Source:
[Onboarding](https://developer.apple.com/design/human-interface-guidelines/onboarding).

**Accounts:** Let people experience value before sign-in when the product permits.
Use supported authentication methods and device-appropriate names. Make account
deletion discoverable; explain its consequences and distinguish it from subscription
cancellation when relevant. Source:
[Managing accounts](https://developer.apple.com/design/human-interface-guidelines/managing-accounts).

**Permissions:** Request the narrow resource when its feature needs it. Explain the
actual use in clear language and respect denial. Do not request everything at launch
unless genuinely necessary. If a pre-alert explanation is warranted, read Apple's
specific rules; do not invent a generic dismissible pre-prompt or imitate the system
permission dialog. Model denied/restricted access and recovery as part of the feature.
Source: [Privacy](https://developer.apple.com/design/human-interface-guidelines/privacy).

For policy-sensitive questions, check current App Store Review and framework
documentation separately. HIG design guidance alone does not establish eligibility.

## Loading, feedback, and state

Show useful content early and keep unrelated work available during loading. Use
determinate progress for known work and indeterminate progress when the amount is
unknown; do not fabricate completion percentages. Watch interactions should avoid
making someone hold up their wrist through a long wait.

Give feedback close to the action, with enough redundancy to survive muted audio or
limited vision. Confirm significant outcomes without interrupting every routine action.
Explain unavailable commands and how to recover.

Sources: [Loading](https://developer.apple.com/design/human-interface-guidelines/loading),
[Feedback](https://developer.apple.com/design/human-interface-guidelines/feedback).

For the affected flow, select relevant states: initial, empty, populated, loading,
partial/stale data, offline/error, denied permission, validation failure, success,
cancel, and undo. This is a testing aid, not a requirement that every component have
every state. Preserve existing work across interruption and return when appropriate.
