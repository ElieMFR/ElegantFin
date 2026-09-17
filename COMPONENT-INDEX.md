# Index des composants — ElegantFin Cinema Edition v1.3.4

Généré par `python scripts/component-index.py`. **Ne pas éditer à la main.**

Les règles d'un même composant sont réparties en couches sur tout le fichier :
l'ordre porte la cascade, c'est voulu, il ne faut pas les regrouper. Mais avant
de modifier le style d'un composant, il faut avoir vu **toutes** ses règles —
sinon on en corrige une pendant qu'une autre, ailleurs, continue de gagner.
C'est exactement ce qui a produit la régression v1.2.88 sur le bouton skip,
dont les huit règles s'étalaient sur 3 700 lignes.

Source indexée : `ElegantFin-cinema-v1.3.4.css` — 6665 lignes.

| Composant | Règles | Zones | Lignes |
|---|---:|---:|---|
| `card` | 36 | 14 | 383–465, 703, 785, 1431–1451, 1954–1987, 2014–2018, 2293–2311, 2347, 5712, 5999–6015, 6095–6117, 6147–6154, 6228, 6543 |
| `cardScalable` | 28 | 13 | 383–394, 442–465, 731–775, 801–839, 2311, 3254, 3365, 3444, 5001, 5726–5736, 5805, 5999, 6138–6154 |
| `cardImageContainer` | 23 | 13 | 437, 753, 781–810, 839, 896–926, 5110–5114, 5195, 5718, 5797–5805, 5858, 5999–6015, 6138, 6276 |
| `material-icons` | 15 | 11 | 319–338, 1650, 1709, 1761, 3211, 3370, 3444–3450, 3556, 3813, 4288, 4322–4332 |
| `itemDetailPage` | 16 | 10 | 1494, 1580, 1659, 1880–1905, 1949, 2049, 2360–2365, 3907, 4195, 6371–6409 |
| `nameContainer` | 27 | 9 | 649, 2056–2079, 2120, 2149, 2184–2230, 2267, 2298–2302, 4661–4713, 6371–6409 |
| `backdropCard` | 12 | 9 | 883–889, 1004, 1880, 1966, 2049, 2302–2311, 2338, 2365, 2635 |
| `card-hoverable` | 23 | 8 | 465, 741, 801–889, 5114, 5736, 5886–5905, 5999, 6283 |
| `parentName` | 23 | 8 | 649, 2061–2079, 2120, 2149, 2184–2230, 4667–4713, 4786, 6371–6409 |
| `detailPageWrapperContainer` | 17 | 8 | 649, 1462–1472, 1905, 2023, 2056–2079, 2149, 2184–2230, 2298 |
| `subtitle` | 16 | 8 | 1880, 1949, 2061, 2120, 2239–2249, 2360–2365, 4721–4754, 6371–6409 |
| `cardBox` | 12 | 8 | 383–431, 457, 703, 823, 930, 5712, 5999, 6283 |
| `detailLogo` | 17 | 7 | 649, 1894–1905, 1940–1949, 2049–2079, 2149, 2184–2230, 2298 |
| `loginPage` | 15 | 7 | 3523, 5013–5028, 5067, 5095–5114, 5741, 5784, 6127–6154 |
| `skinHeader` | 11 | 7 | 5009, 5338, 5394–5402, 5428–5453, 5788, 5967, 6480 |
| `emby-button` | 10 | 7 | 575–592, 619–637, 3013–3020, 3390, 3425, 3578, 3831 |
| `js` | 7 | 7 | 286, 1566, 2120, 2712, 3344, 5914, 6164 |
| `verticalSection` | 11 | 6 | 1654, 2531–2536, 4195, 5797, 5914, 6164 |
| `nowPlayingBar` | 8 | 6 | 2898, 5247, 5751, 5845, 5948–5979, 6233 |
| `person` | 8 | 6 | 1880–1890, 2049, 2302, 2347–2356, 3651, 6366 |
| `detailImageContainer` | 20 | 5 | 1880–1890, 1954–2018, 2049, 2289–2311, 2338–2365 |
| `listItem` | 16 | 5 | 592, 2315, 3733–3759, 3790–3822, 6251–6268 |
| `osdHeader` | 15 | 5 | 1623–1641, 5333–5402, 5428–5453, 5788, 6233 |
| `actionSheetMenuItem` | 11 | 5 | 592, 3733–3744, 3790, 3868–3884, 5769 |
| `navMenuOption` | 11 | 5 | 592, 688–698, 3800–3822, 3888–3893, 6038–6049 |
| `cardImageIcon` | 8 | 5 | 375–379, 2302–2311, 2371, 3238, 5195 |
| `paper-icon-button-light` | 8 | 5 | 537–592, 1580, 1650, 1709, 4580 |
| `emby-scroller-container` | 7 | 5 | 1654–1667, 2521, 2557, 5797, 5914 |
| `portraitCard` | 5 | 5 | 1004, 1082, 1799, 2014, 2635 |
| `btnPlay` | 16 | 4 | 474–498, 537–592, 3454–3496, 3529–3556 |
| `cardOverlayContainer` | 12 | 4 | 857–889, 934–956, 1016, 6233–6251 |
| `itemName` | 11 | 4 | 649, 2120, 4667–4713, 4804–4821 |
| `backdropImage` | 10 | 4 | 2437–2464, 2491–2495, 5705, 5805–5813 |
| `emby-tab-button` | 10 | 4 | 592, 659–668, 3502, 5504–5540 |
| `upNextContainer` | 10 | 4 | 4350–4369, 4395–4421, 5741–5751, 5777 |
| `sectionTabs` | 9 | 4 | 1678, 3502, 5374–5379, 5519–5545 |
| `button-link` | 8 | 4 | 592, 619–637, 2848–2857, 2918–2928 |
| `detailRibbon` | 7 | 4 | 1519–1547, 1714, 1799–1804, 6366 |
| `listItemBodyText` | 7 | 4 | 3754–3773, 3813, 3872, 6268 |
| `visualCardBox` | 7 | 4 | 383, 762–775, 801–806, 930 |
| `detailPagePrimaryContent` | 6 | 4 | 1534–1552, 2254, 4189, 5983 |
| `skip-button` | 6 | 4 | 592, 3507, 4444–4461, 4488–4494 |
| `squareCard` | 6 | 4 | 785, 2302, 2338–2356, 5071–5075 |
| `button-submit` | 5 | 4 | 3523, 3610, 5095–5103, 6341 |
| `mainDrawer` | 5 | 4 | 2862, 5741–5751, 6025, 6064 |
| `sectionTitle` | 5 | 4 | 1654, 1688–1695, 4268, 5062 |
| `skinHeader-blurred` | 5 | 4 | 5009, 5362–5369, 5967, 6233 |
| `appfooter` | 4 | 4 | 2578, 5478, 5828, 6233 |
| `page` | 4 | 4 | 926, 2512, 2557, 5797 |
| `raised` | 4 | 4 | 592, 678, 3390, 3425 |
| `skinHeader-withBackground` | 4 | 4 | 1562, 5009, 5333, 5383 |
| `detailButton` | 13 | 3 | 537–592, 3435–3496, 3552–3556 |
| `emby-scroller` | 9 | 3 | 1659–1673, 6070–6117, 6219–6228 |
| `itemBackdrop` | 9 | 3 | 1846–1890, 2023, 2365 |
| `itemSelectionPanel` | 9 | 3 | 814–818, 3183, 3211–3254 |
| `check` | 8 | 3 | 3211, 3444, 3864–3884 |
| `pageTitle` | 8 | 3 | 1598–1641, 5394, 5453 |
| `detailSectionContent` | 6 | 3 | 3045, 3989–3999, 4080–4090 |
| `emby-checkbox` | 6 | 3 | 3188, 3225–3229, 3278–3290 |
| `headerTop` | 6 | 3 | 5344–5369, 5420–5437, 5464–5468 |
| `actionSheetContent` | 5 | 3 | 3856–3860, 5741–5751, 5777 |
| `cardText-first` | 5 | 3 | 844, 3217–3243, 5176 |
| `cardText-secondary` | 5 | 3 | 844, 3243–3247, 5892–5900 |
| `dialog` | 5 | 3 | 3095–3105, 5741–5751, 5777 |
| `guideProgramName` | 5 | 3 | 592, 4845–4856, 4899–4904 |
| `musicParentName` | 5 | 3 | 1880, 2360–2365, 4786–4795 |
| `noHomeButtonHeader` | 5 | 3 | 1580, 5394, 5504–5512 |
| `overflowBackdropCard` | 5 | 3 | 883–889, 3221, 5171–5176 |
| `album` | 4 | 3 | 2049, 2307–2311, 2347 |
| `cardPadder` | 4 | 3 | 379, 930, 3234–3238 |
| `cardText` | 4 | 3 | 844–854, 3243, 6143 |
| `countIndicator` | 4 | 3 | 722, 5839, 6290–6314 |
| `dialog-fullscreen` | 4 | 3 | 3105, 5741–5751, 5777 |
| `emby-scrollbuttons` | 4 | 3 | 1700–1705, 6164, 6518 |
| `formDialogFooter` | 4 | 3 | 3163, 3617, 6290–6314 |
| `infoWrapper` | 4 | 3 | 1993–1998, 2254, 2282 |
| `listItemImage` | 4 | 3 | 2612–2617, 3727, 6268 |
| `semiTransparent` | 4 | 3 | 1562, 5009, 5362–5383 |
| `toast` | 4 | 3 | 4342, 5741–5751, 5777 |
| `defaultCardBackground` | 3 | 3 | 3365, 5191, 5290 |
| `folder` | 3 | 3 | 1799, 3344, 3408 |
| `formDialogFooterItem` | 3 | 3 | 3163, 3403, 3529 |
| `formDialogHeader` | 3 | 3 | 3617, 6233, 6290 |
| `iconOsd` | 3 | 3 | 4987, 6233, 6290 |
| `itemsContainer` | 3 | 3 | 703, 1682, 4195 |
| `live_tv` | 3 | 3 | 1880, 2347, 3651 |
| `myPreferencesMenuPage` | 3 | 3 | 352, 3898, 4203 |
| `playerStats` | 3 | 3 | 4987, 6290, 6326 |
| `scss` | 3 | 3 | 956, 3260, 5914 |
| `sectionTitle-cards` | 3 | 3 | 1654, 4268, 4318 |
| `x` | 3 | 3 | 2120, 4769, 5914 |
| `itemExternalLinks` | 11 | 2 | 2911–2968, 3045 |
| `checkboxOutline` | 10 | 2 | 3188–3229, 3260–3290 |
| `mdl-slider` | 9 | 2 | 2708, 2763–2821 |
| `listItemIcon` | 8 | 2 | 3647–3651, 3868–3898 |
| `sectionTitleTextButton` | 8 | 2 | 4251–4288, 4322–4332 |
| `sliderContainer` | 8 | 2 | 2712, 2740–2805 |
| `cardOverlayButton-br` | 7 | 2 | 942, 971–1009 |
| `detail-clamp-text` | 7 | 2 | 2981–3007, 3033–3037 |
| `divUsers` | 7 | 2 | 5071–5075, 6127–6154 |
| `multiSelectCheckboxOutline` | 7 | 2 | 3225–3229, 3259–3278 |
| `backgroundContainer` | 6 | 2 | 2427, 2469–2487 |
| `detailPagePrimaryContainer` | 6 | 2 | 1506–1552, 2254 |
| `detailsGroupItem` | 6 | 2 | 3951, 4019–4057 |
| `headerButton` | 6 | 2 | 512–592, 5446 |
| `headerLeft` | 6 | 2 | 1604–1641, 5633 |
| `trackSelections` | 6 | 2 | 3924–3951, 4085–4090 |
| `withBackdrop` | 6 | 2 | 2427, 2469–2487 |
| `detailSection` | 5 | 2 | 3907–3916, 4070–4090 |
| `mainDrawer-scrollContainer` | 5 | 2 | 2871, 6038–6055 |
| `mediaInfoItem` | 5 | 2 | 1718–1761, 5914 |
| `overview-expand` | 5 | 2 | 3013–3037, 3989 |
| `playedIndicator` | 5 | 2 | 3327, 5999–6020 |
| `videoIndicator` | 5 | 2 | 3333–3361, 6290 |
| `withSectionTabs` | 5 | 2 | 2478–2495, 5369 |
| `alphaPickerButton` | 4 | 2 | 592, 4129–4141 |
| `backgroundProgress` | 4 | 2 | 2623–2635, 2665 |
| `emby-tab-button-active` | 4 | 2 | 3589, 5531–5545 |
| `play_arrow` | 4 | 2 | 3370–3386, 3556 |
| `playbackProgress` | 4 | 2 | 2623–2635, 2670 |
| `playlistIndexIndicatorImage` | 4 | 2 | 3754–3759, 5284–5290 |
| `programCell` | 4 | 2 | 4836, 4895–4904 |
| `programGuideSection` | 4 | 2 | 2315–2330, 4090–4105 |
| `secondary` | 4 | 2 | 3763–3773, 3813 |
| `section0` | 4 | 2 | 896–926, 5797 |
| `visualLoginForm` | 4 | 2 | 5062–5079, 5120 |
| `cardFooter` | 3 | 2 | 3254, 5886–5905 |
| `cardOverlayButtonIcon` | 3 | 2 | 942–954, 1009 |
| `castCollapsible` | 3 | 2 | 753, 3229–3238 |
| `detailPageContent` | 3 | 2 | 3920, 4182–4189 |
| `emby-scrollbuttons-button` | 3 | 2 | 1709, 6525–6532 |
| `fullSyncIndicator` | 3 | 2 | 722, 6290–6314 |
| `guestCastContent` | 3 | 2 | 753, 3229–3238 |
| `guide-channelHeaderCell` | 3 | 2 | 592, 4870–4886 |
| `guide-date-tab-button` | 3 | 2 | 592, 3589–3597 |
| `headerUserButton` | 3 | 2 | 512–525, 4207 |
| `manualLoginForm` | 3 | 2 | 5062–5079, 5120 |
| `overview` | 3 | 2 | 3033–3037, 3999 |
| `selectionCommandsPanel` | 3 | 2 | 3173–3179, 6233 |
| `backdropImageFadeIn` | 2 | 2 | 2562, 6330 |
| `blurhash-canvas` | 2 | 2 | 5858, 6276 |
| `book` | 2 | 2 | 1880, 2347 |
| `btnDeleteImage` | 2 | 2 | 3390, 3603 |
| `cardContent` | 2 | 2 | 753, 785 |
| `cardImage` | 2 | 2 | 5858, 6276 |
| `cardOverlayButton` | 2 | 2 | 956, 992 |
| `cardOverlayButton-hover` | 2 | 2 | 839, 971 |
| `chevron_right` | 2 | 2 | 4288, 4332 |
| `collapseContent` | 2 | 2 | 3168, 3615 |
| `content-primary` | 2 | 2 | 4182, 4234 |
| `detailPageSecondaryContainer` | 2 | 2 | 1529, 1556 |
| `editorsChoiceItemOverview` | 2 | 2 | 6455, 6536 |
| `endsAt` | 2 | 2 | 1739, 5914 |
| `formDialogFooter-clear` | 2 | 2 | 3163, 3617 |
| `headroom` | 2 | 2 | 5357, 5394 |
| `mediaInfoOfficialRating` | 2 | 2 | 1739, 5914 |
| `mediaSourceIndicator` | 2 | 2 | 722, 6290 |
| `navMenuOption-selected` | 2 | 2 | 3903, 6049 |
| `nowPlayingInfoContainer` | 2 | 2 | 2902, 5221 |
| `org` | 2 | 2 | 2938, 2968 |
| `paperList` | 2 | 2 | 762, 3628 |
| `playlist` | 2 | 2 | 3749, 5199 |
| `queue` | 2 | 2 | 1880, 2347 |
| `readOnlyContent` | 2 | 2 | 3659, 5562 |
| `recordingFields` | 2 | 2 | 3943, 4085 |
| `runtime` | 2 | 2 | 5132, 5161 |
| `sectionTitleContainer` | 2 | 2 | 1705, 4114 |
| `sectionTitleContainer-cards` | 2 | 2 | 4263, 4318 |
| `tagline` | 2 | 2 | 2418, 3999 |
| `upNextDialog-title` | 2 | 2 | 4374, 4408 |
| `vertical-list` | 2 | 2 | 1682, 6361 |
| `videoOsdBottom` | 2 | 2 | 2894, 5324 |
| `videoOsdBottom-maincontrols` | 2 | 2 | 2894, 5324 |
| `checkboxContainer` | 7 | 1 | 3217–3254 |
| `itemDetailsGroup` | 7 | 1 | 4003–4090 |
| `itemProgressBar` | 6 | 1 | 2612–2646 |
| `trackSelectionFieldContainer` | 6 | 1 | 3962–3985 |
| `editorsChoiceScrollButtonsContainer` | 5 | 1 | 6492–6532 |
| `innerCardFooter` | 5 | 1 | 3058–3087 |
| `chapterCardImageContainer` | 4 | 1 | 3058–3087 |
| `endTimeText` | 4 | 1 | 5132–5161 |
| `mainDetailButtons` | 4 | 1 | 3552–3566 |
| `overview-controls` | 4 | 1 | 3033–3045 |
| `scrollX` | 4 | 1 | 1659–1678 |
| `startTimeText` | 4 | 1 | 5132–5155 |
| `button-flat` | 3 | 1 | 2875–2885 |
| `cardIndicators` | 3 | 1 | 3307–3317 |
| `cardOverlayFab-primary` | 3 | 1 | 934–956 |
| `com` | 3 | 1 | 2944–2962 |
| `content` | 3 | 1 | 4026–4057 |
| `discover-card` | 3 | 1 | 6543–6566 |
| `emby-select-withcolor` | 3 | 1 | 4594–4628 |
| `emby-textarea` | 3 | 1 | 4585–4610 |
| `fab` | 3 | 1 | 3412–3425 |
| `listChildrenCollapsible` | 3 | 1 | 4075–4090 |
| `mdl-slider-background-flex` | 3 | 1 | 2732–2745 |
| `mediaInfoCriticRating` | 3 | 1 | 1780–1789 |
| `nextUpSection` | 3 | 1 | 4070–4090 |
| `nowPlayingPageImageContainerNoAlbum` | 3 | 1 | 5185–5195 |
| `serverInfo` | 3 | 1 | 3632–3641 |
| `transcodingProgress` | 3 | 1 | 2623–2635 |
