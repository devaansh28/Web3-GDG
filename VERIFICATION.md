# Verification and design handoff

## Scrapbook revision: current website

Approved reference-led redesign implemented in `dist/scrapbook.css` and `dist/scrapbook.js`, with focused hero and theme edits. The earlier results below are historical; current evidence is:

- `node scripts/verify-scrapbook.mjs`: passed. The new replay test first failed because the control did not exist, then passed after implementation. Checks actual running animation after replay, static reduced-motion fallback, persisted theme, passport selection, visible hero action and no horizontal overflow at 360/390/768/1024px.
- `node scripts/verify.mjs`: passed the full existing interaction suite, including registration validation/download/privacy, mobile/tablet layouts, search/profile dialogs, tracks, filters and keyboard roles. No page errors, failed requests or broken images were recorded.
- Scroll Craft harness: 55 desktop, 57 mobile and 55 reduced-motion samples. All completed; no dead scroll detected. Three contact sheets visually inspected. Updated normal-page lengths: 8.9 desktop and 12.0 mobile viewport-heights.
- Final desktop, 1024px, 390px and mobile registration screenshots inspected individually. Headline, invitation and photos remain separated, content is readable, and native dialogs remain usable. The full-page screenshot taken without scrolling does not trigger offscreen reveal/lazy-image content; the sequential scroll contact sheets are the correct evidence for those sections.
- Dark/light visual checks and JavaScript syntax checks completed. Focus-ring colours explicitly contrast with light paper and dark track surfaces. No comprehensive accessibility audit or real-phone hardware test is claimed.

Visual reading now moves from playful curiosity (assembling scrapbook hero) through clarity, agency, trust, belonging and resolution. The passport remains the main interactive moment. The supplied reference changed materials and motion, not event facts or registration scope. The earlier PDF remains an initial-design artifact; the revised website archive is `output/Web3-Carnival-Scrapbook-Website.zip`.

### Initial design verification (historical)

Verified 26 September 2026. Local preview: http://localhost:4500.

## Result

The responsive static prototype covers every requested content area: homepage, next-event status, tracks, historical speakers and editions, community/attendee routes, partners, registration preview, contact and social footer. The 12-page PDF demonstrates the desktop/mobile journey and three-step registration interaction.

## Functional evidence

`node scripts/verify.mjs` completed with exit 0. `lab/functional-results.json` records no console/request errors or broken images. Passed checks:

- Track selection and reload persistence.
- Speaker search, empty state, expanded directory, profile dialog and Escape.
- Event location filters and rail navigation.
- Role routes and arrow-key tabs.
- Registration steps, required-field/email validation, interest carryover, downloaded passport contents and name/email clearing on close.
- Image loading, responsive overflow and interactions at 360, 390, 768 and 1440 pixels.
- Reduced-motion layout and no-JavaScript content/non-GET form fallback.

The browser-close test waits for the native dialog close event before asserting form cleanup. Personal information is neither stored nor submitted by this prototype.

## Visual evidence

Scroll Craft's screenshot harness captured 55 desktop, 57 mobile and 55 reduced-motion frames, 167 total, with no dead-scroll report. Contact sheets in `lab/scroll-*` were inspected. Additional section, dialog, theme and mobile screenshots are in `lab/` and `lab/presentation/`.

Corrections verified in the final screenshots: compact-phone headline wrapping/overlap, Threeway mark contrast, small-screen body sizing, no-JavaScript reveal visibility and local font loading. Independent hero planes remain legible; the mobile composition is stacked rather than scaled desktop art. The closing invitation remains a clear destination.

All 12 PDF pages were rendered with Poppler and inspected on a contact sheet; the final coverage page was also inspected separately. No visible clipping, missing images or overlapping text was found. PDF text extraction confirmed 12 text-bearing pages. Poppler emitted cache-directory warnings but rendered successfully.

## Scroll Craft report

The authored Festival Programme grammar uses a navigable photographic masthead, compact logistics, track working surface, portrait directory, dated archive and invitation close. Alternatives and their tradeoffs are recorded in BRIEF.md. This is the first registry entry: no prior rows to conflict with. The engine is unmodified; custom interactions live in app.js.

Signature: selected tracks stamp a personal Carnival Passport and carry into the registration preview and downloadable plan. Four-plus device families combine parallax, count/flow, reveal, stagger and pointer depth without full-page pinning or scroll hijacking. No generated imagery or video was needed.

Visual-read assessment compared with the intended curve: curiosity (photo masthead), clarity (honest next-edition status), agency (passport choices), trust (historical portraits), belonging (community/archives), confidence (partners/routes), resolve (invitation). The track surface has the largest desktop content span and strongest interactive state change. Small-phone typography and mark contrast were corrected to preserve that reading. This is a design assessment, not user-research evidence of emotional response. Brief and ordering were authored from the user's supplied requirements, not a separate interview.

## Limits and production work

- No real ticket booking, payment, backend or public deployment. Next-event date/venue remain unconfirmed.
- Tested in headless Chrome with phone emulation, not physical iPhone/Android hardware.
- No comprehensive accessibility certification. The Scroll Craft contrast harness checks cue elements; this flow-led page has no such cues, so its green run is not proof of measured site-wide contrast compliance.
- Brand/media reuse requires organiser approval for public commercial publication.
- The original Archivo licence file still needs inclusion before redistribution. Download was blocked by the automatic approval reviewer's usage limit, not a network safety finding. See SOURCES.md for the original licence location.
