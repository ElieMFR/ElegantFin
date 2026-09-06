# ElegantFin Cinema Edition v1.2.95

## [English](#english) | [Francais](#francais)

---

<a name="english"></a>
## English

### Cinema Edition — cinematic modules on top of ElegantFin

This release transforms the ElegantFin theme into a professional, premium streaming experience while keeping full compatibility with desktop, mobile, and TV platforms.

---

#### New in v1.2.0 — 8 Cinema Features

- **Skeleton loading** — Animated pulse placeholder while card images load, with subtle gradient shimmer. Disabled on TV and reduced-motion.
- **Hover preview info** — Secondary text (year, rating, genres) smoothly reveals on card hover with a cinematic bottom gradient overlay (desktop only)
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

#### v1.2.98 — Phones: a way back to Home from a film or series page

On a phone, opening a film or series left you with no route home. That comes from Jellyfin, not the theme: `libraryMenu.js` sets `enableLibraryNavDrawer = layoutManager.desktop`, so the hamburger menu exists on desktop everywhere but on a phone only on the home screen. On a detail page you were left with the back arrow and an edge swipe nobody guesses.

The original ElegantFin had written a fix for exactly this — put the Home button back in the header on phone detail pages — but it never took effect: `display: block` with no `!important`, losing to the rule three lines above it that hides the button on every page with a solid header. Confirmed on a real phone: the button was absent, and a test rule with `!important` brought it straight back.

It now wins, and stays scoped: `html` prefix plus `!important` so nothing outranks it, and `inline-flex` rather than `block` — that is what Jellyfin gives `.paper-icon-button-light`, with centred items, so `block` would knock the icon off-centre. The `:has(#itemDetailPage:not(.hide))` guard is what keeps it contained: Jellyfin leaves old pages in the DOM with a `hide` class, so off a detail page the rule stops applying. Without it, `!important` would spill onto the home screen, where Jellyfin hides the button with matching specificity and importance — and custom CSS, injected last, would win the tie.

Checked on a phone: present on a film or series page, absent on the home screen, absent in libraries. Desktop and TV untouched.

---

#### v1.2.97 — Full audit: a dead feature removed, reduced-motion completed, the last TV blur gone

**The "scroller edge fade" is removed, not repaired.** Its two rules read `var(--backgroundForAppBar)` with no fallback, and that variable has never been defined — not here, not upstream, not in Jellyfin; `git log -S` finds it missing from the entire history since it shipped in v1.2.0. An undefined `var()` without a fallback invalidates the declaration, so `background-image` fell back to `none`: the fade never painted anything, across every release since.

It was deleted rather than fixed because it duplicates the scroll arrows: same 3 em width, same gradient to transparent, same hover trigger. The duplication is structural, not accidental — the class it targeted, `.emby-scroller-container`, is added by the scroll-buttons component itself, so the fade could only ever have appeared exactly where the arrows already are. Its two differences both went the wrong way: its right-hand band stayed lit permanently, and starting at `top: 0` it would have covered the section title, which the arrows deliberately avoid. Its `position: relative` went too — Jellyfin declares it on that same class.

**`prefers-reduced-motion` now covers every animation.** Three escaped it: the mobile backdrop, animated in two places, and the blurhash half of the skeleton placeholder — an infinite loop, the worst kind to leave running for someone who asked for less motion. The accessibility claim in the README now holds.

**TV: the last full-screen blur is gone.** `.backdropImage:before` carried `filter: blur(10px)` plus a 1.1× scale across the whole viewport, with no platform scope. The TV block only stripped its `will-change`, and a `backdrop-filter: none` cannot touch a `filter`. It only showed with Jellyfin's "Backdrops" option enabled — off by default — which is why it went unnoticed.

**Four inert declarations removed:** a `z-index` next to a `display: none`, an empty `.mainDrawer` rule, a `backdrop-filter: none` on two elements that never carried one, and a duplicated TV skeleton rule.

The audit also found nothing wrong in several places worth naming: no dead selectors (446 tokens checked against both Jellyfin 10.11 and master), no conflicting redeclarations, all ten documented options wired, and no external resource of any kind — no `@import`, no remote `url()`, fonts served locally. Six unread variables were left alone on purpose: upstream consumes them, and keeping them keeps the next upstream diff readable.

---

#### v1.2.96 — On phones, the backdrop no longer paints over the text

On a film or series page the theme pins the backdrop image with `position: sticky`. That makes it a *positioned* element, and a positioned element paints above the in-flow text of its siblings — and `.itemBackdrop` sits alongside `.detailPageWrapperContainer`, which holds the title, the subtitle and the overview. The image was therefore composited on top of the text instead of behind it, washing out whatever scrolled through it.

Measured at 375×812: pinned at `top: -30%` with `height: 45vh`, the image leaves 15vh permanently stuck to the top of the screen; minus the top bar, that is a band of roughly 50 px where `elementFromPoint` returned `itemBackdrop` rather than the text. The `-30%` resolves against the viewport and not the page, so the length of the page changes nothing — identical results on a 1,329 px page and a 6,818 px one. The band grows with screen height, vanishes in landscape, and never existed on episode or season pages, whose 28vh backdrop ends up pinned off-screen. Hence a defect that dimmed the text rather than hiding it, and went unreported for a long time.

The text container now takes its own stacking context and moves back in front — exactly what the TV layout already does. The image stays visible in the background and no effect is lost. Desktop was never affected: its backdrop is not sticky, therefore not positioned.

---

#### v1.2.95 — The top bar can no longer get stuck hidden on phones

After a long session on a phone, the top bar sometimes stayed off-screen until the page was reloaded. Jellyfin's scroll detector occasionally misses the "re-pin" event and leaves its `headroom--unpinned` class on the header — and Jellyfin itself never styles that class on the header, only on the footer and the now-playing bar. The theme's own rule was therefore the one thing turning that stuck class into a bar pushed off-screen.

It is now neutralised on phones, as it already was on TV since v1.2.80 and above 1200 px wide. The trade-off is deliberate: the header no longer slides away while scrolling on a phone, so a little screen height is lost, in exchange for a bar that cannot disappear. Desktop below that width keeps the hide-on-scroll, no symptom having been observed there.

---
#### v1.2.94 — Jellyfin 12: the credits block is styled again

Ported from the original ElegantFin. In Jellyfin 12's legacy interface the credits block — Genres, Director, Writers, Studios — lost the `.content` class the theme was targeting, so those lines fell back to unstyled: left-aligned, full-strength text, no separators. They now also match `.focuscontainer-x`, which that markup kept, and the separator rule covers the group's direct children as well.

Verified against Jellyfin 10.11's own markup, where the element carries `class="genres content focuscontainer-x"` — both classes — so 10.11 is unaffected. Upstream replaced the old selector; this fork adds the new one alongside instead, in case a 10.11 variant lacks it.

---

#### v1.2.93 — Critics rating hidden on phones

The info line under a title on a phone — year, runtime, rating, critics score — is cramped on a narrow screen. The critics score is now hidden there, and there only: desktop and TV are unchanged. Set `--criticsRatingVisibility: block` to bring it back.

The idea comes from the original ElegantFin, but scoped to the theme's own `.layout-mobile` rather than a width threshold, and shipped in the direction actually wanted here — upstream ships the opposite of what its own comments describe.

---

#### v1.2.92 — Housekeeping: fourteen inert declarations removed

A full dead-code pass against the real Jellyfin 10.11.11 source (1,067 files) found **no dead selector** — everything the theme targets exists. What it did find was inert declarations: CSS variables and animations that nothing reads, neither the theme nor Jellyfin.

Nine variables and two animations are gone, along with three redundancies found in an earlier audit: a `backdrop-filter` declared twice on the side menu with conflicting values (the first was dead, the menu renders with the second), a `max-width` duplicated on mobile, and a `left` overwritten inside its own rule. Zero visual change.

Eight declarations that look inert were deliberately kept — the OSD gradients, the mini-play colours, the highlight outline and two animations. Nothing in this fork reads them, but the original ElegantFin does, so keeping them makes the next upstream diff readable. A comment in the file now says so, to stop a future pass from "fixing" a variable that drives nothing — which is exactly what the v1.2.82 Firefox campaign did to the two OSD gradients, rewriting them for no effect at all.

---

#### v1.2.91 — The logo now sits above the title, on desktop and mobile

The series or movie logo was positioned in screen units — `top: 45vh` on phones, `calc(100vh - 6em …)` on season pages — while the title below it sat in normal document flow. Two independent coordinate systems, so their relative position depended on the height of the screen: on some devices the logo landed on the title, on others it was cut off inside the top bar. Measured on a real page, the logo's rectangle started at **-91 px** — entirely above the window.

It is now a block in normal flow. The DOM already places it before the title, so it ends up above it by construction, with no coordinate to tune. Its top margin is the height of the app bar, so it can never enter it again, and its size is expressed in `em` rather than screen units, so it no longer changes with the window. The two `padding-top` band-aids that used to push the title down (23vh on desktop, 20vh on mobile) are removed — they were what left the large empty gap. TV is untouched: its own placement was tuned separately and stays as it is.

---

#### v1.2.90 — Home Screen Sections: a readable Top 10, and French Discover badges

The Home Screen Sections plugin draws its giant Top 10 rank numbers with the theme's darkest gradient point — near-black — over a near-black background, so the ranking was all but invisible here. The numbers are now a hollow outline in the theme accent, so the ranking reads at a glance. The plugin's Discover row also hard-codes its `Movie` and `Series` badges in blue and purple; they now take the accent and read `Film` and `Série`. Theme-side only — the plugin itself is not touched.

---

#### v1.2.89 — Skip button: the countdown gauge is back

The TV fix shipped in v1.2.88 used the `background` shorthand, which also resets `background-image` — and that is exactly what Jellyfin draws its 10-second countdown gauge with. The purple bar disappeared on TV.

This release takes the opposite approach: instead of adding an override, the two rules that were repainting the button on TV are excluded from it — the white focus fill (which applied permanently there, since the button takes focus the moment it appears) and the white hover fill (the remote fires `:hover` on Tizen). The button now computes exactly the same style as on desktop and mobile, where it had always been correct, and nothing in the theme paints its background on TV any more. An `⚠️ INVARIANT` comment marks the spot.

---

#### v1.2.88 — The right icons, and the Skip button keeps its colours on TV

- **Books, photos and photo albums showed the wrong icon**, and the outlined "info" icon came out filled. They were designated by numeric character codes inherited from the theme's original icon font; moving to a self-hosted font in v1.2.67 changed what those codes point to. They now use icon **names**, which mean the same thing in the theme's font and in Jellyfin's own — so the mismatch cannot come back.
- **Skip Intro on TV: the button now appears in its final colours.** It used to show up washed out — purple countdown bar turned lavender, dark background turned grey — until you moved the mouse or pressed a key. On TV the button takes focus the instant it appears, and the remote also counts as a mouse-over: two separate rules were painting it white underneath Jellyfin's countdown bar. Focus is now carried by the white ring instead. Desktop and mobile are unchanged.

---

#### v1.2.87 — Housekeeping: Material UI rules that could never match

Follow-up to the discovery that Jellyfin never injects custom CSS into the dashboard. Every Material UI rule in the theme was checked against where its component actually appears in the Jellyfin source — ten rules turned out to be unreachable and were removed (zero visual change):

- The four `Tabs` rules and the activity-log table rules targeted **dashboard-only** components.
- Two selectors in the TV blur-stripping rule targeted Material UI panels, but **TV always runs the legacy app**, so none are ever rendered there.

The rest were confirmed live — including two happy accidents: the rule written for the dashboard's app bar is what already paints Jellyfin 12's modern header navy, and the toggle-group rule now styles that version's A-Z library picker.

---

#### v1.2.86 — No more hairline under the top bar (modern shell)

- The modern shell's top bar drew a crisp line across the screen. It came from a border this theme had written back when the rule targeted the dashboard — where custom CSS is never injected, so it had no effect. Removed: the bar now blends into the page, in keeping with the legacy header that fades out in a gradient. Modern shell only.

---

#### v1.2.85 — Readable primary button, and the profile picture stops touching the top bar

- **The modern shell's primary action button** (e.g. "Play all") was Jellyfin blue with dark text forced by Material UI — poor contrast. It is now **white**, extending the theme's long-standing treatment of playback actions (the detail page's Play button has been white since the Cinema module). Semantic variants keep their own colours: red for destructive actions, green for success.
- **Profile page: the picture no longer touches the top bar.** The page carries the `noSecondaryNavPage` class, which the theme's top-padding rule explicitly excludes — so it received no clearance under the header. Invisible in Jellyfin's own side-by-side layout, but plain to see in the centred layout this theme produces, which is kept because it looks better. Spacing validated on screen.

---

#### v1.2.84 — First pass for Jellyfin 12: the theme's accent reaches the new "modern" shell

Checked against a real Jellyfin 12 server rather than assumed. Jellyfin 12 splits the web app in two: **TV keeps the legacy app** (theme unchanged there), while desktop and mobile default to a new React + Material UI shell. The theme already covers about **95%** of it — cards, detail pages, the player, menus — and the top bar even comes out navy already, thanks to a Material UI rule this fork had written for the 10.11 dashboard.

- Four elements were still stuck on Jellyfin's own palette and now follow the theme's accent: the **active tab**, the **profile avatar**, the **library badge** and **links**.
- **Semantic colours are deliberately left alone**: red for destructive actions, green for progress bars, and the activity-log avatar colours that encode severity — hence the avatar rule being scoped to the top bar only.
- Also verified and deliberately *not* shipped: Jellyfin does not inject custom CSS into the **dashboard** (neither in 10.11 nor in 12.0), so styling its Save buttons and checkboxes would have been dead code.

This is a first pass — Jellyfin 12 is not released yet and its modern shell still changes daily, so these rules will be re-checked when it ships. Nothing here affects 10.11: these elements only exist in the modern shell.

---

#### v1.2.83 — TV: no more dark band sweeping the background during page transitions

- On TV, opening an episode briefly showed a dark band across the backdrop, which vanished once the page finished loading. The cause: the title block's dark veil was a gradient expressed **in percentages of its container's height** — and that height jumps from roughly 46vh (page still loading, no content) to ~2600px once filled. Loaded, the dark part sits far below the screen and only its fade shows; while loading, those same percentages land right in the visible area, painting a dark rectangle.
- The veil is now a **fixed pseudo-element anchored to the bottom of the screen**, so its geometry no longer depends on a height that changes mid-flight — identical before and after loading. TV-scoped, no blur (TV performance doctrine), desktop and mobile untouched. Both other suspects (the gradient's colour hint, and `min-height`) were tested and cleared before landing on this.

---

#### v1.2.82 — Firefox: no more banding lines across card and player gradients

- On Firefox only, thin horizontal lines were drawn across card thumbnails (and, less visibly, over the player and header gradients). Live bisection on Firefox pinned it down: **Firefox leaves a visible seam at every intermediate colour stop of a gradient painted over an image** — including a bare colour hint. Confirmed by experiment: the original gradient (one hint) striped the thumbnails, a six-stop rewrite striped at exactly 20/40/60/80%, and a two-stop version came out clean. Chrome, TV and mobile were already smoothing these.
- The six overlay gradients (card footer, player top/bottom, header ×2, card background) are now **two-stop**, with the fade shaped by the second stop's position instead of by extra steps — so the look is preserved. Fades to transparent are written as same-hue `rgba()` to avoid any colour drift mid-fade.

---

#### v1.2.81 — Accurate seekbar (upstream port), expanded thumb on phones, mobile-vars hardening

Upstream catch-up (6 new commits reviewed; 1 real fix applied, adapted to this fork's look — the rest were either already present, inert with our static icon font, or declined as cosmetic):

- **The playback bar is now pixel-accurate.** The visual track ran the full width while the thumb's real travel stops half a thumb before each edge — so clicks near the start/end seeked slightly off-target, the hover preview bubble was misaligned, and the thumb never quite touched the ends. The track and the bubble's reference element are now inset to match the real travel (verified against `emby-slider.js` in the 10.11 source: both the bubble position and the seek fraction are computed from that element's box). The volume slider benefits too.
- **On phones, the seekbar thumb stays in its expanded state** — touch has no reliable hover, so the enlarged grab target is now permanent there.
- **Mobile variables hardened** (`:root.layout-mobile`): the fork's mobile overrides now win by specificity rather than by file order — the same cascade accident that silently broke them upstream can no longer happen here. No visual change.

---

#### v1.2.80 — TV: the top bar can no longer get stuck hidden

- Jellyfin's scroll detector sometimes misses the "re-pin" event when returning to the top of a page — mostly on TV, where scrolling is driven by remote focus rather than real scroll gestures — leaving the top bar stranded off-screen. On TV the theme's header already scrolls naturally with the page, so the hide-on-scroll translation brought nothing there; it is now neutralized on TV. If Jellyfin's detector misfires, the bar simply stays where it belongs. PC and mobile keep the standard hide-on-scroll behavior.

---

#### v1.2.79 — Housekeeping: seven dead rules removed (verified against the jellyfin-web 10.11 source)

- A systematic audit checked all 454 theme selectors against the real `release-10.11.z` source of jellyfin-web. Seven rules inherited from the original theme targeted UI that no longer exists — old dashboard tasks/devices/branding elements, a jQuery-Mobile-era panel, and a scroller-fade rule that could never match — and were removed (~25 lines, zero visual change). Everything else was confirmed alive, including MUI runtime classes, dynamically built section names, and plugin integrations.

---

#### v1.2.78 — Skip button states finished, slimmer header on mobile too (cross-platform audit)

Outcome of a systematic 3-platform pass over the theme:

- **Skip Intro hover no longer erases its own label.** The hover state still painted the cream-era white background while the navy redesign (v1.2.74) had turned the text white → white-on-white on mouse hover. Hover and pressed states now use the same white pill as focus (black text), and the pressed state no longer flashes the old translucent cream.
- **The Skip focus halo actually shows now** — it was silently losing to the resting border (an `!important` the redesign added).
- **No more hover zoom on TV** for the skip button: Tizen remotes trigger `:hover` and match the pointer media query, so the desktop `scale(1.03)` was running on TV — the last remaining transform exception in the TV performance doctrine.
- **The dead padding under the header tab row is now trimmed on mobile as well** (same lever as desktop in v1.2.76). Tab touch-target height is unchanged; TV untouched.

---

#### v1.2.77 — Editor's Choice title logo no longer stretches on small screens

- The carousel's title logo used `object-fit: fill`, so on very narrow windows (and on phones) it was stretched out of shape. It now keeps its aspect ratio at every width — diagnosed from the live logo's natural-vs-rendered ratio, fixed for both desktop and mobile.

---

#### v1.2.76 — Slimmer PC header, Editor's Choice controls retuned to match

- **The desktop header is slimmer.** On the home page it rendered ~97px tall, but ~23px of that was pure empty padding below the Accueil/Favoris tab row. Trimmed on desktop → ~74px, with nothing shifting or clipping (it was dead space). Diagnosed and validated with live on-page measurements. TV and mobile keep their larger touch targets untouched.
- **Editor's Choice carousel controls retuned** to sit just under the slimmer header — the offset was measured against the real header height and carousel position rather than assumed. Desktop-only.

---

#### v1.2.75 — Editor's Choice controls clear the header in fullscreen

- On wide/fullscreen desktop, the carousel's ‹ ❚❚ › controls sat only ~6px below the top bar — right on its dark gradient band, so they looked faint and cramped ("in the bar"). They now clear it by ~32px, landing on the banner image where the navy pills read cleanly. Desktop-only, single-value change, verified on a local test bench.

---

#### v1.2.74 — Legible skip button, no stray text caret, and PC keyboard focus parity

- **Skip-intro button recolored to navy.** At rest it was cream, which made Jellyfin's violet countdown gauge read as an odd lavender smear. On navy that same native gauge now reads as an on-palette violet progress fill; a white label and a hairline outline keep it legible over dark scenes. Keyboard/TV focus still inverts it to the white pill.
- **Removed a stray blinking text caret** that appeared on the video OSD play/pause button in the PC web player. The insertion caret is now hidden everywhere except real text fields (search, forms).
- **Focus treatments now reach PC keyboard navigation.** Tabbing through the interface on desktop shows the same indicators as the TV remote — white pill on action/header icons, navy inversion on the Play button, white ring on the profile avatar — while mouse clicks stay untouched (`:focus-visible`).

---

#### v1.2.73 — Editor's Choice controls, actually fixed this time (verified on a local test bench)

Third and final round, with a humbling discovery: `editorsChoiceContainer` is a **CSS class** in the plugin's template — not an id. Every previous exclusion (`#editorsChoiceContainer`, v1.2.71 **and** v1.2.72) could never match, and even the theme's own v1.2.23 spacing rule had silently never worked. This round was **rebuilt against the plugin's real markup and verified on a local reproduction** before shipping:

- Exclusions switched to the class → the full-height row arrows truly skip the banner now.
- The controls' `mix-blend-mode: difference` (which painted the "square" artifact once lifted above the header) is neutralized; the cramped 7em box is released.
- The ‹ ❚❚ › controls render as **round navy pills below the nav bar, top-right**, always visible, clickable.
- Bonus: the v1.2.23 banner bottom-margin fix finally applies.

---

#### v1.2.72 — Editor's Choice arrows, the real fix (v1.2.71 was ineffective)

Field-tested and still broken — for two stacked reasons, both now fixed:

- **The v1.2.71 exclusion never matched** — the plugin's `#editorsChoiceContainer` **is** the `verticalSection` itself, and `:has()` only tests descendants. The exclusion now also uses a direct `:not(#editorsChoiceContainer)`, so the full-height-arrows restyle truly skips the banner.
- **The plugin's controls sat under the theme's header** — they're positioned at `z-index: 99` with no `top`; with the full-bleed transparent header (`z-index: 1099`) they ended up covered and unclickable. They're now lifted above it (1100) and offset below the bar.

---

#### v1.2.71 — Editor's Choice banner gets its scroll arrows back on desktop (v1.2.58 regression)

The v1.2.58 full-height scroll arrows restyled **every** `.emby-scrollbuttons` on desktop (absolute-positioned, hidden until you hover the row's section). The Editor's Choice banner has a different structure, so its arrows ended up absolutely positioned with `opacity: 0` and no section-hover to ever reveal them — gone. The full-height treatment is now scoped to regular row sections and explicitly excludes the Editor's Choice container, whose stock arrows are back.

---

#### v1.2.70 — Focus completes its logic: dark inversion for the Play button, ring for the avatar

Two elements where the white pill can't work, now given their proper exception patterns (TV):

- **Play/Resume button** — it's permanently white, so only a glow marked its focus (weak on bright scenes, and you couldn't always tell focused from idle). On focus it now **inverts**: navy fill, white text, white ring — the exact negative of the pill. The system reads as one rule: *on focus, everything inverts* (dark elements fill white; the white element fills dark). Smooth transition already in place; no transform, so no perf-rule conflict (the old scale was dead code anyway).
- **Profile avatar (header)** — it's an image: the v1.2.48 white fill was hidden behind the photo, leaving a barely-visible halo. It now gets a **thick white ring + halo**, the same treatment as the "Who's watching?" profiles — consistent with the images-get-rings doctrine (cards, posters, profiles).

---

#### v1.2.69 — Skip-intro button finally gets its white pill on focus

Embarrassing archaeology: the skip button was a **founding member** of the white-pill focus system (v1.2.48)… but was never added to the generic rule's exclusion list — the very list whose `⚠️ INVARIANT` comment exists to prevent exactly this. Its dedicated white-fill rule has been dead code, outranked in specificity since day one; focusing "Skip Intro" showed the generic thin outline over the video (barely visible on bright scenes). Now excluded: focus = solid white pill + dark text, like everything else.

---

#### v1.2.68 — Original (Japanese) title no longer clipped on the right on TV and mobile

The original-title line (e.g. the Japanese title under the episode name) had its line-wrap fix applied **desktop-only** back in v1.2.32 — on Tizen it stayed `nowrap` and got clipped at the right edge of the screen. The wrap now applies on all three platforms, with `overflow-wrap: anywhere` as a safety net for long spaceless romaji runs.

---

#### v1.2.67 — Fonts: 7.4 MB → 590 KB (−92%), same look

The self-hosted fonts were carrying worldwide coverage nobody used:

- **Text (Inter)** — replaced the global builds (723 KB) with Google's official **latin + latin-extended subset builds** (421 KB total, and the latin-extended blocks lazy-load via `unicode-range` only when a page actually contains rōmaji macrons — Shōnen, Jūjutsu…). French is fully covered by the latin block; **Japanese (kana/kanji) was never covered by Inter** and keeps falling back to the system font exactly as before. The wght+opsz axes are kept (`font-weight: 425`, `font-optical-sizing` intact). Pixel-identical rendering.
- **Icons** — the file served under the "Material Icons Round" family name was actually the 5.2 MB Material Symbols variable font. It's now the **real static Material Icons Round** (169 KB, −97%): the complete classic set that Jellyfin and its plugins target (their stock font IS that set), so no glyph list to maintain and no raw-text risk. Filled/outlined states (favorite heart…) survive through distinct ligature names (`favorite` / `favorite_border`). The theme's `font-variation-settings` rules become inert on a static font and are kept in place, harmless, in case a variable font ever returns.
- Everyday launches are unchanged (everything was already cached); first loads on a fresh device no longer show the icon-style swap, and the fonts survive TV cache eviction far better.
- Rollback if the icon details bother you: pin `@v1.2.66` in your import URL.

---

#### v1.2.66 — Hotfix: focused series title was white-on-white again (v1.2.65 regression)

The v1.2.65 unified rule forces `color: inherit` on the series-title link at **ID specificity** — which silently outranked the v1.2.59 class-specificity fix ("black text inside the white focus pill"). On TV, focusing the series title showed white text in the white pill again. An ID-specificity focus exception restores the black text.

---

#### v1.2.65 — Series title: one unified rule ends the whack-a-mole

Third and final round on the series-title harmonization: series without a clear logo took yet another code path (the base ultra-light rules), so "Mao" still rendered thin and small. Instead of patching a fourth spot, a single **ID-specificity rule** now forces the subtitle format (2em semi-bold, 1.5em on mobile) on **every** path — logo or not, TV/desktop/mobile. It's scoped to pages that have a "Season X - Episode" line, so the main title of logo-less series pages keeps its large display size. Clickability untouched.

---

#### v1.2.64 — Accessibility: the version badge was nearly unreadable

Outcome of the WCAG contrast audit: every text in the theme passes AA except one — the "ElegantFin Cinema Edition vX.X.X" badge at the bottom of the Preferences page used the border colour, measuring **1.86:1** (the AA floor is 4.5:1). Ironically it's the text you read to check which version you're on. It now has its own colour at **~5.5:1**. One line; nothing else changes.

---

#### v1.2.63 — Series title harmonization, corrected reference (and all platforms this time)

Two mistakes in v1.2.62, both fixed after field screenshots:

- **Wrong reference** — v1.2.62 matched the series title to the big ultra-light page title; the request was to match the "Season X - Episode" line (the subtitle: 2em, semi-bold, upright). The series title now uses exactly that format — two twin lines.
- **Missed code path** — v1.2.62 only restyled the TV rule, but on PC/mobile the series title is rendered by a different rule (the v1.2.40 clickable-breadcrumb one: small italic). That path is now harmonized too (desktop 2em, mobile 1.5em to match the mobile subtitle), still clickable with the hover underline.

---

#### v1.2.62 — Series title matches the episode title format on season/episode pages

On season/episode pages, the series name (the clickable breadcrumb above the title) was rendered in a different style than the "Season X - Episode" line below it — regular weight vs the theme's ultra-light display type. They now share the exact same format (ultra-light 100, same size, same letter-spacing and shadow) on TV, with the old-client fallback harmonized too. The breadcrumb stays clickable, and the white-pill focus adapts to the new size.

---

#### v1.2.61 — Upstream port: 11 fixes from the original ElegantFin (54 commits reviewed)

Systematic review of everything the original author shipped since this fork's base (54 commits). Eleven applicable fixes ported, adapted to this theme's systems; features and options were deliberately skipped.

- **Three-dot menu button restored** (critical) — newer Jellyfin versions disable right-click, which made the context menu (mark watched, favorite, delete…) unreachable on desktop. The button is now always available on card hover and list rows.
- **Jellyfin Enhanced supported properly** — the TMDB reviews section no longer overflows the detail page, and external links added by the plugin (Radarr/Sonarr, Letterboxd) now get the theme's link styling (selectors were too strict and missed them).
- **Save button always in view** on settings pages — no more scrolling to the bottom to save.
- **Firefox seek-bar parity** — the slider thumb now reacts to hover/drag/focus exactly like on Chromium (kept white, per the theme's White Progress Bars module).
- **Hamburger menu covers the full screen height** on iPhones (dynamic-viewport units), and the app bar is sticky with proper stacking (fixes several drawer/menu glitches).
- **Icon flash fixed** — Jellyfin's stock icon font is declared as fallback, so icons render instantly while the theme's icon font loads (no more flash of invisible text).
- **Music polish** — vertical track lists no longer inherit the grid column gap; disc headings get a small indent; the cast row sits closer to its title on desktop.
- **Material Symbols refreshed** — the self-hosted icon font is updated to Google's latest revision (newer Jellyfin icon names covered).

Not ported, with reasons: the two Media Bar fixes address bugs in the author's separate add-on file that this theme's own Media Bar integration doesn't have; the checkbox-coverage fix repairs broken `calc()` expressions this theme never had; new features/options (covers add-on, theme videos, sizing variables) were declined.

---

#### v1.2.60 — Infrastructure: real minification, font licenses, version tags, CI — zero visual change

Repository/quality release; the rendered theme is byte-for-byte identical in rules.

- **The distributed file is now actually minified** — `latest-minified.css` had always been a plain copy of the commented source (the name lied). ~40% of the file was comments that every TV/phone downloaded and parsed for nothing. A conservative minifier (`scripts/minify.py`, string-aware, keeps the version header line for CDN verification) now generates it at each deploy: **163 KB → 124 KB** (measured). The versioned file stays fully commented — that's the documentation.
- **Font licenses included** — the theme redistributes Inter (SIL OFL 1.1) and Material Symbols Rounded (Apache 2.0) in `Theme/fonts/`; both licenses **require** their text to accompany redistribution. Canonical texts now sit next to the fonts.
- **Version tags** — each release is now tagged (`v1.2.59`, `v1.2.60`, …), so you can pin `@v1.2.60` in your import URL instead of an unreadable commit hash, and roll back by just changing the tag. The README explains it.
- **CI safety net** — a tiny GitHub Actions workflow validates the CSS syntax on every push (a syntax error makes browsers silently drop everything after it — on `@main` that would ship to every device instantly) and checks that the minified file matches the source.
- **Table of contents** — a navigation summary at the top of the (5,800-line) source file.

---


> 🗄️ Versions before v1.2.60 are in [`RELEASE_NOTES_ARCHIVE.md`](./RELEASE_NOTES_ARCHIVE.md).

---

### Compatibility
- Jellyfin **10.11.x**
- Works on all web browsers (Chrome, Edge, Firefox, Safari), Android app, LG WebOS, Samsung Tizen
- Full `@supports` fallback for browsers without `backdrop-filter`

---

<a name="francais"></a>
## Francais

### Edition Cinema — modules cinematiques par-dessus ElegantFin

Cette version transforme le theme ElegantFin en une experience de streaming professionnelle inspiree des grandes apps de streaming, tout en gardant la compatibilite complete avec bureau, mobile et TV.

---

#### Nouveau dans v1.2.0 — 8 fonctionnalites Cinema

- **Skeleton loading** — Placeholder anime avec effet de pulsation pendant le chargement des images, avec degrade subtil. Desactive sur TV et mouvement reduit.
- **Info au survol** — Texte secondaire (annee, note, genres) apparait en douceur au survol des cartes avec un degrade cinematique (bureau uniquement)
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

#### v1.2.98 — Telephone : un chemin vers l'accueil depuis une fiche film ou serie

Sur telephone, ouvrir un film ou une serie ne laissait plus aucun moyen de rentrer a l'accueil. Cela vient de Jellyfin, pas du theme : `libraryMenu.js` pose `enableLibraryNavDrawer = layoutManager.desktop`, si bien que le menu hamburger existe partout sur PC mais, sur telephone, uniquement sur l'accueil. Sur une fiche il ne restait que la fleche retour et un glissement depuis le bord que personne ne devine.

L'ElegantFin d'origine avait ecrit le correctif pour exactement ce cas — remettre le bouton Accueil dans l'en-tete des fiches sur telephone — mais il ne prenait jamais effet : `display: block` sans `!important`, battu par la regle situee trois lignes plus haut qui cache ce bouton sur toute page a en-tete opaque. Constate sur un vrai telephone : le bouton etait absent, et une regle de test en `!important` le ramenait aussitot.

Il l'emporte desormais, sans deborder : prefixe `html` et `!important` pour que plus rien ne le batte, et `inline-flex` plutot que `block` — c'est ce que Jellyfin donne a `.paper-icon-button-light`, avec centrage des elements, donc `block` decentrait l'icone. Le garde-fou `:has(#itemDetailPage:not(.hide))` est ce qui le contient : Jellyfin laisse les anciennes pages dans le DOM avec une classe `hide`, donc hors fiche la regle cesse de s'appliquer. Sans lui, le `!important` deborderait sur l'accueil, ou Jellyfin cache le bouton a specificite et importance egales — et le CSS personnalise, injecte en dernier, remporterait l'egalite.

Verifie sur telephone : present sur une fiche film ou serie, absent sur l'accueil, absent dans les bibliotheques. PC et TV inchanges.

---

#### v1.2.97 — Audit complet : une fonctionnalite morte retiree, mouvement reduit complete, dernier flou TV supprime

**Le « fondu des bords » des rangees est supprime, pas repare.** Ses deux regles lisaient `var(--backgroundForAppBar)` sans valeur de repli, et cette variable n'a jamais ete definie — ni ici, ni chez upstream, ni chez Jellyfin ; `git log -S` la donne absente de tout l'historique depuis son introduction en v1.2.0. Une `var()` indefinie sans repli invalide la declaration : `background-image` retombait a `none`. Le fondu n'a donc jamais rien peint, dans toutes les versions parues depuis.

Il a ete supprime plutot que repare parce qu'il fait double emploi avec les fleches de defilement : memes 3 em, meme degrade vers transparent, meme declenchement au survol. Le doublon est structurel, pas fortuit — la classe qu'il ciblait, `.emby-scroller-container`, est posee par le composant des boutons lui-meme : le fondu ne pouvait apparaitre QUE la ou les fleches existent deja. Ses deux differences allaient toutes deux dans le mauvais sens : sa bande droite restait allumee en permanence, et partant de `top: 0` elle aurait mordu sur le titre de section, que les fleches evitent expres. Son `position: relative` part avec — Jellyfin le declare deja sur cette meme classe.

**`prefers-reduced-motion` couvre desormais toutes les animations.** Trois lui echappaient : l'image de fond mobile, animee a deux endroits, et la moitie blurhash du squelette de chargement — une boucle infinie, la pire chose a laisser tourner pour quelqu'un qui a demande moins de mouvement. La promesse d'accessibilite du README est enfin tenue.

**TV : le dernier flou plein ecran tombe.** `.backdropImage:before` portait un `filter: blur(10px)` et un agrandissement de 1,1x sur toute la fenetre, sans scope de plateforme. Le bloc TV ne lui retirait que son `will-change`, et un `backdrop-filter: none` ne peut rien contre un `filter`. Il ne se manifestait qu'avec l'option « Arriere-plans » de Jellyfin activee — desactivee par defaut — d'ou son passage inapercu.

**Quatre declarations inertes retirees :** un `z-index` pose a cote d'un `display: none`, une regle `.mainDrawer` vide, un `backdrop-filter: none` sur deux elements qui n'en portaient aucun, et une regle TV du squelette declaree deux fois.

L'audit n'a rien trouve a redire ailleurs, et cela merite d'etre dit : aucun selecteur mort (446 jetons verifies contre Jellyfin 10.11 et master), aucune redeclaration en conflit, les dix options documentees toutes cablees, et aucune ressource externe d'aucune sorte — pas d'`@import`, pas d'`url()` distante, polices servies en local. Six variables non lues ont ete laissees en place volontairement : upstream les consomme, et les garder rend le prochain diff amont lisible.

---

#### v1.2.96 — Sur telephone, l'image de fond ne recouvre plus le texte

Sur une fiche film ou serie, le theme epingle l'image de fond en `position: sticky`. Cela en fait un element *positionne*, et un element positionne se peint au-dessus du texte en flux de ses freres — or `.itemBackdrop` est frere de `.detailPageWrapperContainer`, qui porte le titre, le sous-titre et le resume. L'image etait donc composee par-dessus le texte au lieu d'etre derriere, et delavait tout ce qui defilait dessous.

Mesure en 375×812 : epinglee a `top: -30%` pour `height: 45vh`, elle laisse en permanence 15vh colles en haut de l'ecran ; moins la barre du haut, il reste une bande d'environ 50 px ou `elementFromPoint` renvoyait `itemBackdrop` plutot que le texte. Le `-30%` se resout sur la fenetre et non sur la page : la longueur de la fiche n'y change rien, resultat identique sur 1 329 px et sur 6 818 px. La bande grandit avec la hauteur d'ecran, disparait en paysage, et n'a jamais existe sur les fiches episode ou saison, dont l'image de 28vh se retrouve epinglee hors ecran. D'ou un defaut qui ternissait le texte au lieu de le masquer, et qui n'avait jamais ete signale.

Le conteneur de texte prend desormais son propre contexte d'empilement et repasse devant — exactement ce que fait deja la disposition TV. L'image reste visible en fond, aucun effet n'est perdu. Le PC n'a jamais ete concerne : son image de fond n'est pas collante, donc pas positionnee.

---

#### v1.2.95 — La barre du haut ne peut plus rester coincee sur telephone

Apres une longue session sur telephone, la barre du haut restait parfois hors ecran jusqu'au rechargement de la page. Le detecteur de defilement de Jellyfin rate parfois le reepinglage et laisse sa classe `headroom--unpinned` sur l'en-tete — et Jellyfin lui-meme ne style jamais cette classe sur l'en-tete, seulement sur le pied de page et la barre de lecture en cours. La regle du theme etait donc la seule a traduire cette classe coincee en barre poussee hors ecran.

Elle est desormais neutralisee sur telephone, comme elle l'etait deja sur TV depuis la v1.2.80 et au-dela de 1200 px de large. L'arbitrage est assume : l'en-tete ne s'efface plus au defilement sur telephone, on y perd un peu de hauteur d'ecran, en echange d'une barre qui ne peut plus disparaitre. Le bureau en dessous de cette largeur conserve le masquage, faute de symptome constate.

---
#### v1.2.94 — Jellyfin 12 : le bloc des credits retrouve son style

Porte depuis l'ElegantFin d'origine. Dans l'interface legacy de Jellyfin 12, le bloc des credits — Genres, Realisateur, Scenariste, Studios — a perdu la classe `.content` que le theme ciblait : ces lignes retombaient donc sans style, alignees a gauche, en texte plein et sans separateurs. Elles repondent desormais aussi a `.focuscontainer-x`, que ce balisage a conservee, et la regle de separation couvre egalement les enfants directs du groupe.

Verifie contre le balisage de Jellyfin 10.11, ou l'element porte `class="genres content focuscontainer-x"` — les deux classes — donc la 10.11 n'est pas affectee. Upstream a remplace l'ancien selecteur ; ce fork ajoute le nouveau a cote, au cas ou une variante 10.11 ne le porterait pas.

---

#### v1.2.93 — Note des critiques masquee sur telephone

La ligne d'infos sous un titre sur telephone — annee, duree, classification, note des critiques — est a l'etroit sur un ecran fin. La note des critiques y est desormais masquee, et uniquement la : PC et TV sont inchanges. Mettre `--criticsRatingVisibility: block` pour la reafficher.

L'idee vient de l'ElegantFin d'origine, mais scopee au `.layout-mobile` du theme plutot qu'a un seuil de largeur, et livree dans le sens reellement voulu ici — upstream expedie l'inverse de ce que ses propres commentaires annoncent.

---

#### v1.2.92 — Menage : quatorze declarations inertes retirees

Une passe complete de code mort contre le vrai source de Jellyfin 10.11.11 (1 067 fichiers) n'a trouve **aucun selecteur mort** : tout ce que le theme cible existe bien. En revanche elle a trouve des declarations inertes — des variables CSS et des animations que personne ne lit, ni le theme ni Jellyfin.

Neuf variables et deux animations disparaissent, avec trois redondances reperees lors d'un audit precedent : un `backdrop-filter` declare deux fois sur le menu lateral avec des valeurs differentes (la premiere etait morte, le menu rend avec la seconde), un `max-width` duplique sur mobile, et un `left` ecrase a l'interieur de sa propre regle. Zero changement visuel.

Huit declarations d'apparence inerte sont volontairement conservees — les degrades de l'OSD, les couleurs du bouton mini-lecture, le contour de surbrillance et deux animations. Rien dans ce fork ne les lit, mais l'ElegantFin d'origine si : les garder rend le prochain diff amont lisible. Un commentaire le dit desormais dans le fichier, pour qu'une future passe ne « corrige » pas une variable qui ne pilote rien — c'est exactement ce qu'a fait la campagne Firefox de la v1.2.82 sur les deux degrades de l'OSD, reecrits sans le moindre effet.

---

#### v1.2.91 — Le logo passe au-dessus du titre, sur PC et mobile

Le logo de la serie ou du film etait place en unites d'ecran — `top: 45vh` sur telephone, `calc(100vh - 6em …)` sur les pages Saison — alors que le titre, lui, restait dans le flux normal du document. Deux systemes de coordonnees independants : leur position relative dependait donc de la hauteur de l'ecran, et le logo tombait sur le titre sur certains appareils, ou se retrouvait coupe dans la barre du haut sur d'autres. Mesure sur une vraie page : le rectangle du logo commencait a **-91 px**, soit entierement au-dessus de la fenetre.

Il est desormais un bloc dans le flux. Le DOM le place deja avant le titre : il se retrouve donc au-dessus par construction, sans aucune coordonnee a regler. Sa marge haute vaut la hauteur de la barre d'application, il ne peut donc plus y entrer, et sa taille est exprimee en `em` plutot qu'en unites d'ecran, donc elle ne varie plus avec la fenetre. Les deux `padding-top` qui poussaient le titre vers le bas (23vh sur PC, 20vh sur mobile) sont supprimes : c'est eux qui creaient le grand vide. La TV n'est pas touchee, son placement ayant ete regle separement.

---

#### v1.2.90 — Home Screen Sections : un Top 10 lisible, et des badges Decouvrir en francais

Le plugin Home Screen Sections dessine ses grands numeros de Top 10 avec le point le plus sombre du degrade du theme — quasi noir — sur un fond lui aussi quasi noir : le classement etait donc a peine visible. Les chiffres sont desormais un contour evide a la couleur d'accent du theme, et le classement se lit d'un coup d'oeil. La rangee Decouvrir du plugin code aussi ses badges `Movie` et `Series` en bleu et violet ; ils prennent maintenant l'accent et affichent `Film` et `Serie`. Cote theme uniquement — le plugin lui-meme n'est pas modifie.

---

#### v1.2.89 — Bouton Passer : la jauge de compte a rebours est revenue

Le correctif TV livre en v1.2.88 utilisait le raccourci `background`, qui remet aussi `background-image` a zero — or c'est precisement avec ca que Jellyfin dessine sa jauge des 10 secondes. La barre violette avait disparu sur TV.

Cette version prend le chemin inverse : au lieu d'ajouter une surcharge, les deux regles qui repeignaient le bouton sur TV en sont exclues — le fond blanc du focus (qui s'y appliquait en permanence, le bouton recevant le focus des son apparition) et le fond blanc du survol (la telecommande Tizen declenche `:hover`). Le bouton calcule desormais exactement le meme style que sur PC et mobile, ou il avait toujours ete correct, et plus aucune regle du theme ne peint son fond sur TV. Un commentaire `⚠️ INVARIANT` marque l'endroit.

---

#### v1.2.88 — Les bonnes icones, et le bouton Passer garde ses couleurs sur TV

- **Livres, photos et albums photo affichaient la mauvaise icone**, et l'icone « info » en contour sortait pleine. Elles etaient designees par des codes numeriques herites de la police d'icones d'origine ; le passage a une police auto-hebergee en v1.2.67 a change ce que ces codes designent. Elles utilisent desormais les **noms** des icones, qui veulent dire la meme chose dans la police du theme et dans celle de Jellyfin : l'ecart ne peut plus revenir.
- **Passer Generique sur TV : le bouton nait dans ses couleurs finales.** Il apparaissait delave — barre violette virant au lavande, fond sombre virant au gris — jusqu'a ce qu'on bouge la souris ou appuie sur une touche. Sur TV le bouton prend le focus des son apparition, et la telecommande compte aussi comme un survol souris : deux regles distinctes le peignaient en blanc sous la barre de compte a rebours de Jellyfin. Le focus se lit desormais a l'anneau blanc. Bureau et mobile inchanges.

---

#### v1.2.87 — Menage : des regles Material UI qui ne pouvaient jamais matcher

Suite de la decouverte que Jellyfin n'injecte jamais de CSS personnalise dans le tableau de bord. Chaque regle Material UI du theme a ete confrontee a l'endroit ou son composant apparait reellement dans le source de Jellyfin — dix regles se sont revelees inatteignables et ont ete retirees (zero changement visuel) :

- Les quatre regles `Tabs` et celles du tableau du journal d'activite visaient des composants **exclusifs au tableau de bord**.
- Deux selecteurs de la regle TV qui coupe le flou visaient des panneaux Material UI, alors que **la TV tourne toujours sur l'app legacy** : aucun n'y est jamais rendu.

Le reste est confirme actif — dont deux heureux hasards : la regle ecrite pour la barre du tableau de bord est justement celle qui peint deja en navy le header moderne de Jellyfin 12, et la regle des groupes de boutons habille desormais le selecteur A-Z des bibliotheques de cette version.

---

#### v1.2.86 — Plus de lisere sous la barre du haut (coque moderne)

- La barre du haut de la coque moderne tracait une ligne nette en travers de l'ecran. Elle venait d'une bordure ecrite a l'epoque ou cette regle visait le tableau de bord — ou le CSS personnalise n'est jamais injecte, donc sans effet. Retiree : la barre se fond desormais dans la page, dans l'esprit du header legacy qui s'estompe en degrade. Coque moderne uniquement.

---

#### v1.2.85 — Bouton principal lisible, et la photo de profil ne touche plus la barre du haut

- **Le bouton d'action principal de la coque moderne** (« Tout lire », par exemple) etait en bleu Jellyfin avec un texte sombre impose par Material UI — contraste mediocre. Il passe en **blanc**, ce qui prolonge le traitement etabli de longue date par le theme pour les actions de lecture (le bouton Lire des pages de detail est blanc depuis le module Cinema). Les variantes semantiques gardent leurs couleurs : rouge pour les actions destructives, vert pour le succes.
- **Page Profil : la photo ne touche plus la barre du haut.** Cette page porte la classe `noSecondaryNavPage`, que la regle de marge haute du theme exclut explicitement — elle ne recevait donc aucun degagement sous le header. Invisible dans la disposition cote-a-cote d'origine de Jellyfin, mais bien visible dans la disposition centree que produit ce theme, conservee car jugee plus jolie. Espacement valide a l'ecran.

---

#### v1.2.84 — Premiere passe Jellyfin 12 : l'accent du theme atteint la nouvelle coque « moderne »

Verifie sur un vrai serveur Jellyfin 12, et non suppose. La 12.0 scinde l'application web en deux : **la TV reste sur l'app legacy** (theme inchange), tandis que bureau et mobile passent par defaut sur une nouvelle coque React + Material UI. Le theme y fonctionne deja a environ **95 %** — cartes, pages de detail, lecteur, menus — et la barre du haut en ressort meme deja en navy, grace a une regle Material UI que ce fork avait ecrite pour le tableau de bord de la 10.11.

- Quatre elements restaient figes sur la palette de Jellyfin et suivent desormais l'accent du theme : l'**onglet actif**, l'**avatar du profil**, le **badge de bibliotheque** et les **liens**.
- **Les couleurs semantiques sont volontairement preservees** : rouge des actions destructives, vert des barres de progression, et couleurs des avatars du journal d'activite qui encodent la gravite — d'ou la regle de l'avatar limitee a la barre du haut.
- Egalement verifie et volontairement *non* livre : Jellyfin n'injecte pas de CSS personnalise dans le **tableau de bord** (ni en 10.11 ni en 12.0) ; styliser ses boutons Enregistrer et ses cases a cocher aurait donc ete du code mort.

Il s'agit d'une premiere passe — Jellyfin 12 n'est pas encore sortie et sa coque moderne evolue tous les jours ; ces regles seront revalidees a sa sortie. Rien n'affecte la 10.11 : ces elements n'existent que dans la coque moderne.

---

#### v1.2.83 — TV : plus de bande sombre en travers du fond pendant les changements de page

- Sur TV, ouvrir un episode faisait apparaitre brievement une bande sombre en travers de l'image de fond, qui disparaissait une fois la page chargee. La cause : le voile sombre du bloc titre etait un degrade exprime **en pourcentages de la hauteur de son conteneur** — or celle-ci passe d'environ 46vh (page en cours de chargement, sans contenu) a ~2600 px une fois remplie. Chargee, la zone sombre se situe donc tres en dessous de l'ecran et seul son fondu se voit ; pendant le chargement, ces memes pourcentages retombent en pleine zone visible et peignent un rectangle sombre.
- Le voile est desormais un **pseudo-element fixe ancre au bas de l'ecran** : sa geometrie ne depend plus d'une hauteur qui change en cours de route, donc rendu identique avant et apres chargement. Scope TV, sans flou (doctrine perf TV), bureau et mobile intacts. Les deux autres suspects (l'indication de couleur du degrade, et `min-height`) ont ete testes et ecartes avant d'aboutir a celui-ci.

---

#### v1.2.82 — Firefox : fini les traits de banding sur les degrades des cartes et du lecteur

- Sur Firefox uniquement, de fins traits horizontaux barraient les vignettes des cartes (et, plus discretement, les degrades du lecteur et de l'en-tete). Une bissection en direct sur Firefox a tranche : **Firefox laisse une couture visible a chaque arret de couleur intermediaire d'un degrade pose au-dessus d'une image** — y compris une simple indication de couleur. Verifie par l'experience : la version d'origine (un hint) rayait les vignettes, une reecriture a six arrets rayait exactement a 20/40/60/80 %, et une version a deux arrets est ressortie propre. Chrome, TV et mobile lissaient deja.
- Les six degrades de superposition (pied de carte, haut/bas du lecteur, en-tete ×2, fond de carte) sont desormais a **deux arrets**, l'allure du fondu etant reglee par la position du second arret plutot que par des paliers supplementaires — le rendu est donc preserve. Les fondus vers transparent sont ecrits en `rgba()` de meme teinte pour eviter toute derive de couleur.

---

#### v1.2.81 — Seekbar precise (portage upstream), curseur etendu sur telephone, blindage des vars mobiles

Rattrapage upstream (6 nouveaux commits passes en revue ; 1 vrai fix applique, adapte au look de ce fork — le reste etait deja present, inerte avec notre police d'icones statique, ou decline comme cosmetique) :

- **La barre de lecture est maintenant precise au pixel.** La piste visuelle courait sur toute la largeur alors que la course reelle du curseur s'arrete un demi-curseur avant chaque bord — donc les clics pres du debut/fin sautaient legerement a cote, la bulle de preview etait decalee, et le curseur ne touchait jamais vraiment les extremites. La piste et l'element de reference de la bulle sont desormais ajustes a la course reelle (verifie dans le source 10.11 d'`emby-slider.js` : la position de la bulle ET la fraction de seek sont calculees depuis la boite de cet element). Le slider de volume en profite aussi.
- **Sur telephone, le curseur de la seekbar reste en etat etendu** — le tactile n'a pas de survol fiable, la prise agrandie y est donc permanente.
- **Variables mobiles blindees** (`:root.layout-mobile`) : les overrides mobiles du fork gagnent desormais par specificite plutot que par ordre dans le fichier — l'accident de cascade qui les a silencieusement casses upstream ne peut plus arriver ici. Aucun changement visuel.

---

#### v1.2.80 — TV : la barre du haut ne peut plus rester coincee cachee

- Le detecteur de scroll de Jellyfin rate parfois l'evenement de re-epinglage en revenant tout en haut d'une page — surtout sur TV, ou le defilement est pilote par le focus telecommande plutot que par de vrais gestes de scroll — laissant la barre du haut figee hors ecran. Sur TV, le header du theme defile deja naturellement avec la page : la translation de masquage au scroll n'y apportait rien ; elle est desormais neutralisee sur TV. Si le detecteur de Jellyfin se coince, la barre reste simplement a sa place. PC et mobile gardent le masquage au defilement standard.

---

#### v1.2.79 — Menage : sept regles mortes supprimees (verifiees contre le source jellyfin-web 10.11)

- Un audit systematique a confronte les 454 selecteurs du theme au vrai source `release-10.11.z` de jellyfin-web. Sept regles heritees du theme original visaient une interface qui n'existe plus — anciens elements taches/appareils/branding du dashboard, un panneau de l'ere jQuery Mobile, et une regle de fondu de scroller qui ne pouvait jamais matcher — et ont ete retirees (~25 lignes, zero changement visuel). Tout le reste est confirme vivant, y compris les classes MUI generees au runtime, les noms de sections construits dynamiquement, et les integrations de plugins.

---

#### v1.2.78 — Etats du bouton Passer termines, header affine aussi sur mobile (audit cross-plateforme)

Resultat d'une passe systematique du theme sur les 3 plateformes :

- **Le survol du bouton Passer Generique n'efface plus son propre libelle.** L'etat hover peignait encore le fond blanc de l'ere creme alors que la refonte navy (v1.2.74) avait passe le texte en blanc → blanc sur blanc au survol souris. Les etats survol et appui utilisent maintenant la meme pastille blanche que le focus (texte noir), et l'appui ne flashe plus l'ancien creme translucide.
- **Le halo du focus Passer s'affiche vraiment** — il perdait silencieusement contre le lisere de repos (un `!important` ajoute par la refonte).
- **Plus de zoom au survol sur TV** pour le bouton Passer : la telecommande Tizen declenche `:hover` et matche la media query pointeur, donc le `scale(1.03)` bureau tournait sur TV — la derniere exception transform restante dans la doctrine perf TV.
- **Le padding mort sous la rangee d'onglets du header est maintenant retire aussi sur mobile** (meme levier que le bureau en v1.2.76). La hauteur des cibles tactiles des onglets est inchangee ; TV non touchee.

---

#### v1.2.77 — Le logo de titre Editor's Choice ne s'etire plus sur petit ecran

- Le logo du carrousel etait en `object-fit: fill`, donc sur fenetre tres etroite (et sur telephone) il s'etirait hors de sa forme. Il garde maintenant son ratio a toutes les largeurs — diagnostique via le rapport naturel/affiche du logo en direct, corrige pour le bureau ET le mobile.

---

#### v1.2.76 — Header PC affine, controles Editor's Choice recales en consequence

- **Le header du bureau est affine.** Sur l'accueil il rendait ~97px, mais ~23px etaient du padding vide sous la rangee d'onglets Accueil/Favoris. Retire sur desktop → ~74px, sans que rien ne bouge ni ne se coupe (espace mort). Diagnostique et valide par mesure en direct sur la page. TV et mobile gardent leurs grandes cibles, intacts.
- **Controles du carrousel Editor's Choice recales** pour se poser juste sous le header affine — l'offset a ete mesure sur la vraie hauteur du header et la position du carrousel, plutot que suppose. Bureau uniquement.

---

#### v1.2.75 — Les controles Editor's Choice degagent le header en plein ecran

- Sur bureau large / plein ecran, les controles ‹ ❚❚ › du carrousel n'etaient qu'a ~6px sous la barre du haut — en plein sur son degrade sombre, donc ternes et a l'etroit (« dans la barre »). Ils s'en degagent maintenant de ~32px, poses sur l'image de la banniere ou les pastilles navy ressortent nettement. Bureau uniquement, changement d'une seule valeur, verifie sur banc d'essai local.

---

#### v1.2.74 — Bouton passer lisible, plus de caret texte parasite, parite du focus clavier PC

- **Bouton « passer le generique » repasse en navy.** Au repos il etait creme, ce qui faisait ressortir la jauge de compte a rebours violette native de Jellyfin en une lavande « bizarre ». Sur navy, cette meme jauge se lit comme une progression violette coherente avec la palette ; libelle blanc et fin lisere pour la lisibilite sur scenes sombres. Le focus clavier / TV l'inverse toujours en pastille blanche.
- **Suppression d'un caret de texte clignotant parasite** qui apparaissait sur le bouton lecture/pause de l'OSD video en lecteur web PC. Le curseur d'insertion est desormais masque partout sauf dans les vrais champs de saisie (recherche, formulaires).
- **Les traitements de focus atteignent maintenant la navigation clavier PC.** Parcourir l'interface au clavier (Tab) sur bureau affiche les memes reperes que la telecommande TV — pastille blanche sur les icones action/header, inversion navy sur le bouton Lecture, anneau blanc sur l'avatar du profil — tandis que les clics souris restent intacts (`:focus-visible`).

---

#### v1.2.73 — Controles Editor's Choice, vraiment corriges cette fois (verifies sur banc d'essai local)

Troisieme et derniere passe, avec une decouverte humiliante : `editorsChoiceContainer` est une **classe CSS** dans le template du plugin — pas un id. Toutes les exclusions precedentes (`#editorsChoiceContainer`, v1.2.71 **et** v1.2.72) ne pouvaient jamais matcher, et meme la regle d'espacement v1.2.23 du theme n'avait silencieusement jamais fonctionne. Cette passe a ete **reconstruite sur le markup reel du plugin et verifiee sur une reproduction locale** avant publication :

- Exclusions passees en classe → les fleches pleine-hauteur des rangees ignorent vraiment la banniere.
- Le `mix-blend-mode: difference` des controles (qui peignait le « carre » une fois remonte au-dessus du header) est neutralise ; la boite de 7em qui les ecrasait est liberee.
- Les controles ‹ ❚❚ › s'affichent en **pastilles rondes navy sous la barre de navigation, en haut a droite**, toujours visibles, cliquables.
- Bonus : le fix de marge v1.2.23 sous la banniere s'applique enfin.

---

#### v1.2.72 — Fleches Editor's Choice, le vrai fix (la v1.2.71 etait inefficace)

Teste sur le terrain, toujours casse — pour deux raisons empilees, toutes deux corrigees :

- **L'exclusion v1.2.71 ne matchait jamais** — le `#editorsChoiceContainer` du plugin **est** la `verticalSection` elle-meme, et `:has()` ne teste que les descendants. L'exclusion utilise maintenant aussi un `:not(#editorsChoiceContainer)` direct : le restyle des fleches pleine-hauteur ignore vraiment la banniere.
- **Les controles du plugin etaient sous le header du theme** — positionnes en `z-index: 99` sans `top` ; avec le header transparent full-bleed (`z-index: 1099`) ils finissaient recouverts et incliquables. Ils sont remontes au-dessus (1100) et decales sous la barre.

---

#### v1.2.71 — La banniere Editor's Choice retrouve ses fleches de defilement sur PC (regression v1.2.58)

Les fleches pleine hauteur de la v1.2.58 restylaient **tous** les `.emby-scrollbuttons` du desktop (positionnes en absolu, caches jusqu'au survol de la section de rangee). La banniere Editor's Choice a une structure differente : ses fleches se retrouvaient en absolu avec `opacity: 0` sans aucun survol-de-section pour les reveler — disparues. Le traitement pleine-hauteur est maintenant scope aux sections de rangees classiques et exclut explicitement le conteneur Editor's Choice, dont les fleches d'origine sont de retour.

---

#### v1.2.70 — Le focus boucle sa logique : inversion sombre pour le bouton Lire, anneau pour l'avatar

Deux elements ou la pastille blanche ne peut pas fonctionner, dotes de leurs patterns d'exception (TV) :

- **Bouton Lire/Reprendre** — blanc en permanence, seule une lueur marquait son focus (faible sur scenes claires, et on ne distinguait pas toujours focus et repos). Au focus il s'**inverse** desormais : fond navy, texte blanc, anneau blanc — le negatif exact de la pastille. Le systeme se lit d'une seule regle : *au focus, tout s'inverse* (les elements sombres se remplissent de blanc ; l'element blanc se remplit de sombre). Transition douce deja en place ; aucun transform, donc aucun conflit avec la regle perf (l'ancien scale etait du code mort).
- **Avatar du profil (header)** — c'est une image : le fill blanc v1.2.48 etait cache derriere la photo, ne laissant qu'un halo a peine visible. Il recoit maintenant un **anneau blanc epais + halo**, le meme traitement que les profils « Qui regarde ? » — coherent avec la doctrine « les images recoivent un anneau » (cartes, affiches, profils).

---

#### v1.2.69 — Le bouton Passer Generique recoit enfin sa pastille blanche au focus

Archeologie genante : le bouton skip etait un **membre fondateur** du systeme pastille blanche (v1.2.48)… mais n'a jamais ete ajoute a la liste d'exclusion de la regle generique — celle-la meme dont le commentaire `⚠️ INVARIANT` existe pour empecher exactement ca. Sa pastille dediee etait du code mort, battue en specificite depuis le premier jour ; au focus, « Passer Generique » n'affichait que le contour fin generique par-dessus la video (peu visible sur les scenes claires). Desormais exclu : focus = pastille blanche pleine + texte sombre, comme tout le reste.

---

#### v1.2.68 — Le titre original (japonais) n'est plus coupe a droite sur TV et mobile

La ligne du titre original (ex. le titre japonais sous le nom d'episode) avait recu son correctif de retour a la ligne **uniquement sur desktop** en v1.2.32 — sur Tizen elle restait en `nowrap` et se faisait couper au bord droit de l'ecran. Le retour a la ligne s'applique maintenant sur les trois plateformes, avec `overflow-wrap: anywhere` en filet pour les longues suites romaji sans espaces.

---

#### v1.2.67 — Polices : 7,4 Mo → 590 Ko (−92 %), meme rendu

Les polices auto-hebergees embarquaient une couverture mondiale que personne n'utilisait :

- **Texte (Inter)** — les builds mondiaux (723 Ko) sont remplaces par les **builds subset officiels Google latin + latin-etendu** (421 Ko au total, et les blocs latin-etendu se chargent PARESSEUSEMENT via `unicode-range`, uniquement quand une page contient des macrons romaji — Shonen, Jujutsu…). Le francais est entierement couvert par le bloc latin ; **le japonais (kana/kanji) n'a jamais ete couvert par Inter** et continue de retomber sur la police systeme, exactement comme avant. Les axes wght+opsz sont conserves (`font-weight: 425`, `font-optical-sizing` intacts). Rendu identique au pixel.
- **Icones** — le fichier servi sous le nom de famille « Material Icons Round » etait en realite la police variable Material Symbols de 5,2 Mo. C'est desormais la **vraie statique Material Icons Round** (169 Ko, −97 %) : le set classique complet que Jellyfin et ses plugins ciblent (leur police stock EST ce set) → aucune liste de glyphes a maintenir, aucun risque de texte brut. Les etats plein/contour (coeur favori…) survivent via les noms de ligatures distincts (`favorite` / `favorite_border`). Les regles `font-variation-settings` du theme deviennent inertes sur une statique et restent en place, inoffensives, au cas ou une variable revienne un jour.
- Les lancements quotidiens ne changent pas (tout etait deja en cache) ; les premiers chargements d'un appareil neuf n'affichent plus la bascule de style des icones, et les polices survivent bien mieux a l'eviction du cache TV.
- Retour arriere si les details d'icones te genent : pinner `@v1.2.66` dans l'URL d'import.

---

#### v1.2.66 — Hotfix : le titre de serie focus etait redevenu blanc-sur-blanc (regression v1.2.65)

La regle unifiee v1.2.65 force `color: inherit` sur le lien du titre de serie a **specificite ID** — ce qui ecrasait silencieusement le fix v1.2.59 en specificite classe (« texte noir dans la pastille blanche »). Sur TV, le focus sur le titre de serie raffichait du blanc dans la pastille blanche. Une exception focus a specificite ID retablit le texte noir.

---

#### v1.2.65 — Titre de serie : une regle unique met fin au chat-et-la-souris

Troisieme et derniere passe sur l'harmonisation du titre de serie : les series SANS logo passaient par encore un autre chemin (les regles de base ultra-fines), donc « Mao » restait fin et petit. Plutot que de rustiner un quatrieme endroit, une seule **regle a specificite ID** force desormais le format du subtitle (2em semi-gras, 1.5em mobile) sur **tous** les chemins — avec ou sans logo, TV/PC/mobile. Elle est scopee aux pages qui ont une ligne « Saison X - Episode », donc le titre principal des pages Serie sans logo garde sa grande taille. Cliquabilite intacte.

---

#### v1.2.64 — Accessibilite : le badge de version etait quasi illisible

Resultat de l'audit de contraste WCAG : tous les textes du theme passent AA sauf un — le badge « ElegantFin Cinema Edition vX.X.X » en pied de la page Preferences utilisait la couleur des bordures, mesuree a **1.86:1** (le plancher AA est 4.5:1). Ironiquement, c'est le texte qu'on lit pour verifier sa version. Il a maintenant sa propre couleur a **~5.5:1**. Une ligne ; rien d'autre ne change.

---

#### v1.2.63 — Harmonisation du titre de serie, bon referent cette fois (et toutes les plateformes)

Deux erreurs en v1.2.62, corrigees grace aux captures terrain :

- **Mauvais referent** — v1.2.62 avait aligne le titre de serie sur le grand titre ultra-fin ; la demande etait de l'aligner sur la ligne « Saison X - Episode » (le subtitle : 2em, semi-grasse, droite). Le titre de serie utilise maintenant exactement ce format — deux lignes jumelles.
- **Chemin de code rate** — v1.2.62 ne restylait que la regle TV, mais sur PC/mobile le titre de serie passe par une autre regle (celle du fil d'Ariane cliquable v1.2.40 : petite italique). Ce chemin est maintenant harmonise aussi (PC 2em, mobile 1.5em pour coller au subtitle mobile), toujours cliquable avec le souligne au survol.

---

#### v1.2.62 — Le titre de serie adopte le format du titre d'episode sur les pages saison/episode

Sur les pages saison/episode, le nom de la serie (le fil d'Ariane cliquable au-dessus du titre) etait rendu dans un style different de la ligne « Saison X - Episode » en dessous — graisse normale contre l'ultra-fine signature du theme. Ils partagent maintenant exactement le meme format (ultra-fine 100, meme taille, memes lettres et ombre) sur TV, avec le fallback vieux clients harmonise aussi. Le fil d'Ariane reste cliquable, et la pastille blanche du focus s'adapte a la nouvelle taille.

---

#### v1.2.61 — Portage upstream : 11 fixes du ElegantFin original (54 commits passes en revue)

Revue systematique de tout ce que l'auteur original a publie depuis la base de ce fork (54 commits). Onze fixes applicables portes, adaptes aux systemes de ce theme ; les nouveautes et options ont ete volontairement ecartees.

- **Bouton trois-points restaure** (critique) — les Jellyfin recents desactivent le clic droit, ce qui rendait le menu contextuel (marquer vu, favoris, supprimer…) inaccessible sur PC. Le bouton est de nouveau disponible au survol des cartes et sur les rangees de liste.
- **Jellyfin Enhanced correctement supporte** — la section avis TMDB ne deborde plus de la page detail, et les liens externes ajoutes par le plugin (Radarr/Sonarr, Letterboxd) recoivent maintenant le style de liens du theme (les selecteurs trop stricts les rataient).
- **Bouton Enregistrer toujours visible** dans les pages de parametres — fini de defiler jusqu'en bas pour sauvegarder.
- **Parite Firefox sur la barre de lecture** — le curseur reagit au survol/glisser/focus exactement comme sur Chromium (reste blanc, conformement au module White Progress Bars).
- **Le menu hamburger couvre toute la hauteur d'ecran** sur iPhone (unites de viewport dynamiques), et la barre d'application est sticky avec un empilement correct (corrige plusieurs bugs de menu/tiroir).
- **Flash des icones corrige** — la police d'icones stock de Jellyfin est declaree en repli : les icones s'affichent instantanement pendant le chargement de la police du theme (fini le flash de texte invisible).
- **Finitions musique** — les listes verticales de pistes n'heritent plus du gap de colonnes des grilles ; les en-tetes de disque ont un leger retrait ; la rangee du casting se rapproche de son titre sur PC.
- **Material Symbols rafraichi** — la police d'icones auto-hebergee passe a la derniere revision de Google (nouvelles icones des Jellyfin recents couvertes).

Non portes, avec raisons : les deux fixes Media Bar corrigent des bugs du fichier add-on separe de l'auteur, que l'integration Media Bar propre a ce theme n'a pas ; le fix des checkboxes repare des `calc()` casses que ce theme n'a jamais eus ; les nouveautes/options (add-on covers, theme videos, variables de taille) ont ete ecartees.

---

#### v1.2.60 — Infrastructure : vraie minification, licences des polices, tags de version, CI — zero changement visuel

Release depot/qualite ; le theme rendu est identique regle pour regle.

- **Le fichier distribue est maintenant vraiment minifie** — `latest-minified.css` avait toujours ete une simple copie de la source commentee (le nom mentait). ~40 % du fichier etait des commentaires que chaque TV/telephone telechargeait et parsait pour rien. Un minifieur conservateur (`scripts/minify.py`, respecte les chaines, garde la ligne d'en-tete de version pour la verification CDN) le genere a chaque deploiement : **163 Ko → 124 Ko** (mesure). Le fichier versionne reste entierement commente — c'est la documentation.
- **Licences des polices incluses** — le theme redistribue Inter (SIL OFL 1.1) et Material Symbols Rounded (Apache 2.0) dans `Theme/fonts/` ; ces deux licences **exigent** que leur texte accompagne la redistribution. Les textes canoniques sont maintenant a cote des polices.
- **Tags de version** — chaque release est desormais taguee (`v1.2.59`, `v1.2.60`, …) : vous pouvez pinner `@v1.2.60` dans votre URL d'import au lieu d'un hash illisible, et revenir en arriere en changeant juste le tag. Le README l'explique.
- **Filet de securite CI** — un petit workflow GitHub Actions valide la syntaxe CSS a chaque push (une erreur de syntaxe fait ignorer silencieusement tout ce qui suit — sur `@main` ca partirait instantanement sur tous les appareils) et verifie que le fichier minifie correspond a la source.
- **Sommaire** — un guide de navigation en tete du fichier source (5 800 lignes).

---


> 🗄️ Les versions anterieures a la v1.2.60 sont dans [`RELEASE_NOTES_ARCHIVE.md`](./RELEASE_NOTES_ARCHIVE.md).

---

### Compatibilite
- Jellyfin **10.11.x**
- Fonctionne sur tous les navigateurs web (Chrome, Edge, Firefox, Safari), application Android, LG WebOS, Samsung Tizen
- Fallback `@supports` complet pour les navigateurs sans `backdrop-filter`
