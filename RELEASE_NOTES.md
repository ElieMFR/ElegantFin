# ElegantFin Cinema Edition v1.2.53

## [English](#english) | [Francais](#francais)

---

<a name="english"></a>
## English

### Cinema Edition — 28 cinematic modules on top of ElegantFin v26.04.07

This release transforms the ElegantFin theme into a professional, premium streaming experience while keeping full compatibility with desktop, mobile, and TV platforms.

---

#### New in v1.2.0 — 8 Cinema Features

- **Skeleton loading** — Animated pulse placeholder while card images load, with subtle gradient shimmer. Disabled on TV and reduced-motion.
- **Hover preview info** — Secondary text (year, rating, genres) smoothly reveals on card hover with a cinematic bottom gradient overlay (desktop only)
- **Scroller edge fade** — Left/right gradient edges on horizontal scroll rows, indicating scrollable content. Uses `--backgroundForAppBar` for seamless blending.
- **Scroll-to-top glass** — Glass-effect button with `backdrop-filter: blur(15px)`, border glow, and hover lift animation
- **Resolution badges** — Color-coded media info badges: 4K (gold), HDR (green), Dolby Vision (purple), Atmos (cyan) with matching borders and subtle backgrounds
- **Now Playing bar glass** — Glassmorphism on the Now Playing bar with `blur(20px) saturate(1.4)`, dark border-top, and shadow. Disabled on TV.
- **Watched overlay** — Subtle dark overlay (`rgba(0,0,0,0.35)`) on already-watched cards, fading out on hover. Uses `:has(.playedIndicator)`.
- **Sidebar glass enhanced** — Sidebar with `blur(20px)`, styled nav items with rounded corners, hover highlights, selected state styling, and uppercase section headers

---

#### Glassmorphism & Animations

- **Login page glassmorphism** — Frosted glass card with `backdrop-filter: blur(20px)`, smooth `loginCardAppear` animation, and `@supports` fallback for older browsers
- **Page transitions** — `pageFadeIn` (0.4s) and `sectionSlideIn` (0.5s) animations with cascade delays on sections (0.05s increments)
- **Shimmer effect** — Subtle light sweep on the first row of cards (desktop only, disabled on mobile/TV)
- **Backdrop animation** — Cinematic `detailBackdropIn` with scale + fade on detail pages

---

#### Visual Enhancements

- **Cinema card pop** — Scale 1.06x on hover with glowing borders (`rgba(255,255,255,0.3)`), deep shadows, and text color transition to white
- **Cinema detail page** — Ultra-light titles (weight 100), italic tagline, `line-height: 1.65` synopsis, white Play button with hover lift
- **White progress bars** — Clean `#fff` progress bars replacing theme-colored ones, with glow effect on OSD slider hover
- **Premium badges** — Glass-blurred indicators (`backdrop-filter: blur(8px)`) for count, resolution, and watched badges
- **Glass dialogs** — `backdrop-filter: blur(20px)` on dialogs, `blur(15px)` on drawer/menus/toast/upNext, all with `@supports` fallback

---

#### Typography & Layout

- **Section titles** — Bold (700), negative letter-spacing, hidden chevron arrows, overflow ellipsis with `max-width: calc(100vw - 8em)`
- **Navigation tabs** — White active tab (`#fff`/`#000`), subtle inactive (`rgba(255,255,255,0.06)`) with smooth hover
- **Long titles fix** — Responsive line-clamp (2 desktop, 3 mobile, 2 TV), word-break on metadata, card text overflow handling
- **Typography hierarchy** — Refined font-weights for episode titles (600), secondary text (`dimTextColor`), page title (500)
- **Fluid title sizing** — `clamp(2em, 5vw, 4em)` for smooth scaling across all screen sizes

---

#### Performance & Accessibility

- **TV optimizations** — All `backdrop-filter`, `box-shadow`, animations, `will-change`, and shimmer disabled on TV layout
- **Mobile optimizations** — Reduced blur intensity (`blur(10px)` instead of `blur(20px)`) via `@supports` query
- **GPU hints** — `will-change: transform` on hover only (not permanent), disabled on TV to free GPU memory
- **Reduced motion** — Full `prefers-reduced-motion: reduce` coverage: page transitions, shimmer, skeleton, login bounce, backdrop fade, card hover
- **Thin scrollbars** — 4px cross-browser scrollbars scoped to `html` (inherited, not universal `*`)
- **Focus-visible** — Keyboard navigation focus rings on tabs, Play button, detail buttons, skip button, login

---

#### Header & OSD

- **Cinema header gradient** — Deep transparent gradient (`rgba(0,0,0,0.75)` to transparent) replacing theme-colored one
- **OSD header glass** — `rgba(0,0,0,0.85)` background with `blur(10px)` on the video player header
- **OSD bottom gradient** — Softer 3-stop gradient (85% to 50% to transparent)
- **Reactive slider** — Expands to `0.5em` on hover, white thumb with `border-radius: 2px`, glow on progress bar
- **Firefox slider** — Full `::-moz-range-thumb` styling matching WebKit (size, border, radius, transitions)
- **Skip button** — Bold (700), `letter-spacing: 0.03em`, `scale(1.03)` on hover

---

#### v1.2.1 — Visual & Compatibility Fixes

- **Backdrop extended** — Mask extended from 45% to 65%, opacity raised from 0.55 to 0.65 — image visible further down the detail page (PC)
- **TV backdrop** — Reduced darkness from 0.95 to 0.6 — backdrop was nearly invisible on TV
- **upNext title** — Replaced `nowrap` with `line-clamp: 2` — long episode titles no longer truncated (all platforms)
- **OSD header TV** — Allows 2-line titles, reduced header height to 3.5em — fixes oversized black bar
- **OSD title mobile** — `line-clamp: 2` with wider max-width for long titles
- **Card hover** — Removed double zoom (1.06 x 1.04 = 1.10) — now single clean 1.06x pop

---

#### v1.2.2 — Editor's Choice Cinema

- **Editor's Choice Cinema** — Full cinematic styling for the Editor's Choice plugin: gradient overlay, glass buttons, zoom backdrop, smooth transitions
- **Full-width slides** — Splide carousel now shows one slide at a time (`min-width: 100%`) instead of cutting multiple slides
- **Cinema buttons** — Plugin buttons (`.button-submit`, `.emby-button.raised`) now styled with glass effect, white text, and hover lift matching the Cinema theme
- **TV disable** — All Editor's Choice blur, shadows, and animations disabled on TV layout

---

#### v1.2.3 — CSS Quality & Next Up Fix

- **Next Up dialog overflow** — Added `max-height` + `overflow-y: auto` so content scrolls instead of escaping the container
- **Next Up buttons always visible** — `flex-shrink: 0` prevents buttons from being pushed out of view
- **Next Up word-break** — Long titles now break cleanly with `word-break: break-word`
- **Next Up TV/Mobile** — TV: max 35em wide, 70vh tall with padding. Mobile: 90vw wide, 75vh tall
- **CSS audit fixes** — `justify-content: left/right` → `flex-start/flex-end` (invalid CSS), `rgb()` → `rgba()`, merged duplicate `html {}` blocks, added standard `line-clamp`, removed `calc(100% - 0em)`, fixed non-existent font, updated module count to 29

---

#### v1.2.4 — Next Up Dialog Polish

- **Wider container** — Added `min-width: 28em` so the dialog is never too narrow for long titles and buttons
- **3-line title** — `line-clamp` increased from 2 to 3 — long anime/episode titles now display fully
- **Buttons contained** — `width: 100%` on button row ensures they never overflow the container
- **No horizontal overflow** — `overflow-x: hidden` prevents content from escaping sideways
- **Mobile reset** — `min-width: unset` on mobile to avoid forcing a wide container on small screens

---

#### v1.2.5 — Next Up Title Wrap Fix

- **Root cause fixed** — Jellyfin default has `white-space: nowrap` + `width: 25.5em` + `text-overflow: ellipsis` on `.upNextDialog-title`, which forced single-line truncation. Overridden with `!important` to allow multi-line display
- **Title now wraps** — `white-space: normal`, `width: auto`, `text-overflow: unset` combined with `line-clamp: 3` — long anime titles display on up to 3 lines

---

#### v1.2.6 — Jellyfin Default CSS Overrides

- **upNext container width** — Jellyfin forces `width: 30em` fixed; overridden with `width: auto` so `min-width`/`max-width` work correctly
- **upNext buttons width** — Jellyfin forces `width: 29.75em` fixed; overridden with `width: 100%` to fill container
- **RTL support** — Added `[dir="rtl"] .upNextContainer` margin for right-to-left languages

---

#### v1.2.7 — Cleanup & CSS Quality

- **Removed Editor's Choice Cinema** — Plugin styling removed (28 modules)
- **Added standard `line-clamp`** — Missing on `.detail-clamp-text` (desktop/mobile/TV) and `.listItem-overview`
- **Fixed `justify-content: right`** — Last remaining invalid value on `.endTimeText` → `flex-end`
- **Removed permanent `will-change`** — Shimmer `::before` no longer declares `will-change: transform`
- **Fixed stale version comments** — Updated section comment references
- **Updated module count** — 29 → 28 across CSS, README, and RELEASE_NOTES

---

#### v1.2.8 — OSD Header Height Fix

- **OSD header reduced** — Video player header was using `--appBarHeight` (5em), now fixed to `3em` for all platforms — no more oversized black bar during playback

---

#### v1.2.9 — OSD Header Height Fix (stronger overrides)

- **OSD header forced to 2.75em** — Previous 3em rule was overridden by Jellyfin defaults. Now uses `!important` on both `.osdHeader` container and `.headerTop`
- **OSD buttons sized down** — Header buttons reduced to 2.5em to match the shorter bar
- **TV OSD at 3em** — Slightly taller on TV for remote visibility, still much smaller than default 5em

---

#### v1.2.10 — CSS hardening & TV hover fixes

- **`.upNextContainer` sizing forced** — Added `!important` on `min-width`, `max-width`, `max-height` to prevent Jellyfin defaults from overriding
- **Merged duplicate selectors** — `.toast` was defined 3 times, `.upNextContainer` was defined 2 times — consolidated into single blocks
- **TV hover protection** — Moved `.skip-button:hover`, `.emby-tab-button:hover`, `.MuiButtonBase-root:hover` inside `@media (hover: hover) and (pointer: fine)` so TV remotes don't trigger accidental hover states

---

#### v1.2.11 — Honest cleanup: removed broken Resolution Badges colors

- **Removed color-coded Resolution Badges** — The 4K/HDR/Dolby Vision/Atmos coloring never actually worked in Jellyfin 10.11.x because badge text lives in `textContent` (not in a `title` attribute), and pure CSS cannot match inner text. Kept the generic badge styling (rounded border, padding, subtle border color).
- **Module count: 28 → 27** — Documentation updated in README and CSS header
- **README FR correction** — Fixed stale "29 modules" reference that was already outdated

---

#### v1.2.12 — Language-neutral selectors & dead code removal

- **Favorite icon fill** — Replaced `.emby-button[title="Favorite"]` with `[is="emby-ratingbutton"]`. The previous selector only matched English Jellyfin; now the filled-heart animation works in **French, German, Spanish, etc.**
- **Book "Play → Read" button** — Removed `[title="Play"]` qualifier so the Book-page label override works in all languages
- **Scroll-to-Top module removed** — Jellyfin 10.11.x has no native `.btnScrollToTop` / `[data-action="scrolltotop"]` element. The 25 lines of CSS were styling nothing. Module count: 27 → 26.
- **Editor's Choice negation simplified** — `.itemsContainer:not(.editorsChoiceItemsContainer)` → `.itemsContainer` (the excluded class no longer exists in Jellyfin, so the `:not()` was dead logic)

---

#### v1.2.13 — OSD header desktop fix: title no longer clipped

- **Desktop OSD header bumped from 2.75em → 3em** — The previous 2.75em height was too tight on desktop/browser: accented characters (é, è, à) and descenders (g, p, y) in the episode title were being clipped at the top/bottom. TV/mobile were fine (different rules). Now consistent 3em everywhere.
- **Font-size: 1.1em → 1em** on `.pageTitle` to give more breathing room
- **Buttons: 2.5em → 2.75em** to match the taller header proportionally
- **Added `overflow: visible`** on `.headerTop` and `.pageTitle` as safety for accented characters

---

#### v1.2.14 — OSD title vertical alignment fix

- **`.pageTitle` now flex-centered** — Previous `line-height: 3em` hack pushed text baseline down, making the title appear lower than the back arrow. Replaced with `display: flex; align-items: center; line-height: 1.2` so the title aligns perfectly with the buttons.

---

#### v1.2.15 — Next Up dialog: force long titles to wrap

- **`.upNextContainer` max-width 80vw → 34em** — Previous 80vw made the popup huge on desktop (~1500px on 1920p screens), so long episode titles fit on one line. Constrained to 34em (~544px) so long titles naturally wrap to 2-3 lines as intended by the existing `line-clamp: 3` rule.

---

#### v1.2.16 — Next Up fix: proper TV & mobile overrides

- **Mobile & TV `max-width` now use `!important`** — v1.2.15 introduced a regression: the new `34em !important` desktop rule was overriding mobile's `90vw` (popup overflowed on phones <544px wide) and TV's `35em` values. Added `!important` to all layout-specific overrides so each platform gets its correct sizing: **desktop 34em**, **TV 38em**, **mobile 90vw**.

---

#### v1.2.17 — Top header: streaming-style gradient on item detail pages

- **Replaced fully-transparent header with gradient** — On item detail pages (movies/series), the top bar used `background-color: transparent` which became invisible when the backdrop was dark or missing, making icons hard to spot. Replaced with `linear-gradient(to bottom, rgba(0,0,0,0.75) 0%, rgba(0,0,0,0.4) 60%, transparent 100%)` matching premium streaming pattern. Icon legibility guaranteed on any backdrop, cinematic full-bleed effect preserved — actually enhanced thanks to added visual depth. Consistent across **desktop**, **TV** and **mobile**.

---

#### v1.2.18 — Spotlight hover on card rows + header cleanup

- **streaming-style spotlight on horizontal rows** — Hovering a card in a scroll row now fades + desaturates the sibling cards (`opacity 0.55`, `saturate(0.7)`, smooth 0.3s transition) so the focused card really pops. Desktop-only (scoped with `@media (hover: hover) and (pointer: fine)`), limited to `.emby-scroller` so library grid views stay untouched, fully disabled under `prefers-reduced-motion`. Graceful degrade on browsers without `:has()` — no effect, nothing breaks.
- **Removed obsolete `text-shadow` fallback on header icons** — With the v1.2.17 gradient guaranteeing contrast on any backdrop, the `1px 1px 0 #00000080` shadow was just softening icon edges for no reason. Cleaner rendering now.
- **Module count bumped to 27** (Spotlight Hover added).

---

#### v1.2.19 — "See all →" chevron on row title hover (streaming-pattern)

- **Native chevron revealed on hover** — The theme previously unconditionally hid Jellyfin's native `chevron_right` next to row titles (Continue Watching, Recently Added, etc.). It now animates in on `:hover` using a `max-width` + `opacity` + `translateX` transition (0.25s ease). Clean streaming-style "view all →" affordance without any new HTML. Desktop-only (`@media hover: hover and pointer: fine`), fully disabled under `prefers-reduced-motion`. The link behind is already wired to "view all" by Jellyfin.

---

#### v1.2.20 — Cleanup pass: removed ~70 lines of dead commented CSS

- **No functional change**, no visual change, no module change — pure code hygiene.
- Removed **8 commented-out CSS blocks** (`.detailPagePrimaryContent` ×2, `.videoPlayerContainer`, Episode listItem, `.padded-left`, `#homeTab .overflowBackdropCard`, and a 24-line `layout-tv *` perf graveyard). Total ~70 lines saved.
- **Merged duplicate `.detailsGroupItem > .label` rule** — two separate blocks consolidated into one, same rendering.
- **Fixed 2 stale section comments** — `CINEMA FEATURES v1.2.2` → `(introduced v1.2.2, expanded through current)`; Scroll-to-Top removal note relocated out of the Badges section; v1.2.18 historical text-shadow note removed (now in this changelog).
- Audit checked `:has()` (76 uses, all intentional and gracefully degrading), shimmer animation (already optimized), vendor prefixes (still load-bearing) — none touched.

---

#### v1.2.21 — TV episode subtitle wrap + backdrop gradient redesign

- **TV: subtitle now wraps on 3 lines instead of overflowing** — On Tizen / Samsung TV, entering a series episode caused the `.subtitle` (e.g. `S01E03 — Episode Title`) to overflow off-screen because only the global `white-space: nowrap` rule applied. Added a `.layout-tv .subtitle` override with `display: -webkit-box; -webkit-line-clamp: 3; line-clamp: 3; max-height: 4em;`. 3 lines (vs mobile's 2) gives more breathing room appropriate for TV viewing distance, with `max-height` as a fallback for older Tizen WebKit if `-webkit-line-clamp` misbehaves.
- **Desktop: backdrop gradient flipped from side to bottom (streaming-pattern)** — The original `--itemBackdropSideGradient` darkened the LEFT half of the backdrop with `linear-gradient(90deg, var(--darkerGradientPoint) 0%, transparent 50%)`, designed for left-aligned content. But Jellyfin 10.11.x centers logo/buttons/description, so the side darkening was hiding the left of the image without purpose (e.g. cropping out characters in series like Classroom of the Elite). Replaced with a bottom-up vertical gradient `rgba(0,0,0,0.85) → transparent` matching premium streaming pattern: dark at the bottom for button contrast, fully revealed at top.

---

#### v1.2.22 — Desktop backdrop overlay completely removed (fix v1.2.21 regression)

- **`.layout-desktop .itemBackdrop::before` now `display: none`** — The v1.2.21 vertical gradient worked fine on the main series detail page (~50vh backdrop) but drowned the short backdrops on **Season** and **Episode** pages (~13vh) where the gradient covered 100% of the visible image, making the backdrop nearly invisible. After visual review, the natural dark theme page background BELOW the backdrop already provides ample contrast for the Lire button and description text. The overlay was double-darkening for no benefit. Backdrop image is now fully visible on all detail page types (series, season, episode). Mobile and TV unaffected (they use their own `mask` rules).

---

#### v1.2.23 — Editor's Choice plugin: button/section collision fix

- **Added overrides for the [Editor's Choice plugin](https://github.com/lachlandcp/jellyfin-editors-choice-plugin)** — When the description (`.editorsChoiceItemOverview`) was long enough to fill the plugin's default `-webkit-line-clamp: 4`, the absolutely-positioned "Regarder" button (`bottom: 30px` of the banner) visually collided with the next home section title (e.g. "Mes médias") because the banner had no `margin-bottom`. Added `#editorsChoiceContainer { margin-bottom: 2em }` for breathing room, and tightened the description to **3 lines on desktop** (`-webkit-line-clamp: 3 !important`) so the gap between text and button is always preserved. Mobile/TV keep the plugin's default 4-line behavior. If the plugin isn't installed, these rules are inert (selectors don't exist).

---

#### v1.2.24 — Restore parent-series link on season/episode pages (UX fix)

- **Series breadcrumb back-link restored** — When a series has a clear logo (`.detailLogo`), the theme was hiding ALL `h1` elements inside `.nameContainer` for the cinematic logo-only look. This silently removed the `<a>` link inside `h1.parentName` that lets users navigate back to the series from a season or episode page — leaving only the header back arrow as a way to go up the hierarchy. Now `h1.parentName` is re-shown as a small subtle clickable breadcrumb (font-size 1em, opacity 0.7, underline) while `h1.itemName` stays hidden (avoids redundancy with the logo image). Affects desktop, mobile, and TV. Cleanly degrades when no logo exists (old behavior). Pure visual addition — no other rules touched.

---

#### v1.2.25 — Parent breadcrumb now matches the title style ("Saison 3" look)

- **Restyled parentName breadcrumb to match itemName rendering** — Per user feedback, the small/subtle breadcrumb introduced in v1.2.24 looked out of place compared to the big "Saison 3" title below. Now `h1.parentName` inherits the default `.nameContainer h1` style (`font-size: clamp(2em, 5vw, 4em)`, weight 100, white) — same as the season/episode title — so the parent series link appears at full title size. Click affordance comes from a 2px underline at 30% white opacity that brightens to 90% on hover. Visual hierarchy now reads: **Logo → Series link → Season title**, all consistent.

---

#### v1.2.26 — Parent breadcrumb final design (clean, no permanent underline)

- **Final breadcrumb style: matches the visible "Saison X" / "Episode Y" rendering** — Iterating on user feedback after v1.2.25 ("the underline is ugly, I want the same look as Saison 3, properly bold, neither too big nor too small"). Now `h1.parentName` is styled to match the visible season/episode title: **font-size 2em**, **font-weight 400 (normal, not the inherited thin 100)**, **letter-spacing normal** (overrides theme's -0.02em), **white**, **centered**, with a soft text-shadow for legibility. **No permanent underline** — the link is clean by default. Click affordance comes from a subtle underline that **appears only on `:hover`** (1.5px, 60% white opacity, 0.2em offset). Mobile users discover by tapping; desktop users see the underline reveal on mouseover. Final result is consistent with the cinema/elegant aesthetic of the theme.

---

#### v1.2.27 — Mobile detail page fixes + TV header gradient force

Bundle of 4 fixes addressing real user-reported issues across all platforms:

- **Mobile: parentName breadcrumb hidden when logo present** — On the narrow mobile viewport, the absolutely-positioned `.detailLogo` visually overlapped with the in-flow `h1.parentName` text (e.g. "Moi quand je me réincarne en Slime" rendering through the dragon logo on the Saison 4 page). Mobile users navigate back via the header arrow ← which is the natural mobile UX pattern — the redundant breadcrumb removed.
- **Mobile: detail page containers constrained to viewport width** — In-progress episodes use a `backdropCard` (wide thumbnail) instead of `portraitCard`, which combined with the grid auto-sizing on `.infoWrapper` could push content past the screen edge (text and image overflow on the right). Forced `max-width: 100vw; overflow-x: hidden; box-sizing: border-box` on `.infoWrapper`, `.detailPagePrimaryContent`, `.detailPagePrimaryContainer`, `.detailImageContainer`. Plus `overflow-wrap: anywhere; word-break: break-word` on `.nameContainer` h1/h3 so long titles wrap cleanly. Card max-width capped at 60vw.
- **Mobile: line-clamp 4 for long episode titles** — Was 3 lines, now 4. Long anime episode titles ("Saison 3 - 10. La première cause de conclusions absurdes, je l'attribue au manque de méthode") were getting cut. Added `max-width: 100%; overflow-wrap: anywhere` to the `bdi` rule too.
- **TV: forced header gradient regardless of class combination** — The v1.2.17 gradient relied on `.skinHeader-withBackground.semiTransparent` class which Tizen via Jellyfin2Samsung doesn't always apply on detail pages, leaving the bar fully transparent (icons floating on bright backdrops). Now forces the gradient on `.layout-tv .skinHeader`, `.layout-tv .skinHeader-withBackground`, `.layout-tv .skinHeader-withBackground.semiTransparent`. Slightly stronger top opacity (0.85 vs desktop's 0.75) to compensate for couch viewing distance.

---

#### v1.2.28 — TV gradient fixes (saison/episode pages) + restore mobile breadcrumb

Iteration based on user testing:

- **TV gradient now applies on saison/episode pages too** — v1.2.27 only worked on the series main page; the saison and episode pages have a different class combination on the header that wasn't covered by `.skinHeader-withBackground`. Selector simplified to `.layout-tv .skinHeader:not(.osdHeader)` which catches every header context except the playback OSD.
- **TV gradient softened to feel like a thin top shadow** — Previous gradient (0.85 → 0.5 → 0.15 over full height) made the bar look like a thick dark band. New gradient `0.7 → 0.3 → transparent at 80%` fades much faster, so the visible "dark area" only covers the top ~30% of the header — a subtle shadow rather than a thick stripe.
- **Mobile breadcrumb restored, positioned to avoid logo overlap** — v1.2.27 hid the breadcrumb on mobile when the logo was visible (to avoid the visual overlap reported in v1.2.24-26). Now the breadcrumb is back, displayed at moderate size (1.5em, weight 400, white, centered) with `margin-top: 18vh` to push it past the absolutely-positioned `.detailLogo` (which spans roughly 45vh-62vh on mobile). No permanent underline, clean tap target. Mobile users can now tap the series name to navigate back, without the logo/text overlap of previous iterations.

---

#### v1.2.29 — Tighter mobile spacing + TV header z-index lock

Quick iteration based on user testing of v1.2.28:

- **Mobile breadcrumb margin reduced from 18vh to 5vh** — The 18vh push left a large empty black gap between the logo and the breadcrumb on the saison page. 5vh is just enough to clear the logo zone without creating a visual void.
- **TV header z-index forced to 1000** — User reported that on Tizen, the backdrop image appeared visually ABOVE the header bar on saison and episode pages. Adding `position: relative; z-index: 1000 !important` ensures the header stays on top of the backdrop regardless of how Tizen orders layers.

---

#### v1.2.30 — Chip alignment + tighter mobile breadcrumb spacing

3 fixes addressing visual alignment issues:

- **`.mediaInfoOfficialRating` (FR-XX age rating chip) unified with other chips** — The original styling used `transform: translateY(-0.15em)` plus `background: transparent`, which made the FR-12 / FR-10 badge appear visually raised compared to year, star rating, and percentage chips. On TV the offset could even cause the chip to be clipped at the top edge. Now matches `.mediaInfoItem:not(.endsAt)` styling: same background (`rgba(255,255,255,0.05)`), same border (`1px rgba(255,255,255,0.15)`), same border-radius, padding, font-size, font-weight, letter-spacing. Transform removed. All chips now sit at the same height with consistent appearance.
- **Mobile breadcrumb margin-top reduced from 5vh to 2vh** — 5vh still left a visible empty gap between the logo and the breadcrumb. 2vh is the minimum that still avoids overlap with the logo's bottom edge.

---

#### v1.2.31 — Full chip alignment (year / FR-XX / ★ rating / 100%)

- **All `.mediaInfoItem` chips now share strict identical dimensions** — v1.2.30 only fixed the FR-XX badge alignment (removed translateY) but the chips still had different visual heights because their content (text vs text+icon) drove their natural rendering size. v1.2.31 enforces `height: 1.8em; min-height: 1.8em; padding: 0 0.6em; line-height: 1; display: inline-flex; align-items: center` on **every** chip variant — year, FR-XX, star rating, percentage. Same background, same border, same border-radius. Inline icons inside (`.material-icons`, `.starIcon`, `svg`) clamped to `font-size: 0.9em` so they don't push chip heights apart.
- **`.itemMiscInfo-primary` container**: now `display: flex; flex-wrap: wrap; align-items: center; justify-content: center; column-gap: 0.5em; row-gap: 0.5em` — chips wrap to a second line on very narrow viewports instead of overflowing/clipping (safety net only — typically stays on one line).

---

#### v1.2.32 — Clickable logo navigation + subtitle wrap fixes + emby-linkbutton hover global

Plan derived from SDK analysis of `jellyfin/jellyfin-web` (`controllers/itemDetails/index.js`):

- **Logo cliquable vers la série parente (PC + Mobile)** — `<a is="emby-linkbutton" data-type="Series">` existant dans `h1.parentName` est maintenant utilisé comme overlay invisible cliquable couvrant exactement la zone du `.detailLogo`. Click n'importe où sur le logo → navigation vers la série parente. Adaptation automatique par type de page via `:has(.subtitle)` (saison/épisode = position différente). Sur page série principale (pas de `<a>` dans parentName), le breadcrumb est caché (`:not(:has(a))`) — cohérent car déjà sur la série. TV non touché (garde rendu v1.2.26).
- **Season link visible dans subtitle** — Le `<a data-type="Season">` dans `.subtitle` (sur pages épisode) reçoit un underline subtil au hover, signalant qu'il est cliquable pour remonter à la saison.
- **Global `[is="emby-linkbutton"]` hover** — Tous les Web Components Jellyfin Web qui sont des liens (artist, album, série, saison, etc.) reçoivent maintenant `cursor: pointer` + léger hover opacity. Améliore l'UX sur toutes les pages, pas juste détail.
- **Music breadcrumbs (`.musicParentName`) cohérence** — Les `<a>` artiste/album dans les pages musique stylés au même niveau que les autres breadcrumbs (cursor + hover underline).
- **`.originalTitle` polish** — Les titres VO (japonais pour animes type Re:ZERO) maintenant en italique, opacity 55%, font-weight 300 pour distinction discrète. Wrap autorisé sur PC pour les longs titres romaji.
- **Mobile subtitle line-clamp 4** (était 2) — Longs titres épisodes anime (ex: "Saison 4 - 7. En sortant de la supérette, je me suis retrouvé dans un monde étrange") s'affichent maintenant sur 4 lignes au lieu d'être coupés à 2.
- **PC subtitle wrap 3 lignes** (était `white-space: nowrap` + ellipsis) — Plus de débordement horizontal sur les longs titres, wrap propre sur 3 lignes.

---

#### v1.2.33 — Cross-platform polish (iOS, TV remote, old Tizen compat)

Plan derived from full ecosystem audit (jellyfin-web, jellyfin-tizen, jellyfin-android, jellyfin-androidtv):

- **iOS Safari: `text-size-adjust: 100%`** — Prevents iOS auto-zooming text on orientation change/rotation. Without this, iPhones zoomed text by 10-20% when rotating from portrait to landscape, breaking carefully-designed CSS layouts. iPhone/iPad Safari users now see stable text sizes.
- **iOS: tap-highlight already present** — Confirmed at line 203 (`-webkit-tap-highlight-color: transparent !important;`). No change needed.
- **Mobile: safe-area-inset support (notches)** — iPhone X+ have notches/Dynamic Island at top, Home Indicator at bottom. Android with gesture nav has system bar at bottom. Added `padding-top: env(safe-area-inset-top)` on `.layout-mobile .skinHeader`, `padding-bottom: env(safe-area-inset-bottom)` on `.nowPlayingBar`. Landscape: also handles left/right safe areas for sideways notch. `env()` falls back to 0 on devices without safe areas (iPad classic, older Android).
- **TV: reinforced focus for remote navigation** — Cards at 3-5m viewing distance had only `0.15em` outline — barely visible. Now: `3px solid` outline + `box-shadow` glow + subtle `scale(1.06)` for immediate focus distinction. premium streaming TV pattern. Same applied to buttons (`.btnPlay`, `.detailButton`). Transition `0.15s` for fluidity.
- **Old Tizen `:has()` fallback** — v1.2.32 uses `:has(a)` for conditional logo overlay. Tizen 2018-2021 (Chromium 76-79) doesn't support `:has()`. Added `@supports not (selector(:has(*)))` block that reverts the breadcrumb to a visible clickable text on these old TVs. Tizen 9.0+ users unaffected (overlay v1.2.32 behavior preserved).

---

#### v1.2.34 — TV focus refactor : box-shadow inset (fix bordures clipped)

- **TV focus passé d'outline outside à box-shadow inset** — v1.2.33 (Fix A) utilisait `outline: 3px + outline-offset: 4px + box-shadow: 24px` qui sortaient des conteneurs parents `overflow: hidden`. Résultat : bordures clipped asymétriquement sur les cards en bord de viewport (vu sur screenshots utilisateur — cards Films, Programmes, Stargate, Dr. STONE). Refonte avec `box-shadow inset 0 0 0 3px var(--uiAccentColor)` : la bordure de focus est À L'INTÉRIEUR du bord de la card, ne peut JAMAIS être clipped. Glow externe et drop-shadow conservés (peuvent être clipped sans souci visuel). Scale réduit de 1.06 à 1.03 (moins risque de débordement viewport).
- **Boutons : même refonte** — `outline + offset` remplacé par `inset 0 0 0 2px` (bordure 2px car boutons plus petits). Cohérent avec les cards.

---

#### v1.2.35 — TV focus passé du violet au BLANC (cohérence thème)

- **Focus TV de `var(--uiAccentColor)` (violet) à blanc** — Le violet hérité de l'upstream ElegantFin ne correspondait pas à l'identité Cinema Edition (bouton Lire blanc, dégradés sombres, palette warm cinema). Passé à `rgba(255, 255, 255, 0.95)` pour bordure inset, `rgba(255, 255, 255, 0.3)` pour glow. Visible à distance TV + cohérent avec le reste du thème (pattern des grandes apps de streaming qui utilisent tous des focus clairs).
- Box-shadow inset conservé de v1.2.34 (jamais clipped sur cards en bord viewport).
- Cards et boutons traités cohéremment (3px sur cards, 2px sur boutons).

---

#### v1.2.36 — Subtitle "Saison X" positionné sous le logo (fix overlap PC + Mobile)

- **Push `.nameContainer` sous le logo sur pages Saison/Episode** — Sur PC et Mobile, le logo est `position: absolute` et occupe ~9vh-34vh en vertical. Le `h3.itemName.subtitle` ("Saison 4" ou "Saison X - 7. Episode Y") tombait dans le flow à ~13vh → overlap visuel avec le logo. La règle globale `--itemTitleVisibility: none` cache les `h1` mais pas les `h3`. Fix : `padding-top: 23vh` (PC) / `20vh` (Mobile) sur `.nameContainer` quand `:has(.subtitle)` + logo présent. Le `h1.parentName` overlay invisible v1.2.32 (logo cliquable) reste absolute et n'est pas affecté. Les siblings (`itemMiscInfo`, boutons "Lire") suivent naturellement plus bas. TV non touché.

---

#### v1.2.37 — Padding-top restreint aux pages Saison (fix vide sur Episode)

- **Sélecteur affiné** : `:has(.subtitle:not(.focuscontainer-x))` au lieu de `:has(.subtitle)`. v1.2.36 appliquait le padding-top 23vh/20vh sur Saison ET Episode pages, créant un grand vide sur Episode (où l'élément en haut est une card image, pas un logo). SDK confirme : sur Saison page le `h3.subtitle` n'a PAS `.focuscontainer-x` (juste "Saison X"), sur Episode page `.focuscontainer-x` est présent (contient un `<a Season>` link). Le push ne s'applique maintenant que sur Saison pages où l'overlap logo/subtitle existe vraiment.

---

#### v1.2.38 — Lien série visible (italique) au-dessus de "Saison X" sur pages Saison

- **Le h1.parentName redevient visible** comme lien italique sur les pages Saison — L'overlay invisible v1.2.32 ne fonctionne pas fiablement en pratique (positioned ancestor mismatch + emby-linkbutton web component sensible à visibility). Plus simple et meilleur UX : rendre le `h1.parentName` visible directement comme un lien italique (taille 1.4em, weight 500, opacity 0.8, italic) au-dessus du subtitle "Saison X". Sur PC, hover révèle un underline subtil. Utilise le sélecteur `:has(.subtitle:not(.focuscontainer-x))` pour cibler uniquement les pages Saison (pas Series principale ni Episode). Le `<a>` existant dans parentName (pointant vers `data-type="Series"`) reste fonctionnel et marche garantie. Sur Episode pages, l'overlay v1.2.32 reste (sans changement).

---

#### v1.2.39 — v1.2.38 bug fix: add display:block (override --itemTitleVisibility)

- **v1.2.38 bug** : the visible rule on h1.parentName had no visual effect — h1 was still `display: none` inherited from the global rule `display: var(--itemTitleVisibility)` (default: none). v1.2.38 overrode position/color/font-size but NOT display. Element styled but hidden → nothing on screen. Fix: added `display: block !important;` in the v1.2.38 rule. The italic link "Re:ZERO" / "Moi quand je me réincarne en Slime" / etc. now correctly appears above "Saison X" on Saison pages.

---

#### v1.2.40 — Consolidation: single visible series link, removed broken invisible overlay

- **Removed the v1.2.32 invisible clickable overlay** — The original "click the logo to go to the series" mechanism used an invisible overlay (`font-size: 0; color: transparent; position: absolute` with hardcoded `calc()`/`left:30%;width:40%`). User confirmed it never actually worked (logo click HS) — the absolute positioning didn't reliably cover the logo, and the emby-linkbutton web component was sensitive to the transparency. ~60 lines of fragile dead code removed.
- **Generalized the visible series link to ALL pages with a logo** — v1.2.38 had introduced a visible italic series link but only on Season pages. Now it applies to Season AND Episode pages (any `h1.parentName:has(a)` with a logo). Single, reliable, consistent navigation mechanism: the series name shows as a clickable italic link above the subtitle, hover underline on desktop. Main series page (no `<a>`) still hidden via `:not(:has(a))`. No-logo fallback (big title) preserved. TV unaffected (keeps v1.2.26 rendering). Less code, no fragile `calc()` positioning, easier to maintain.

---

#### v1.2.41 — Cold audit fixes: iPhone notch actually fixed + dead code removal

Full theme audit (cascade conflicts, dead code, stale docs). Findings and fixes:

- **🔴 iPhone notch padding was silently dead on the home page** — The v1.2.33 rule `.layout-mobile .skinHeader { padding-top: env(safe-area-inset-top) }` (specificity 0,2,0) was beaten by the pre-existing `.layout-mobile .skinHeader-blurred:not(.osdHeader) { padding: 0 }` (0,3,0) — and the home header carries `.skinHeader-blurred`, so the anti-notch padding never applied exactly where notch overlap happens. Fixed with `!important`. Only visible on iPhone X+ (env() = 0 elsewhere, zero change).
- **Removed dead TV focus rule** — The old purple `0.15em outline` block was 100% overridden by the v1.2.35 white inset rule right below it (same selector, `outline: none !important`). 5 lines of dead code removed; zero visual change on TV.
- **Removed dead landscape safe-area rule part** — `.detailPagePrimaryContent` already has `padding-left/right: var(--sidePadding) !important` so the landscape env() rule never applied to it. Removed from the media query; container keeps it.
- **Fixed misleading fallback comment** — The `@supports not (selector(:has(*)))` block was documented as "old Tizen fallback" but Tizen TVs use `.layout-tv` (own always-visible rule, no `:has()`). The fallback actually serves **Jellyfin Media Player** (old QtWebEngine desktop app) and iOS <15.4 — without it the series link would be invisible there. Comment now documents the real reason this block must stay.
- Audit also confirmed clean: zero leftovers from the removed v1.2.32 overlay, single consolidated navigation mechanism, `prefers-reduced-motion` respected, TV rules `:has()`-free (old Tizen safe), versions in sync. Privacy note (informational): the Google Fonts `@import` sends visitor IPs to Google — self-hosting Inter is an option if GDPR ever becomes a concern.

---

#### v1.2.42 — Self-hosted fonts (Google Fonts fully removed)

- **Both Google-served fonts now live in this repo** — Previously every visitor's browser contacted `fonts.googleapis.com` + `fonts.gstatic.com` (IP, User-Agent and server URL sent to Google — the Munich court 2022 GDPR precedent). Since the theme CSS is already delivered by jsDelivr, hosting the font files in the repo eliminates Google **without adding any new third party**. Files in `Theme/fonts/`, declared via `@font-face` with **relative URLs** (resolve against the CSS URL → works for `@main`, pinned tags and forks alike):
  - **Inter** (text) — official `rsms/inter` v4.1 variable files, `InterVariable.woff2` 352 KB + Italic 388 KB. The variable font is required: the theme uses `font-weight: 425` and `font-optical-sizing` (wght/opsz axes).
  - **Material Symbols Rounded** (icon pack, the theme's default `--iconPack`) — the exact same v267 variable file Google was serving (~4.9 MB, complete ligature-based icon font, not subsettable). Same download size as before for visitors, just a different source.
- **Bonus**: one less DNS+TLS handshake at load, and fonts keep working where Google is blocked (strict Pi-hole, corporate networks). `font-display: swap` + existing fallbacks = rendering never blocks. Zero action required from users.

---

#### v1.2.43 — Mobile: long series titles no longer clipped on the right

- **Fixed CSS grid blowout on the detail title** — On mobile, long series titles (e.g. "From Overshadowed to Overpowered: Second Reincarnation of a Talentless Sage") were clipped mid-word at the right edge. Root cause: `.infoWrapper` is a `display: grid`, and grid items default to `min-width: auto` — meaning the title container refused to shrink below its content's min-content width, overflowing the viewport. The existing `max-width: 100%` couldn't help because it resolves against an already-blown-out column. Fix: `min-width: 0` on `.nameContainer`/h1/h3 (lets them shrink) + `grid-template-columns: minmax(0, 1fr)` on `.infoWrapper` (caps the column at viewport width). The title now wraps normally at word boundaries within the screen. Mobile-only; desktop/TV unchanged.

---

#### v1.2.44 — Unified monochrome white selection (no more filled squares, no more scattered violet/blue)

Theme-wide consistency pass on every selection/focus state and progress bar. Previously the theme mixed three accent treatments with no clear role — white (Play button, OSD scrubber), violet (`--uiAccentColor`: some focus, some progress, accent text) and blue (`--highlightOutlineColor`: TV focus fills, list/guide focus). The result looked like layered eras rather than one design. Now: a single white-on-dark monochrome system.

- **Selection = white outline, never a filled block.** On TV, focusing a tab/button/list-row/guide-cell/alpha-letter previously filled it with a solid blue (or white) square. Now everything uses a transparent background with a crisp 2px white inset border. Two clear levels: **active** (current tab/page) = white outline; **focus** (remote/keyboard cursor) = white outline + subtle glow (+ scale on cards) so the two are distinguishable when both are on screen.
- **Applies uniformly across TV, mobile and PC.** The active section tab (Films/Séries/Musique) went from a solid white pill to a white outline on all platforms; PC keyboard `:focus-visible` rings went from violet to white; the LiveTV Guide channel/program focus went from blue fill to white outline.
- **Progress bars finished in white.** The card progress bars and OSD scrubber were already white, but the `<progress>` element and `.playbackProgress` indicator were still violet. Now white everywhere — the "White Progress Bars" module is finally complete.
- **Remaining violet neutralized** on minor accents (save-button text, active-button text, progress label, loading spinner) → white.
- **Deliberately kept colored**: the browser text-selection highlight (a white highlight would make selected text invisible) and form-input focus borders (blue, the standard web convention for data-entry fields). These are not navigation-selection states.

---

#### v1.2.45 — TV selection refinements (image-only outline + active ≠ focus)

Two TV issues reported after v1.2.44's white-outline rollout:

- **Card focus outline now wraps the image only, not the title** — The focus outline was on `.cardBox`, which contains both the thumbnail and the title/subtitle text below it, so the white border boxed the whole card including the text. Moved the inset outline to `.cardScalable` (the image area), keeping the scale + depth shadow on `.cardBox`. The outline now hugs just the image.
- **Active tab no longer looks "selected" when it isn't** — v1.2.44 gave the active section tab (current page) the same white outline as the focus state. On TV, where the active indicator and the remote cursor are both visible, the current tab looked permanently selected even when the remote was elsewhere. Active now uses a subtle white tint (`rgba(255,255,255,0.14)`) instead of an outline, so the bright outline is reserved exclusively for the focused element. Clear hierarchy: active = faint tint, focus = bright outline + glow.

---

#### v1.2.46 — TV button focus: fixed white-button bug + much more visible

Follow-up to the v1.2.44 monochrome rollout — the focus on detail-page buttons wasn't working well:

- **🔴 Fixed the white Play/Resume button bug** — v1.2.44's `.show-focus:focus { background-color: transparent }` rule (meant for tabs/nav) also hit the white `.btnPlay` button, turning it transparent on focus so the bluish backdrop showed through ("Reprendre became blue"). And a white outline on a white button is invisible anyway. The button now keeps its white background and gets a **glow + scale (lift)** instead — like a premium set-top box, it lights up and grows toward you. Clearly visible without needing an (invisible) outline.
- **Action icons + header icons much more visible** — The shuffle/check/heart/more buttons and the top header icons (bell, cast, search) had only a thin 2px outline that got lost at TV distance. Now they get a white outline **+ stronger glow + scale 1.12** so they clearly pop when focused.
- **Three focus treatments by button type** — white button = glow + lift (no outline, it'd be invisible); icon buttons = outline + glow + scale; generic list/dialog buttons = outline + glow (no scale, so layout doesn't jump). All white, all on `.layout-tv` only — desktop/mobile unchanged.

---

#### v1.2.47 — Two-tone color system: white focus + violet selection, no more blue

Reconsidered the full-monochrome direction (v1.2.44): pure white turned out to flatten the visual hierarchy — a faint white tint for "active" was hard to see, and it didn't distinguish "selected" from "focused". Switched to a disciplined **two-tone palette**, each color with one clear role:

- **⚪ White = focus / cursor** — where the remote/keyboard is (card outlines, button glow/lift, form-field focus). Unchanged from v1.2.45-46.
- **🟣 Violet = selected / active** — the current tab, selected sidebar item, checked menu item, `.Mui-selected`, filter indicator, hovered metadata links, active toggles, the save action and loading spinner. Violet pops far better than a white tint against the blue-navy base, and being a different colour from white it never gets confused with the focus cursor (which fixes the active-vs-focus ambiguity we fought in v1.2.44-45).
- **❌ Blue removed everywhere** — the `--highlightOutlineColor` blue (form-field focus, checkboxes) was a third accent doing the same job as violet, and blue blends into the navy base. Form-field focus is now **white** (so "focus = white" is the absolute rule across the whole theme).
- **Two near-identical violets unified** — `--uiAccentColor` (rgb 117,111,226) and `--activeColor` (rgb 119,91,244) were two barely-distinguishable purples used interchangeably. Now a single violet.
- **Progress bars stay white** (card bars + OSD scrubber + `<progress>`).

Net palette: navy base + grey text, **white for focus**, **violet for selection/active**, white progress. One accent, one role each.

---

#### v1.2.48 — TV focus: premium streaming solid fill (much more visible) + perf-rule discovery

The thin white outline on focused icons was weak at TV distance. Turns out no major streaming app uses outlines — the major streaming apps use a **solid fill** (the element fills white, icon/text inverts dark), premium set-top UIs use **scale + lift + glow**. Two findings + the fix:

- **🔎 Discovery: a perf rule was silently killing the focus zoom on TV** — `.layout-tv .show-focus:focus { transform: none !important }` (a "low-end TV" optimization) was overriding the `transform: scale()` added in v1.2.46 — so on real TVs the focus only showed the thin outline, no zoom. That's why it felt weak. The fill approach sidesteps this entirely (no transform needed).
- **Icon buttons (action + header) → solid white fill, dark icon** (streaming pattern). Unmistakable at distance, and immune to the perf rule.
- **List rows + LiveTV Guide cells → solid white fill + dark text** — a filled row highlight instead of a thin border. Child text/icons forced dark to avoid white-on-white.
- **Guide date tabs** — were nearly invisible on focus (text-color change only); now solid white fill (focus) / violet (active).
- **Skip-intro button** — outline → solid white fill, so it's clear during playback.
- **Play/Resume button** — since its scale is killed by the perf rule on TV, its **glow was strengthened** (4px ring + 30px halo) so it pops without depending on zoom (premium-TV lift, glow-forward).

All `.layout-tv` only; desktop keyboard focus and mobile unchanged. Focus stays white, active stays violet — just expressed as a fill where an outline was too faint.

---

#### v1.2.49 — Card focus: fixed the "weird zoom" + streaming sibling-dimming on TV

Two card-focus issues on TV, both kept strictly within the theme's colours (white focus, no new colour):

- **🔴 Fixed the "weird zoom" on cards** — focusing a card scaled the whole `.cardBox` to 1.03, but the remote also triggers `:hover`, which scaled the child `.cardScalable` (the image) to 1.06 **on top**. Parent × child transforms multiply (≈1.09 on the image, only 1.03 on the title), so the poster bulged out of sync with its frame/title. The image's own scale is now neutralised on TV — only the card pops, as **one unit** (image + outline + title together) at a clean 1.05. Applies to posters and round cast/director cards alike.
- **✨ streaming sibling-dimming now works on TV** — the "spotlight" effect (focused card stays bright, the rest of the row fades) previously existed on **desktop only** (driven by `:hover`). It's now also driven by remote **focus** on TV: siblings drop to `opacity: 0.5` so the cursor is obvious from across the room. Opacity only — no `filter: saturate` (too GPU-heavy for TV, banned by the perf section). Scoped to `.emby-scroller` so library grids aren't touched, and gated by `:has()` support so older TVs simply get no effect (nothing breaks). No colour added.

Cards can't use the v1.2.48 solid fill (it would hide the poster/face), so the right pattern for cards stays outline + clean pop — exactly what the major streaming apps do.

---

#### v1.2.50 — TV readability: opaque backgrounds for "glass" panels over video

The theme's glass panels (settings menu, dialogs, side menu, toasts…) rely on `backdrop-filter: blur()` for contrast, but the low-end-TV perf section disables that blur on `.layout-tv` — leaving the translucent (or, for the playback-settings menu, fully unstyled Jellyfin-default) background to let the bright video show straight through. Result on Tizen: menus and dialogs were unreadable during playback. The blur was never replaced by anything opaque.

- **Opaque navy background restored on TV** for every panel that loses its blur: the **playback-settings menu** (`.actionSheetContent`), **dialogs** incl. the "Quit Jellyfin?" confirm (`.dialog`), the **"Up Next" card** over the video (`.upNextContainer`), the **side menu** (`.mainDrawer`), **toasts** (`.toast`), the **Now Playing bar** (`.nowPlayingBar`) and the **login card** (`#loginPage`). Same theme navy, just without transparency — no blur needed, so it stays perf-safe.
- **Playback (OSD) header** — its title could look washed-out over a bright scene when its translucent background wasn't active (e.g. with the settings menu open). It now always sits on a dark backdrop on TV.
- Desktop & mobile keep their blur — strictly `.layout-tv` only. The detail-page header was already correct (solid gradient, not blur-dependent) and is unchanged.

---

#### v1.2.51 — TV fix: playback-settings menu was still unreadable (transparent focus + see-through panel)

Follow-up to v1.2.50: the playback-settings menu (Aspect ratio / Speed / Quality / Subtitle offset…) was still unreadable on TV. Two precise causes:

- **Focused row had a transparent background** — a generic "emby-button focus = transparent + white outline" rule (meant for tabs/nav, from v1.2.44) also matched the menu rows (`.listItem.actionSheetMenuItem.emby-button`). The v1.2.48 rule still forced their text dark → dark text on a transparent row over the video = invisible. Fixed by excluding `.listItem` from that rule, so the rows get the intended **white fill** on focus.
- **Panel background wasn't opaque** — v1.2.50 only targeted `.actionSheetContent`, but the visible container is the `.actionSheet` parent. Added it to the opaque-background list, so the whole sheet is solid navy on TV.

`.layout-tv` only; desktop & mobile unchanged.

---

#### v1.2.52 — Hardening: global guard against the TV "unreadable panel" class of bug

Rather than keep fixing these one at a time, a systematic sweep of the two failure modes behind v1.2.50/51:

- **Glass panels that lose their blur on TV** (perf section) — verified every one already has an opaque fallback (dialog, action sheet, side menu, toast, Up-Next, Now-Playing, login). ✅ No gap.
- **Elements given a white fill + forced-dark text on focus** — these break if the generic "transparent on focus" rule catches them (dark text on a transparent background). Beyond the menu rows fixed in v1.2.51, the **LiveTV Guide date tabs and channel-header cells** carried the same latent risk; both are now excluded from that rule so they keep their white fill. (Program cells were already safe — transparent by design, fill on the inner element.)
- **Two invariants are now documented directly in the CSS** so a future edit can't silently reintroduce either bug: any panel added to the TV blur-removal list must also get an opaque background; any white-fill-on-focus element must be excluded from the transparent-focus rule.

`.layout-tv` only; no visible change unless you use the LiveTV Guide on a TV.

---

#### v1.2.53 — Colour consistency: green mini-Play button → white

A design-review sweep of the whole TV interface flagged the one off-palette element: green. The theme is navy + violet (active/selected) + white (focus). Two greens existed — now reconciled:

- **Mini-Play button on cards** (`.cardOverlayFab-primary`, `.listItemImageButton`) was green, clashing with the white main Play button on the detail page. It's now **white with a dark icon**, identical to the main Play.
- **The "watched" indicator** (✓ on played episodes) stays green — it's the universal "watched" convention, and with the mini-Play no longer green it's now the only green, so the palette reads cleanly (navy / violet / white, plus green only for "watched").

---

### Compatibility
- Jellyfin **10.11.x**
- Works on all web browsers (Chrome, Edge, Firefox, Safari), Android app, LG WebOS, Samsung Tizen
- Full `@supports` fallback for browsers without `backdrop-filter`

---

<a name="francais"></a>
## Francais

### Edition Cinema — 28 modules cinematiques par-dessus ElegantFin v26.04.07

Cette version transforme le theme ElegantFin en une experience de streaming professionnelle inspiree des grandes apps de streaming, tout en gardant la compatibilite complete avec bureau, mobile et TV.

---

#### Nouveau dans v1.2.0 — 8 fonctionnalites Cinema

- **Skeleton loading** — Placeholder anime avec effet de pulsation pendant le chargement des images, avec degrade subtil. Desactive sur TV et mouvement reduit.
- **Info au survol** — Texte secondaire (annee, note, genres) apparait en douceur au survol des cartes avec un degrade cinematique (bureau uniquement)
- **Fondu bords scroller** — Degrades lateraux sur les rangees de defilement horizontal, indiquant le contenu defilable. Utilise `--backgroundForAppBar` pour une integration fluide.
- **Scroll-to-top verre** — Bouton avec `backdrop-filter: blur(15px)`, bordure lumineuse, et animation de levitation au survol
- **Badges resolution** — Badges media colores : 4K (dore), HDR (vert), Dolby Vision (violet), Atmos (cyan) avec bordures assorties et fonds subtils
- **Barre Now Playing verre** — Glassmorphism sur la barre de lecture en cours avec `blur(20px) saturate(1.4)`, bordure sombre et ombre. Desactive sur TV.
- **Overlay vu** — Overlay sombre subtil (`rgba(0,0,0,0.35)`) sur les cartes deja vues, s'estompant au survol. Utilise `:has(.playedIndicator)`.
- **Sidebar verre amelioree** — Sidebar avec `blur(20px)`, items de navigation avec coins arrondis, surbrillance au survol, etat selectionne stylise, et en-tetes de section en majuscules

---

#### Glassmorphism & Animations

- **Login glassmorphism** — Carte en verre depoli avec `backdrop-filter: blur(20px)`, animation fluide `loginCardAppear`, et fallback `@supports` pour les anciens navigateurs
- **Transitions de pages** — Animations `pageFadeIn` (0.4s) et `sectionSlideIn` (0.5s) avec delais en cascade sur les sections (increments de 0.05s)
- **Effet shimmer** — Balayage lumineux subtil sur la premiere rangee de cartes (bureau uniquement, desactive sur mobile/TV)
- **Animation du backdrop** — `detailBackdropIn` cinematique avec scale + fade sur les pages de details

---

#### Ameliorations visuelles

- **Cartes Cinema pop** — Scale 1.06x au survol avec bordures lumineuses (`rgba(255,255,255,0.3)`), ombres profondes, et transition du texte vers le blanc
- **Page de details cinema** — Titres ultra-legers (poids 100), tagline italique, synopsis `line-height: 1.65`, bouton Play blanc avec effet de levitation
- **Barres de progression blanches** — Barres `#fff` epurees remplacant les barres colorees, avec effet de lueur sur le slider OSD au survol
- **Badges premium** — Indicateurs floutes en verre (`backdrop-filter: blur(8px)`) pour compteur, resolution et badges vus
- **Dialogues en verre** — `backdrop-filter: blur(20px)` sur les dialogues, `blur(15px)` sur drawer/menus/toast/upNext, tous avec fallback `@supports`

---

#### Typographie & Mise en page

- **Titres de sections** — Gras (700), espacement negatif, fleches chevron masquees, overflow ellipsis avec `max-width: calc(100vw - 8em)`
- **Onglets de navigation** — Onglet actif blanc (`#fff`/`#000`), inactifs subtils (`rgba(255,255,255,0.06)`) avec hover fluide
- **Fix longs titres** — Line-clamp responsive (2 bureau, 3 mobile, 2 TV), word-break sur les metadonnees, gestion overflow du texte des cartes
- **Hierarchie typographique** — Poids affines pour titres d'episodes (600), texte secondaire (`dimTextColor`), titre de page (500)
- **Taille de titres fluide** — `clamp(2em, 5vw, 4em)` pour un dimensionnement fluide sur toutes les tailles d'ecran

---

#### Performances & Accessibilite

- **Optimisations TV** — Tous les `backdrop-filter`, `box-shadow`, animations, `will-change` et shimmer desactives sur layout TV
- **Optimisations mobile** — Intensite de blur reduite (`blur(10px)` au lieu de `blur(20px)`) via requete `@supports`
- **Hints GPU** — `will-change: transform` uniquement au survol (pas permanent), desactive sur TV pour liberer la memoire GPU
- **Mouvement reduit** — Couverture complete `prefers-reduced-motion: reduce` : transitions, shimmer, skeleton, login bounce, backdrop, hover cartes
- **Scrollbars fines** — Scrollbars 4px cross-browser sur `html` (herite, pas `*` universel)
- **Focus-visible** — Indicateurs de focus clavier sur onglets, bouton Play, boutons detail, skip, login

---

#### En-tete & OSD

- **Degrade cinema** — Degrade transparent profond (`rgba(0,0,0,0.75)` vers transparent) remplacant le degrade du theme
- **Header OSD en verre** — Fond `rgba(0,0,0,0.85)` avec `blur(10px)` sur l'en-tete du lecteur video
- **Degrade OSD bas** — Degrade plus doux a 3 paliers (85% vers 50% vers transparent)
- **Slider reactif** — S'agrandit a `0.5em` au survol, pouce blanc avec `border-radius: 2px`, lueur sur la barre de progression
- **Slider Firefox** — Stylisation complete `::-moz-range-thumb` identique a WebKit (taille, bordure, radius, transitions)
- **Bouton skip** — Gras (700), `letter-spacing: 0.03em`, `scale(1.03)` au survol

---

#### v1.2.1 — Corrections visuelles & compatibilite

- **Backdrop etendu** — Masque etendu de 45% a 65%, opacite augmentee de 0.55 a 0.65 — image visible plus bas sur la page detail (PC)
- **Backdrop TV** — Obscurite reduite de 0.95 a 0.6 — le backdrop etait quasi invisible sur TV
- **Titre upNext** — `nowrap` remplace par `line-clamp: 2` — les longs titres d'episodes ne sont plus tronques (toutes plateformes)
- **Header OSD TV** — Titres sur 2 lignes autorises, hauteur reduite a 3.5em — corrige la barre noire surdimensionnee
- **Titre OSD mobile** — `line-clamp: 2` avec largeur max elargie pour les longs titres
- **Hover cartes** — Double zoom supprime (1.06 x 1.04 = 1.10) — maintenant un seul pop propre a 1.06x

---

#### v1.2.2 — Editor's Choice Cinema

- **Editor's Choice Cinema** — Style cinematique complet pour le plugin Editor's Choice : degrade overlay, boutons en verre, zoom backdrop, transitions fluides
- **Slides pleine largeur** — Le carrousel Splide affiche maintenant un slide a la fois (`min-width: 100%`) au lieu de couper plusieurs slides
- **Boutons Cinema** — Les boutons du plugin (`.button-submit`, `.emby-button.raised`) sont maintenant styles avec effet verre, texte blanc et levitation au survol, en accord avec le theme Cinema
- **Desactivation TV** — Tous les blur, ombres et animations Editor's Choice desactives sur layout TV

---

#### v1.2.3 — Qualite CSS & Correctif Next Up

- **Debordement Next Up** — Ajout `max-height` + `overflow-y: auto` pour que le contenu defile au lieu de sortir du cadre
- **Boutons Next Up toujours visibles** — `flex-shrink: 0` empeche les boutons d'etre pousses hors de la vue
- **Retour a la ligne Next Up** — Les longs titres coupent proprement avec `word-break: break-word`
- **Next Up TV/Mobile** — TV : max 35em large, 70vh haut avec padding. Mobile : 90vw large, 75vh haut
- **Corrections audit CSS** — `justify-content: left/right` → `flex-start/flex-end` (CSS invalide), `rgb()` → `rgba()`, fusion des blocs `html {}` dupliques, ajout `line-clamp` standard, suppression `calc(100% - 0em)`, correction police inexistante, compteur modules mis a jour a 29

---

#### v1.2.4 — Finition dialogue Next Up

- **Conteneur plus large** — Ajout `min-width: 28em` pour que le dialogue ne soit jamais trop etroit pour les longs titres et boutons
- **Titre sur 3 lignes** — `line-clamp` augmente de 2 a 3 — les longs titres d'anime/episodes s'affichent completement
- **Boutons contenus** — `width: 100%` sur la rangee de boutons pour qu'ils ne debordent jamais du conteneur
- **Pas de debordement horizontal** — `overflow-x: hidden` empeche le contenu de sortir sur les cotes
- **Reset mobile** — `min-width: unset` sur mobile pour eviter de forcer un conteneur large sur petit ecran

---

#### v1.2.5 — Correctif retour a la ligne Next Up

- **Cause racine corrigee** — Le CSS par defaut de Jellyfin a `white-space: nowrap` + `width: 25.5em` + `text-overflow: ellipsis` sur `.upNextDialog-title`, forcant la troncature sur une seule ligne. Override avec `!important` pour permettre l'affichage multi-lignes
- **Le titre retourne a la ligne** — `white-space: normal`, `width: auto`, `text-overflow: unset` combines avec `line-clamp: 3` — les longs titres d'anime s'affichent sur jusqu'a 3 lignes

---

#### v1.2.6 — Surcharges CSS par defaut de Jellyfin

- **Largeur conteneur upNext** — Jellyfin force `width: 30em` fixe ; surcharge avec `width: auto` pour que `min-width`/`max-width` fonctionnent correctement
- **Largeur boutons upNext** — Jellyfin force `width: 29.75em` fixe ; surcharge avec `width: 100%` pour remplir le conteneur
- **Support RTL** — Ajout `[dir="rtl"] .upNextContainer` margin pour les langues de droite a gauche

---

#### v1.2.7 — Nettoyage & Qualite CSS

- **Retrait Editor's Choice Cinema** — Style du plugin retire (28 modules)
- **Ajout `line-clamp` standard** — Manquant sur `.detail-clamp-text` (bureau/mobile/TV) et `.listItem-overview`
- **Correction `justify-content: right`** — Derniere valeur invalide sur `.endTimeText` → `flex-end`
- **Retrait `will-change` permanent** — Shimmer `::before` ne declare plus `will-change: transform`
- **Correction commentaires obsoletes** — Mise a jour des references de version dans les commentaires
- **Compteur modules mis a jour** — 29 → 28 dans CSS, README et RELEASE_NOTES

---

#### v1.2.8 — Correction hauteur header OSD

- **Header OSD reduit** — Le header du lecteur video utilisait `--appBarHeight` (5em), maintenant fixe a `3em` sur toutes les plateformes — plus de barre noire surdimensionnee pendant la lecture

---

#### v1.2.9 — Correction hauteur header OSD (overrides renforces)

- **Header OSD force a 2.75em** — La regle 3em de v1.2.8 etait surchargee par les defauts Jellyfin. Utilise maintenant `!important` sur `.osdHeader` ET `.headerTop`
- **Boutons OSD reduits** — Boutons du header passes a 2.5em pour s'aligner avec la barre plus courte
- **TV OSD a 3em** — Legerement plus grand sur TV pour la visibilite telecommande, mais toujours bien plus petit que les 5em par defaut

---

#### v1.2.10 — Durcissement CSS & corrections hover TV

- **Tailles `.upNextContainer` forcees** — Ajout de `!important` sur `min-width`, `max-width`, `max-height` pour eviter l'override par les defauts Jellyfin
- **Fusion des selecteurs dupliques** — `.toast` etait defini 3 fois, `.upNextContainer` 2 fois — consolidation en un seul bloc par selecteur
- **Protection hover TV** — Deplacement de `.skip-button:hover`, `.emby-tab-button:hover`, `.MuiButtonBase-root:hover` dans `@media (hover: hover) and (pointer: fine)` pour eviter les etats hover accidentels avec les telecommandes

---

#### v1.2.11 — Nettoyage honnete : retrait des badges resolution colores

- **Couleurs des badges resolution supprimees** — Les couleurs 4K/HDR/Dolby Vision/Atmos ne fonctionnaient en realite jamais sur Jellyfin 10.11.x car le texte du badge est dans `textContent` (pas dans un attribut `title`), et le CSS pur ne peut pas matcher un texte interne. Style generique conserve (bordure arrondie, padding, bordure subtile).
- **Compteur de modules : 28 → 27** — Documentation mise a jour dans README et en-tete CSS
- **Correction README FR** — Reference obsolete "29 modules" corrigee

---

#### v1.2.12 — Selecteurs neutres a la langue & retrait code mort

- **Icone favori remplie** — Remplacement de `.emby-button[title="Favorite"]` par `[is="emby-ratingbutton"]`. L'ancien selecteur ne matchait que Jellyfin en anglais ; l'animation du coeur rempli fonctionne maintenant en **francais, allemand, espagnol, etc.**
- **Bouton livre "Play → Read"** — Retrait du qualificatif `[title="Play"]` pour que le label des livres fonctionne dans toutes les langues
- **Module Scroll-to-Top retire** — Jellyfin 10.11.x n'a aucun element natif `.btnScrollToTop` / `[data-action="scrolltotop"]`. Les 25 lignes de CSS ne ciblaient rien. Compteur modules : 27 → 26.
- **Negation Editor's Choice simplifiee** — `.itemsContainer:not(.editorsChoiceItemsContainer)` → `.itemsContainer` (la classe exclue n'existe plus dans Jellyfin, donc le `:not()` etait de la logique morte)

---

#### v1.2.13 — Correction header OSD desktop : titre plus coupe

- **Hauteur OSD desktop 2.75em → 3em** — Les 2.75em de v1.2.9 etaient trop justes sur navigateur PC : les accents (é, è, à) et les descendants (g, p, y) dans les titres d'episodes etaient coupes en haut/bas. TV et mobile n'etaient pas concernes (regles differentes). Maintenant 3em partout, coherent.
- **Taille de police : 1.1em → 1em** sur `.pageTitle` pour plus d'espace
- **Boutons : 2.5em → 2.75em** pour garder les proportions avec le header plus grand
- **Ajout `overflow: visible`** sur `.headerTop` et `.pageTitle` par securite pour les caracteres accentues

---

#### v1.2.14 — Correction alignement vertical du titre OSD

- **`.pageTitle` centre en flexbox** — L'ancien hack `line-height: 3em` poussait la baseline du texte vers le bas, faisant apparaitre le titre plus bas que la fleche de retour. Remplace par `display: flex; align-items: center; line-height: 1.2` pour que le titre s'aligne parfaitement avec les boutons.

---

#### v1.2.15 — Dialogue Next Up : longs titres forces a passer sur plusieurs lignes

- **`.upNextContainer` max-width 80vw → 34em** — Les 80vw rendaient la popup enorme sur desktop (~1500px sur ecran 1920p), donc les longs titres d'episodes tenaient sur une ligne. Contrainte a 34em (~544px) pour que les longs titres passent naturellement sur 2-3 lignes comme prevu par la regle `line-clamp: 3` existante.

---

#### v1.2.16 — Correction Next Up : overrides TV et mobile

- **`max-width` mobile & TV passe en `!important`** — La v1.2.15 a introduit une regression : le `34em !important` desktop ecrasait les valeurs `90vw` (mobile) et `35em` (TV) qui n'avaient pas `!important`. Sur telephone <544px de large, la popup debordait de l'ecran. Ajout de `!important` sur les overrides layout pour que chaque plateforme garde sa taille : **desktop 34em**, **TV 38em**, **mobile 90vw**.

---

#### v1.2.17 — Barre du haut : degrade style streaming sur les pages de detail

- **Remplacement du header totalement transparent par un degrade** — Sur les pages de detail (films/series), la barre du haut utilisait `background-color: transparent` ce qui la rendait invisible quand le backdrop etait sombre ou absent, rendant les icones difficiles a reperer. Remplace par `linear-gradient(to bottom, rgba(0,0,0,0.75) 0%, rgba(0,0,0,0.4) 60%, transparent 100%)` selon le pattern des grandes apps de streaming. Lisibilite des icones garantie sur n'importe quel backdrop, effet cinema plein ecran preserve — meme renforce grace a la profondeur visuelle ajoutee. Coherent sur **desktop**, **TV** et **mobile**.

---

#### v1.2.18 — Effet spotlight au survol des rangees de cards + nettoyage header

- **Spotlight style streaming sur les rangees horizontales** — Au survol d'une card dans une rangee, les cards voisines se fondent + desaturent (`opacity 0.55`, `saturate(0.7)`, transition 0.3s) pour faire ressortir la card ciblee. Desktop uniquement (scope `@media (hover: hover) and (pointer: fine)`), limite aux `.emby-scroller` pour ne PAS affecter les vues grille des bibliotheques, entierement desactive sous `prefers-reduced-motion`. Degrade gracieux sur les navigateurs sans `:has()` — aucun effet, rien ne casse.
- **Suppression du `text-shadow` fallback obsolete sur les icones du header** — Avec le degrade v1.2.17 qui garantit le contraste sur n'importe quel backdrop, l'ombre `1px 1px 0 #00000080` adoucissait les bords des icones pour rien. Rendu plus net maintenant.
- **Compteur de modules passe a 27** (ajout de Spotlight Hover).

---

#### v1.2.19 — Chevron "Voir tout →" au survol des titres de rangees (pattern streaming)

- **Chevron natif revele au survol** — Le theme cachait jusqu'ici sans condition le `chevron_right` natif de Jellyfin a cote des titres de rangees (Continue Watching, Ajouts recents, etc.). Il apparait desormais au `:hover` via une transition `max-width` + `opacity` + `translateX` (0.25s ease). Affordance propre "voir tout →" style streaming, sans aucun HTML nouveau. Desktop uniquement (`@media hover: hover and pointer: fine`), entierement desactive sous `prefers-reduced-motion`. Le lien derriere est deja cable vers "voir tout" par Jellyfin.

---

#### v1.2.20 — Passe de nettoyage : ~70 lignes de CSS commente mort supprimees

- **Aucun changement fonctionnel**, aucun changement visuel, aucun changement de module — pure hygiene de code.
- Suppression de **8 blocs CSS commentes** (`.detailPagePrimaryContent` ×2, `.videoPlayerContainer`, listItem Episode, `.padded-left`, `#homeTab .overflowBackdropCard`, et un cimetiere de perf `layout-tv *` de 24 lignes). Total ~70 lignes economisees.
- **Fusion de la regle dupliquee `.detailsGroupItem > .label`** — deux blocs separes consolides en un seul, rendu identique.
- **Correction de 2 commentaires de section stale** — `CINEMA FEATURES v1.2.2` → `(introduced v1.2.2, expanded through current)` ; note de retrait Scroll-to-Top deplacee hors de la section Badges ; note historique text-shadow v1.2.18 supprimee (desormais dans ce changelog).
- Audit verifie : `:has()` (76 usages, tous intentionnels et degradant gracieusement), shimmer (deja optimise), prefixes vendor (toujours necessaires) — rien touche.

---

#### v1.2.21 — Wrap du sous-titre episode sur TV + refonte du degrade backdrop

- **TV : le sous-titre wrap sur 3 lignes au lieu de deborder** — Sur Tizen / TV Samsung, en entrant dans un episode de serie, le `.subtitle` (ex. `S01E03 — Titre de l'episode`) sortait de l'ecran car seule la regle globale `white-space: nowrap` s'appliquait. Ajout d'un override `.layout-tv .subtitle` avec `display: -webkit-box; -webkit-line-clamp: 3; line-clamp: 3; max-height: 4em;`. 3 lignes (contre 2 sur mobile) donnent plus d'aisance adapte a la distance de lecture TV, avec `max-height` en garde-fou pour les vieux WebKit Tizen si `-webkit-line-clamp` deconne.
- **Desktop : degrade backdrop bascule du cote au bas (pattern streaming)** — Le `--itemBackdropSideGradient` d'origine assombrissait la moitie GAUCHE du backdrop avec `linear-gradient(90deg, var(--darkerGradientPoint) 0%, transparent 50%)`, concu pour du contenu aligne a gauche. Mais Jellyfin 10.11.x centre logo / boutons / description, donc l'assombrissement lateral cachait la gauche de l'image sans but (ex. coupait des personnages dans Classroom of the Elite). Remplace par un degrade vertical bottom-up `rgba(0,0,0,0.85) → transparent` selon le pattern des grandes apps de streaming : sombre en bas pour le contraste des boutons, image entierement revelee en haut.

---

#### v1.2.22 — Suppression complete de l'overlay backdrop sur desktop (fix regression v1.2.21)

- **`.layout-desktop .itemBackdrop::before` passe en `display: none`** — Le degrade vertical de v1.2.21 fonctionnait bien sur la page principale de serie (~50vh de backdrop) mais noyait les backdrops courts des pages **Saison** et **Episode** (~13vh) ou le degrade couvrait 100% de l'image visible, rendant le backdrop quasi invisible. Apres examen visuel, le fond sombre naturel du theme SOUS le backdrop fournit deja un contraste suffisant pour le bouton Lire et le texte de description. L'overlay assombrissait deux fois sans benefice. Backdrop entierement visible sur tous les types de pages detail (serie, saison, episode). Mobile et TV non affectes (ils utilisent leurs propres regles de `mask`).

---

#### v1.2.23 — Plugin Editor's Choice : fix collision bouton / section suivante

- **Ajout d'overrides pour le [plugin Editor's Choice](https://github.com/lachlandcp/jellyfin-editors-choice-plugin)** — Quand la description (`.editorsChoiceItemOverview`) etait assez longue pour remplir le `-webkit-line-clamp: 4` par defaut du plugin, le bouton "Regarder" en `position: absolute; bottom: 30px` du banner entrait visuellement en collision avec le titre de la section suivante (ex. "Mes medias") car le banner n'avait aucun `margin-bottom`. Ajout de `#editorsChoiceContainer { margin-bottom: 2em }` pour respirer, et resserrement de la description a **3 lignes sur desktop** (`-webkit-line-clamp: 3 !important`) pour garantir l'espace entre le texte et le bouton. Mobile/TV gardent le comportement 4 lignes du plugin. Si le plugin n'est pas installe, ces regles sont inertes (les selecteurs n'existent pas).

---

#### v1.2.24 — Lien parent-serie restaure sur les pages saison / episode (fix UX)

- **Breadcrumb cliquable vers la serie restaure** — Quand une serie possede un clear logo (`.detailLogo`), le theme cachait TOUS les `h1` dans `.nameContainer` pour preserver le look cinema "logo only". Effet de bord silencieux : le lien `<a>` a l'interieur du `h1.parentName` qui permet de revenir a la serie depuis une page saison ou episode etait egalement cache — laissant la fleche du header comme seule methode de remontee. Le `h1.parentName` est maintenant re-affiche comme un petit breadcrumb cliquable et discret (font-size 1em, opacity 0.7, underline) tandis que `h1.itemName` reste cache (evite la redondance avec le logo image). Affecte desktop, mobile et TV. Degrade proprement quand il n'y a pas de logo (ancien comportement). Ajout purement visuel — aucune autre regle modifiee.

---

#### v1.2.25 — Le breadcrumb parent prend le style du titre ("look Saison 3")

- **Breadcrumb parentName restyle pour matcher itemName** — Suite au retour utilisateur, le petit breadcrumb subtil introduit en v1.2.24 jurait avec le gros titre "Saison 3" en dessous. Maintenant `h1.parentName` herite du style par defaut de `.nameContainer h1` (`font-size: clamp(2em, 5vw, 4em)`, weight 100, blanc) — meme que le titre saison/episode — pour que le lien serie parent apparaisse a la taille de titre complete. L'indicateur de clic vient d'un underline 2px en blanc 30% qui s'intensifie a 90% au survol. La hierarchie visuelle est maintenant : **Logo → Lien serie → Titre saison**, tous coherents.

---

#### v1.2.26 — Design final du breadcrumb parent (propre, sans soulignement permanent)

- **Style final du breadcrumb : matche le rendu visible "Saison X" / "Episode Y"** — Iteration suite au retour utilisateur apres v1.2.25 ("le souligne est moche, je veux le meme look que Saison 3, en gras correctement, ni trop grand ni trop petit"). Maintenant `h1.parentName` est style pour matcher le titre saison/episode visible : **font-size 2em**, **font-weight 400 (normal, pas le thin 100 herite)**, **letter-spacing normal** (override le -0.02em du theme), **blanc**, **centre**, avec un text-shadow doux pour la lisibilite. **Pas de souligne permanent** — le lien est propre par defaut. L'indicateur de clic vient d'un souligne subtil qui **apparait uniquement au `:hover`** (1.5px, blanc 60%, offset 0.2em). Sur mobile, decouvert au tap ; sur desktop, le souligne revele au survol souris. Le rendu final est coherent avec l'esthetique cinema/elegante du theme.

---

#### v1.2.27 — Fixes pages detail mobile + force du gradient header TV

Bundle de 4 fixes adressant des problemes utilisateurs reels sur toutes les plateformes :

- **Mobile : breadcrumb parentName cache quand logo present** — Sur le viewport mobile etroit, le `.detailLogo` en `position: absolute` chevauchait visuellement le texte `h1.parentName` du flow (ex. "Moi, quand je me reincarne en Slime" passant a travers le logo dragon sur la page Saison 4). Sur mobile, l'utilisateur navigue en arriere via la fleche `←` du header — pattern UX mobile naturel. Breadcrumb redondant supprime.
- **Mobile : conteneurs detail page contraints au viewport** — Les episodes en cours utilisent un `backdropCard` (vignette large) au lieu de `portraitCard`, ce qui combine avec l'auto-sizing grid de `.infoWrapper` pouvait pousser le contenu hors de l'ecran (texte et image qui depassent a droite). Force `max-width: 100vw; overflow-x: hidden; box-sizing: border-box` sur `.infoWrapper`, `.detailPagePrimaryContent`, `.detailPagePrimaryContainer`, `.detailImageContainer`. Plus `overflow-wrap: anywhere; word-break: break-word` sur les h1/h3 de `.nameContainer` pour que les longs titres wrap proprement. `max-width: 60vw` cape sur la card.
- **Mobile : line-clamp 4 pour longs titres episodes** — Etait 3 lignes, passe a 4. Les longs titres anime ("Saison 3 - 10. La premiere cause de conclusions absurdes, je l'attribue au manque de methode") etaient coupes. Ajout de `max-width: 100%; overflow-wrap: anywhere` sur le bdi aussi.
- **TV : gradient header force quel que soit la combinaison de classes** — Le gradient v1.2.17 reposait sur la classe `.skinHeader-withBackground.semiTransparent` que Tizen via Jellyfin2Samsung n'applique pas toujours sur les pages detail, laissant la barre totalement transparente (icones flottantes sur backdrops clairs). Force maintenant le gradient sur `.layout-tv .skinHeader`, `.layout-tv .skinHeader-withBackground`, `.layout-tv .skinHeader-withBackground.semiTransparent`. Opacite top legerement renforcee (0.85 vs 0.75 desktop) pour compenser la distance de visionnage canape.

---

#### v1.2.28 — Fixes gradient TV (pages saison/episode) + breadcrumb mobile restaure

Iteration suite au test utilisateur :

- **Gradient TV s'applique maintenant aussi sur saison/episode** — v1.2.27 ne marchait que sur la page principale de serie ; les pages saison et episode ont une combinaison de classes differente sur le header non couverte par `.skinHeader-withBackground`. Selecteur simplifie en `.layout-tv .skinHeader:not(.osdHeader)` qui attrape tous les contextes header sauf l'OSD player.
- **Gradient TV adouci pour ressembler a une fine ombre top** — Le gradient precedent (0.85 → 0.5 → 0.15 sur toute la hauteur) faisait paraitre la barre comme un epais bandeau sombre. Nouveau gradient `0.7 → 0.3 → transparent a 80%` fade beaucoup plus vite, donc la zone "sombre" visible ne couvre que le top ~30% du header — une ombre subtile plutot qu'une bande epaisse.
- **Breadcrumb mobile restaure, positionne pour eviter l'overlap logo** — v1.2.27 cachait le breadcrumb sur mobile quand le logo etait visible (pour eviter l'overlap visuel signale en v1.2.24-26). Maintenant le breadcrumb est de retour, affiche a taille moderee (1.5em, weight 400, blanc, centre) avec `margin-top: 18vh` pour le pousser sous le `.detailLogo` en `position: absolute` (qui s'etend grosso modo de 45vh a 62vh sur mobile). Pas de souligne permanent, cible tap propre. Les utilisateurs mobile peuvent maintenant taper le nom de la serie pour revenir en arriere, sans l'overlap logo/texte des iterations precedentes.

---

#### v1.2.29 — Espacement mobile resserre + z-index header TV verrouille

Iteration rapide suite au test utilisateur de v1.2.28 :

- **Marge breadcrumb mobile reduite de 18vh a 5vh** — Le push de 18vh laissait un grand vide noir entre le logo et le breadcrumb sur la page saison. 5vh suffit pour passer sous la zone logo sans creer de vide visuel.
- **Z-index header TV force a 1000** — L'utilisateur a signale que sur Tizen, l'image backdrop apparaissait visuellement AU-DESSUS de la barre header sur les pages saison et episode. L'ajout de `position: relative; z-index: 1000 !important` assure que le header reste au-dessus du backdrop quel que soit l'ordre des couches sur Tizen.

---

#### v1.2.30 — Alignement des chips + espacement mobile breadcrumb resserre

3 fixes adressant des problemes d'alignement visuel :

- **`.mediaInfoOfficialRating` (chip FR-XX age rating) unifie avec les autres chips** — Le style original utilisait `transform: translateY(-0.15em)` + `background: transparent`, ce qui faisait paraitre le badge FR-12 / FR-10 visuellement remonte par rapport aux chips annee, etoile rating, et pourcentage. Sur TV l'offset pouvait meme causer le clipping de la chip en haut. Maintenant matche le style de `.mediaInfoItem:not(.endsAt)` : meme background (`rgba(255,255,255,0.05)`), meme border (`1px rgba(255,255,255,0.15)`), meme border-radius, padding, font-size, font-weight, letter-spacing. Transform supprime. Toutes les chips ont maintenant la meme hauteur avec apparence coherente.
- **Marge mobile breadcrumb reduite de 5vh a 2vh** — 5vh laissait encore un vide visible entre le logo et le breadcrumb. 2vh est le minimum qui evite encore l'overlap avec le bord bas du logo.

---

#### v1.2.31 — Alignement complet des chips (annee / FR-XX / ★ rating / 100%)

- **Tous les chips `.mediaInfoItem` ont maintenant des dimensions strictement identiques** — v1.2.30 ne corrigeait que l'alignement du badge FR-XX (retrait du translateY) mais les chips avaient encore des hauteurs visuelles differentes parce que leur contenu (texte vs texte+icone) determinait leur taille de rendu naturelle. v1.2.31 force `height: 1.8em; min-height: 1.8em; padding: 0 0.6em; line-height: 1; display: inline-flex; align-items: center` sur **chaque** variante de chip — annee, FR-XX, star rating, pourcentage. Meme background, meme border, meme border-radius. Les icones inline (`.material-icons`, `.starIcon`, `svg`) bornees a `font-size: 0.9em` pour ne pas pousser les hauteurs des chips.
- **Conteneur `.itemMiscInfo-primary`** : maintenant `display: flex; flex-wrap: wrap; align-items: center; justify-content: center; column-gap: 0.5em; row-gap: 0.5em` — les chips wrappent sur une seconde ligne sur viewports tres etroits au lieu de deborder/clipper (filet de securite uniquement — reste typiquement sur une ligne).

---

#### v1.2.32 — Navigation logo cliquable + fix wrap subtitle + hover emby-linkbutton global

Plan derive de l'analyse SDK `jellyfin/jellyfin-web` (`controllers/itemDetails/index.js`) :

- **Logo cliquable vers la serie parente (PC + Mobile)** — Le `<a is="emby-linkbutton" data-type="Series">` existant dans `h1.parentName` est utilise comme overlay invisible cliquable couvrant exactement la zone du `.detailLogo`. Click n'importe ou sur le logo → navigation vers la serie parente. Adaptation auto par type de page via `:has(.subtitle)`. Sur page serie principale (pas de `<a>`), le breadcrumb est cache (`:not(:has(a))`) — coherent car deja sur la serie. TV non touche.
- **Lien Saison visible dans subtitle** — Le `<a data-type="Season">` dans `.subtitle` (sur pages episode) recoit un underline subtil au hover, signalant qu'il est cliquable pour remonter a la saison.
- **Hover global `[is="emby-linkbutton"]`** — Tous les Web Components Jellyfin qui sont des liens (artist, album, serie, saison, etc.) recoivent maintenant `cursor: pointer` + leger hover opacity. Ameliore l'UX sur toutes les pages, pas juste detail.
- **Coherence `.musicParentName`** — Les `<a>` artist/album dans les pages musique stylises au meme niveau que les autres breadcrumbs (cursor + hover underline).
- **Polish `.originalTitle`** — Les titres VO (japonais pour animes type Re:ZERO) maintenant en italique, opacity 55%, font-weight 300 pour distinction discrete. Wrap autorise sur PC pour les longs titres romaji.
- **Mobile subtitle line-clamp 4** (etait 2) — Longs titres episodes anime s'affichent maintenant sur 4 lignes au lieu d'etre coupes a 2.
- **PC subtitle wrap 3 lignes** (etait `white-space: nowrap` + ellipsis) — Plus de debordement horizontal sur les longs titres, wrap propre sur 3 lignes.

---

#### v1.2.33 — Polish cross-platform (iOS, telecommande TV, compat vieux Tizen)

Plan derive de l'audit complet de l'ecosysteme (jellyfin-web, jellyfin-tizen, jellyfin-android, jellyfin-androidtv) :

- **iOS Safari : `text-size-adjust: 100%`** — Empeche iOS d'auto-zoomer le texte en cas de changement d'orientation. Sans ca, les iPhones zoomaient le texte de 10-20% en passant portrait → landscape, cassant les layouts CSS soigneusement designes. Tailles texte stables maintenant pour iPhone/iPad Safari.
- **iOS : tap-highlight deja present** — Confirme ligne 203 (`-webkit-tap-highlight-color: transparent !important;`). Aucun changement necessaire.
- **Mobile : support safe-area-inset (notches)** — iPhone X+ ont des notches/Dynamic Island en haut, Home Indicator en bas. Android avec gestures a une system bar en bas. Ajout de `padding-top: env(safe-area-inset-top)` sur `.layout-mobile .skinHeader`, `padding-bottom: env(safe-area-inset-bottom)` sur `.nowPlayingBar`. Landscape : gere aussi left/right safe areas pour notch lateral. `env()` fallback a 0 sur les appareils sans safe areas.
- **TV : focus renforce pour navigation telecommande** — Cards a 3-5m de distance visionnage avaient seulement `0.15em` outline — a peine visible. Maintenant : `3px solid` outline + `box-shadow` glow + leger `scale(1.06)` pour distinction immediate. Pattern premium streaming TV. Idem applique aux boutons (`.btnPlay`, `.detailButton`). Transition `0.15s` pour fluidite.
- **Fallback `:has()` vieux Tizen** — v1.2.32 utilise `:has(a)` pour overlay logo conditionnel. Tizen 2018-2021 (Chromium 76-79) ne supporte pas `:has()`. Ajout d'un bloc `@supports not (selector(:has(*)))` qui ramene le breadcrumb en texte cliquable visible sur ces vieux TVs. Utilisateurs Tizen 9.0+ non affectes (comportement overlay v1.2.32 preserve).

---

#### v1.2.34 — Refactor focus TV : box-shadow inset (fix bordures clipped)

- **Focus TV passe d'outline outside a box-shadow inset** — v1.2.33 (Fix A) utilisait `outline: 3px + outline-offset: 4px + box-shadow: 24px` qui sortaient des conteneurs parents `overflow: hidden`. Resultat : bordures clipped asymetriquement sur les cards en bord de viewport (vu sur screenshots utilisateur — cards Films, Programmes, Stargate, Dr. STONE). Refonte avec `box-shadow inset 0 0 0 3px var(--uiAccentColor)` : la bordure de focus est A L'INTERIEUR du bord de la card, ne peut JAMAIS etre clipped. Glow externe et drop-shadow conserves (peuvent etre clipped sans souci visuel). Scale reduit de 1.06 a 1.03 (moins risque de debordement viewport).
- **Boutons : meme refonte** — `outline + offset` remplace par `inset 0 0 0 2px` (bordure 2px car boutons plus petits). Coherent avec les cards.

---

#### v1.2.35 — Focus TV passe du violet au BLANC (coherence theme)

- **Focus TV de `var(--uiAccentColor)` (violet) a blanc** — Le violet herite de l'upstream ElegantFin ne correspondait pas a l'identite Cinema Edition (bouton Lire blanc, degrades sombres, palette warm cinema). Passe a `rgba(255, 255, 255, 0.95)` pour bordure inset, `rgba(255, 255, 255, 0.3)` pour glow. Visible a distance TV + coherent avec le reste du theme (pattern des grandes apps de streaming qui utilisent tous des focus clairs).
- Box-shadow inset conserve de v1.2.34 (jamais clipped sur cards en bord viewport).
- Cards et boutons traites coherement (3px sur cards, 2px sur boutons).

---

#### v1.2.36 — Subtitle "Saison X" positionne sous le logo (fix overlap PC + Mobile)

- **Push `.nameContainer` sous le logo sur pages Saison/Episode** — Sur PC et Mobile, le logo est `position: absolute` et occupe ~9vh-34vh en vertical. Le `h3.itemName.subtitle` ("Saison 4" ou "Saison X - 7. Episode Y") tombait dans le flow a ~13vh → overlap visuel avec le logo. La regle globale `--itemTitleVisibility: none` cache les `h1` mais pas les `h3`. Fix : `padding-top: 23vh` (PC) / `20vh` (Mobile) sur `.nameContainer` quand `:has(.subtitle)` + logo present. Le `h1.parentName` overlay invisible v1.2.32 (logo cliquable) reste absolute et n'est pas affecte. Les siblings (`itemMiscInfo`, boutons "Lire") suivent naturellement plus bas. TV non touche.

---

#### v1.2.37 — Padding-top restreint aux pages Saison (fix vide sur Episode)

- **Selecteur affine** : `:has(.subtitle:not(.focuscontainer-x))` au lieu de `:has(.subtitle)`. v1.2.36 appliquait le padding-top 23vh/20vh sur Saison ET Episode pages, creant un grand vide sur Episode (ou l'element en haut est une card image, pas un logo). SDK confirme : sur Saison page le `h3.subtitle` n'a PAS `.focuscontainer-x` (juste "Saison X"), sur Episode page `.focuscontainer-x` est present (contient un `<a Season>` link). Le push ne s'applique maintenant que sur Saison pages ou l'overlap logo/subtitle existe vraiment.

---

#### v1.2.38 — Lien serie visible (italique) au-dessus de "Saison X" sur pages Saison

- **Le h1.parentName redevient visible** comme lien italique sur les pages Saison — L'overlay invisible v1.2.32 ne fonctionne pas fiablement en pratique (positioned ancestor mismatch + emby-linkbutton web component sensible a visibility). Plus simple et meilleur UX : rendre le `h1.parentName` visible directement comme un lien italique (taille 1.4em, weight 500, opacity 0.8, italic) au-dessus du subtitle "Saison X". Sur PC, hover revele un underline subtil. Utilise le selecteur `:has(.subtitle:not(.focuscontainer-x))` pour cibler uniquement les pages Saison (pas Series principale ni Episode). Le `<a>` existant dans parentName (pointant vers `data-type="Series"`) reste fonctionnel et marche garantie. Sur Episode pages, l'overlay v1.2.32 reste (sans changement).

---

#### v1.2.39 — Fix v1.2.38 : ajout display:block (override --itemTitleVisibility)

- **Bug v1.2.38** : la regle visible sur h1.parentName n'avait aucun effet visuel — le h1 restait `display: none` herite de la regle globale `display: var(--itemTitleVisibility)` (defaut: none). v1.2.38 overridait position/color/font-size mais PAS display. Element styled mais cache → rien a l'ecran. Fix : ajout `display: block !important;` dans la regle v1.2.38. Le lien italique "Re:ZERO" / "Moi quand je me reincarne en Slime" / etc. apparait maintenant correctement au-dessus de "Saison X" sur les pages Saison.

---

#### v1.2.40 — Consolidation : un seul lien serie visible, suppression de l'overlay invisible casse

- **Suppression de l'overlay invisible cliquable v1.2.32** — Le mecanisme original "clic sur le logo pour aller a la serie" utilisait un overlay invisible (`font-size: 0; color: transparent; position: absolute` avec `calc()`/`left:30%;width:40%` hardcode). L'utilisateur a confirme qu'il ne marchait jamais vraiment (clic logo HS) — le positionnement absolu ne couvrait pas le logo de facon fiable, et le web component emby-linkbutton etait sensible a la transparence. ~60 lignes de code mort fragile supprimees.
- **Generalisation du lien serie visible a TOUTES les pages avec logo** — v1.2.38 avait introduit un lien serie italique visible mais uniquement sur les pages Saison. Il s'applique maintenant aux pages Saison ET Episode (tout `h1.parentName:has(a)` avec un logo). Mecanisme de navigation unique, fiable, coherent : le nom de la serie s'affiche comme lien italique cliquable au-dessus du subtitle, underline au hover sur desktop. Page serie principale (pas de `<a>`) toujours cachee via `:not(:has(a))`. Fallback sans logo (gros titre) preserve. TV non affecte (garde rendu v1.2.26). Moins de code, plus de positionnement `calc()` fragile, plus facile a maintenir.

---

#### v1.2.41 — Audit a froid : encoche iPhone vraiment corrigee + suppression code mort

Audit complet du theme (conflits de cascade, code mort, doc obsolete). Constats et correctifs :

- **🔴 Le padding anti-encoche iPhone etait silencieusement mort sur la home** — La regle v1.2.33 `.layout-mobile .skinHeader { padding-top: env(safe-area-inset-top) }` (specificite 0,2,0) etait battue par la regle pre-existante `.layout-mobile .skinHeader-blurred:not(.osdHeader) { padding: 0 }` (0,3,0) — or le header de la home porte `.skinHeader-blurred`, donc le padding ne s'appliquait jamais la ou l'encoche gene. Corrige avec `!important`. Visible uniquement sur iPhone X+ (env() = 0 ailleurs, zero changement).
- **Suppression de la regle TV focus morte** — L'ancien bloc violet `0.15em outline` etait ecrase a 100% par la regle blanche inset v1.2.35 juste en dessous (meme selecteur, `outline: none !important`). 5 lignes de code mort supprimees ; zero changement visuel sur TV.
- **Suppression de la partie morte du safe-area landscape** — `.detailPagePrimaryContent` a deja `padding-left/right: var(--sidePadding) !important`, la regle env() landscape ne s'y appliquait donc jamais. Retiree de la media query ; le container la garde.
- **Correction du commentaire trompeur du fallback** — Le bloc `@supports not (selector(:has(*)))` etait documente comme "fallback vieux Tizen", mais les TV Tizen utilisent `.layout-tv` (regle toujours-visible dediee, sans `:has()`). Le fallback sert en realite **Jellyfin Media Player** (app desktop, vieux QtWebEngine) et iOS <15.4 — sans lui le lien serie y serait invisible. Le commentaire documente maintenant la vraie raison de garder ce bloc.
- L'audit a aussi confirme : zero residu de l'overlay v1.2.32 supprime, mecanisme de navigation unique consolide, `prefers-reduced-motion` respecte, regles TV sans `:has()` (vieux Tizen safe), versions synchro. Note vie privee (informatif) : le `@import` Google Fonts envoie l'IP des visiteurs a Google — self-hoster Inter est une option si le RGPD devient un sujet.

---

#### v1.2.42 — Polices self-hostees (Google Fonts entierement supprime)

- **Les deux polices servies par Google vivent maintenant dans ce repo** — Avant, le navigateur de chaque visiteur contactait `fonts.googleapis.com` + `fonts.gstatic.com` (IP, User-Agent et URL du serveur envoyes a Google — precedent RGPD du tribunal de Munich 2022). Comme la CSS du theme est deja distribuee par jsDelivr, heberger les polices dans le repo elimine Google **sans ajouter aucun nouveau tiers**. Fichiers dans `Theme/fonts/`, declares via `@font-face` avec des **URLs relatives** (resolues contre l'URL de la CSS → marche pour `@main`, les tags pinnes et les forks) :
  - **Inter** (texte) — fichiers variables officiels `rsms/inter` v4.1, `InterVariable.woff2` 352 Ko + Italic 388 Ko. La variable font est obligatoire : le theme utilise `font-weight: 425` et `font-optical-sizing` (axes wght/opsz).
  - **Material Symbols Rounded** (pack d'icones, le `--iconPack` par defaut du theme) — exactement le meme fichier variable v267 que Google servait (~4,9 Mo, police d'icones complete a ligatures, non-subsettable). Meme poids de telechargement qu'avant pour les visiteurs, juste une source differente.
- **Bonus** : un handshake DNS+TLS de moins au chargement, et les polices fonctionnent la ou Google est bloque (Pi-hole strict, reseaux d'entreprise). `font-display: swap` + fallbacks existants = le rendu ne bloque jamais. Zero action requise cote utilisateurs.

---

#### v1.2.43 — Mobile : les longs titres de serie ne sont plus coupes a droite

- **Correction du "grid blowout" sur le titre de la page detail** — Sur mobile, les longs titres de serie (ex. "From Overshadowed to Overpowered: Second Reincarnation of a Talentless Sage") etaient coupes en plein milieu d'un mot au bord droit. Cause racine : `.infoWrapper` est une `display: grid`, et les items de grille ont `min-width: auto` par defaut — le conteneur du titre refusait donc de retrecir sous la largeur min-content de son contenu, debordant du viewport. Le `max-width: 100%` existant ne pouvait pas aider car il se calcule contre une colonne deja debordee. Fix : `min-width: 0` sur `.nameContainer`/h1/h3 (autorise le retrecissement) + `grid-template-columns: minmax(0, 1fr)` sur `.infoWrapper` (plafonne la colonne a la largeur du viewport). Le titre wrap maintenant normalement aux espaces dans l'ecran. Mobile uniquement ; desktop/TV inchanges.

---

#### v1.2.44 — Selection monochrome blanche unifiee (fini les carres pleins et le violet/bleu eparpille)

Passe de coherence sur tous les etats de selection/focus et les barres de progression. Avant, le theme melangeait trois traitements d'accent sans role clair — blanc (bouton Lire, scrubber OSD), violet (`--uiAccentColor` : certains focus, certaines barres, du texte) et bleu (`--highlightOutlineColor` : fonds focus TV, focus listes/guide). Resultat : un empilement d'epoques plutot qu'un design unique. Maintenant : un seul systeme monochrome blanc-sur-sombre.

- **Selection = contour blanc, jamais un bloc plein.** Sur TV, surligner un onglet/bouton/ligne de liste/cellule de guide/lettre A-Z le remplissait d'un carre bleu (ou blanc) plein. Maintenant tout utilise un fond transparent avec un contour blanc inset 2px net. Deux niveaux clairs : **actif** (onglet/page courante) = contour blanc ; **focus** (curseur telecommande/clavier) = contour blanc + legere lueur (+ zoom sur les cards) pour les distinguer quand les deux sont a l'ecran.
- **Uniforme sur TV, mobile et PC.** L'onglet actif (Films/Series/Musique) est passe de la pastille blanche pleine au contour blanc sur toutes les plateformes ; le focus clavier PC `:focus-visible` est passe du violet au blanc ; le focus du Guide LiveTV (chaines/programmes) est passe du fond bleu au contour blanc.
- **Barres de progression finies en blanc.** Les barres des cards et le scrubber OSD etaient deja blancs, mais l'element `<progress>` et l'indicateur `.playbackProgress` etaient encore violets. Maintenant blanc partout — le module "White Progress Bars" est enfin complet.
- **Violet restant neutralise** sur les accents mineurs (texte bouton enregistrer, texte bouton actif, label de progression, spinner de chargement) → blanc.
- **Garde delibérement une couleur** : le surlignage du texte selectionne (un surlignage blanc rendrait le texte invisible) et le focus des champs de formulaire (bleu, la convention web standard pour la saisie). Ce ne sont pas des etats de selection-navigation.

---

#### v1.2.45 — Raffinements selection TV (contour sur l'image seule + actif ≠ focus)

Deux soucis TV remontes apres le passage au contour blanc de v1.2.44 :

- **Le contour du focus entoure maintenant l'image seule, plus le titre** — Le contour etait sur `.cardBox`, qui contient la vignette ET le texte titre/sous-titre en dessous, donc la bordure blanche encadrait toute la card y compris le texte. Contour inset deplace sur `.cardScalable` (la zone image), le scale + l'ombre de profondeur restent sur `.cardBox`. Le contour epouse maintenant juste l'image.
- **L'onglet actif ne parait plus "selectionne" a tort** — v1.2.44 donnait a l'onglet actif (page courante) le meme contour blanc que l'etat focus. Sur TV, ou l'indicateur d'actif et le curseur telecommande sont visibles en meme temps, l'onglet courant paraissait selectionne en permanence meme quand la telecommande etait ailleurs. L'actif utilise maintenant une teinte blanche discrete (`rgba(255,255,255,0.14)`) au lieu d'un contour, le contour vif est donc reserve exclusivement a l'element focus. Hierarchie claire : actif = teinte legere, focus = contour vif + lueur.

---

#### v1.2.46 — Focus boutons TV : bug bouton blanc corrige + bien plus visible

Suite du passage monochrome v1.2.44 — le focus des boutons de la page detail ne fonctionnait pas bien :

- **🔴 Bug du bouton blanc Lire/Reprendre corrige** — La regle v1.2.44 `.show-focus:focus { background-color: transparent }` (prevue pour les onglets/nav) touchait aussi le bouton blanc `.btnPlay`, le rendant transparent au focus, laissant transparaitre le backdrop bleuté ("Reprendre devenait bleu"). Et un contour blanc sur un bouton blanc est invisible de toute facon. Le bouton garde maintenant son fond blanc et recoit une **lueur + un zoom (lift)** a la place — comme une box premium, il s'illumine et grandit vers toi. Bien visible sans avoir besoin d'un contour (invisible).
- **Icones action + header bien plus visibles** — Les boutons aleatoire/vu/favori/plus et les icones du header (cloche, cast, recherche) n'avaient qu'un fin contour 2px qui se perdait a distance TV. Ils recoivent maintenant un contour blanc **+ lueur renforcee + zoom 1.12** pour ressortir clairement au focus.
- **Trois traitements de focus selon le type de bouton** — bouton blanc = lueur + lift (pas de contour, il serait invisible) ; boutons icone = contour + lueur + zoom ; boutons generiques liste/dialogue = contour + lueur (sans zoom, pour ne pas faire sauter la mise en page). Tout en blanc, tout sur `.layout-tv` uniquement — desktop/mobile inchanges.

---

#### v1.2.47 — Systeme 2-tons : focus blanc + selection violette, fini le bleu

Reconsideration du tout-monochrome (v1.2.44) : le blanc pur aplatissait la hierarchie visuelle — une teinte blanche legere pour "actif" etait peu visible, et ne distinguait pas "selectionne" de "focus". Passage a une **palette 2-tons** disciplinee, chaque couleur avec un role unique :

- **⚪ Blanc = focus / curseur** — la ou pointe la telecommande/le clavier (contours de cards, lueur/lift des boutons, focus des champs de saisie). Inchange depuis v1.2.45-46.
- **🟣 Violet = selectionne / actif** — l'onglet courant, l'item sidebar selectionne, l'element coche dans un menu, `.Mui-selected`, l'indicateur de filtre, les liens metadata au survol, les bascules actives, l'action enregistrer et le spinner de chargement. Le violet ressort bien mieux qu'une teinte blanche sur le fond bleu-navy, et etant d'une couleur differente du blanc il ne se confond jamais avec le curseur focus (ce qui regle l'ambiguite actif-vs-focus combattue en v1.2.44-45).
- **❌ Bleu supprime partout** — le bleu `--highlightOutlineColor` (focus des champs, cases a cocher) etait un 3e accent faisant le meme job que le violet, et le bleu se fond dans le navy. Le focus des champs est maintenant **blanc** (donc "focus = blanc" est la regle absolue dans tout le theme).
- **Deux violets quasi identiques unifies** — `--uiAccentColor` (rgb 117,111,226) et `--activeColor` (rgb 119,91,244) etaient deux violets a peine distinguables utilises indifferemment. Un seul violet desormais.
- **Barres de progression toujours blanches** (barres des cards + scrubber OSD + `<progress>`).

Palette finale : base navy + texte gris, **blanc pour le focus**, **violet pour selection/actif**, barres blanches. Un accent, un role chacun.

---

#### v1.2.48 — Focus TV : pastille pleine streaming premium (bien plus visible) + decouverte d'une regle perf

Le contour blanc fin sur les icones focus etait faible a distance TV. En fait aucune grande app streaming n'utilise de contour — les grandes apps de streaming utilisent une **pastille pleine** (l'element se remplit en blanc, l'icone/texte passe en sombre), les box premium utilisent **zoom + lift + lueur**. Deux constats + le fix :

- **🔎 Decouverte : une regle perf tuait silencieusement le zoom du focus sur TV** — `.layout-tv .show-focus:focus { transform: none !important }` (une optimisation "vieilles TV") ecrasait le `transform: scale()` ajoute en v1.2.46 — donc sur les vraies TV le focus ne montrait que le contour fin, pas de zoom. D'ou l'impression de faiblesse. L'approche fill contourne ca entierement (pas de transform necessaire).
- **Boutons icone (action + header) → pastille blanche pleine, icone sombre** (pattern streaming premium). Imparable a distance, et immunise a la regle perf.
- **Rangees de liste + cellules du Guide LiveTV → fond blanc plein + texte sombre** — une rangee remplie au lieu d'un fin contour. Texte/icones enfants forces en sombre pour eviter le blanc-sur-blanc.
- **Onglets date du Guide** — etaient quasi invisibles au focus (juste un changement de couleur de texte) ; maintenant fond blanc plein (focus) / violet (actif).
- **Bouton Skip intro/generique** — contour → fond blanc plein, bien clair pendant la lecture.
- **Bouton Lire/Reprendre** — comme son zoom est tue par la regle perf sur TV, sa **lueur a ete renforcee** (anneau 4px + halo 30px) pour ressortir sans dependre du zoom (lift premium TV, axe sur la lueur).

Tout sur `.layout-tv` uniquement ; focus clavier desktop et mobile inchanges. Le focus reste blanc, l'actif reste violet — juste exprime en plein la ou un contour etait trop faible.

---

#### v1.2.49 — Focus des cards : correction du "zoom bizarre" + dimming des voisines facon streaming sur TV

Deux soucis de focus des cards sur TV, tous deux strictement dans les couleurs du theme (focus blanc, aucune nouvelle couleur) :

- **🔴 "Zoom bizarre" des cards corrige** — le focus scalait toute la `.cardBox` a 1.03, mais la telecommande declenche aussi le `:hover`, qui scalait l'enfant `.cardScalable` (l'image) a 1.06 **en plus**. Les transforms parent × enfant se multiplient (≈1.09 sur l'image, seulement 1.03 sur le titre) : l'affiche gonflait en decalage avec son cadre/titre. Le scale propre de l'image est maintenant neutralise sur TV — seule la card pop, **d'un seul tenant** (image + contour + titre ensemble) a un 1.05 propre. S'applique aux affiches comme aux cards rondes cast/realisateur.
- **✨ Le dimming streaming des voisines marche maintenant sur TV** — l'effet "spotlight" (la card ciblee reste vive, le reste de la rangee s'attenue) existait **sur PC uniquement** (pilote par `:hover`). Il est maintenant aussi pilote par le **focus** telecommande sur TV : les voisines passent a `opacity: 0.5` pour qu'on repere le curseur depuis le canape. Opacity seule — pas de `filter: saturate` (trop lourd GPU pour la TV, banni par la section perf). Scope a `.emby-scroller` pour ne pas toucher les grilles de bibliotheque, et conditionne au support de `:has()` pour que les vieilles TV n'aient simplement aucun effet (rien ne casse). Aucune couleur ajoutee.

Les cards ne peuvent pas utiliser la pastille pleine de v1.2.48 (ca cacherait l'affiche/le visage), donc le bon pattern pour les cards reste contour + pop propre — exactement ce que font les grandes apps de streaming.

---

#### v1.2.50 — Lisibilite TV : fonds opaques pour les panneaux "verre" sur la video

Les panneaux verre du theme (menu reglages, dialogues, menu lateral, notifications…) comptent sur le `backdrop-filter: blur()` pour leur contraste, mais la section perf "vieilles TV" coupe ce flou sur `.layout-tv` — laissant le fond translucide (ou, pour le menu reglages, totalement par defaut cote Jellyfin) laisser passer la video vive. Resultat sur Tizen : menus et dialogues illisibles en lecture. Le flou n'etait remplace par rien d'opaque.

- **Fond navy opaque restaure sur TV** pour chaque panneau qui perd son flou : le **menu reglages de lecture** (`.actionSheetContent`), les **dialogues** dont le "Quitter Jellyfin ?" (`.dialog`), la **carte "Episode suivant"** par-dessus la video (`.upNextContainer`), le **menu lateral** (`.mainDrawer`), les **notifications** (`.toast`), la **barre "lecture en cours"** (`.nowPlayingBar`) et la **carte de connexion** (`#loginPage`). Meme navy du theme, juste sans transparence — aucun flou requis, donc perf-safe.
- **Header de lecture (OSD)** — son titre pouvait paraitre delave sur une scene vive quand son fond translucide n'etait pas actif (ex. menu reglages ouvert). Il est maintenant toujours sur fond sombre sur TV.
- Desktop et mobile gardent leur flou — strictement `.layout-tv`. Le header de page detail etait deja correct (degrade solide, pas dependant du flou) et reste inchange.

---

#### v1.2.51 — Fix TV : le menu reglages de lecture etait toujours illisible (focus transparent + panneau qui laisse passer)

Suite de v1.2.50 : le menu reglages de lecture (Format d'image / Vitesse / Qualite / Decalage sous-titres…) restait illisible sur TV. Deux causes precises :

- **La ligne ciblee avait un fond transparent** — une regle generique "emby-button focus = transparent + contour blanc" (prevue pour les onglets/nav, depuis v1.2.44) attrapait aussi les lignes du menu (`.listItem.actionSheetMenuItem.emby-button`). La regle v1.2.48 forcait quand meme leur texte en sombre → texte sombre sur ligne transparente par-dessus la video = invisible. Corrige en excluant `.listItem` de cette regle : les lignes reprennent le **fill blanc** au focus.
- **Le fond du panneau n'etait pas opaque** — v1.2.50 ne ciblait que `.actionSheetContent`, mais le conteneur visible est le parent `.actionSheet`. Ajoute a la liste des fonds opaques → toute la feuille est en navy plein sur TV.

`.layout-tv` uniquement ; desktop et mobile inchanges.

---

#### v1.2.52 — Durcissement : garde-fou global contre la classe de bug « panneau illisible sur TV »

Plutot que de corriger au cas par cas, balayage systematique des deux modes de defaillance derriere v1.2.50/51 :

- **Panneaux verre qui perdent leur flou sur TV** (section perf) — verifie que chacun a deja un fond opaque de secours (dialogue, menu reglages, menu lateral, notification, Episode suivant, lecture en cours, connexion). ✅ Aucun manque.
- **Elements avec fill blanc + texte force sombre au focus** — ils cassent si la regle generique « transparent au focus » les attrape (texte sombre sur fond transparent). En plus des lignes de menu corrigees en v1.2.51, les **onglets de date et cellules d'en-tete de chaine du Guide LiveTV** avaient le meme risque latent ; les deux sont maintenant exclus de cette regle et gardent leur fill blanc. (Les cellules de programme etaient deja safe — transparentes par design, fill sur l'enfant.)
- **Deux invariants sont maintenant documentes directement dans le CSS** pour qu'une future modif ne reintroduise silencieusement aucun des deux bugs : tout panneau ajoute a la liste blur:none TV doit aussi recevoir un fond opaque ; tout element fill-blanc-au-focus doit etre exclu de la regle transparent-au-focus.

`.layout-tv` uniquement ; aucun changement visible sauf si tu utilises le Guide LiveTV sur TV.

---

#### v1.2.53 — Coherence couleur : bouton mini-Lire vert → blanc

Une revue design de toute l'interface TV a releve le seul element hors-palette : le vert. Le theme est navy + violet (actif/selectionne) + blanc (focus). Deux verts coexistaient — maintenant reconcilies :

- **Le bouton mini-Lire des cartes** (`.cardOverlayFab-primary`, `.listItemImageButton`) etait vert, ce qui jurait avec le bouton Lire principal blanc de la page detail. Il est maintenant **blanc avec une icone sombre**, identique au Lire principal.
- **L'indicateur « vu »** (✓ sur les episodes regardes) reste vert — c'est la convention universelle « regarde », et comme le mini-Lire n'est plus vert, c'est desormais le seul vert : la palette se lit proprement (navy / violet / blanc, plus vert uniquement pour « vu »).

---

### Compatibilite
- Jellyfin **10.11.x**
- Fonctionne sur tous les navigateurs web (Chrome, Edge, Firefox, Safari), application Android, LG WebOS, Samsung Tizen
- Fallback `@supports` complet pour les navigateurs sans `backdrop-filter`
