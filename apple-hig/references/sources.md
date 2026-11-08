# Sources and freshness

Primary source: [Apple Human Interface Guidelines](https://developer.apple.com/design/human-interface-guidelines).
This independent synthesis was checked against live Apple content on **2026-11-08**.
The linked references cover selected foundations, common interactions, and six
platform overviews. They do not claim to reproduce or exhaustively review the HIG.
Videos, image details, and device behavior were not independently evaluated when
authoring this skill.

## Retrieve the authoritative page

Open the relevant Apple page and its platform considerations. If the page returns
a JavaScript-only shell, follow its **View Markdown** link. Apple currently exposes
these canonical Markdown routes (case matters):

```text
https://developer.apple.com/design/human-interface-guidelines.md
https://developer.apple.com/design/Human-Interface-Guidelines/materials.md
https://developer.apple.com/design/Human-Interface-Guidelines/accessibility.md
```

For example, with an available terminal:

```bash
curl --fail --location --silent --show-error \
  'https://developer.apple.com/design/Human-Interface-Guidelines/materials.md'
```

Check that the response is the requested article, not HTML, a navigation shell,
an error, or a redirect to another topic. A successful HTTP status alone is not
evidence that the content was retrieved. Prefer the advertised link if routes change.
The DocC JSON endpoint is another current fallback, for example:
`https://developer.apple.com/tutorials/data/design/human-interface-guidelines/materials.json`.
Read actual article sections from that document rather than just referenced titles.

## Find more specific guidance

| Task | Start here |
|---|---|
| Current principles and platform entry points | [Getting started](https://developer.apple.com/design/human-interface-guidelines/getting-started) |
| Layout, accessibility, type, visual language | [Foundations](https://developer.apple.com/design/human-interface-guidelines/foundations) |
| End-to-end tasks, collaboration, notifications, file management | [Patterns](https://developer.apple.com/design/human-interface-guidelines/patterns) |
| A particular control or container | [Components](https://developer.apple.com/design/human-interface-guidelines/components) |
| Gestures, keyboard, pointer, spatial input | [Inputs](https://developer.apple.com/design/human-interface-guidelines/inputs) |
| Platform integrations and capabilities | [Technologies](https://developer.apple.com/design/human-interface-guidelines/technologies) |

The other bundled references link each recommendation to its topic page. Follow
additional pages from these indexes when the task involves a specialty not covered
here, such as widgets, Live Activities, CarPlay, games, charts, or purchasing. Do not
infer detailed rules from a category title.

## Recheck before making a precise claim

- **Current design:** Inspect the page's guidance and change log; older familiar
  summaries may miss revised principles, materials, navigation, or input behavior.
- **Numbers:** Identify platform, units, default versus minimum, component, and
  context. Keep a recommendation distinct from a hard requirement.
- **Implementation:** Follow developer-documentation links for API names, availability,
  entitlements, and supported behavior. Match them to the project SDK and minimum OS.
- **Evidence:** Cite the specific source and explain an adaptation as an adaptation.
  A source recommendation is not proof that the implementation was tested.
- **Policy/assets:** Consult current App Store rules or relevant licenses when those
  questions arise; this skill does not resolve them by implication.

If a current source contradicts the bundled synthesis, use the current applicable
guidance and explain any important change. If it cannot be retrieved, disclose the
uncertainty and avoid inventing details.
